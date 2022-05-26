from email import message


print ("Hello World")

x=5
y=10
y=x
print ("x=",x)
print ("y=",y)   

userFullname="Peter".upper() + "Lee".upper()
print (userFullname)

#Formatting Strings
  #using the % operator
brand='Apple'
exchangeRate=1.235235245

message='The price of this %s laptop is %d USD and the exchange rate is %4.2f USD to 1 EUR'%(brand,1299,exchangeRate)
print (message)

  #using the format() method
message='The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format('Apple',1299,1.235235245)
print (message)

#Declaring a List
userAge=[5,7,9,8,2]
userName=[]
print(userAge[2])
userAge2=userAge[2:4]
print(userAge2)

#declaring the list, list elements can be of different data types
myList1=[1,2,3,4,5,'Hello'] 

#print the entire list. 
print(myList1)                              
#You’ll get [1, 2, 3, 4, 5, “Hello”]

#print the third item (recall: Index starts from zero). 
print(myList1[2])                        
#You’ll get 3

#print the last item. 
print(myList1[-1])      
#You’ll get “Hello”

#assign myList (from index 1 to 4) to myList2 and print myList2
myList2 = myList1[1:5]
print (myList2)
#You’ll get [2, 3, 4, 5]

#modify the second item in myList and print the updated list
myList1[1] = 20
print(myList1)                              
#You’ll get [1, 20, 3, 4, 5, 'Hello']
            
#append a new item to myList and print the updated list
myList1.append('How are you')            
print(myList1)                              
#You’ll get [1, 20, 3, 4, 5, 'Hello', 'How are you']

#remove the sixth item from myList and print the updated list
del myList1[5]
print(myList1)



#Add item to the end of a list
myList3 = ['a','b','c','d']
myList3.append('e')
print (myList3)


#Delete items from a list
myList4 = ['a','b','c','d','e','f','g','h','i','j','k','l']

#delete the third item (index = 2)
del myList4[2]
print (myList4)

#delete items from index 1 to 5-1
del myList4[1:5]
print (myList4)

#delete items from index 0 to 3-1
del myList4[ :3]
print (myList4)

#delete items from index 2 to end
del myList4[2:]
print (myList4)

#Combine two lists
myList5 = [1, 2, 3, 4]
myList4.extend(myList5)
print (myList4)


#Check if an item is in a list
'c' in myList4
'e' in myList5

#Add item to a list at a particular position
myList4.insert(1,'Hi')
print (myList4)


#Find the number of items in a list
print (len(myList4))

#Get the value of an item and remove it from the list: Requires index of item as the parameter

#remove the third item
member = myList4.pop(2)
print (member)

print (myList4)

#remove the last item
member1 = myList4.pop( )
print (member1)

print (myList4)

#Remove an item from a list. Requires the value of the item as the parameter.
#remove the item ‘c’
myList4.remove('i')
print (myList4)

#Tuple
monthsOfYear = ('Jan','Feb','Mar')

#Dictionary
#dictionaryName = {'dictionary key':data}. Dictionary keys must be unique OR dictionaryName = dict (dictionary key=data)
