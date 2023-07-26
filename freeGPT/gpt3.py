from aiohttp import ClientSession, ClientError
from json import loads, JSONDecodeError


class Completion:
    """
    This class provides methods for generating completions based on prompts.
    """

    @classmethod
    async def create(cls, prompt):
        """
        Create a new completion based on the given prompt.

        Args:
            prompt (str): The prompt to generate a completion for.

        Returns:
            str: The generated completion.

        Raises:
            Exception: If unable to fetch the response.
        """
        try:
            async with ClientSession() as session:
                async with session.post(
                    "https://ava-alpha-api.codelink.io/api/chat",
                    headers={"Content-Type": "application/json"},
                    json={
                        "model": "gpt-4",
                        "temperature": 0.6,
                        "stream": True,
                        "messages": [
                            {
                                "role": "system",
                                "content": "You are Ava, an AI assistant.",
                            },
                            {"role": "user", "content": prompt},
                        ],
                    },
                    timeout=45,
                ) as resp_obj:
                    resp = ""
                    async for line in resp_obj.content:
                        line_text = line.decode("utf-8").strip()
                        if line_text.startswith("data:"):
                            data = line_text.split("data:")[1]
                            try:
                                data_json = loads(data)
                                if "choices" in data_json:
                                    choices = data_json["choices"]
                                    for choice in choices:
                                        if (
                                            "finish_reason" in choice
                                            and choice["finish_reason"] == "stop"
                                        ):
                                            break
                                        if (
                                            "delta" in choice
                                            and "content" in choice["delta"]
                                        ):
                                            resp += choice["delta"]["content"]
                            except JSONDecodeError:
                                pass
                    return resp
        except ClientError:
            raise Exception("Unable to fetch the response.")
