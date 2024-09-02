for number in range (1,101):   
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (str(number) + " " + str("0" * number))  
            