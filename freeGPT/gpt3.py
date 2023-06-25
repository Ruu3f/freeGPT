import time, requests
from fake_useragent import UserAgent


class Completion:
    @staticmethod
    def create(prompt):
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
                    "withoutContext": True,
                },
            )
            return resp.json()["result"]
        except (requests.RequestException, ValueError, KeyError):
            raise Exception(f"Unable to fetch the response.")
