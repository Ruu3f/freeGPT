from freeGPT.Client import gpt3, gpt3_5, gpt4, prodia, pollinations

textGenModels = {
    "gpt3": gpt3,
    "gpt4": gpt4,
    "gpt3_5": gpt3_5,
}

imageGenModels = {"prodia": prodia, "pollinations": pollinations}


def create_completion(model, prompt):
    if model not in textGenModels:
        raise Exception("Model not found.")
    return textGenModels[model].Completion().create(prompt)


def create_generation(model, prompt):
    if model not in imageGenModels:
        raise Exception("Model not found.")
    return imageGenModels[model].Generation().create(prompt)
