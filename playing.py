def interpret(code):
    board = [x for x in code.split("\n")]
    x,y = 0,0
    stack = []

    movement = ""
    direction, current_element = 0, board[y][x]
    while True:
        match current_element:
            case current_element if board[y][x] in "0123456789":
                stack.append(current_element)
            case "+":
                stack.append(str(int(stack[-1])+int(stack[-2])))
                stack.pop(-2)
                stack.pop(-2)
            case ">":
                direction = 1
            case "<":
                direction = 3
            case "@":
                break
        match direction:
            case 0:
                y+=1
            case 1:
                x+=1
            case 2:
                y-=1
            case 3:
                x-=1
        
        current_element = board[y][x]
    return stack

print(interpret(">25+@"))
# print(interpret('>987v>.v\nv456<  :\n>321 ^ _@'))