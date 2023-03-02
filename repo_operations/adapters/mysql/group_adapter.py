from domain.repository.interfaces.group import GroupOperationsInterface
from infra.repo.mysql.mysql_infra import MySql, Group as db_group, User as db_user
from domain.repository.users import User
from domain.repository.groups import Group
from domain.repository.messages import Message

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