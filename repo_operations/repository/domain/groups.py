from dataclasses import dataclass, field
from repository.domain.users import User
from repository.domain.messages import Message
from typing import List

@dataclass
class Group:
    group_name: str
    description: str
    users: List[User]
    messages: List[Message]