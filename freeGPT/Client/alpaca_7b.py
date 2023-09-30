"""
freeGPT's alpaca_7b module
"""

from requests import post
from requests.exceptions import RequestException


class Completion:
    """
    This class provides methods for generating completions based on prompts.
    """

    def create(self, prompt):
        """
        Create a completion using the provided prompt.

        Args:
            prompt (str): The text prompt for generating a completion.

        Returns:
            str: The generated completion text.

        Raises:
            requests.exceptions.RequestException: If there is an issue with the HTTP request or response.
        """
        try:
            resp = post(
                "https://us-central1-arched-keyword-306918.cloudfunctions.net/run-inference-1",
                json={"prompt": prompt},
            )
            resp_json = resp.json()
        except RequestException as exc:
            raise RequestException("Unable to fetch the response.") from exc
        return resp_json["completion"]
