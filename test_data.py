import data


def test_data_returns_persons_who_have_the_same_name():
    collection = [{'name':'piotr', 'surname':'lesisz'},{'name':'karol','surname':'lesisz'},{'name':'piotr','surname':'wasilewski'}]
    expected_result = [{'name':'piotr', 'surname':'lesisz'}, {'name':'piotr','surname':'wasilewski'}]
    result = data.data(collection,'piotr')
    assert expected_result == result
