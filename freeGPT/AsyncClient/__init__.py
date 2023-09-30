from freeGPT.AsyncClient import gpt3, gpt4, alpaca_7b, falcon_40b, prodia, pollinations

textGenModels = {
    "gpt3": gpt3,
    "gpt4": gpt4,
    "alpaca_7b": alpaca_7b,
    "falcon_40b": falcon_40b,
}

imageGenModels = {"prodia": prodia, "pollinations": pollinations}


async def create_completion(model, prompt):
    if model not in textGenModels:
        raise Exception("Model not found.")
    return await textGenModels[model].Completion().create(prompt)


async def create_generation(model, prompt):
    if model not in imageGenModels:
        raise Exception("Model not found.")
    return await imageGenModels[model].Generation().create(prompt)
