import pytest
import group_up


def test_group_up_returns_correct_groups():
    collection = [{'name':'Magdalena','sex':'Female'},{'name':'Piotr', 'sex':'Male'},{'name':'Ewa','sex':'Female'},
                   {'name':'Marcin', 'sex':'Male'}, {'name':'Barbara','sex':'Female'},{'name':'Jan', 'sex':'Male'}]
    expected_result = {'Female':[{'name':'Magdalena','sex':'Female'}, {'name':'Ewa','sex':'Female'},{'name':'Barbara','sex':'Female'}], 
                        'Male':[{'name':'Piotr', 'sex':'Male'}, {'name':'Marcin', 'sex':'Male'}, {'name':'Jan', 'sex':'Male'}]} 
    result = group_up.group_up(collection,'sex')
    assert expected_result == result

