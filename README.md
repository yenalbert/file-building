# file-building

I will write a program that keeps track of who works in what building. Each person will be identified by their first name, and each building will be identified by a number. While the program is running, this information will be stored in a dictionary. When the program is not running, the information will be kept in a file.

The program does the following:

 - It asks the user for a name they'd like to add. The name can be any arbitrary string. 
 - If the user actually enters a name, the program asks them for a building number. This is an integer. 
 - It then puts an entry  in a dictionary called building_numbers (it must have that name) that has the name as the key and the building number as the value.
 - If the user just pressed enter in the first step (if they entered the empty string), the program skips the next step.
 - The program then asks the user for a name they'd like to look up. Again, the name can be any arbitrary string.
 - If the name entered in step 4 is a key in the dictionary, the program prints the associated building number. If the name is not in the dictionary, the program prints nothing.
 
Please note: this will create and write to a file called 'dictionary.txt' - and if you do not have a file with that name, the exception will handle it and create a file with that name for you.
