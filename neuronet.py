from transformers import pipeline
LOGGING = True
repository_id = "NikitaKukuzey/Urukhan_based"

# load model from huggingface.co/models using our repository id
classifier = pipeline("summarization", model=repository_id, tokenizer=repository_id, device=0)

def predict(text: str) -> str:
    '''Prediction fuction

    Args:
        text (str): Text to summarize

    Returns:
        str: Summarized text
    '''

    ans = classifier(text)[0]['summary_text']
    if LOGGING: 
        print(f'\n\n\n\nGENERATION:\n\n"""{text}"""\n\n================>\n\n"""{ans}"""')
        with open("log.txt", "ab") as f: f.write(bytes(f'\n\n\n\nGENERATION:\n\n"""{text}"""\n\n================>\n\n"""{ans}"""', 'utf-8', 'replace'))
    return ans
