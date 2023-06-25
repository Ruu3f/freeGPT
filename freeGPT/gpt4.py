import json
import requests


class Completion:
    """
    A class that interacts with the Ava API to generate completions for prompts.
    """

    @staticmethod
    def create(prompt):
        """
        Generates a completion based on the given prompt.

        Args:
            prompt (str): The prompt text to generate a completion for.

        Returns:
            str: The generated completion response.

        Raises:
            Exception: If there is an error while fetching the response from the API.
        """
        try:
            resp = ""
            with requests.post(
                "https://ava-alpha-api.codelink.io/api/chat",
                headers={"Content-Type": "application/json"},
                data=json.dumps(
                    {
                        "model": "gpt-4",
                        "temperature": 0.7,
                        "stream": True,
                        "messages": [
                            {
                                "role": "system",
                                "content": "You are Ava, an AI assistant. You are running on GPT-4 by OpenAI.",
                            },
                            {"role": "user", "content": prompt},
                        ],
                    }
                ),
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
