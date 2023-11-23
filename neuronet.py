from transformers import pipeline

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

    ...
    
    return classifier(text)[0]['summary_text']
