import pytest
import log_in


def test_log_in_returns_True_when_name_is_start_from_big_letter_and_surname_is_start_from_big_letter_and_password_has_at_least_8_character():
    result = log_in.log_in('Magda','Lesisz','calineczka')
    assert result == True


def test_log_in_returns_False_when_name_is_start_from_small_letter_and_surname_is_start_from_smal_letter_and_password_has_less_than_8_characters():
    result = log_in.log_in('magda','lesisz','dupa')
    assert result == False



@pytest.mark.parametrize('case', [
                            {'name':'Magda','surname':'Lesisz','password':'123456789','expected_result':True},
                            {'name':'magda','surname':'Lesisz','password':'123456789','expected_result':False},
                            {'name':'Magda','surname':'lesisz','password':'123456789','expected_result':False},
                            {'name':'Magda','surname':'Lesisz','password':'1234567','expected_result':False}
])
def test_log_in_returns_correct_result(case):
    result = log_in.log_in(case['name'],case['surname'],case['password'])
    assert result == case['expected_result']
