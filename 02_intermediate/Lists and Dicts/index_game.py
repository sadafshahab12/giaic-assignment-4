# Index Game
def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range"


# Slicing the List:
def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Index out of range"


def index_game():
    lst = [1, 2, 3, 4, 5]
    print(f"Current list : {lst}")
    print("Choose and operation: access , modify or slice: ")
    operation = input("Enter an operation: ")

    if operation.lower() == "access":
        index = int(input("Enter index to access:"))
        print(access_element(lst, index))
    elif operation.lower() == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter a new value: ")
        print(modify_element(lst, index, new_value))
    elif operation.lower() == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(lst, start, end))
    else:
        print("Invalid operation")


def main():
    index_game()


if __name__ == "__main__":
    main()


# practice code

# def access_element():
#     num_str_list = [1, "sadaf", "sep", 97, "cookie"]
#     index = int(input("Enter index for accesssing element: "))
#     if 0 <= index < len(num_str_list):
#         if index == num_str_list.index(num_str_list[index]):
#             print(f"Element at index {index} is {num_str_list[index]}")
#             return
#     else:
#         print(f"Index {index} is out of range")


# Modifying Elements:
# def modify_element():
# num_str_list = [1, "sadaf", "sep", 97, "cookie"]
# index = int(input("Enter index for accesssing element: "))
# new_value = input("Enter a new value to replace the element: ")


# if 0 <= index < len(num_str_list):
#     num_str_list[index] = new_value
#     print(num_str_list)
#     return
# else:
#     print(f"Index {index} is out of range")