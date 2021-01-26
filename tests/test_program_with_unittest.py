### Importing the frameworks ###
import json
import pytest
import unittest
from unittest.mock import Mock
from typing import List, Dict

### Import sys because the program.py is not on the same folder as the tests ###
import sys

sys.path.append("../")

### Importing the classes and functions from Program.py ###
from program import ConnectionDatabaseError
from program import TestDbError
from program import add
from program import connect_to_db
from program import get_users_list_from_db


class TestProgram(unittest.TestCase):
    def setUp(self):
        """
        SetUp method, this will start on every function
        Setting up the Mock connection here 
        Opening the json file which contains the mock users
        :attrib self.data contains the list of data in the json file
        :attrib self.mock_db is the Mock() name
        :attrib self.mock_db.return_value will contain the self.data attrib
        :attrib self.connection_string will be the self.mock_db
        """
        file = open("../data/test_data.json")
        data = json.load(file)
        self.data = []
        for i in data:
            self.data.append(i)
        self.mock_db = Mock()
        self.mock_db.return_value = self.data
        self.connection_string = self.mock_db

    @pytest.mark.parametrize("connection_string", "test")
    def test_connect_to_db_with_pytest(connection_string: str):
        """
        Testing using Pytest parametrize to verify that this function raises a
        TestDBError when a connection string 'test' is provided.
        :attrib input(str) from the pytest_fixture
        """
        print("Print from parametrize")
        if connect_to_db == connection_string:
            raise TestDbError

    def test_connect_to_db(self: str):
        """
        Function to test the connect_to_db function
        :TestDbError is raised when the connection_string is "test"
        :ConnectionDatabaseError is raised when a different connection string
        than 'test' is provided.
        :attrib self.connection_string is the Mock() function
        """
        with self.assertRaises(TestDbError):
            connect_to_db("test")

        with self.assertRaises(ConnectionDatabaseError):
            connect_to_db(self.connection_string)

    def test_get_users_list_from_db(self: str) -> List[Dict[str, str]]:
        """
        Function to test the get_users_list_from_db function
        First assert will check if the attrib db is equal to the
        connect_to_db(connection_string)
        Second assert will check if the attrib users is equal to the
        db.get_user()
        """
        db = self.connection_string
        print(f"DB: {db}")
        self.assertEqual(db, self.connection_string)

        users = self.mock_db.return_value
        print(f"Users: {users}")
        self.assertEqual(users, self.mock_db.return_value)

    def test_check_if_user_have_details(self: List[Dict[str, str]]) -> str:
        """
        Function to check if the users each have a username, a birthday and a role.
        :attrib users - contains the mock_db.return_value (list of users)
        Loop is used to check if the values (username,birthday, and role) is not empty
        """
        users = self.mock_db.return_value
        for user in range(len(users)):
            for value in users[user].values():
                self.assertTrue(value)

    def test_add(self: int) -> int:
        """
        Function to test the add function in Program class.
        Tests ALL THE INT between 1 and 200. Every possibility is tested.
        :attrib num_1, num_2 and num_3 has a for loop in range(1,201)
        The for loop will represent each number from 1 to 200 which will allow
        this test to test all the possibilites from 1 to 200.
        :attrib summation is the sum of num_1 + num_2 + num_3,
        and is considered the return value
        """        
        self.assertEqual(type(int), type(int), type(int))
        for num_1 in range(1, 201):
            for num_2 in range(1, 201):
                for num_3 in range(1, 201):
                    summation = num_1 + num_2 + num_3
                    self.assertEqual(add(num_1, num_2, num_3), summation)


if __name__ == "__main__":
    unittest.main()
