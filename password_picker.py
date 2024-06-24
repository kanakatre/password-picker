# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:14:07 2024

@author: LENOVO
"""

import random 

import string 

adjectives= ['sleepy', 'slow', 'smelly', 
             'wet','fat','red',
             'orange','yellow', 'green',
             'blue', 'purple','fluffy'
             'white', 'proud', 'brave']

nouns= ['apple', 'dinosaur', 'ball'
        'toaster','goat','dragon'
        'hammer','duck''panda']

print ('welcome to password picker!')

adjective=random.choice(adjectives)
noun=random.choice(nouns)

number=random.randrange(0,100)
special_char=random.choice(string.punctuation)

password=adjective+noun+str (number)+special_char
print('your new password is: %s' % password)


