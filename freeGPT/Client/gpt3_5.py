"""
freeGPT's gpt3.5 module
"""

from requests import post
from requests.exceptions import RequestException


class Completion:
    """
    This class provides methods for generating completions based on prompts.
    """

    def create(self, prompt):
        """
        Create a completion for the given prompt using an AI text generation API.

        Args:
            prompt (str): The input prompt for generating the text.

        Returns:
            str: The generated text as a response from the API.

        Raises:
            requests.exceptions.RequestException: If there is an issue with sending the request or fetching the response.
        """
        try:
            resp = post(
                "https://vtlchat-g1.vercel.app/api/openai/v1/chat/completions",
                json={
                    "messages": [{"role": "user", "content": prompt}],
                    "stream": False,
                    "model": "gpt-3.5-turbo",
                    "temperature": 0.5,
                    "presence_penalty": 0,
                    "frequency_penalty": 0,
                    "top_p": 1,
                },
            )
            return resp.json()["choices"][0]["message"]["content"]
        except RequestException as exc:
            raise RequestException("Unable to fetch the response.") from exc
