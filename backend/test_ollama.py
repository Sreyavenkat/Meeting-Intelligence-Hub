from app.services.ai_service import extract_meeting_insights

sample_transcript = """
Arjun: We should launch the new dashboard next Friday.

Priya: Agreed.

Arjun: Priya, please update the API documentation before Thursday.

Priya: Sure.
"""

result = extract_meeting_insights(sample_transcript)

print(result)
print(type(result))