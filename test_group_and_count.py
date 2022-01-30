import pytest
import group_and_count
import datetime


def test_group_and_count_returns_correct_result():
    collection = [(datetime.date(2021,12, 29), 10),(datetime.date(2021,12,30), 15), (datetime.date(2019,12,31), 20), (datetime.date(2020,1,1), 25), (datetime.date(2020,1,2), 30)]
    expected_result = {(2021, 12): 45, (2022, 1): 55}
    result = group_and_count.group_and_count(collection)    
    assert expected_result == result
