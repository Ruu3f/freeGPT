from random import randint
from aiohttp import ClientSession


class Generation:
    async def create(prompt):
        """
        Create a new image generation based on the given prompt.

        Args:
            prompt (str): The prompt for generating the image.

        Returns:
            resp: The generated image content
        """
        params = {
            "new": "true",
            "prompt": prompt,
            "model": "Realistic_Vision_V2.0.safetensors [79587710]",
            "negative_prompt": "(nsfw:1.5),verybadimagenegative_v1.3, ng_deepnegative_v1_75t, (ugly face:0.5),cross-eyed,sketches, (worst quality:2), (low quality:2.1), (normal quality:2), lowres, normal quality, ((monochrome)), ((grayscale)), skin spots, acnes, skin blemishes, bad anatomy, DeepNegative, facing away, tilted head, {Multiple people}, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worstquality, low quality, normal quality, jpegartifacts, signature, watermark, username, blurry, bad feet, cropped, poorly drawn hands, poorly drawn face, mutation, deformed, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, extra fingers, fewer digits, extra limbs, extra arms,extra legs, malformed limbs, fused fingers, too many fingers, long neck, cross-eyed,mutated hands, polar lowres, bad body, bad proportions, gross proportions, text, error, missing fingers, missing arms, missing legs, extra digit, extra arms, extra leg, extra foot, repeating hair",
            "steps": "50",
            "cfg": "9.5",
            "seed": randint(1, 10000),
            "sampler": "Euler",
            "aspect_ratio": "square",
        }
        headers = {
            "authority": "api.prodia.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.6",
            "dnt": "1",
            "origin": "https://app.prodia.com",
            "referer": "https://app.prodia.com/",
            "sec-ch-ua": '"Brave";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Linux"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36",
        }

        async with ClientSession() as session:
            async with session.get(
                "https://api.prodia.com/generate",
                params=params,
                headers=headers,
                timeout=45,
            ) as resp:
                data = await resp.json()
                job_id = data["job"]
                while True:
                    async with session.get(
                        f"https://api.prodia.com/job/{job_id}", headers=headers
                    ) as resp:
                        json = await resp.json()
                        if json["status"] == "succeeded":
                            async with session.get(
                                f"https://images.prodia.xyz/{job_id}.png?download=1",
                                headers=headers,
                            ) as resp:
                                return await resp.content.read()
