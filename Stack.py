#stack using python 
#using funtion push and pop and display
his=[]

def push(data):
    his.append(data)
    print(f"{data} is push")

def pop():
    if len(his)==0:
        print("stack is under flow")
    else:
        result=his.pop()
        print(f"{result} <-is delete in stack")

def display():
    print("stack is:",his)
    
    
pop()
push("my name is ankit")
push("my name is ankit kumar")

display()
