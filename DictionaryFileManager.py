import pickle

class DictionaryFileManager:

    def __init__(self, fileName):
        self.filename = fileName

    def write_dictionary_to_file(self, givenDictionary):
        with open(self.filename, 'wb') as writeToFile:
            pickle.dump(givenDictionary, writeToFile)

    def read_dictionary_from_file(self):
        try:
            with open(self.filename, 'rb') as readFromFile:
                return pickle.load(readFromFile)
        except FileNotFoundError:
            x = {}
            return (x)

try:
    with open('dictionary.txt', 'r+b') as BldgDictionary:
        building_numbers = pickle.load(BldgDictionary)
except FileNotFoundError:
    building_numbers = {}


manager = DictionaryFileManager('dictionary.txt')
abc = manager.read_dictionary_from_file()
building_numbers.update(abc)

x = input('Enter new name: ')
if not x:
    pass
else:
    y = int(input('Enter new building number: '))
    building_numbers[x] = y
    manager.write_dictionary_to_file(building_numbers)

xyz = input('Enter name to look up: ')

if xyz in building_numbers:
    bldgNum = building_numbers[xyz]
    print(bldgNum)
else:
    pass
