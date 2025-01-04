'''
operand--> result
"("--->push to stack
")"----> find the open (
opertor----> check the stack is empty,lower percendence mean push it to the result
'''
#infix to postfix
from collections import deque
def infix_to_postfix(infix_expr):
    stack=deque()
    postfix_expr=''
    precedence={'+':1,'-':2,'*':3,'/':2,'^':3}
    for char in infix_expr:
        if char.isalnum():
            postfix_expr+=char
        elif char =='(':
            stack.append(char)
        elif char==')':
            while stack[-1]!='(':
                postfix_expr+=stack.pop()
        else:
            while stack and stack [-1]!= '(' and precendence[char]<= precendence[stack[-1]]:
                postfix_expr+=stack.pop()
            stack.append(char)
    while stack:
        postfix_expr+=stack.pop()
    return postfix_expr                                       
exp="A*(B+C)/D"
print(infix_to_postfix(exp))



#INFIX TO PREFIX
'''

REVERSE
FLIP ()
INTFIX TO POST FIX
REVERESE THE INFIX TO POSTFIX RESULT'''
