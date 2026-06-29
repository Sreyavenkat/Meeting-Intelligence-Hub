import re

from app.services.sentiment_ai_service import analyze_sentiment
from app.models.sentiment import Sentiment


# --------- helpers ----------

TIMESTAMP_PATTERN = re.compile(r"\[\d{2}:\d{2}:\d{2}\]\s*")
SPEAKER_PATTERN = re.compile(r"^([A-Za-z][A-Za-z0-9_ ]{0,30}):\s*(.*)")


def clean_line(line: str) -> str:
    """Remove timestamps and extra spaces."""
    line = TIMESTAMP_PATTERN.sub("", line)
    return line.strip()


def is_noise(line: str) -> bool:
    """Filter out non-dialogue content."""
    if not line:
        return True

    noise_keywords = [
        "meeting:",
        "date:",
        "participants:",
        "decisions:",
        "action items:"
        "context:"
    ]

    lower = line.lower().strip()

    if any(lower.startswith(k) for k in noise_keywords):
        return True

    # skip pure numbering like "1." "2."
    if re.fullmatch(r"\d+\.", line.strip()):
        return True

    return False


def split_sentences(text: str):
    """Basic sentence splitter."""
    return re.split(r"(?<=[.!?])\s+", text)


# --------- main function ----------

def process_sentiment(text, meeting_id, db):

    results = []

    current_speaker = None

    lines = text.split("\n")

    for line in lines:

        # Step 1: clean timestamps
        line = clean_line(line)

        if is_noise(line):
            continue

        # Step 2: detect speaker line
        match = SPEAKER_PATTERN.match(line)

        if match:
            current_speaker = match.group(1).strip()
            message = match.group(2).strip()

        else:
            message = line.strip()

        # Step 3: skip if no meaningful text
        if not message:
            continue

        # Step 4: split long sentences safely
        sentences = split_sentences(message)

        for sentence in sentences:

            sentence = sentence.strip()

            if not sentence:
                continue

            sentiment = analyze_sentiment(sentence)

            record = Sentiment(
                meeting_id=meeting_id,
                speaker=current_speaker,
                text=sentence,
                sentiment=sentiment["sentiment"],
               
            )

            db.add(record)

            results.append({
                "speaker": current_speaker,
                "text": sentence,
                "sentiment": sentiment["sentiment"],
                
            })

    db.commit()

    return results