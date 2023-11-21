from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class CollectSessionEntry:
    group_leader: str
    group_name: str
    session_name: str
    member_name: str
    status: str
    amount: Decimal
