# Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.
def main ():
  fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
  length_fruit_list = len(fruit_list)
  print(length_fruit_list)
  fruit_list.append("mango")
  print(fruit_list)
  
if __name__ == "__main__":
  main()