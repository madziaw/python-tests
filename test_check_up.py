import check_up


def test_check_up_returns_False_when_element_in_list_is_false():
    collection = [1,2,3,4,'']
    result = check_up.check_up(collection)
    assert result == False

def test_check_up_returns_True_when_element_in_list_is_true():
    collection = [1,2,3,4]
    result = check_up.check_up(collection)
    assert result == True



