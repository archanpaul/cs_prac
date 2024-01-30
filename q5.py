# 5. Write a menu based python program to implement a stack for the following operations
#    1) Push 2) Pop 3) Display 4)Size of stack 5) Value at top

def push(stack):
    item_in = input("Enter the item:")
    stack.append(item_in)
    print("Item pushed to Stack: ", item_in)


def pop(stack):
    if len(stack) != 0:  # check for stack underflow
        item_out = stack.pop()
        print("Item poped from Stack: ", item_out)


def display(stack):
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print(stack)


def size_of_stack(stack):
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        print("Size of the Stack:", len(stack))


def value_at_top(stack):
    if len(stack) == 0:
        print("Stack is empty.")
    else:
        item_top = stack[len(stack) - 1]
        print("value_at_top:", item_top)


def mainmenu():
    stack = []

    while True:
        print("\nChoices available:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Size of Stack")
        print("5. Value At Top")
        print("6: Exit")
        choice = int(input("Enter choice:"))

        if choice == 1:
            push(stack)
        elif choice == 2:
            pop(stack)
        elif choice == 3:
            display(stack)
        elif choice == 4:
            size_of_stack(stack)
        elif choice == 5:
            value_at_top(stack)
        elif choice == 6:
            print("\nExiting...")
            break


mainmenu()
