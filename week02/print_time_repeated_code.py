from datetime import datetime

firs_name = input('What is your first name? ')
second_name = input('What is your last name? ')

def print_time():
    print(f'{datetime.now()} \n')

print(firs_name)
print_time()

for x in range(0,10):
    print(x)
print_time()

