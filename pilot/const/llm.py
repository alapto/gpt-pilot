import os
MAX_GPT_MODEL_TOKENS = int(os.getenv('MAX_TOKENS', 8192))
MIN_TOKENS_FOR_GPT_RESPONSE = 600
MAX_QUESTIONS = 5
END_RESPONSE = "EVCLEAR"