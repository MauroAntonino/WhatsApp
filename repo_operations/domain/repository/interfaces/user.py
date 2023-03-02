import abc
from typing import List
from domain.repository.groups import Group

class UserOperationsInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_user(self, name, password) -> Group:
        """Get an user"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_group_names_user_in(self, id) -> List:
        """Get group names a user is in"""
        raise NotImplementedError