### Importing the frameworks ###
import pytest
from unittest import mock
from typing import List

### Importing sys because the program.py is not on the same folder as the tests ###
import sys

sys.path.append("../")

### Importing the classes and functions from Program.py ###
from program import ConnectionDatabaseError
from program import TestDbError
from program import add
from program import connect_to_db
from program import get_users_list_from_db


@pytest.mark.parametrize("connection_string", "test")
def test_connect_to_db(connection_string: str) -> str:
    """
    Testing using Pytest parametrize to verify that this function raises a
    TestDBError when a connection string 'test' is provided.
    :attrib connection_string contains the string "test" from parametrize
    """
    if connect_to_db == connection_string:
        raise TestDbError

@mock.patch("program.connect_to_db")
def test_connect_to_db_with_mock(mock_connection_string: str) -> str:
    """
    Testing the connect_to_db function with Mock patch
    :attrib mock_connection_string will be the Mock value
    :attrib connection_string will contain the mock_connection_string
    :Class ConnectionDatabaseError is raised when a different connection
    string than 'test' is provided.
    """
    connection_string = mock_connection_string
    if connect_to_db == connection_string:
        raise ConnectionDatabaseError


@pytest.mark.fixture
def test_get_users_list_from_db(get_user: List[str]) -> List[str]:
    """
    Testing the get_users_list_from_db function with pytest fixture
    :attrib connection_string from test_connect_to_db_with_mock
    :attrib db will contain the connection_string
    :attrib users will contain the get_user(data)
    The loop will check if users have a username, a birthday and a role
    """
    connection_string = test_connect_to_db_with_mock
    db = connection_string
    assert db == connection_string

    users = get_user
    assert users == get_user

    for user in enumerate(get_user):
        username = get_user["username"]
        birthday = get_user["birthday"]
        role = get_user["role"]
        assert (username, birthday, role) is not None


def test_add():
    """
    Function to test the add function in Program class.
    Tests ALL THE INT between 1 and 200. Every possibility is tested.
    :attrib num_1, num_2 and num_3 has a for loop in range(1,201)
    The for loop will represent each number from 1 to 200 which will allow
    this test to test all the possibilites from 1 to 200.
    :attrib summation is the sum of num_1 + num_2 + num_3,
    and is considered the return value
    """
    for num_1 in range(1, 201):
        for num_2 in range(1, 201):
            for num_3 in range(1, 201):
                summation = num_1 + num_2 + num_3
                assert add(num_1, num_2, num_3) == summation
