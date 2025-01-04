from collections import deque
import math
def evalRPN(self, exp):
    stack=deque()
    for token in exp:
        if(len(token)==1 and not ord(token)>=48 and ord(token)<=57):
            second=stack.pop()
            first=stack.pop()
            res=0
            if(token=='/'):
                res=int(first / second)
            else:
                res=eval(str(first)+token+str(second))
            stack.append(res)
        else:
            stack.append(int(token))
    return stack.pop()
exp=["2","2","+"]
print(evalRPN(exp))

        
