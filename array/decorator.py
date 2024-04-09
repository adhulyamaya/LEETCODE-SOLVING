def change_greeting(func):

  def wrapper():
   
    return "Hai world"
  return wrapper

@change_greeting
def print_hello_world():
  print("Hello world")


print(print_hello_world())