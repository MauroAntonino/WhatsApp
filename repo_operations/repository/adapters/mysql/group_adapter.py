from repository.domain.interfaces.group import GroupOperationsInterface
from repository.infra.mysql.mysql_infra import MySql, Group as db_group, User as db_user
from repository.domain.users import User
from repository.domain.groups import Group
from repository.domain.messages import Message

class GroupAdapter(GroupOperationsInterface):
    def __init__(self) -> None:
        self.group = db_group()

    def get_group(self, group_name) -> Group:
        name, description = self.group.get_group(group_name)

        return Group(
            group_name=name,
            description=description,
            messages=None,
            users=None
        )

    def create_group(self, name, description):
        self.group.create_group(name, description)
        return
    
    def group_add_user(self, id, group_name):
        self.group.group_add_user(id=id, group_name=group_name)
    
    def get_messages(self, group_name):
        messages = self.group.get_messages_by_group_name(group_name=group_name)
        return [Message(value=item[0], date=item[1], user=item[2], group_name=item[3]) for item in messages]

    def get_group_users(self, group_name):
        users = self.group.get_users_id_in_group(group_name=group_name)
        return [User(id=item, name=None, email=None, password=None) for item in users]