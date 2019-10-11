# Enter your code here. Read input from STDIN. Print output to STDOUT
phone_book = dict()

def add_contact(phonebook):
  contact = phonebook.split(' ')
  contact_dict = {contact[0] : contact[1]}
  phone_book.update(contact_dict)

def query_contact(name):
  try:
    return name + '=' + phone_book[name]
  except:
    return 'Not found'

n = int(input())
for i in range(n):
  add_contact(str(input()))

for i in range(n):
  print(query_contact(str(input())))

## runtime error if n=100000