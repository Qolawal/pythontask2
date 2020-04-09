from random import choice
from string import ascii_letters
#collect details
#Set First Name
FirstName = input(" Input your first Name: ")
#Set Last Name
LastName = input(" Input your last name: ")
#Set Email
email = input(" Input your Email: ")

from random import choice
from string import ascii_letters
#Name a vaiable called password
password = FirstName[0:2]+LastName[-2:]+"".join(choice(ascii_letters) for x in range(5))
#set password
print(password)