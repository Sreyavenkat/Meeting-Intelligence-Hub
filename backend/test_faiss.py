from app.services.embedding_service import (
    create_embedding
)

from app.services.vector_store_service import (
    create_faiss_index
)


texts = [

    "Arjun will update API documentation",

    "Rahul will fix frontend issues",

    "Sneha will test the application"
]


embeddings = []


for text in texts:

    vector = create_embedding(
        text
    )

    embeddings.append(
        vector
    )


index = create_faiss_index(
    embeddings
)

print(
    "Vectors stored:",
    index.ntotal
)