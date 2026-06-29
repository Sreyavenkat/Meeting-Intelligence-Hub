from ollama import chat
import json


MODEL = "llama3.1:8b"


def analyze_sentiment(text):

    prompt = f"""
You are a meeting sentiment analyzer.

Analyze the sentiment of the sentence below.

Classify it as:
- positive
- neutral
- negative

Rules:
- Normal updates, plans, decisions and assignments are neutral
- Problems, blockers, complaints, failures are negative
- Success, completion, approval or appreciation are positive

Return ONLY valid JSON.

Format:

{{
    "sentiment": "positive|neutral|negative"
    
}}

Sentence:
{text}
"""


    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    result = response.message.content


    return json.loads(result)