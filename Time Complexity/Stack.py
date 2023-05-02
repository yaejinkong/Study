class Stack:
    
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0

	
def get_token_list(expr):
    number = list('0123456789.')
    temp = []
  
    i = 0
    while i < len(expr):
        j = 1
        if expr[i] in number:
            while i + j < len(expr):
                if expr[i + j] in number:
                    j += 1
                else : 
                    break
            temp.append(''.join(expr[i:i + j]))
            i += j
        elif expr[i] in '+-*/^()':
            temp.append(expr[i])
            i += 1
        else:
            i += 1
    return temp
	
	
def infix_to_postfix(infix):
    opstack = Stack()
    outstack = []
    token_list = get_token_list(infix)  

    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3
    prec[')'] = 4

    for token in token_list:
        if token == '(':
            opstack.push(token)

        elif token == ')':
            top_token = opstack.pop()
            while top_token != '(':
                outstack.append(top_token)
                top_token = opstack.pop()

        elif token in '+-*/^':
            while (not opstack.isEmpty() and prec[opstack.top()] >= prec[token]):
                outstack.append(opstack.pop())
            opstack.push(token)

        else:
            outstack.append(token)

    while not opstack.isEmpty():
        outstack.append(opstack.pop())

    return " ".join(outstack)

	
def compute_postfix(postfix_expr):
    temp = Stack()
	
    for i in postfix_expr.split():
        if i not in "+-*/^":
            temp.push(float(i))
        else:
            operand1 = temp.top()
            temp.pop()
            operand2 = temp.top()
            temp.pop()
			
            if i == "+":
                temp.push(operand2 + operand1)
            elif i == "-":
                temp.push(operand2 - operand1)
            elif i == "*":
                temp.push(operand2 * operand1)
            elif i == "/":
                temp.push(operand2 / operand1)
            elif i == "^":
                temp.push(operand2 ** operand1)
    return temp.top()


expr = input()
postfix_expr = infix_to_postfix(expr)
value = compute_postfix(postfix_expr)
print(value)