from dataclasses import dataclass, field
from domain.repository.users import User

@dataclass
class Message:
    value: str
    date: str
    user: User
    group_name: str