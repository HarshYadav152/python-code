# Dictionary is the collection of key value pair
# Dictionary can store multiple datatype string ,numbers ,floats and even lists ,tuples and dictionary

# it is unordered
myDict = {
    "Fast":"In a quick manner",
    "Harsh":"A coder",
    "Marks":[1,2,3],
    "tup":(1,2),
    "Rollno":101,
    "AnotherDictionary": {"Harsh":"Coder"},
    1:'a'
}
print(myDict['AnotherDictionary' ])
dictionary = { 1:'a',2:'b',3:'c'}
# print(dictionary[1])
# print(myDict['Fast'])
# print(myDict['Harsh'])
# print(myDict['Marks'])
# print(myDict['Rollno'])

# print(myDict['AnotherDictionary']['Harsh']) # accessing the nested dictionary

# it is mutale
# indexed
# can't have duplicate ( else it overwrite existing value )
# myDict['Marks'] = [10,20,30]
# print(myDict['Marks']) # marks change

# methods
#.keys() prints the keys of the list 
t = myDict.keys()
print(type(t))
print(myDict.keys()) # it give output as list but its type is not a list type
# print(type(myDict.keys()))

# .values() prints the values 
t = myDict.values()
print(type(t))
print(myDict.values())

# .items() print the (key,value) for all content of the dictionary
t = myDict.items()
print(type(t))
print(myDict.items())

# .update(another_dictionary) the dictionary by adding the (key:value) pair to the original dictionary
updateDictionary = {
    "Sengar":"P"
}

myDict.update(updateDictionary) 
print(myDict)

# whatif we add already added item to the dictionary
myDict.update({'Sengar':'ps'}) # it will overwrite the dictionary content
# print(myDict)

# .get(key) give the value of the corresponding key otherwise return the none
# print(myDict.get('Sengar')) # prints the corressponding value to the specified key 
# print(myDict['Sengar']) # prints the corressponding value to the specified key 
# print(myDict.get('Sengar1')) # but it is not
# print(myDict['Sengar1']) # it will trown an error since Sengar1 in not in the myDict keys

print(myDict.get(1))

print(len(myDict))
print(len({1:'a',2:'b'}))

dict_Using_constructor = dict(name = 'harsh' , age = 91)
print(dict_Using_constructor)