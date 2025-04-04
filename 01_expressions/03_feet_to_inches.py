# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

per_foot_inches = 12
def main():
  feet = float(input("Enter feet: "))
  inches = feet * per_foot_inches
  print(f"{feet} feet is {inches} inches")

if __name__ == "__main__":
  main()
  
  