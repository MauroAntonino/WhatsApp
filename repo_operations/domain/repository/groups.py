from dataclasses import dataclass, field
from domain.repository.users import User
from domain.repository.messages import Message
from typing import List

@dataclass
class Group:
    group_name: str
    description: str
    users: List[User]
    messages: List[Message]