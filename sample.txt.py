class paranthesis:
    stack=[]
    def check(self,exp):
        # i=0
        for i in exp:
            # print(i)
            if i=='(' or i=='{' or i=='[':
                paranthesis.stack.append(i)
                print(i)
            elif i==')':
                if paranthesis.stack.pop() != '(':
                    print("invalid")
                    break;
            elif i=='}':
                if paranthesis.stack.pop() != '{':
                    print("invalid")
                    break;
            elif i==']':
                if paranthesis.stack.pop() != '[':
                    print("invalid")
                    break;

        print(paranthesis.stack)
        # if len(paranthesis.stack) == 0:
        if paranthesis.stack == []:
            print("Valid")
        else:
            print("invalid")

        # print(paranthesis.stack)
p1=paranthesis()
p1.check("{()[]}{")