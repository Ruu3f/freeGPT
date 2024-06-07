"""
freeGPT's pollinations module
"""

from requests import get
from requests.exceptions import RequestException
from random import randint


class Generation:
    """
    This class provides methods for generating images based on prompts.
    """

    def create(self, prompt):
        """
        Create a new image generation based on the given prompt.

        Args:
            prompt (str): The prompt for generating the image.

        Returns:
            resp: The generated image content
        """
        try:
            return get(
                url=f"https://image.pollinations.ai/prompt/{prompt}{randint(1, 10000)}",
                timeout=30,
            ).content
        except RequestException as exc:
            raise RequestException("Unable to fetch the response.") from exc
