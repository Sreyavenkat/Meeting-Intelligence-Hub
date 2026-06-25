import ollama

from app.services.retrieval_service import (
    retrieve_chunks
)


def answer_question(
    question,
    meeting_id
):

    chunks = retrieve_chunks(
        question,
        meeting_id
    )


    context = "\n\n".join(
        chunks
    )


    prompt = f"""

You are a meeting assistant.

Answer the user question
using only the meeting context.

Context:

{context}


Question:

{question}


If the answer is not present,
say you cannot find it.

"""


    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    return response["message"]["content"]