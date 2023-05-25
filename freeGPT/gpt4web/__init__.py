import os, re, json, curl_cffi
from typing import Any, List, Generator, Optional
from uuid import uuid4
from time import time, sleep
from pydantic import BaseModel
from fake_useragent import UserAgent
from pymailtm import MailTm, Message


class Choice(BaseModel):
    """
    Represents a choice in the response from ForeFront API.

    Attributes:
        text (str): The text of the choice.
        index (int): The index of the choice.
        logprobs (Any): Log probabilities associated with the choice.
        finish_reason (str): The reason for finishing the choice.
    """    
    text: str
    index: int
    logprobs: Any
    finish_reason: str


class Usage(BaseModel):
    """
    Represents the token usage information in the response from ForeFront API.

    Attributes:
        prompt_tokens (int): The number of tokens in the prompt.
        completion_tokens (int): The number of tokens in the completion.
        total_tokens (int): The total number of tokens (prompt + completion).
    """    
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ForeFrontResponse(BaseModel):
    """
    Represents the response from ForeFront API.

    Attributes:
        id (str): The ID of the response.
        object (str): The object type of the response.
        created (int): The timestamp of when the response was created.
        model (str): The model used for generating the response.
        choices (List[Choice]): The list of choices in the response.
        usage (Usage): The token usage information in the response.
        text (str): The generated text from the response.
    """    
    id: str
    object: str
    created: int
    model: str
    choices: List[Choice]
    usage: Usage
    text: str


class Account:
    @staticmethod
    def create(proxy: Optional[str] = None, logging: bool = False) -> str:
        """
        Creates a ForeFront account and returns the authentication token.

        Args:
            proxy (Optional[str]): The proxy to be used for the account creation.
            logging (bool): Whether to enable logging or not.

        Returns:
            str: The authentication token for the created account.
        """    
        proxies = (
            {"http": "http://" + proxy, "https": "http://" + proxy} if proxy else False
        )

        start = time.time()

        mail_client = MailTm().get_account()
        mail_address = mail_client.address

        client = curl_cffi.Curl()
        client.setopt(curl_cffi.URL, "https://clerk.forefront.ai/v1/client/sign_ups?_clerk_js_version=4.38.4")
        client.setopt(curl_cffi.HTTPHEADER, ["origin: https://accounts.forefront.ai", "user-agent: " + UserAgent().random])
        client.setopt(curl_cffi.POSTFIELDS, json.dumps({"email_address": mail_address}))
        client.perform()

        try:
            response_data = json.loads(client.body())
            trace_token = response_data["response"]["id"]
            if logging:
                print(trace_token)
        except KeyError:
            return "Failed to create account!"

        client.setopt(curl_cffi.URL, f"https://clerk.forefront.ai/v1/client/sign_ups/{trace_token}/prepare_verification?_clerk_js_version=4.38.4")
        client.setopt(curl_cffi.POSTFIELDS, json.dumps({"strategy": "email_link", "redirect_url": "https://accounts.forefront.ai/sign-up/verify"}))
        client.perform()

        if logging:
            print(client.body())

        if "sign_up_attempt" not in client.body().decode("utf-8"):
            return "Failed to create account!"

        while True:
            time.sleep(1)
            new_message: Message = mail_client.wait_for_message()
            if logging:
                print(new_message.data["id"])

            verification_url = re.findall(
                r"https:\/\/clerk\.forefront\.ai\/v1\/verify\?token=\w.+",
                new_message.text,
            )[0]

            if verification_url:
                break

        if logging:
            print(verification_url)

        client.setopt(curl_cffi.URL, verification_url)
        client.perform()

        client.setopt(curl_cffi.URL, "https://clerk.forefront.ai/v1/client?_clerk_js_version=4.38.4")
        client.perform()

        response_data = json.loads(client.body())
        token = response_data["response"]["sessions"][0]["last_active_token"]["jwt"]

        with open("accounts.txt", "a") as f:
            f.write(f"{mail_address}:{token}\n")

        if logging:
            print(time.time() - start)

        return token


class Completion:
    @staticmethod
    def create(
        token=None,
        chat_id=None,
        prompt="",
        action_type="new",
        default_persona="607e41fe-95be-497e-8e97-010a59b2e2c0",
        model="gpt-4",
        proxy=None,
    ) -> ForeFrontResponse:
        """
        Creates a completion request using ForeFront API and returns the response.

        Args:
            token (str): The authentication token for the account.
            chat_id: The ID of the chat.
            prompt (str): The prompt for the completion.
            action_type (str): The action type for the completion.
            default_persona (str): The default persona for the completion.
            model (str): The model used for generating the completion.
            proxy (str): The proxy to be used for the completion.

        Returns:
            ForeFrontResponse: The response from ForeFront API.
        
        Raises:
            Exception: If unable to get the response from the API.
        """    
        proxies = (
            {"http": "http://" + proxy, "https": "http://" + proxy} if proxy else None
        )

        headers = {
            "authority": "chat-server.tenant-forefront-default.knative.chi.coreweave.com",
            "accept": "*/*",
            "accept-language": "en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3",
            "authorization": "Bearer " + token,
            "cache-control": "no-cache",
            "content-type": "application/json",
            "origin": "https://chat.forefront.ai",
            "pragma": "no-cache",
            "referer": "https://chat.forefront.ai/",
            "sec-ch-ua": '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "user-agent": UserAgent().random,
        }

        json_data = {
            "text": prompt,
            "action": action_type,
            "parentId": chat_id,
            "workspaceId": chat_id,
            "messagePersona": default_persona,
            "model": model,
        }

        client = curl_cffi.Curl()
        client.setopt(curl_cffi.URL, "https://chat-server.tenant-forefront-default.knative.chi.coreweave.com/chat")
        client.setopt(curl_cffi.HTTPHEADER, [f"{key}: {value}" for key, value in headers.items()])
        client.setopt(curl_cffi.POSTFIELDS, json.dumps(json_data))
        client.perform()

        if client.getinfo(curl_cffi.RESPONSE_CODE) == 200:
            response_data = json.loads(client.body())
            token = response_data["choices"][0]["delta"].get("content")

            if token is not None:
                final_response = ForeFrontResponse(
                    **{
                        "id": chat_id,
                        "object": "text_completion",
                        "created": int(time.time()),
                        "text": token,
                        "model": model,
                        "choices": [
                            {
                                "text": token,
                                "index": 0,
                                "logprobs": None,
                                "finish_reason": "stop",
                            }
                        ],
                        "usage": {
                            "prompt_tokens": len(prompt),
                            "completion_tokens": len(token),
                            "total_tokens": len(prompt) + len(token),
                        },
                    }
                )
                return final_response

        raise Exception("Unable to get the response, please try again later.")
