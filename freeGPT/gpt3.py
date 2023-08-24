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
        Generates completions based on prompts.

        Args:
            prompt (str): The prompt for generating completions.

        Returns:
            str: The generated completion.
        Raises:
            ClientError: If unable to fetch the response.
        """
        async with ClientSession() as session:
            try:
                async with session.post(
                    "https://www.chatbase.co/api/fe/chat",
                    json={
                        "chatId": "chatbase--1--pdf-p680fxvnm",
                        "captchaCode": "hadsa",
                        "messages": [{"role": "user", "content": prompt}],
                    },
                ) as resp:
                    return await resp.text()
            except ClientError as exc:
                raise ClientError("Unable to fetch the response.") from exc
