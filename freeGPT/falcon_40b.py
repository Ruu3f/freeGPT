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
        conversation = ""
        messages = [
            {"role": "system", "content": "You are Falcon, an AI assistant."},
            {"role": "user", "content": prompt},
        ]

        for message in messages:
            conversation += f'{message["role"]}: {message["content"]}\n'

        async with ClientSession() as session:
            headers = {
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
                "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                "Content-Type": "application/x-www-form-urlencoded",
                "Upgrade-Insecure-Requests": "1",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-User": "?1",
                "Referer": "https://gpt-gm.h2o.ai/r/jGfKSwU",
            }
            try:
                async with session.post(
                    "https://gpt-gm.h2o.ai/settings",
                    headers=headers,
                    data={
                        "ethicsModalAccepted": "true",
                        "shareConversationsWithModelAuthors": "true",
                        "ethicsModalAcceptedAt": "",
                        "activeModel": "h2oai/h2ogpt-gm-oasst1-en-2048-falcon-40b-v1",
                        "searchEnabled": "true",
                    },
                ), session.post(
                    "https://gpt-gm.h2o.ai/conversation",
                    headers=headers,
                    json={"model": "h2oai/h2ogpt-gm-oasst1-en-2048-falcon-40b-v1"},
                ) as conversation_resp:
                    headers = {
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
                        "Accept": "*/*",
                        "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
                        "Content-Type": "application/json",
                        "Sec-Fetch-Dest": "empty",
                        "Sec-Fetch-Mode": "cors",
                        "Sec-Fetch-Site": "same-origin",
                        "Referer": "https://gpt-gm.h2o.ai/",
                    }

                    conversation_id_data = await conversation_resp.json()
                    conversation_id = conversation_id_data["conversationId"]

                    async with session.post(
                        f"https://gpt-gm.h2o.ai/conversation/{conversation_id}",
                        headers=headers,
                        json={
                            "inputs": conversation,
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
                    ) as generation_resp:
                        generated_text = await generation_resp.text()
                        resp_data = loads(
                            generated_text.replace("\n", "").split("data:")[-1]
                        )
                        return resp_data["generated_text"]
            except ClientError as exc:
                raise ClientError("Failed to fetch response.") from exc
