import look_for


def test_look_for_return_minus_1_when_element_does_not_exist_in_the_list():
    l=[1,2,3,4,5]    
    expected_result=-1
    result=look_for.look_for(6,l)
    assert result==-1

def test_look_for_return_index_when_element_exist_in_the_list():
    l=[1,2,3,4,5]
    expected_result=1
    result=look_for.look_for(2,l)
    assert expected_result==result
