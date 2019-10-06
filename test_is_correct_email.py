import pytest
import is_correct_email


@pytest.mark.parametrize('case',[
                          {'email':'magda@wp.pl','expected_result':True},
                          {'email':'1@wp.pl','expected_result':False},
                          {'email':'@wp.pl','expected_result':False},
                          {'email':'m@wp.pl','expected_result':True},
                          {'email':'magda@.pl','expected_result':False},
                          {'email':'magda@wppl','expected_result':False},
                          {'email':'magda@1.1','expected_result':True},
                          {'email':'magda.wp.pl','expected_result':False},
                          {'email':'magda@w.p','expected_result':True}])



def test_is_correct_email_return_correct_result(case):
    result = is_correct_email.is_correct_email(case['email'])
    assert result == case['expected_result']
    
