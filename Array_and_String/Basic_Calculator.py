class Solution(object):
    def calculate(self, s):
        operator = []
        lastIsOperand = False
        postOrder = []
        leftParaCount = 0
        
        priority_dict ={
            "(": 0,
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

        for c in s:
            if c != ' ':
                if c == "+" or c == "-" or c == "*" or c == "/":
                    if operator:
                        while operator and operator[-1] != "(" and priority_dict[operator[-1]] >= priority_dict[c]:
                            postOrder.append(operator.pop())

                    operator.append(c)
                    lastIsOperand = False

                elif c == "(":
                    operator.append(c)
                    leftParaCount += 1
                
                elif c == ")":
                    if leftParaCount == 0:
                        return "Error"

                    while operator:
                        num = operator.pop()
                        if num == "(":
                            leftParaCount -= 1
                            break
                        postOrder.append(num)

                else:
                    if lastIsOperand:
                        num = postOrder.pop() * 10 + int(c)
                        postOrder.append(num)

                    else:
                        postOrder.append(int(c))
                    lastIsOperand = True
        
        while operator:
            postOrder.append(operator.pop())
        if leftParaCount != 0:
            return "Error"

        calculate_list = []
        for num in postOrder:
            if num == '+':
                b = calculate_list.pop()
                a = calculate_list.pop()
                calculate_list.append(a+b)
            
            elif num == '-':
                b = calculate_list.pop()
                a = calculate_list.pop()
                calculate_list.append(a-b)

            elif num == '*':
                b = calculate_list.pop()
                a = calculate_list.pop()
                calculate_list.append(a*b)

            elif num == '/':
                b = calculate_list.pop()
                a = calculate_list.pop()
                calculate_list.append(int(a/b))

            else:
                calculate_list.append(num)

        return calculate_list[0]




assert Solution().calculate("3+2*2") == 7
assert Solution().calculate(" 3/2 ") == 1
assert Solution().calculate(" 3+5 / 2 ") == 5
assert Solution().calculate(" 10/2 ") == 5
assert Solution().calculate("0+0") == 0
assert Solution().calculate("40*(3+16*2)-2*7") == 1386
assert Solution().calculate("40*(16/16*2+3-5*10+6)-2*7") == -1574
assert Solution().calculate("40*(16/16*2+3-5*10+6-2*7") == "Error"
assert Solution().calculate("40*16/16*2+3-5*10+6)-2*7") == "Error"
