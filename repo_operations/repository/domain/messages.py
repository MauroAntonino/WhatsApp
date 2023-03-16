from dataclasses import dataclass, field
from repository.domain.users import User

@dataclass
class Message:
    value: str
    date: str
    user: User
    group_name: str