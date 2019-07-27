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
    with open('SensorMeasurements.txt', 'r+b') as SensorMeasurements:
        sensor_numbers = pickle.load(SensorMeasurements)
except FileNotFoundError:
    sensor_numbers = {}

SensorMeasurements = DictionaryFileManager('SensorMeasurements.txt')
newMeasurements = SensorMeasurements.read_dictionary_from_file()
sensor_numbers.update(newMeasurements) 
    
'''This will run a loop until our GCMS range, sensorRange, until the margin of error is lower than 100,/
because if the range is higher than 100, then that means we have outliers in our data sample set.'''
while sensorRange > 100:
    SensorMeasurements = DictionaryFileManager('SensorMeasurements.txt')
    newMeasurements = SensorMeasurements.read_dictionary_from_file()
    sensor_numbers.update(newMeasurements)

    '''Our prototype will input a new measurement upon every action to make sure it's within our normal range.'''
    
    x = input('New measurement: ')
    if not x:
        pass
    else:
        y = int(input('Enter new measurement: '))
        sensor_numbers[x] = y
        SensorMeasurements.write_dictionary_to_file(sensor_numbers)
    xyz = input('Enter name to look up: ')
    if xyz in sensor_numbers:
        sensorNum = sensor_numbers[xyz]
        print(sensorNum)
    else:
        pass
    totalMeasurements = SensorMeasurements.readlines()
    sensorRange = max(totalMeasurements) - min(totalMeasurements)
'''End of sensor testing'''



'''This is the beginning of MP3 testing for verification upon descent'''
try:
    with open('mp3Measurements.txt', 'r+b') as mp3Measurements:
        mp3_numbers = pickle.load(mp3Measurements)
except FileNotFoundError:
    mp3_numbers = {}
    
mp3Measurements = DictionaryFileManager('mp3Measurements.txt')
newmp3Measurements = mp3Measurements.read_dictionary_from_file()
mp3_numbers.update(newmp3Measurements) 


'''This will run a loop until our range, sensorRange, until the margin of error is lower than 100,/
because if the range is higher than 100, then that means we have outliers in our data sample set.'''
while sensorRange > 100:
    mp3Measurements = DictionaryFileManager('mp3Measurements.txt')
    newmp3Measurements = mp3Measurements.read_dictionary_from_file()
    mp3_numbers.update(newmp3Measurements)

    '''Our prototype will input a new measurement upon every action to make sure it's within our normal range.'''
    
    x = input('New measurement: ')
    if not x:
        pass
    else:
        y = int(input('Enter new measurement: '))
        mp3_numbers[x] = y
        mp3Measurements.write_dictionary_to_file(mp3_numbers)
    xyz = input('Enter name to look up: ')
    if xyz in mp3_numbers:
        mp3Num = mp3_numbers[xyz]
        print(mp3Num)
    else:
        pass
    totalmp3Measurements = mp3Measurements.readlines()
    mp3Range = max(totalmp3Measurements) - min(totalmp3Measurements)
'''End of sensor testing'''
