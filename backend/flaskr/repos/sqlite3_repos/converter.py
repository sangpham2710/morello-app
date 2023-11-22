import sqlite3

from flaskr.repos.sqlite3_repos import (
    COLLECT_SESSION_ENTRY_TYPE_NAME,
    COLLECT_SESSION_TYPE_NAME,
    GROUP_TYPE_NAME,
    MEMBER_TYPE_NAME,
    MODERATOR_TYPE_NAME,
    USER_TYPE_NAME,
)
from ..datatypes.user import User
from ..datatypes.moderator import Moderator
from ..datatypes.member import Member
from ..datatypes.group import Group
from ..datatypes.collect_session_entry import CollectSessionEntry
from ..datatypes.collect_session import CollectSession
from decimal import Decimal


def adapt_user(user: User) -> str:
    return "{};{};{};{};{};{}".format(
        user.username,
        user.password,
        user.email,
        user.first_name,
        user.last_name,
        user.date_created,
    )


def convert_user(user_str) -> User:
    data = user_str.split(";")
    return User(*data)


def adapt_moderator(moderator: Moderator) -> str:
    return "{};{};{};{}".format(
        moderator.group_leader,
        moderator.group_name,
        moderator.moderator_username,
        moderator.data_joined,
    )


def convert_moderator(moderator_str) -> Moderator:
    data = moderator_str.split(";")
    return Moderator(*data)


def adapt_member(member: Member) -> str:
    return "{};{};{};{}".format(
        member.group_leader,
        member.group_name,
        member.name,
        member.date_added,
    )


def convert_member(member_str) -> Member:
    data = member_str.split(";")
    return Member(*data)


def adapt_group(group: Group) -> str:
    return "{};{};{};{}".format(
        group.leader,
        group.name,
        group.description,
        group.date_created,
    )


def convert_group(group_str) -> Group:
    data = group_str.split(";")
    return Group(*data)


def convert_collect_session_entry(
    collect_session_entry_str,
) -> CollectSessionEntry:
    data = collect_session_entry_str.split(";")
    converted_data = [*data[:-1], Decimal(data[-1])]
    return CollectSessionEntry(*converted_data)


def adapt_collect_session_entry(collect_session_entry: CollectSessionEntry) -> str:
    return "{};{};{};{};{};{}".format(
        collect_session_entry.group_leader,
        collect_session_entry.group_name,
        collect_session_entry.session_name,
        collect_session_entry.member_name,
        collect_session_entry.status,
        collect_session_entry.amount,
    )


def adapt_collect_session(collect_session: CollectSession) -> str:
    return "{};{};{};{}".format(
        collect_session.group_leader,
        collect_session.group_name,
        collect_session.moderator_username,
        collect_session.data_joined,
    )


def convert_collect_session(collect_session_str) -> CollectSession:
    data = collect_session_str.split(";")
    return CollectSession(*data)


sqlite3.register_adapter(User, adapt_user)
sqlite3.register_converter(USER_TYPE_NAME, convert_user)
sqlite3.register_adapter(Moderator, adapt_moderator)
sqlite3.register_converter(MODERATOR_TYPE_NAME, convert_moderator)
sqlite3.register_adapter(Member, adapt_member)
sqlite3.register_converter(MEMBER_TYPE_NAME, convert_member)
sqlite3.register_adapter(Group, adapt_group)
sqlite3.register_converter(GROUP_TYPE_NAME, convert_group)
sqlite3.register_adapter(CollectSessionEntry, adapt_collect_session_entry)
sqlite3.register_converter(
    COLLECT_SESSION_ENTRY_TYPE_NAME, convert_collect_session_entry
)
sqlite3.register_adapter(CollectSession, adapt_collect_session)
sqlite3.register_converter(COLLECT_SESSION_TYPE_NAME, convert_collect_session)
