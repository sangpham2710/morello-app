from dataclasses import dataclass


@dataclass(frozen=True)
class CollectSession:
    group_leader: str
    group_name: str
    moderator_username: str
    data_joined: str
