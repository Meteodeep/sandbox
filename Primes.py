for num in range(10,20):     #to iterate between 10 to 20
   for i in range(2,num):    #to iterate on the factors of the number
      if num%i == 0:         #to determine the first factor
         j=num/i             #to calculate the second factor
         print('%d equals %d * %d') % (num,i,j)
         break #to move to the next number, the #first FOR
      else:                  # else part of the loop
         print (num, "is a prime number")
