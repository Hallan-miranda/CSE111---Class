import csv
dictionary = {}
I_NUMBER = 0
I_NAME = 1


def main():
    found = False
    read_dictionary('week05\students.csv')
    i_number = input("Input the I_Number here: ")
    for line in dictionary:
        if line == i_number:
            print(dictionary[line])
            found = True
            break

    if found != True :
        print('No such student')


def read_dictionary(filename):
    """Read the contents of a CSV file into a
  dictionary and return the dictionary.
  Parameters
      filename: the name of the CSV file to read.
  Return: a dictionary that contains
      the contents of the CSV file.
  """
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_line in reader:
            dictionary[row_line[I_NUMBER]] = row_line[I_NAME]
    return dictionary


main()