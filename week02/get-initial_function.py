

def get_intial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
       initial = name[0:1] 
    return initial

first_name= input('Enter your Fisrt namer: ')
first_name_inicial = get_intial(force_uppercase=False, name= 'hallan')

print(f'Inicial first name is {first_name_inicial}')