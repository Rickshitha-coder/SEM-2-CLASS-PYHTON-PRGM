import random
random.seed(10) #it is used to initialize
print(random.random()) 

import random
l=[12,3,4,5]
print(random.choices(l,k=2)) #it generates any 2 values


import random
l=[12,3,4,5]
random.shuffle(l)   #reorganize hte order of items
print(l)

import random
print(random.randrange(1,20)) #choose any number in the range value

import random
L=[12,13,45,67]
print(random.choice(L)) #choose the choice with in the list

import random
print(random.uniform(1,10)) #generates the floating point values with any number withiin the range

import secrets
l=[12,13,45,67]
print(secrets.choice(l))  #secrets  module which enhances the security

