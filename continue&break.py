# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 23:04:11 2016

@author: YI
"""

#continue
for i in xrange(10):
    if i % 2 != 0:
        print i 
        continue      #if the condition  is rule,
    i += 2            #start from the first statemnt
    print i
    
#break
bingo = 'I love U'
answer = raw_input('What do you want me to say?: ')

while True:
    if answer == bingo:
        break
    answer = raw_input('It is not what I want. Say it again.:')
    
print 'I love U, too'
    