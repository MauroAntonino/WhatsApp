from mysql import connector
import os

class MySql:    
    def connect(self):
        return connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DB')
        )

class Group:
    def __init__(self) -> None:
        self.get_db = MySql().connect

    def get_group(self, group_name):
        db = self.get_db()
        cursor = db.cursor()
        query = ("SELECT * FROM Groups1 WHERE name = '{name}'".format(name=group_name))

        cursor.execute(query)
        response = [item for item in cursor]
        cursor.close()
        db.close()
        try:
            response = response[0]
        except:
            raise(Exception("group not found"))
        return response
    
    def get_messages_by_group_name(self, group_name):
        try:
            db = self.get_db()
            cursor = db.cursor()
            query = ("SELECT * FROM Messages "
                    "WHERE group_name = '{group_name}'".format(group_name=group_name))

            list_of_messages  = [item for item in cursor]

            cursor.execute(query)
            cursor.close()
            db.close()

            return list_of_messages
        except:
            return []
    
    def get_users_id_in_group(self, group_name):
        try:
            db = self.get_db()
            cursor = db.cursor()
            query = ("SELECT user, group_name FROM UserGroups "
                    "WHERE group_name = '{group_name}'".format(group_name=group_name))

            cursor.execute(query)
            list_of_users  = [item[0] for item in cursor]
            cursor.close()
            db.close()

            return list_of_users
        except Exception as e:
            raise(Exception("failed to get users"))
    
    def create_group(self, name, description):
        db = self.get_db()
        cursor = db.cursor()
        query = ("INSERT INTO Groups1 ( name, description ) VALUES( '{name}', '{description}');".format(name=name, description=description))
        try:
            cursor.execute(query)
        except:
            raise Exception('Group already exists')
        db.commit()
        cursor.close()
        db.close()
        return
    
    def group_add_user(self, id, group_name):
        try:
            db = self.get_db()
            cursor = db.cursor()
            query = ("INSERT INTO UserGroups ( user, group_name ) VALUES( '{id}', '{group_name}');".format(id=id, group_name=group_name))
            cursor.execute(query)
            db.commit()
            cursor.close()
            db.close()
            return
        except:
            raise Exception("User already in the group")

class User:
    def __init__(self) -> None:
        self.get_db = MySql().connect

    def get_user(self, name, password):
        db = self.get_db()
        cursor = db.cursor()
        query = ("SELECT * FROM Users "
                "WHERE name = '{name}' AND password = '{password}'".format(name=name, password=password))

        cursor.execute(query)
        response = list(cursor)
        cursor.close()
        db.close()

        try:
            response = response[0]
        except:
            raise(Exception("password with user not found"))
        return response
    

    
    def get_groups_name_user_is_in(self, id):
        db = self.get_db()
        cursor = db.cursor()
        query = ("SELECT user, group_name FROM UserGroups "
                "WHERE user = '{user}'".format(user=id))
        cursor.execute(query)

        try: 
            results = cursor.fetchall()
            list_of_groups  = [(item[1]) for item in results]
        except:
            list_of_groups = []

        cursor.close()
        db.close()

        return list_of_groups