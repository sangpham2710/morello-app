from dataclasses import dataclass


@dataclass(frozen=True)
class Member:
    group_leader: str
    group_name: str
    name: str
    date_added: str
