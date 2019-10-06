import values


def test_values_returns_new_collection_with_values_of_key():
    collection = [{'a':1,'b':2,'c':3},{'a':4,'b':5},{'b':6}]
    new_collection = [2,5,6]    
    result = values.values(collection,'b')
    assert result == new_collection


