from abc import ABC, abstractmethod
from typing import Dict, List

from click import Group

from flaskr.repos.datatypes.member import Member

from ..datatypes.collect_session_entry import CollectSessionEntry
from ..datatypes.collect_session import CollectSession
from ..datatypes.user import User


class AbstractCollectSessionRepo(ABC):
    @abstractmethod
    def get(self, name: str, group_name: str, leader: str) -> CollectSession:
        pass

    @abstractmethod
    def get_all(self, max: int) -> List[CollectSession]:
        pass

    @abstractmethod
    def add(self, collect_session: CollectSession):
        pass

    @abstractmethod
    def update(self, collect_session: CollectSession):
        pass

    @abstractmethod
    def delete(self, name: str, group_name: str, leader: str):
        pass

    @abstractmethod
    def get_members(
        self, collect_session_name: str, collect_session_leader: str
    ) -> Dict[CollectSession, List[Member]]:
        pass

    @abstractmethod
    def get_group(self, name: str, group_name: str, leader: str) -> Group:
        pass

    @abstractmethod
    def get_entries(
        self, name: str, group_name: str, leader: str
    ) -> List[CollectSessionEntry]:
        pass

    @abstractmethod
    def add_entry(self, entry: CollectSessionEntry):
        pass

    @abstractmethod
    def remove_entry(self, entry: CollectSessionEntry):
        pass
