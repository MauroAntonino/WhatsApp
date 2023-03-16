import abc
from repository.domain.groups import Group

class GroupOperationsInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_group(self, group_name) -> Group:
        """Get a group"""
        raise NotImplementedError

    @abc.abstractmethod
    def create_group(self, group_name, description):
        """Create a group"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def group_add_user(self, id, group_name):
        """add user to a group"""
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_messages(self, group_name):
        """get messages of a group"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_group_users(self, group_name):
        """get messages of a group"""
        raise NotImplementedError


        group_add_user