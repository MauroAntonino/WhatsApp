import unittest
from adapters.utils import injector
from domain.usecases.group import group

class TestUser(unittest.TestCase):

    # def setUp(self):
    #     self.widget = Widget('The widget')

    def test_get_valid_user(self):
        resp = injector.user.get_user(name="carlos", password="123")
        if resp != None:
            self.assertEqual(True, True)
    
    def test_get_invalid_user(self):
        with self.assertRaises(Exception):
            injector.user.get_user(name="invalid", password="123")
    
    def test_usecase(self):
        group.create_group(name="carlos", password="123", group_name="bola2", description="amigos do futebol")
        resp = injector.group.get_group(group_name="bola2")
        print(resp)

if __name__ == '__main__':
    unittest.main()