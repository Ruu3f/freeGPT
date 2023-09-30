"""
freeGPT's falcon_40b module
"""

from json import loads
from uuid import uuid4
from aiohttp import ClientSession, ClientError


class Completion:
    """
    Methods for generating text completions.
    """

    async def create(self, prompt):
        """
        Generate text based on a given prompt.

        Args:
            prompt (str): The prompt for text generation.

        Returns:
            str: The generated text.
        """

        async with ClientSession() as session:
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
                "Referer": "https://gpt-gm.h2o.ai/",
            }
            try:
                async with session.post(
                    "https://gpt-gm.h2o.ai/settings",
                    headers=headers,
                    data={
                        "ethicsModalAccepted": "true",
                        "shareConversationsWithModelAuthors": "false",
                        "ethicsModalAcceptedAt": "",
                        "activeModel": "h2oai/h2ogpt-gm-oasst1-en-2048-falcon-40b-v1",
                        "searchEnabled": "true",
                    },
                ), session.post(
                    "https://gpt-gm.h2o.ai/conversation",
                    headers=headers,
                    json={"model": "h2oai/h2ogpt-gm-oasst1-en-2048-falcon-40b-v1"},
                ) as resp:
                    resp_json = await resp.json()
                    resp_json = resp_json["conversationId"]

                    async with session.post(
                        f"https://gpt-gm.h2o.ai/conversation/{resp_json}",
                        headers={
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
                        },
                        json={
                            "inputs": prompt,
                            "parameters": {
                                "temperature": 0.6,
                                "truncate": 2048,
                                "max_new_tokens": 2048,
                                "do_sample": True,
                                "repetition_penalty": 1.2,
                                "return_full_text": False,
                            },
                            "options": {
                                "id": str(uuid4()),
                                "response_id": str(uuid4()),
                                "is_retry": False,
                                "use_cache": False,
                                "web_search_id": "",
                            },
                        },
                    ) as resp:
                        resp_text = await resp.text()
                        return loads(resp_text.replace("\n", "").split("data:")[-1])[
                            "generated_text"
                        ]
            except ClientError as exc:
                raise ClientError("Unable to fetch response.") from exc
