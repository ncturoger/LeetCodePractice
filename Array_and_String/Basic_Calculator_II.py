class Solution(object):
    def calculate(self, s):
        operator = []
        lastIsOperand = False
        postOrder = []
        
        priority_dict ={
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

        for c in s:
            if c != ' ':
                if c == "+" or c == "-" or c == "*" or c == "/":
                    if operator:
                        while operator and priority_dict[operator[-1]] >= priority_dict[c]:
                            postOrder.append(operator.pop())

                    operator.append(c)
                    lastIsOperand = False

                else:
                    if lastIsOperand:
                        num = postOrder.pop() * 10 + int(c)
                        postOrder.append(num)

                    else:
                        postOrder.append(int(c))
                    lastIsOperand = True
        
        while operator:
            postOrder.append(operator.pop())

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
