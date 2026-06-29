from ollama import chat
import json
import re


MODEL = "llama3.1:8b"


def extract_meeting_insights(transcript: str):

    prompt = f"""
You are a meeting assistant.

Analyze the meeting transcript below.

Extract:

1. Decisions
2. Action Items

Rules:
- A decision is a finalized choice or agreement made by the participants.
- A decision must represent something that was decided, approved, selected, or committed.
- Do NOT include suggestions, ideas, goals, reasons, strategies, or discussions as decisions.
- If there are no clear decisions, return an empty list.
- If a statement is only a discussion, suggestion, question, or future possibility, do not include it.
- An action item is a task assigned to a person.
- Do not convert hypothetical statements, risks, concerns, or conditions into action items.
- Only extract action items when someone explicitly agrees to do something or someone assigns a task.
- Include deadlines if mentioned.
- Do not create action items that are not explicitly assigned.

Return ONLY a valid JSON object.

Do NOT:
- add explanations
- add markdown
- use ```json
- add text before or after the JSON

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


    result = response.message.content


    print("\n===== OLLAMA RESPONSE =====\n")
    print(result)


    # Extract JSON safely
    match = re.search(
        r"\{[\s\S]*\}",
        result
    )


    if not match:
        raise ValueError(
            "Ollama did not return valid JSON"
        )


    json_text = match.group(0)


    try:
        return json.loads(json_text)

    except json.JSONDecodeError as e:
        print("JSON parsing failed")
        print(json_text)
        raise e