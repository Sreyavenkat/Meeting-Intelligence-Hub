from app.services.retrieval_service import (
    retrieve_chunks
)


results = retrieve_chunks(
    question="Who updates API documentation?",
    meeting_id=1
)


for result in results:

    print(
        "----"
    )

    print(result)