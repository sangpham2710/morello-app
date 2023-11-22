from datetime import datetime
from typing_extensions import override
from flaskr.db import get_db
from flaskr.repos.datatypes.member import Member
from flaskr.repos.datatypes.moderator import Moderator
from flaskr.repos.datatypes.user import User
from flaskr.repos.interfaces.group_repo import AbstractGroupRepo
from flaskr.repos.datatypes.group import Group
from typing import List, Tuple, Dict
from . import *


class GroupRepo(AbstractGroupRepo):
    def __init__(self, db=None):
        if db is None:
            self.db = get_db()
        else:
            self.db = db

    @override
    def get_group(self, group_name: str, group_leader: str) -> Group | None:
        group = self.db.execute(
            f'SELECT p AS "p [{GROUP_TYPE_NAME}]" FROM groups WHERE name = ? AND leader = ?',
            (group_name, group_leader),
        ).fetchone()
        return group

    @override
    def get_all_groups(self, max: int) -> List[Group]:
        groups = self.db.execute(
            f'SELECT p AS "p [{GROUP_TYPE_NAME}]" FROM {GROUP_TABLE_NAME} LIMIT {max}'
        ).fetchall()
        return groups

    @override
    def add(self, group: Group):
        self.db.execute(f"INSERT INTO {GROUP_TABLE_NAME} (p) VALUES (?)", (group,))

    @override
    def update(self, group_id: int, group: Group) -> Group:
        raise NotImplementedError

    @override
    def delete(self, group_id: int) -> bool:
        raise NotImplementedError

    @override
    def get_members(self, group_name: str, group_leader: str) -> List[Member]:
        members = self.db.execute(
            f'SELECT p AS "p [{MEMBER_TYPE_NAME}]" FROM {MEMBER_TABLE_NAME} WHERE name = ? AND leader = ?',
            (group_name, group_leader),
        ).fetchall()
        return members

    @override
    def get_moderators(self, group_name: str, group_leader: str) -> List[User]:
        moderators = self.db.execute(
            f'SELECT p AS "p [{USER_TYPE_NAME}]" FROM {MODERATOR_TABLE_NAME} WHERE name = ? AND leader = ?',
            (group_name, group_leader),
        ).fetchall()
        return moderators

    @override
    def get_groups_and_members(self, max: int) -> Dict[Group, List[Member]]:
        raise NotImplementedError

    @override
    def get_group_leader(self, group_name: str, group_leader: str) -> User | None:
        rs = self.db.execute(
            f'SELECT p AS "p [{USER_TYPE_NAME}]" FROM {USER_TABLE_NAME} WHERE username = ?',
            (group_leader,),
        ).fetchone()
        return rs

    @override
    def add_member(self, member: Member):
        self.db.execute(f"INSERT INTO {MEMBER_TABLE_NAME} (p) VALUES (?)", (member,))

    @override
    def remove_member(self, member: Member):
        self.db.execute(
            f"DELETE FROM {MEMBER_TABLE_NAME} "
            + "WHERE group_name = ? AND group_leader = ? AND name = ?",
            (member.group_name, member.group_leader, member.name),
        )

    @override
    def add_moderator(self, moderator: Moderator):
        self.db.execute(
            f"INSERT INTO {MODERATOR_TABLE_NAME} (p) VALUES (p)",
            (moderator,),
        )

    @override
    def remove_moderator(self, group_name: str, group_leader: str, moderator: User):
        self.db.execute(
            f"DELETE FROM {MODERATOR_TABLE_NAME} "
            + "WHERE name = ? AND leader = ? AND moderator_username = ?",
            (group_name, group_leader, moderator.username),
        )
