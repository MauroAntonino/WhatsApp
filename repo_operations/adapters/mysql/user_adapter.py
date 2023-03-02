from domain.repository.interfaces.group import GroupOperationsInterface
from infra.repo.mysql.mysql_infra import MySql, Group as db_group, User as db_user
from domain.repository.users import User
from domain.repository.groups import Group
from domain.repository.messages import Message

class UserAdapter():
    def __init__(self) -> None:
        self.user = db_user()

    def get_group_names_user_in(self, id):
        return self.user.get_groups_name_user_is_in(id)

    def get_user(self, name, password) -> User:
        id, name, email, password = self.user.get_user(name, password)
        return User(
            id = id,
            name = name,
            email = email,
            password = password
        )