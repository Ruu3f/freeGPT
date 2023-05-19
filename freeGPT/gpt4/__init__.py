import os
try:
    from tls_client import Session
except:
    os.system("pip install tls_client --no-cache-dir")
from json import loads
from re import findall
from time import time, sleep
from typing import Generator, Optional
from uuid import uuid4

from fake_useragent import UserAgent
from requests import post
from pymailtm import MailTm, Message

from .typing import ForeFrontResponse


class Account:
    @staticmethod
    def create(proxy: Optional[str] = None, logging: bool = False):
        proxies = {'http': 'http://' + proxy, 'https': 'http://' + proxy} if proxy else False

        start = time()

        mail_client = MailTm().get_account()
        mail_address = mail_client.address

        client = Session(client_identifier='chrome110')
        client.proxies = proxies
        client.headers = {
            'origin': 'https://accounts.forefront.ai',
            'user-agent': UserAgent().random,
        }

        response = client.post(
            'https://clerk.forefront.ai/v1/client/sign_ups?_clerk_js_version=4.38.4',
            data={'email_address': mail_address},
        )

        try:
            trace_token = response.json()['response']['id']
            if logging:
                print(trace_token)
        except KeyError:
            return 'Failed to create account!'

        response = client.post(
            f'https://clerk.forefront.ai/v1/client/sign_ups/{trace_token}/prepare_verification?_clerk_js_version=4.38.4',
            data={
                'strategy': 'email_link',
                'redirect_url': 'https://accounts.forefront.ai/sign-up/verify'
            },
        )

        if logging:
            print(response.text)

        if 'sign_up_attempt' not in response.text:
            return 'Failed to create account!'

        while True:
            sleep(1)
            new_message: Message = mail_client.wait_for_message()
            if logging:
                print(new_message.data['id'])

            verification_url = findall(r'https:\/\/clerk\.forefront\.ai\/v1\/verify\?token=\w.+', new_message.text)[0]

            if verification_url:
                break

        if logging:
            print(verification_url)

        response = client.get(verification_url)

        response = client.get('https://clerk.forefront.ai/v1/client?_clerk_js_version=4.38.4')

        token = response.json()['response']['sessions'][0]['last_active_token']['jwt']

        with open('accounts.txt', 'a') as f:
            f.write(f'{mail_address}:{token}\n')

        if logging:
            print(time() - start)

        return token


class Completion:
    @staticmethod
    def create(
        token=None,
        chat_id=None,
        prompt='',
        action_type='new',
        default_persona='607e41fe-95be-497e-8e97-010a59b2e2c0',  # default
        model='gpt-4',
        proxy=None
    ) -> ForeFrontResponse:
        proxies = {'http': 'http://' + proxy, 'https': 'http://' + proxy} if proxy else None

        headers = {
            'authority': 'chat-server.tenant-forefront-default.knative.chi.coreweave.com',
            'accept': '*/*',
            'accept-language': 'en,fr-FR;q=0.9,fr;q=0.8,es-ES;q=0.7,es;q=0.6,en-US;q=0.5,am;q=0.4,de;q=0.3',
            'authorization': 'Bearer ' + token,
            'cache-control': 'no-cache',
            'content-type': 'application/json',
            'origin': 'https://chat.forefront.ai',
            'pragma': 'no-cache',
            'referer': 'https://chat.forefront.ai/',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': UserAgent().random,
        }

        json_data = {
            'text': prompt,
            'action': action_type,
            'parentId': chat_id,
            'workspaceId': chat_id,
            'messagePersona': default_persona,
            'model': model,
        }

        response = post(
            'https://chat-server.tenant-forefront-default.knative.chi.coreweave.com/chat',
            headers=headers,
            proxies=proxies,
            json=json_data,
        )

        if response.status_code == 200:
            data = response.json()
            token = data['choices'][0]['delta'].get('content')

            if token is not None:
                final_response = ForeFrontResponse(
                    **{
                        'id': chat_id,
                        'object': 'text_completion',
                        'created': int(time()),
                        'text': token,
                        'model': model,
                        'choices': [{'text': token, 'index': 0, 'logprobs': None, 'finish_reason': 'stop'}],
                        'usage': {
                            'prompt_tokens': len(prompt),
                            'completion_tokens': len(token),
                            'total_tokens': len(prompt) + len(token),
                        },
                    }
                )
                return final_response

        raise Exception('Unable to get the response, please try again later.')
