from app.services.chunking_service import (
    chunk_text
)

text = """
This is a sample transcript.
""" * 100


chunks = chunk_text(
    text
)

print(
    "Number of chunks:",
    len(chunks)
)

print()

print(
    "First chunk length:",
    len(chunks[0])
)