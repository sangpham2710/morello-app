from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

from flaskr.repos.datatypes.member import Member
from ..datatypes.group import Group
from ..datatypes.user import User


class AbstractGroupRepo(ABC):
    @abstractmethod
    def get_group(self, group_id: int) -> Group | None:
        pass

    @abstractmethod
    def get_groups(self) -> List[Group]:
        pass

    @abstractmethod
    def add(self, group: Group) -> Group:
        pass

    @abstractmethod
    def update(self, group_id: int, group: Group) -> Group:
        pass

    @abstractmethod
    def delete(self, group_id: int) -> bool:
        pass

    @abstractmethod
    def get_members(
        self, group_name: str, group_leader: str
    ) -> Tuple[Group, List[User]] | None:
        pass

    @abstractmethod
    def get_moderators(
        self, group_name: str, group_leader: str
    ) -> Dict[Group, List[User]]:
        pass

    @abstractmethod
    def get_groups_and_members(self) -> Dict[Group, List[Member]]:
        pass

    @abstractmethod
    def get_group_leader(self, group_name: str, group_leader: str) -> User | None:
        pass

    @abstractmethod
    def add_member(self, member: Member) -> bool:
        pass

    @abstractmethod
    def remove_member(self, group_name: str, group_leader: str, member: Member) -> bool:
        pass

    @abstractmethod
    def add_moderator(
        self, group_name: str, group_leader: str, moderator: User
    ) -> bool:
        pass

    @abstractmethod
    def remove_moderator(
        self, group_name: str, group_leader: str, moderator: User
    ) -> bool:
        pass
