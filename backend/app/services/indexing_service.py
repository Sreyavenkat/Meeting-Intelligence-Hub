import os
import faiss
import json

from app.services.chunking_service import (
    chunk_text
)

from app.services.embedding_service import (
    create_embedding
)

from app.services.vector_store_service import (
    create_faiss_index
)


def build_index(
    transcript_text,
    meeting_id
):

    chunks = chunk_text(
        transcript_text
    )


    embeddings = []


    for chunk in chunks:

        vector = create_embedding(
            chunk
        )

        embeddings.append(
            vector
        )


    index = create_faiss_index(
        embeddings
    )


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


    os.makedirs(
        vector_dir,
        exist_ok=True
    )


    index_path = os.path.join(
        vector_dir,
        f"{meeting_id}.index"
    )


    faiss.write_index(
        index,
        index_path
    )

    chunks_path = os.path.join(
         vector_dir,
         f"{meeting_id}_chunks.json"
    )

    with open(
        chunks_path,
         "w"
    ) as f:
         json.dump(
             chunks,
             f,
            indent=4
         )   


    return {
        "chunks": len(chunks),
        "index_path": index_path
    }