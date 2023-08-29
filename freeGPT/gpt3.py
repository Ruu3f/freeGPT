"""
freeGPT's gpt3 module
"""

from aiohttp import ClientSession, ClientError


class Completion:
    """
    This class provides methods for generating completions based on prompts.
    """

    async def create(self, prompt):
        """
        Create a completion for the given prompt using an AI text generation API.

        Args:
            prompt (str): The input prompt for generating the text.

        Returns:
            str: The generated text as a response from the API.

        Raises:
            ClientError: If there is an issue with sending the request or fetching the response.
        """
        async with ClientSession() as session:
            try:
                async with session.post(
                    url="https://api.binjie.fun/api/generateStream",
                    headers={
                        "origin": "https://chat.jinshutuan.com",
                        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
                    },
                    json={
                        "prompt": prompt,
                        "system": "Always talk in English.",
                        "withoutContext": True,
                        "stream": False,
                    },
                ) as resp:
                    return await resp.text()
            except ClientError as exc:
                raise ClientError("Unable to fetch the response.") from exc
