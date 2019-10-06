import pytest
import is_correct_cut



@pytest.mark.parametrize('case',[
                        {'string':'12345','number':3,'expected_result':['123','45']},
                        {'string':'12345','number':0,'expected_result':['12345']},
                        {'string':'12345','number':2,'expected_result':['12','34','5']}])



def test_is_correct_cut(case):
   result = is_correct_cut.is_correct_cut(case['string'],case['number'])
   assert result == case['expected_result']
