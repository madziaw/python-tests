import compare


def test_compare_return_1_when_a_is_bigger_than_b():
    expected_result=1
    result=compare.compare(10,5)
    assert expected_result==result

def test_compare_return_minus_1_when_a_is_smaller_then_b():
    expected_result=-1
    result=compare.compare(10,15)
    assert expected_result==result

def test_compare_return_0_when_a_equal_to_b():
    expected_result=0
    result=compare.compare(10,10)
    assert expected_result==result



