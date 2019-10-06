import pytest
import is_title



@pytest.mark.parametrize('case',[
                                {'string':'ala ma kota','expected_result':'Ala Ma Kota'},
                                {'string':'Ala Ma Kota','expected_result':'Ala Ma Kota'},
                                {'string':'alA mA kotA','expected_result':'Ala Ma Kota'},
                                {'string':'Ala ma kota','expected_result':'Ala Ma Kota'},
                                {'string':'ALA MA KOTA','expected_result':'Ala Ma Kota'}])


def test_is_title_return_correct_result(case):
    result = is_title.is_title(case['string']) 
    assert result == case['expected_result']
