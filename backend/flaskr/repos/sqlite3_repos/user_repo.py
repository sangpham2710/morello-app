from typing import List
from flaskr.db import get_db
from flaskr.repos.datatypes.group import Group
from flaskr.repos.datatypes.user import User
from flaskr.repos.interfaces.user_repo import AbstractUserRepo
from typing_extensions import override

from flaskr.repos.sqlite3_repos import (
    GROUP_TABLE_NAME,
    GROUP_TYPE_NAME,
    USER_TABLE_NAME,
    USER_TYPE_NAME,
)


class UserRepo(AbstractUserRepo):
    def __init__(self, db=None):
        if db is None:
            self.db = get_db()
        else:
            self.db = db

    @override
    def get_user(self, username: str) -> User | None:
        self.db.execute(
            f"SELECT p AS 'p [{USER_TYPE_NAME}]' FROM {USER_TABLE_NAME} WHERE username = ?",
            (username,),
        ).fetchone()

    @override
    def get_users(self, max: int) -> List[User]:
        return self.db.execute(
            f"SELECT p AS 'p [{USER_TYPE_NAME}]' FROM {USER_TABLE_NAME} LIMIT {max}"
        ).fetchall()

    @override
    def add(self, user: User):
        self.db.execute(f"INSERT INTO users (p) VALUES (?)", (user,))

    @override
    def update(self, username: str, user: User) -> User:
        raise NotImplementedError

    @override
    def delete(self, username: str) -> bool:
        raise NotImplementedError

    @override
    def get_groups(self, username: str) -> List[Group]:
        return self.db.execute(
            f"SELECT p AS 'p [{GROUP_TYPE_NAME}]'"
            + f" FROM {GROUP_TABLE_NAME} WHERE username = ?",
            (username,),
        ).fetchall()

    @override
    def get_group(
        self, username: str, group_name: str, group_leader: str
    ) -> Group | None:
        raise NotImplementedError

    @override
    def add_group(self, username: str, group: Group):
        raise NotImplementedError

    @override
    def remove_group(self, username: str, group_name: str, group_leader: str):
        raise NotImplementedError

    @override
    def get_moderated_groups(self, username: str) -> List[Group]:
        raise NotImplementedError
