from repository.adapters.mysql.group_adapter import GroupAdapter
from repository.domain.interfaces.group import GroupOperationsInterface
from repository.adapters.mysql.user_adapter import UserAdapter
from repository.domain.interfaces.user import UserOperationsInterface

class Injector:
    def __init__(self) -> None:
        self.group :GroupOperationsInterface = GroupAdapter()
        self.user :UserOperationsInterface = UserAdapter()

injector = Injector()