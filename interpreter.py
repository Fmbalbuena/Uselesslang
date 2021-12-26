if 1:
    x = open(sys.argv[1]).read()
    halt = False
    stack = []
    while True:
        for i in x:
            if i == " ":
                halt = True
                break
            if i.isdigit():
                stack.append(int(i))
            if i == "+":
                try:
                    stack.append(stack.pop() + stack.pop())
                except IndexError:
                    stack.append(0)
            if i == "-":
                try:
                    stack.append(stack.pop() - stack.pop())
                except IndexError:
                    stack.append(-1)
            if i == "*":
                try:
                    stack.append(stack.pop() * stack.pop())
                except IndexError:
                    stack.append(0)
            if i == "/":
                try:
                    stack.append(stack.pop() // stack.pop())
                except Exception as e:
                    if e == ZeroDivisionError:
                        stack.append(-1)
                    else:
                        stack.append(0)
            if i == ".":
                print(stack.pop(), end="")
            if i == "!":
                try:
                    print(chr(stack.pop()), end="")
                except:
                    stack.append(-1)
            if i == "`":
                s = stack.pop()
                stack.append(s)
                stack.append(s)
            if i == "=":
                try:
                    stack.append(int(stack.pop() == stack.pop()))
                except IndexError:
                    stack.append(-1)
            if i == ">":
                try:
                    stack.append(stack.pop() + 1)
                except IndexError:
                    stack.append(1)
            if i == "<":
                try:
                    stack.append(stack.pop() - 1)
                except IndexError:
                    stack.append(-1)
            if i == "G":
                try:
                    if stack.pop() > stack.pop():
                        break
                except IndexError:
                    break
            if i == "L":
                try:
                    if stack.pop() < stack.pop():
                        break
                except IndexError:
                    break
            if i == "E":
                try:
                    if stack.pop() == stack.pop():
                        break
                except IndexError:
                    break
            if i == "I":
                try:
                    stack.extend([ord(w) for w in input()])
                except:
                    stack.append(-2)
            if i == "@":
                try:
                    stack.pop()
                except IndexError:
                    pass
            if i == "}":
                try:
                    s = stack.pop()
                    stack.reverse()
                    stack.append(s)
                    stack.reverse()
                except IndexError:
                    pass
            if i == "{":
                try:
                    stack.reverse()
                    s = stack.pop()
                    stack.reverse()
                    stack.append(s)
                except IndexError:
                    pass
            if i == "^":
                try:
                    stack.reverse()
                except IndexError:
                    pass
            if i == "V":
                try:
                    stack.append(stack.pop() * -1)
                except IndexError:
                    pass
        if halt:
            break
