from app.services.chat_service import (
    answer_question
)


answer = answer_question(
    "Who updates API documentation?",
    1
)


print(answer)