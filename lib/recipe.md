# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string `#TODO`.


## 2. Design the Function Signature

def task_tracker(text)
...check if the string contains TODO

`
   

    Parameters:
    
     the string contains text

    Returns: 
    a string to check foer presence of "TODO"

    Side effects: (state any side effects)

    N/A


```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

given a text containing "TODO
tast_tracker ("this string contains "TODO")
returns True

"""
given a text does not  contain "TODO"
tast_tracker ("this string doesnt contain "TODO")
returns False
"""
given a text in an emty string""
task_tracker ("")
returns Error message (This is an empty string)

"""
given a value that isnt a string
task_tracker (TODO1)
returns error messager("a string must be provided")
"""
extract_uppercase("HELLO WORLD") => ["HELLO", "WORLD"]

 go._

## 4. Implement the Behaviour

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
         