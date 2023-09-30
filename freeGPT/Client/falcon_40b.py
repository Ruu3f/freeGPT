"""
freeGPT's falcon_40b module
"""

from requests import Session
from requests.exceptions import RequestException
from json import loads
from uuid import uuid4


class Completion:
    """
    Methods for generating text completions.
    """

    def create(self, prompt):
        """
        Generate text based on a given prompt.

        Args:
            prompt (str): The prompt for text generation.

        Returns:
            str: The generated text.
        """

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
            "Referer": "https://gpt-gm.h2o.ai/",
        }

        with Session() as session:
            try:
                session.post(
                    "https://gpt-gm.h2o.ai/settings",
                    headers=headers,
                    data={
                        "ethicsModalAccepted": "true",
                        "shareConversationsWithModelAuthors": "false",
                        "ethicsModalAcceptedAt": "",
                        "activeModel": "h2oai/h2ogpt-gm-oasst1-en-2048-falcon-40b-v1",
                        "searchEnabled": "true",
                    },
                )
                resp = session.post(
                    "https://gpt-gm.h2o.ai/conversation",
                    headers=headers,
                    json={"model": "h2oai/h2ogpt-gm-oasst1-en-2048-falcon-40b-v1"},
                )
                resp_json = resp.json()
                resp = session.post(
                    f"https://gpt-gm.h2o.ai/conversation/{resp_json['conversationId']}",
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
                )
                return loads(resp.text.replace("\n", "").split("data:")[-1])[
                    "generated_text"
                ]
            except RequestException as exc:
                raise RequestException("Unable to fetch response.") from exc
