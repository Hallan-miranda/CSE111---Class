import random, string

def main():
    # print the list call append_random_number to add a default quantity of numbers print again 
    # call append_random_number add 3 new number and print the list
    numbers = [16.2, 75.1, 52.3]
    print(numbers)

    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 3)
    print(numbers)



def append_random_numbers(number_list, quantity=1):
    # recive a number list e quantity of number to add randoly in the list(the quantity default is 1)
    # then add the randoly number rounded to the list
    i = 0
    while i < quantity:
        new_number = round(random.uniform(16,75), 1)
        number_list.append(new_number)
        i += 1
    
main()

rand = random.choice(string.ascii_letters)
print(rand)