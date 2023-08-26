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
            prompt (str): The prompt for which completion needs to be generated.

        Returns:
            str: The generated completion text.

        Raises:
            ClientError: If there's an issue with the API request or response.
        """
        async with ClientSession() as session:
            try:
                async with session.post(
                    url="https://api.aichatos.cloud/api/generateStream",
                    headers={"origin": "https://chat9.yqcloud.top"},
                    json={
                        "prompt": f"Always respond in English. Prompt: {prompt}",
                        "network": True,
                        "system": "",
                        "withoutContext": False,
                        "stream": False,
                    },
                ) as resp:
                    return await resp.text()
            except ClientError as exc:
                raise ClientError("Unable to fetch the response.") from exc
