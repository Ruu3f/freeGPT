from json import loads, JSONDecodeError
from requests import post, exceptions


class Completion:
    """
    This class provides methods for generating completions based on prompts.
    """

    async def create(prompt):
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
            resp_obj = post(
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
                timeout=30,
            )
        except exceptions.RequestException:
            raise Exception("Unable to fetch the response.")

        resp = ""
        for line in resp_obj.iter_lines():
            line_text = line.decode("utf-8").strip()
            if line_text.startswith("data:"):
                data = line_text.split("data:")[1]
                try:
                    data_json = loads(data)
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
                except JSONDecodeError:
                    pass
        return resp
