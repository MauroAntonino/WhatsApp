from dataclasses import dataclass, field

@dataclass
class User:
    id: int
    name: str
    email: str
    password: str