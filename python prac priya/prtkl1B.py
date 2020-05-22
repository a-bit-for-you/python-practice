prtkl1B: wap to demonstrate exceptional handling using zero division error

(x,y)=(50,0)
try:
    z=x/y
except ZeroDivisionError:
    print("divide by zero")
