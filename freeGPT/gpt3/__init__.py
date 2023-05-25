import json
from threading import Thread
from curl_cffi import CurlEasy
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

        c = CurlEasy()
        c.setopt(c.URL, "https://chatbot.theb.ai/api/chat-completion")
        c.setopt(c.HTTPHEADER, [f"{k}: {v}" for k, v in headers.items()])
        if proxy:
            c.setopt(c.PROXY, proxy)

        data = {
            "role": "assistant",
            "prompt": prompt,
            "options": {},
        }
        c.setopt(c.POSTFIELDS, json.dumps(data))

        c.setopt(c.WRITEFUNCTION, Completion.handle_response)
        c.perform()

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
