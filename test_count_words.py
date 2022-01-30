import pytest
import count_words


@pytest.mark.parametrize('case', [
    {'string': 'ala, ma ma ma Kota', 'expected_result': {'ala': 1, 'ma': 3, 'kota': 1}},
    {'string': 'ala, Kota', 'expected_result': {'ala': 1, 'kota': 1}},
])
def test_count_words_returns_correct_result(case):
   result = count_words.count_words(case['string'])
   assert result == case['expected_result']
                                
