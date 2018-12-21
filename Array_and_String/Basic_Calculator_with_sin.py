import math

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
            "sin": 3,
            "cos": 3,
            "tan": 3,
            "sqrt": 3
        }

        pivot = 0
        while pivot < len(s):
            print(postOrder)
            print(operator)
            c = s[pivot]
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
                    lastIsOperand = False
                
                elif c == ")":
                    if leftParaCount == 0:
                        return "Error"

                    while operator:
                        num = operator.pop()
                        if num == "(":
                            leftParaCount -= 1
                            break
                        postOrder.append(num)
                    lastIsOperand = False

                elif "a" <= c <= "z":
                    special_word = ""
                    idx = pivot
                    while idx <len(s) and "a" < s[idx] < "z":
                         special_word += s[idx]
                         idx += 1

                    if special_word == "cos" or special_word == "tan" or special_word == "sin" or special_word == "sqrt":
                        operator.append(special_word)
                        pivot = idx - 1
                    
                    else:
                        return "invalid special word"
                    lastIsOperand = False

                elif c == '.':
                    if not postOrder:
                        return "error"
                    
                    last_num = postOrder.pop()
                    float_digit = 0.1

                    idx = pivot + 1
                    while idx <len(s) and s[idx].isdigit():
                        last_num += float_digit * float(s[idx])
                        float_digit *= 0.1
                        idx += 1
                    
                    postOrder.append(last_num)
                    pivot = idx - 1
                    lastIsOperand = False

                else:
                    if lastIsOperand:
                        num = postOrder.pop() * 10 + float(c)
                        postOrder.append(num)

                    else:
                        postOrder.append(float(c))
                    lastIsOperand = True
                
            pivot += 1
        

        while operator:
            postOrder.append(operator.pop())
        if leftParaCount != 0:
            return "Error"

        print(postOrder)
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
                calculate_list.append(a/b)
            
            elif num == 'cos':
                n = calculate_list.pop()
                calculate_list.append(math.cos(n))

            elif num == 'sin':
                n = calculate_list.pop()
                calculate_list.append(math.sin(n))

            elif num == 'tan':
                n = calculate_list.pop()
                calculate_list.append(math.tan(n))

            elif num == 'sqrt':
                n = calculate_list.pop()
                calculate_list.append(math.sqrt(n))

            else:
                calculate_list.append(num)


        return calculate_list[0]

# print(Solution().calculate("5.8 + 0.12222"))
print(Solution().calculate("40 + sqrt(9)*6 + 2"))


# assert Solution().calculate("3+2*2") == 7.0
# assert Solution().calculate(" 3/2 ") == 1.5
# assert Solution().calculate(" 3+5 / 2 ") == 5.5
# assert Solution().calculate(" 10/2 ") == 5.0
# assert Solution().calculate("0+0") == 0.0
# assert Solution().calculate("40*(3+16*2)-2*7") == 1386
# assert Solution().calculate("40*(16/16*2+3-5*10+6)-2*7") == -1574
# assert Solution().calculate("40*(16/16*2+3-5*10+6-2*7") == "Error"
# assert Solution().calculate("40*16/16*2+3-5*10+6)-2*7") == "Error"
# assert Solution().calculate("40 + sin(30)") == "Error"
