# key-value pair,mutable,unordered,key immutable,value mutable,duplicate values  not allowed

# empty dictionary
my_dict ={}

# 1.dictionary operations (CRUD)

# 1.1 dictionary create,print and find length of created dictionary
my_dict={'name':'achu','age':20,'city':'tvm'}
print(my_dict)
print(len(my_dict))

# 1.1 get dictionary value
print(my_dict['name'])

a=my_dict.get('name')
print(a)

# 1.2  update-dictionary value
my_dict['name']='kochu'
print(my_dict)

my_dict.update({'name':'kinja'})
print(my_dict)

my_dict['age'] = {11,22}
print(my_dict)

# 1.3  delete-dictionary value
del my_dict['name']
print(my_dict)
my_dict.pop()