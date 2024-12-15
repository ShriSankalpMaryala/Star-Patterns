


for Row in range (0,5):
  for Column in range (0,Row+1):
    print("*",end=" ")
  print()


# PATTERNS 
# range(start , stop , step)

# NESTED FOR LOOPS - i j k l m

# for Row in range(65,70):      
#     for Column in range(65,Row+1):
#       print(chr(Column), end= " ") # char is used to convery a no. into a character 
#     print() # new row 
  
  

# patterns with functions
    
number = int(input("enter the number of rows you want: "))

def pattern(number):
    for Row in range (0,number):
        for Column in range (0,Row+1):
         print("*", end=" ")
        print()
        
pattern(number)