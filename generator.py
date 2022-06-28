import random
import string
import os

password_name = input("PASSWORD NAME: ")
pass_length = int(input("PASSWORD LENGTH: \n"))

passwordgen = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "£", "$", "€", "%", "&", "/"]
final = []

for password in range(pass_length + 1):
    generated = random.choice(passwordgen)
    final.append(generated)

password_generated = str(final).replace('[', '').replace(']', '').replace(',', '').replace("'", '').replace(' ', '')


file = open("passwords.txt", "a")
file.write(password_name + ' : ' + password_generated + "\n")
file.close()

filepath = os.path.realpath(file.name)

print('PASSWORD FOR ', password_name ,' GENERATED:', password_generated, "\nPASSWORD SAVED IN: ",filepath)

