from random import *
from string import *
letters = list(ascii_lowercase)

for i in range(20):
    company_name = ''.join([letters[random.randint(1,26)] for i in range(random.randint(1,15))])
    informations = ''.join([letters[random.randint(1,26)] for i in range(random.randint(1,15))])
