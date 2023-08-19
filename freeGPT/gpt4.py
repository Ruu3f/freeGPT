"""
freeGPT's gpt4 module
"""

from os import system
from uuid import uuid4
from re import findall

try:
    import tls_client
except ModuleNotFoundError:
    system("pip install tls_client --no-cache-dir")
    import tls_client

class Completion:
    """
    This class provides methods for generating completions based on prompts.
    """

    async def create(self, prompt):
        """
        Create a new completion session.

        Args:
            prompt (str): The input prompt for generating text.

        Returns:
            str: Generated text based on the provided prompt.

        Raises:
            Exception: If unable to fetch a valid response.
        """
        client = tls_client.Session(client_identifier="chrome_108")
        client.headers = {
            "authority": "you.com",
            "accept": "text/event-stream",
            "accept-language": "en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3",
            "cache-control": "no-cache",
            "referer": "https://you.com/search?q=who+are+you&tbm=youchat",
            "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "cookie": f"safesearch_guest=Off; uuid_guest={str(uuid4())}",
            "user-agent": "Mozilla/5.0 (Windows NT 5.1; U;  ; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.52",
        }
        params = {
            "q": prompt,
            "page": 1,
            "count": 10,
            "safeSearch": "Off",
            "onShoppingPage": False,
            "mkt": "",
            "responseFilter": "WebPages,Translations,TimeZone,Computation,RelatedSearches",
            "domain": "youchat",
            "queryTraceId": str(uuid4()),
            "chat": [],
        }
        resp = client.get(
            "https://you.com/api/streamingSearch", params=params, timeout_seconds=30
        )
        if "youChatToken" not in resp.text:
            raise Exception("Unable to fetch response.")
        return (
            "".join(findall(r"{\"youChatToken\": \"(.*?)\"}", resp.text))
            .replace("\\n", "\n")
            .replace("\\\\", "\\")
            .replace('\\"', '"')
        )
