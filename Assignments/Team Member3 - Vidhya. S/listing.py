from re import L


l=[35,30,52,30,112,38,99]
l.insert(4,115) #inserts 115 at 4
print(l)
l.remove(30) #removes the first occurence of 30
print(l)
l.append(41) #inserts 41 at the end of the list
print(l)
print(sorted(l)) #prints the sorted list
print(l.pop()) #pops the last element
l.reverse() #reverses the list
print(l)