# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

def get_last_element(lst):
  """print the last element of the list"""
  print(lst[-1])
  
def get_last():
  """prompt the user to input the list one element at a time"""
  lst = [] # empty list to store the elements
  elem = input("Enter an element of list and press enter to stop.")
  while elem != "":
    lst.append(elem)
    elem = input("Enter an element of list and press enter to stop.")
  return lst

def main():
  """Main function to get the list and print the last element"""
  lst  = get_last()
  get_last_element(lst)
  
if __name__ == "__main__":
  main()