from time import sleep                           
from random import randint                       
import random                                    
import string                                    
                                                 
letters = random.choice(string.ascii_letters)    
print(letters)                                   
                                                 
count = 0                                        
while (count < 6):                               
        print(randint(0,9))                      
        count = count + 1                        
                                                 
sleep(30)
