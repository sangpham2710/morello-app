from dataclasses import dataclass


@dataclass(frozen=True)
class Group:
    leader: str
    name: str
    description: str
    date_created: str
