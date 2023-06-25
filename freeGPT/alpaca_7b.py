import requests
from fake_useragent import UserAgent


class Completion:
    @staticmethod
    def create(prompt):
        """
        Create a completion using a given prompt.

        Args:
            prompt (str): The prompt for generating the completion.

        Returns:
            str: The generated completion.

        Raises:
            Exception: If there is an error while fetching the response.

        """
        try:
            resp = requests.post(
                "https://us-central1-arched-keyword-306918.cloudfunctions.net/run-inference-1",
                headers={
                    "Origin": "https://chatllama.baseten.co",
                    "Referer": "https://chatllama.baseten.co/",
                    "Accept": "application/json, text/plain, */*",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Content-Length": "17",
                    "Content-Type": "application/json",
                    "Sec-Ch-Ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
                    "Sec-Ch-Ua-Mobile": "?0",
                    "Sec-Ch-Ua-Platform": "Windows",
                    "Sec-Fetch-Dest": "empty",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Site": "cross-site",
                    "User-Agent": UserAgent().random,
                },
                json={"prompt": prompt},
            ).json()
        except requests.exceptions.RequestException:
            raise Exception("Unable to fetch the response.")

        return resp["completion"]
