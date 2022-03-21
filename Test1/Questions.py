def qst(arg):
    questions = {}
    questions[1] = "Question1:\nThe following decorator will:\n\ndef decorator(func):\n     @wraps(func):\n     def wrapper(*args,**kwargs):\n          return int(func(*args,**kwargs))\nreturn wrapper"
    questions[2] = "Question2:\nWhat objects can be decorated?"
    questions[3] = "Question3:\nWhat will my_func() return?\n\ndef decorator1(func):\n     @wraps(func)\n     def wrapper(*args,**kwargs):\n               return tuple(func(*args,**kwargs))\n     return wrapper\n\ndef decorator2(obj_type):\n     def decorator(func):\n          @wraps(func)\n          def wrapper(*args,**kwargs):\n               return obj_type(func(*args,**kwargs))\n          return wrapper\n     return decorator\n\n@decorator1\n@decorator2(str)\ndef my_func():\n     print('some_value')"
    questions[4]="Question4:\nWhat is the correct regular expression \nfor capturing a named group that \ncontains one word?"
    questions[5]="Question5:\nWhich of the following methods does \nnot return a Mach object?"
    questions[6]="Question6:\nWhat is the output of the following code?\n\ntext=\'Sample\'\npattern=\'(?P<text>.*)\'\nprint(re.search(pattern,text).group(0))"
    return questions[arg]
