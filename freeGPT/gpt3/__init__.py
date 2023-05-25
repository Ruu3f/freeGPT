import json, requests
from threading import Thread
from queue import Queue, Empty
from fake_useragent import UserAgent
from typing import Generator, Optional


class Completion:
    """
    A class for generating chat completions using the chatbot API.
    """

    message_queue = Queue()

    @staticmethod
    def request(prompt: str, proxy: Optional[str] = None):
        """
        Sends a request to the chatbot API with the given prompt.

        Args:
            prompt (str): The input prompt for the chatbot.
            proxy (str, optional): The proxy server to use for the request. Defaults to None.
        """
        headers = {
            "authority": "chatbot.theb.ai",
            "content-type": "application/json",
            "origin": "https://chatbot.theb.ai",
            "user-agent": UserAgent().random,
        }

        url = "https://chatbot.theb.ai/api/chat-completion"
        data = {
            "role": "assistant",
            "prompt": prompt,
            "options": {},
        }
        
        response = requests.post(url, headers=headers, json=data, proxies={'https': proxy} if proxy else None)

        if response.ok:
            completion = response.json()["delta"]
            Completion.message_queue.put(completion)
        else:
            response.raise_for_status()

    @staticmethod
    def handle_response(body):
        completion = json.loads(body.decode())["delta"]
        Completion.message_queue.put(completion)

    @staticmethod
    def create(prompt: str, proxy: Optional[str] = None) -> Generator[str, None, None]:
        """
        Creates a generator that yields chat completions for the given prompt.

        Args:
            prompt (str): The input prompt for the chatbot.
            proxy (str, optional): The proxy server to use for the request. Defaults to None.

        Yields:
            str: The generated chat completion.
        """
        Thread(target=Completion.request, args=[prompt, proxy]).start()

        try:
            completion = Completion.message_queue.get(timeout=10)
            yield completion
        except Empty:
            raise Exception("Unable to get the response, please try again later.")
