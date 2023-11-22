from typing import Dict, List
from flaskr.db import get_db
from flaskr.repos.datatypes.collect_session import CollectSession
from flaskr.repos.datatypes.collect_session_entry import CollectSessionEntry
from flaskr.repos.datatypes.member import Member
from flaskr.repos.interfaces.collect_session_repo import AbstractCollectSessionRepo
from typing_extensions import override

from flaskr.repos.sqlite3_repos import (
    COLLECT_SESSION_ENTRY_TYPE_NAME,
    COLLECT_SESSION_TABLE_NAME,
)


class CollectSessionRepo(AbstractCollectSessionRepo):
    def __init__(self, db=None):
        if db is None:
            self.db = get_db()
        else:
            self.db = db

    @override
    def get(self, name: str, group_name: str, leader: str) -> CollectSession:
        pass

    @override
    def get_all(self, max: int) -> List[CollectSession]:
        return self.db.execute(
            f"SELECT * FROM {COLLECT_SESSION_TABLE_NAME} LIMIT ?", (max,)
        ).fetchall()

    @override
    def add(self, collect_session: CollectSession):
        self.db.execute(
            f"INSERT INTO {COLLECT_SESSION_TABLE_NAME} (session) VALUES (?)",
            (collect_session,),
        )

    @override
    def update(self, collect_session: CollectSession):
        raise NotImplementedError

    @override
    def delete(self, name: str, group_name: str, leader: str):
        raise NotImplementedError

    @override
    def get_members(
        self, collect_session_name: str, collect_session_leader: str
    ) -> Dict[CollectSession, List[Member]]:
        raise NotImplementedError

    @override
    def get_entries(
        self, name: str, group_name: str, leader: str
    ) -> List[CollectSessionEntry]:
        return self.db.execute(
            f"SELECT p AS '[p {COLLECT_SESSION_ENTRY_TYPE_NAME}]'"
            + " FROM {COLLECT_SESSION_TABLE_NAME} "
            + " WHERE name = ? AND group_name = ? AND group_leader = ?",
            (name, group_name, leader),
        ).fetchall()

    @override
    def add_entry(
        self,
        entry: CollectSessionEntry,
    ):
        self.db.execute(
            f"INSERT INTO {COLLECT_SESSION_ENTRY_TYPE_NAME} (entry) VALUES (?)",
            (entry,),
        )

    @override
    def remove_entry(
        self,
        entry: CollectSessionEntry,
    ):
        self.db.execute(
            f"DELETE FROM {COLLECT_SESSION_ENTRY_TYPE_NAME} "
            + "WHERE group_name = ? AND group_leader = ? AND session_name = ?",
            (entry.group_name, entry.group_leader, entry.session_name),
        )
