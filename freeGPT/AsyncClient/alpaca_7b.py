"""
freeGPT's alpaca_7b module
"""

from aiohttp import ClientSession, ClientError


class Completion:
    """
    This class provides methods for generating completions based on prompts.
    """

    async def create(self, prompt):
        """
        Create a completion using the provided prompt.

        Args:
            prompt (str): The text prompt for generating a completion.

        Returns:
            str: The generated completion text.

        Raises:
            ClientError: If there is an issue with the HTTP request or response.
        """
        async with ClientSession() as session:
            try:
                async with session.post(
                    "https://us-central1-arched-keyword-306918.cloudfunctions.net/run-inference-1",
                    json={"prompt": prompt},
                ) as resp:
                    resp_json = await resp.json()
            except ClientError as exc:
                raise ClientError("Unable to fetch the response.") from exc
        return resp_json["completion"]
