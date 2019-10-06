import pytest
import keys1


def test_keys1_returns_correct_key():
    dictionary = {'a':1,'b':2,'c':3}
    expected_result = 'c'
    result = keys1.keys1(dictionary,3)
    assert expected_result == result


    
