s="[()]()"
def validParanthesis(s):
    mystack=[]
    mapping = {"(": ")", "{": "}", "[": "]"}
    for p in s:
        if p in('(','{','['):
            mystack.append(p)
        elif p in(')','}',']'):
            # look in to stack
            if mystack:
                topElement=mystack.pop()
                topElement=mapping[topElement]
                if topElement!=p:
                    return False
            else:
                return False
    if mystack:
        return False
    else:
        return True
        

print(validParanthesis(s))            



# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         my_stack=[]
#         mapping={"(":")","{":"}","[":"]"}
#         for p in s:
#             if my_stack:
#                 top_element=my_stack.pop()
#                 top_element=mapping[top_element]
#                 if p!=top_element:
#                     return False
#             else:
#                 my_stack.append(p)
#         return not my_stack
        

     




