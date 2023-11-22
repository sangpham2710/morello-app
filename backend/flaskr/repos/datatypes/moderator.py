from dataclasses import dataclass


@dataclass(frozen=True)
class Moderator:
    group_leader: str
    group_name: str
    moderator_username: str
    date_joined: str
