from abc import ABC, abstractmethod
from typing import Dict, List, Tuple

from flaskr.repos.datatypes.member import Member
from flaskr.repos.datatypes.moderator import Moderator
from ..datatypes.group import Group
from ..datatypes.user import User


class AbstractGroupRepo(ABC):
    @abstractmethod
    def get_group(self, group_name: str, group_leader: str) -> Group | None:
        pass

    @abstractmethod
    def get_all_groups(self, max: int) -> List[Group]:
        pass

    @abstractmethod
    def add(self, group: Group):
        pass

    @abstractmethod
    def update(self, group: Group):
        pass

    @abstractmethod
    def delete(self, group_id: int):
        pass

    @abstractmethod
    def get_members(self, group_name: str, group_leader: str) -> List[Member] | None:
        pass

    @abstractmethod
    def get_moderators(self, group_name: str, group_leader: str) -> List[User]:
        pass

    @abstractmethod
    def get_groups_and_members(self, max: int) -> Dict[Group, List[Member]]:
        pass

    @abstractmethod
    def get_group_leader(self, group_name: str, group_leader: str) -> User | None:
        pass

    @abstractmethod
    def add_member(self, member: Member):
        pass

    @abstractmethod
    def remove_member(self, member: Member):
        pass

    @abstractmethod
    def add_moderator(self, moderator: Moderator):
        pass

    @abstractmethod
    def remove_moderator(self, moderator: Moderator):
        pass
