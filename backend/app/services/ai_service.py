from ollama import chat
import json


MODEL = "llama3.1:8b"


def extract_meeting_insights(transcript: str):

    prompt = f"""
You are a meeting assistant.

Analyze the meeting transcript below.

Extract:

1. Decisions
2. Action Items

Return ONLY valid JSON.

Do not include:
- explanations
- markdown
- code blocks
- text before or after the JSON

Format:

{{
    "decisions": [
        "decision 1",
        "decision 2"
    ],

    "action_items": [
        {{
            "responsible_person": "",
            "task": "",
            "deadline": ""
        }}
    ]
}}

Transcript:

{transcript}
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

    result = response["message"]["content"]
    
    print("\n===== OLLAMA RESPONSE =====\n")
    print(result)

    json_start = result.find("{")
    json_text = result[json_start:]

    #return result

    #return json.loads(result)

    return json.loads(json_text)