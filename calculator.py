no_1=input("Enter first number: ")
no_2=input("Enter second number: ")
operators=input("choose your operator for the operation:(+,-,/,*,%)")#tuple here
no_1=int(no_1)
no_2=int(no_2)
for operator in operators:
     if operator =="+":
         ans =no_1+no_2
         print("YOUR REQUIRED ANS IS:" + str(ans))
     elif operator =="-":
         ans = no_1 - no_2
         print("YOUR REQUIRED ANS IS:" + str(ans))
     elif operator == "/":
         ans = no_1 / no_2
         print("YOUR REQUIRED ANS IS:" + str(ans))
     elif operator =="*":
         ans = no_1 * no_2
         print("YOUR REQUIRED ANS IS:" + str(ans))
     elif operator =="%":
         ans = no_1 % no_2
         print("YOUR REQUIRED ANS IS:" + str(ans))
     else:
         print("choose valid operator")


