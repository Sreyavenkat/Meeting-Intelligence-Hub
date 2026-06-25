from app.services.indexing_service import (
    build_index
)


text = """
Meeting: Product Feature Planning

Arjun will update API documentation by Wednesday.

Rahul will fix frontend validation issues.

Sneha will verify the changes.
"""


result = build_index(
    text,
    meeting_id=1
)

print(result)