from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    username: str
    password: str
    email: str
    first_name: str
    last_name: str
    date_created: str

