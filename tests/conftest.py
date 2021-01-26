import pytest
import json


def load_jsondata(path):
    """
    Function that will load the json file and return data
    """
    with open(path) as my_data:
        data = json.load(my_data)
        return data


@pytest.fixture(params=load_jsondata("../data/test_data.json"))
def get_user(request):
    """
    Function that will request to load the json file and return data
    This has a pytest fixture params which contains the path of the file
    """
    data = request.param
    return data
