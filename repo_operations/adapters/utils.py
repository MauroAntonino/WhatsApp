from adapters.mysql.group_adapter import GroupAdapter
from domain.repository.interfaces.group import GroupOperationsInterface
from adapters.mysql.user_adapter import UserAdapter
from domain.repository.interfaces.user import UserOperationsInterface

class Injector:
    def __init__(self) -> None:
        self.group :GroupOperationsInterface = GroupAdapter()
        self.user :UserOperationsInterface = UserAdapter()

injector = Injector()