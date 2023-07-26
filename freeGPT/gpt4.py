import re
import json
import subprocess
from uuid import uuid4
from typing import Optional, List

try:
    import tls_client
except Exception:
    subprocess.run(["pip", "install", "tls_client", "--no-cache-dir"])


class Completion:
    async def create(
        prompt,
        page: int = 1,
        count: int = 10,
        safe_search: str = "Off",
        on_shopping_page: bool = False,
        mkt: str = "",
        response_filter: str = "WebPages, Translations, Computation, RelatedSearches",
        domain: str = "youchat",
        query_trace_id: Optional[str] = None,
        chat: Optional[List[str]] = None,
        include_links: bool = False,
        detailed: bool = False,
        proxies: Optional[str] = None,
    ) -> dict:
        """
        Create a completion.

        Args:
            prompt (str): The prompt for the completion.
            page (int): The page number for the search results. Default is 1.
            count (int): The number of results to return. Default is 10.
            safe_search (str): The safe search setting. Default is "Off".
            on_shopping_page (bool): Whether the search is on a shopping page. Default is False.
            mkt (str): The market code for the search. Default is an empty string.
            response_filter (str): The response filter for the search. Default is "WebPages, Translations, Computation, RelatedSearches".
            domain (str): The domain for the search. Default is "youchat".
            query_trace_id (str, optional): The query trace ID. If not provided, a new UUID will be generated. Default is None.
            chat (List[str], optional): A list of chat messages. Default is None.
            include_links (bool): Whether to include third-party search links in the results. Default is False.
            detailed (bool): Whether to include detailed information in the results. Default is False.
            proxies (str, optional): Proxies to use for the request. Default is None.

        Returns:
            dict: The completion result as a dictionary.

        Raises:
            Exception: If unable to fetch the response.
        """

        if chat is None:
            chat = []

        client = tls_client.Session(client_identifier="chrome_108")
        client.headers = {
            "authority": "you.com",
            "accept": "text/event-stream",
            "accept-language": "en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3",
            "cache-control": "no-cache",
            "referer": "https://you.com/search?q=hi&tbm=youchat",
            "sec-ch-ua": '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "Linux",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "cookie": f"safesearch_guest=Off; uuid_guest={str(uuid4())}",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
        }
        client.proxies = proxies

        response = client.get(
            "https://you.com/api/streamingSearch",
            params={
                "q": prompt,
                "page": page,
                "count": count,
                "safeSearch": safe_search,
                "onShoppingPage": on_shopping_page,
                "mkt": mkt,
                "responseFilter": response_filter,
                "domain": domain,
                "queryTraceId": str(uuid4())
                if query_trace_id is None
                else query_trace_id,
                "chat": str(chat),
            },
        )

        if "youChatToken" not in response.text:
            raise Exception("Unable to fetch the response.")

        you_chat_serp_results = re.search(
            r"(?<=event: youChatSerpResults\ndata:)(.*\n)*?(?=event: )", response.text
        ).group()
        third_party_search_results = re.search(
            r"(?<=event: thirdPartySearchResults\ndata:)(.*\n)*?(?=event: )",
            response.text,
        ).group()

        text = "".join(re.findall(r'{"youChatToken": "(.*?)"}', response.text))

        extra = {
            "youChatSerpResults": json.loads(you_chat_serp_results),
        }

        resp = {
            "text": text.replace("\\n", "\n").replace("\\\\", "\\").replace('\\"', '"')
        }

        if include_links:
            resp["links"] = json.loads(third_party_search_results)["search"][
                "third_party_search_results"
            ]

        if detailed:
            resp["extra"] = extra

        return resp["text"]
