def task_tracker(text):
    if not isinstance(text, str):
        raise Exception("a string must be provided") 

    elif text == "":
        raise Exception("empty string provided")

    elif "TODO" in text:
        return True 
    else:
        return False 