import random
import string


def main():

    #User set the digits passwor wished then recive the secure password.

    digits_quantity = int(input("The more characters, the more secure your password. How many digits do you want in your password?s "))
    password = creat_password(digits_quantity)

    print(f"This is your new password: {password}")




def creat_password(digits):

    # Divide the the total nuber recived(digits) in five parts, two for letter, two for number and one for especial characters.
    # Mix all array itens then make this array in a string.

    letters = round((digits / 5) * 2)
    numbers = round((digits / 5) * 2)
    especial = round((digits) / 5)
        

    password = create_type_characters(letters, numbers, especial)

    random.shuffle(password) # Mix the array itens
    print(password)

    your_password = "".join(password) # Make all arrays itens mixed in one string

    return your_password

def create_type_characters(letters, numbers, especial):

    # The functio recive tree INT values the quantity of each type o Character
    # then create a tree array for number, letter and epescial tht recive a randoly character for 
    # the quantity recived and return all character in one variavel.

    random_letters = [] 
    random_numbers = []
    random_character = []
    pre_password = ""
    
    for letter in range(0, letters):
        random_letters.append(random.choice(string.ascii_letters))

    for number in range(0, numbers):
        random_numbers.append(str(random.randint(0,9)))

    for character in range(0,especial):
        random_character.append(random.choice(string.punctuation))

    pre_password = random_numbers + random_character + random_letters

    return(pre_password)
        

main()