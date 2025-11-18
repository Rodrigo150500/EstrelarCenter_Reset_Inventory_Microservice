from dataclasses import dataclass

@dataclass
class UpdateOneInterface:

    matched_count: int
    modifiedCount: int
    upsertedId: str | None
    upsertedCount: int