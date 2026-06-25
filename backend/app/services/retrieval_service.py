import os
import json
import faiss

from app.services.embedding_service import (
    create_embedding
)


def retrieve_chunks(
    question,
    meeting_id,
    top_k=3
):

    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.dirname(
                os.path.dirname(__file__)
            )
        )
    )


    vector_dir = os.path.join(
        BASE_DIR,
        "storage",
        "vector_store"
    )


    index_path = os.path.join(
        vector_dir,
        f"{meeting_id}.index"
    )


    chunks_path = os.path.join(
        vector_dir,
        f"{meeting_id}_chunks.json"
    )


    # Load FAISS index

    index = faiss.read_index(
        index_path
    )


    # Load original chunks

    with open(
        chunks_path,
        "r"
    ) as f:

        chunks = json.load(f)



    # Convert question into vector

    question_embedding = create_embedding(
        question
    )


    question_embedding = question_embedding.reshape(
        1,
        -1
    )


    # Search FAISS

    distances, indices = index.search(
        question_embedding,
        top_k
    )


    results = []


    for i in indices[0]:

        if i != -1:

            results.append(
                chunks[i]
            )


    return results