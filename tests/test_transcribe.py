# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)
import pytest


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    test_seq_1 = "ACTGAACCC"
    test_seq_2 = "actgaaccc"
    test_seq_3 = "actGaacCc"
    test_seq_4 = ""
    test_seq_5 = "BBB"

    forward_answer = "UGACUUGGG"
    reverse_answer = "GGGUUCAGU"

    #test with reverse = false
    forward_result_1 = transcribe(test_seq_1)
    forward_result_2 = transcribe(test_seq_2)
    forward_result_3 = transcribe(test_seq_3)
    forward_result_4 = transcribe(test_seq_4)

    assert forward_result_1 == forward_answer
    assert forward_result_2 == forward_answer
    assert forward_result_3 == forward_answer
    assert forward_result_4 == ""
   
    with pytest.raises(ValueError) as forward_err:
        forward_result_5 = transcribe(test_seq_5)
    assert str(forward_err.value) == "seq contains an unrecognized charater"

    #test with reverse = true
    reverse_result_1 = transcribe(test_seq_1, reverse = True)
    reverse_result_2 = transcribe(test_seq_2, reverse = True)
    reverse_result_3 = transcribe(test_seq_3, reverse = True)
    reverse_result_4 = transcribe(test_seq_4, reverse = True)

    assert reverse_result_1 == reverse_answer
    assert reverse_result_2 == reverse_answer
    assert reverse_result_3 == reverse_answer
    assert reverse_result_4 == ""
   
    with pytest.raises(ValueError) as reverse_err:
        reverse_result_5 = transcribe(test_seq_5, reverse = True)
    assert str(reverse_err.value) == "seq contains an unrecognized charater"
    
    


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    test_seq_1 = "ACTGAACCC"
    test_seq_2 = "actgaaccc"
    test_seq_3 = "actGaacCc"
    test_seq_4 = ""
    test_seq_5 = "BBB"
    reverse_answer = "GGGUUCAGU"

    reverse_result_1 = reverse_transcribe(test_seq_1)
    reverse_result_2 = reverse_transcribe(test_seq_2)
    reverse_result_3 = reverse_transcribe(test_seq_3)
    reverse_result_4 = reverse_transcribe(test_seq_4)

    assert reverse_result_1 == reverse_answer
    assert reverse_result_2 == reverse_answer
    assert reverse_result_3 == reverse_answer
    assert reverse_result_4 == ""
   
    with pytest.raises(ValueError) as reverse_err:
        reverse_result_5 = reverse_transcribe(test_seq_5)
    assert str(reverse_err.value) == "seq contains an unrecognized charater"