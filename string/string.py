# string-ordered,immutable,text representation

# 1.concantination
str1 = 'hello'
str2 = 'world'
str3 = str1+" "+str2
print(str3)

# 2.string length
str1='hellow world'
a=len(str1)
print(a)

# 3.repetition
str1 ='hello'
a=str1*3
print(a)

# 4.string methods
# 4.1.removing white spaces/---->strip()

str = '  hello world    '
new_name = str.strip()
print(new_name)

# 4.2.lower(),upper()
new_name = 'hello world'

upper = new_name.upper()
print(upper)
lower=upper.lower()
print(lower)

# 4.3.startwith(),endwith()/TRUE FALSE return

string = 'python fullstack'
a=string.startswith('python')
print(a)
b=string.endswith('fullstack')
print(b)

# 4.4.find index of particular letter

string = 'python fullstack'
find_index=string.find('l')
print(find_index)

# 4.5.count ->occurance of that char,'l' 2 times

string = 'python fullstack'
count_finding = string.count('l')
print(count_finding)

# 4.6.replace()

str = 'hello world'
replacing = str.replace('hello','hai')
print(replacing)
print(str,"     //strings are immutable,when replacing ,str not change")

# 5- formatting strings
# 5.1- % --its traditional method
# 5.1- %s
var = 'unnikrishnan'
my_string = 'my name is %s' %var
print(my_string)

# 5.1- %d
age = 20
my_string = 'my age is %d' %age
print(my_string)

# 5.1- %f

pi = 3.14159
my_string = 'pi value is %f' %pi
print(my_string)
my_string = 'pi value is %.2f' %pi
print(my_string,"  adjusting float")

#5.2- format()

pi = 3.14159
pi_value = 'pi value is {}'.format(pi)
print(pi_value)

pi = 3.14159
pi_value = 'pi value is {:.2f}'.format(pi)
print(pi_value ,'adj float')

#5.2- f-string
pi = 3.14159
pi_value = 'pi value is {pi}'
print(pi_value,'                 using f-string')

#OUTPUT

# hello world
# 12
# hellohellohello
# hello world
# HELLO WORLD
# hello world
# True
# True
# 9
# 2
# hai world
# hello world      //strings are immutable,when replacing ,str not change
# my name is unnikrishnan
# my age is 20
# pi value is 3.141590
# pi value is 3.14   adjusting float
# pi value is 3.14159
# pi value is 3.14 adj float
# pi value is {pi}                  using f-string