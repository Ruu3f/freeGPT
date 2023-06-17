import json, requests


class Completion:
    @staticmethod
    def create(prompt):
        """
        Creates a completion for the given prompt using the GPT-4 model.

        Args:
            prompt (str): The user prompt for generating the completion.

        Returns:
            str: The generated completion text.

        Raises:
            Exception: If there is an error while fetching the response.
        """

        headers = {"Content-Type": "application/json"}
        payload = {
            "model": "gpt-4",
            "temperature": 0.5,
            "stream": True,
            "messages": [
                {
                    "role": "system",
                    "content": "You are freeGPT, an AI assistant provided by Ruu3f (an individual). Your model is GPT-4 by OpenAI.",
                },
                {"role": "user", "content": prompt},
            ],
        }

        try:
            resp = ""
            with requests.post(
                "https://ava-alpha-api.codelink.io/api/chat",
                headers=headers,
                data=json.dumps(payload),
                stream=True,
            ) as resp_obj:
                resp_obj.raise_for_status()
                for line in resp_obj.iter_lines():
                    line_text = line.decode("utf-8").strip()
                    if line_text.startswith("data:"):
                        data = line_text[len("data:") :]
                        try:
                            data_json = json.loads(data)
                            if "choices" in data_json:
                                choices = data_json["choices"]
                                for choice in choices:
                                    if (
                                        "finish_reason" in choice
                                        and choice["finish_reason"] == "stop"
                                    ):
                                        break
                                    if (
                                        "delta" in choice
                                        and "content" in choice["delta"]
                                    ):
                                        resp += choice["delta"]["content"]
                        except json.JSONDecodeError:
                            pass
        except requests.exceptions.RequestException:
            raise Exception("Unable to fetch the response.")

        return resp
