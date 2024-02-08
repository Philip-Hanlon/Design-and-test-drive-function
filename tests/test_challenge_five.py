import pytest
from lib.challenge_five import *

"""test to see if string contains the text TODO returns True"""
def test_text_contains_todo():
    result = task_tracker("This does contain TODO")
    assert result == True  

"""test to see if string doesnt containsthe text TODO returns False"""      

def test_text_doesnt_todo():
    result = task_tracker("This doesnt contain the right text")
    assert result == False       

"""test to return error message if empty string"""

def test_text_text_contains_empty_string():
    with pytest.raises(Exception) as e:
        task_tracker("")
    error_message = str(e.value) 
    assert error_message == "empty string provided"  

"""test to make sure a string is provided returns error message"""
def test_text_non_string():
    with pytest.raises(Exception) as e:
        task_tracker(341)
    error_message = str(e.value) 
    assert error_message == "a string must be provided"      
         