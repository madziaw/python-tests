import pytest
import is_delta_compression


@pytest.mark.parametrize('case',[
                                {'collection':[1,2,3,4],'expected_result':[1,1,1,1]},
                                {'collection':[1,5,9,14],'expected_result':[1,4,4,5]},
                                {'collection':[0,0,0,0],'expected_result':[0,0,0,0]}])

def test_is_delta_compression(case):
   result = is_delta_compression.is_delta_compression(case['collection'])
   assert result == case['expected_result']
