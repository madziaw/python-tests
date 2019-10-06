import squares

def test_squares_return_list_that_has_lenght_equal_to_limit():
    expected_length = 5
    result = squares.squares(5)
    assert len(result) == expected_length

def test_squares_return_list_that_hes_not_last_element_equel_to_limit_squared():
    expected_result = 25
    result = squares.squares(5)
    assert expected_result != result

def test_squares_return_lista_that_hes_first_element_equel_to_zero():
    result = squares.squares(5)
    assert result[0] == 0
