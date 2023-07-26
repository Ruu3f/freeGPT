from requests import post, exceptions


class Completion:
    """
    A class for generating text completions using an API.

    Attributes:
        None

    Methods:
        create(prompt): Generates a text completion for the given prompt using an API.
    """

    async def create(prompt):
        """
        Generates a text completion for the given prompt using an API.

        Args:
            prompt (str): The prompt for which to generate a text completion.

        Returns:
            str: The generated text completion.

        Raises:
            Exception: If there is an error fetching the response from the API.
        """
        try:
            resp = post(
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
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
                },
                json={"prompt": prompt},
                timeout=30,
            ).json()
        except exceptions.RequestException:
            raise Exception("Unable to fetch the response.")

        return resp["completion"]
