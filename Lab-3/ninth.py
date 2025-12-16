# implement a stack using a list (PUSH AND POP)

def stack(list, operation, element=None):
    if operation == 'push':
        list.append(element)
    elif operation == 'pop':
        if len(list) == 0:
            return "Stack is empty"
        else:
            return list.pop()
    else:
        return "Invalid operation"