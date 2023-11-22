from abc import ABC, abstractmethod
from typing import Dict, List
from ..datatypes.user import User
from ..datatypes.group import Group


class AbstractUserRepo(ABC):
    @abstractmethod
    def get_user(self, username: str) -> User | None:
        pass

    @abstractmethod
    def get_users(self, max: int) -> List[User]:
        pass

    @abstractmethod
    def add(self, user: User):
        pass

    @abstractmethod
    def update(self, username: str, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, username: str) -> bool:
        pass

    @abstractmethod
    def get_groups(self, username: str) -> List[Group]:
        pass

    @abstractmethod
    def get_group(
        self, username: str, group_name: str, group_leader: str
    ) -> Group | None:
        pass

    @abstractmethod
    def add_group(self, username: str, group: Group) -> bool:
        pass

    @abstractmethod
    def remove_group(self, username: str, group_name: str, group_leader: str) -> bool:
        pass

    @abstractmethod
    def get_moderated_groups(self, username: str) -> List[Group]:
        pass
