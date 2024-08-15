import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  # TODO replace pass with an implementation that returns True
  # if the delimiters (), [], and {} are balanced and False otherwise.
   file = open(filename)
   text = file.read() # text == '(((((tcfh)'
   file.close()

   stack = Stack()
   print(text)

   if text == "":
     return True
   for char in text:
      if char in '([{':
       stack.push(char)
       #push to stack
       #you need three stacks: one for parentheses, one for for brackets, {[)}
      if char in ')]}':
       top_on_stack = stack.peek()
       if char ==')':
         if top_on_stack != '(':
          return False
       if char ==']':
         if top_on_stack != '[':
          return False
       if char =='}':
         if top_on_stack != '{':
          return False
       if char in '([[[[]]]{{{{}}}}]':
         if top_on_stack != '([[[[]]]{{{{}}}}]':
          return False
      stack.pop()
      print('hello')
      if len(stack) == 0:
        return True
      else:
        return False

if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


