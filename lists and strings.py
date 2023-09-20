list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) #prints ["a","b”,”c”,1,2,3]

b=["hello"]
output_list = b*2
print(output_list) # outputs ["hello","hello"]

My_string = 'hello'
#Make My_string uppercase and store it in a new variable:
My_string_upper = My_string.upper()
print(My_string_upper) # output is 'HELLO'
#Make My_string uppercase and store it in the old variable
My_string = My_string.upper()
print(My_string) # output is 'HELLO'

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#Change more than one item at a time
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.\n")
lst=[ 1, 6, 3, 5, 3, 4 ]
if 7 in lst:
  print("7 is in lst")
else:
  print("7 is not in lst")
  
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.\n")
lst=[ 1, 6, 3, 5, 3, 4 ]
if 7 not in lst:
  print("7 is not in lst")
else:
  print("7 is in lst")
 