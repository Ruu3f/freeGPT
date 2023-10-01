"""
freeGPT's gpt4 module
"""

from uuid import uuid4
from re import findall
from curl_cffi.requests import get, RequestsError


class Completion:
    """
    This class provides methods for generating completions based on prompts.
    """

    def create(self, prompt):
        """
        Generate a completion based on the provided prompt.

        Args:
            prompt (str): The input prompt to generate a completion from.

        Returns:
            str: The generated completion as a text string.

        Raises:
            Exception: If the response does not contain the expected "youChatToken".
        """
        resp = get(
            "https://you.com/api/streamingSearch",
            headers={
                "cache-control": "no-cache",
                "referer": "https://you.com/search?q=gpt4&tbm=youchat",
                "cookie": f"safesearch_guest=Off; uuid_guest={str(uuid4())}",
            },
            params={
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
            },
            impersonate="chrome107",
        )
        text = resp.content.decode("unicode-escape")
        if "youChatToken" not in text:
            raise RequestsError("Unable to fetch response.")
        return (
            "".join(findall(r"{\"youChatToken\": \"(.*?)\"}", text))
            .replace("\\n", "\n")
            .replace("\\\\", "\\")
            .replace('\\"', '"')
        )
