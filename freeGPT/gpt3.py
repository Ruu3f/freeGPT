import json
import requests


class Completion:
    @staticmethod
    def create(prompt):
        """
        Create a new completion based on the given prompt.

        Args:
            prompt (str): The prompt to generate a completion for.

        Returns:
            str: The generated completion.

        Raises:
            Exception: If unable to fetch the response.
        """
        try:
            session = requests.Session()
            resp_obj = session.post(
                "https://ava-alpha-api.codelink.io/api/chat",
                headers={"Content-Type": "application/json"},
                json={
                    "model": "gpt-4",
                    "temperature": 0.6,
                    "stream": True,
                    "messages": [
                        {"role": "system", "content": "You are Ava, an AI assistant."},
                        {"role": "user", "content": prompt},
                    ],
                },
            )
        except:
            raise Exception("Unable to fetch the response.")
        resp = ""
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
                            if "delta" in choice and "content" in choice["delta"]:
                                resp += choice["delta"]["content"]
                except json.JSONDecodeError:
                    pass
        return resp
