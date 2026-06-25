from app.services.embedding_service import (
    create_embedding
)

vector = create_embedding(
    "Arjun will update API documentation"
)

print(type(vector))
print(len(vector))