import time, requests
from fake_useragent import UserAgent


class Completion:
    @staticmethod
    def create(prompt):
        """
        Creates a completion for a given prompt.

        Args:
            prompt (str): The text prompt to generate a completion for.

        Returns:
            str: The generated completion text.

        Raises:
            Exception: If there is an error while fetching the response.
        """
        try:
            resp = requests.post(
                "https://api.aichatos.cloud/api/generate",
                headers={
                    "authority": "api.aichatos.cloud",
                    "origin": "https://chat9.yqcloud.top",
                    "referer": "https://chat9.yqcloud.top/",
                    "user-agent": UserAgent().random,
                },
                json={
                    "prompt": f"Always reply in English, prompt: {prompt}",
                    "userId": f"#/chat/{int(time.time() * 1000)}",
                },
            )
            return resp.json()["result"]
        except (requests.RequestException, ValueError, KeyError):
            raise Exception("Unable to fetch the response.")
