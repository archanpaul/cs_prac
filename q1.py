# 1. Write a menu driven python program to perform PUSH, POP & display operation on stack (PRICE)
#    implement as List.
#    1) PUSH 2) POP 3) DISPLAY 4) EXIT

# Push/Append item at the top of stack
def op_push(stack, item):
    stack.append(item)


# Pop/Remove item from the top of stack
def op_pop(stack):
    if len(stack) == 0:
        # stack underflow
        return None
    else:
        return stack.pop()


# Display content of stack
def op_display(stack):
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print(stack)


def mainmenu():
    # define a stack
    stack = []

    while True:
        print("\nChoices available:")
        print("1. PUSH")
        print("2. POP")
        print("3. DISPLAY")
        print("4. EXIT")
        choice = int(input("Enter choice:"))

        if choice == 1:
            item_in = input("Enter the item:")
            op_push(stack, item_in)
        elif choice == 2:
            item_out = op_pop(stack)
            print("on_pop:", item_out)
        elif choice == 3:
            op_display(stack)
        elif choice == 4:
            print("\nExiting...")
            break


mainmenu()
