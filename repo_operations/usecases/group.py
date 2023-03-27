from repository.domain.interfaces.group import GroupOperationsInterface
from repository.domain.interfaces.user import UserOperationsInterface
from repository.domain.users import User
from utils import injector

class Group:
    def __init__(self, group: GroupOperationsInterface, user: UserOperationsInterface) -> None:
        self.group = group
        self.user = user
    
    def create_group(self, group_name, description, name, password):
        self.group.create_group(name=group_name , description=description)
        user = self.user.get_user(name, password)
        self.group.group_add_user(id=user.id, group_name=group_name)

    def get_group_messages(self, group_name):
        return self.group.get_messages(group_name=group_name)
    
    def get_groups_user_is_in(self, name, password):
        user = self.user.get_user(name, password)
        resp = self.user.get_group_names_user_in(user.id)
        list_of_groups = []
        for group_name in resp:
            group = self.group.get_group(group_name) 
            group.messages = self.group.get_messages(group_name) 
            group.users = self.group.get_group_users(group_name)

            list_of_groups.append(group)
        return list_of_groups

    def get_group_users(self, group_name):
        return self.group.get_group_users(group_name)
    
    def add_user_in_group(self, group_name, name, password):
        user = self.user.get_user(name, password)
        self.group.group_add_user(id=user.id, group_name=group_name)


group = Group(injector.group, injector.user)
