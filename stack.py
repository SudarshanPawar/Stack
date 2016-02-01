
def print_doc():
    print'''
Stack in python
First In Last Out

+----------+----+----+----+-------+----+------+
| Location |  0 | 1  | 2  |  ...  | ...| n-1  |
+----------+----+----+----+-------+----+------+
| Elements | E1 | E2 | E3 |  ...  | ...| En   |
+----------+----+----+----+-------+----+------+


**Operations:

1.Push(Insert stack)  2. Pop (Remove stack)

** Stack creation:
1. accept length of stack-> integer
2. store in list,if stacks added.

**Algo.: [Push]

1. Check if stack is full. If yes,return "Stack Full"
2. If stack is empty,Insert an stack & increase the count by 1

**Algo.: [Pop]

1. Check if stack is empty. If yes,return "Stack Empty"
2. If stack is full,pop stack at last location & decrease the count by 1

'''

#Create stack
length=input("Enter the stack size(n):")
i=0
stack=[]

def print_stack(stack):
    print "FINAL STACK:",stack

#PUSH
def push_operation(i,length,stack):
    print "***Push Operation***"
    while i <= length:
        el=raw_input("Enter the stack:")
        stack.insert(i,el)
        i=i+1

    print"Stack is Full!\n",stack

#POP
def pop_operation():
    stack.pop()
    print"Element Popped!"
    print "Stack:",stack
    cont=raw_input("Continue Popping?(y/n):")
    if cont=='y' or cont=='Y':
        pop_operation()
    elif cont=='n'or cont=='N':
        print_stack(stack)
        #print "Stack:",stack
    else:
        print "Invalid choice!"

#User Operation Choices
push_operation(i,length,stack)
operation_choice=raw_input("Perform POP Operation?(y/n):")
if operation_choice=='y' or operation_choice=='Y':
    pop_operation()
elif operation_choice=='n' or operation_choice=='N':
    print "No POP operation selected!"
    print_stack(stack)
else:
    print "Invalid operation Choice!"

