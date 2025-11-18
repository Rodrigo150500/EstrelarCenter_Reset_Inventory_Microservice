from dataclasses import dataclass

@dataclass
class IUpdateOne:

    matched_count: int
    modifiedCount: int
    upsertedId: str | None
    upsertedCount: int