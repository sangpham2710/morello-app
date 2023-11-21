from abc import ABC, abstractmethod
from typing import Dict, List

from click import Group

from ..datatypes.collect_session_entry import CollectSessionEntry
from ..datatypes.collect_session import CollectSession
from ..datatypes.user import User


class AbstractCollectSessionRepo(ABC):
    @abstractmethod
    def get(self, name: str, group_name: str, leader: str) -> CollectSession:
        pass

    @abstractmethod
    def get_all(self) -> List[CollectSession]:
        pass

    @abstractmethod
    def add(self, collect_session: CollectSession) -> CollectSession:
        pass

    @abstractmethod
    def update(self, collect_session: CollectSession) -> CollectSession:
        pass

    @abstractmethod
    def delete(self, name: str, group_name: str, leader: str) -> bool:
        pass

    @abstractmethod
    def get_members(
        self, collect_session_name: str, collect_session_leader: str
    ) -> Dict[CollectSession, List[User]]:
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
    def add_entry(
        self, name: str, group_name: str, leader: str, entry: CollectSessionEntry
    ) -> bool:
        pass

    @abstractmethod
    def remove_entry(
        self, name: str, group_name: str, leader: str, entry: CollectSessionEntry
    ) -> bool:
        pass
