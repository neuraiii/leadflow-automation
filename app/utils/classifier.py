from transformers import pipeline

# Load text classification pipeline
# "distilbert-base-uncased-finetuned-sst-2-english" is just a placeholder; later you can fine-tune
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def classify_lead(text: str):
    """
    Returns category label and confidence score
    """
    result = classifier(text[:512])[0]  # limit to 512 tokens
    label = result["label"]             # e.g., "POSITIVE" or "NEGATIVE"
    score = result["score"]
    return label, score
