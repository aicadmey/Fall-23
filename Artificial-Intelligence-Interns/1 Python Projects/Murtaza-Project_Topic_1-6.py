mylist = []
mydict = {}
num = int(input("Enter How many words you want "))
for i in range(num):
    a = input("Enter anything ") # We use for loop for how much time we want to input
    mylist.append(a) # Our input data add in mylist 

for i in mylist:
    if i in mydict: # This will check that our word in mydict or not
        mydict[i] = mydict[i] + 1
    else:
        mydict[i] = 1
print(len(mydict),"are unique words in dictionary")
for j in mydict:
    print(mydict[j],end=" ") # This will tell us that the word will available in dictionary how much time
