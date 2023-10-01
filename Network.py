import random

#class A
def A():
    print("What type of network do u need? \n[1] Internet \t[2]Intranet(Private internet) \t[3]Cancel")
    i = int(input())
    if i == 1: #Internet A
        print("[1]Generate Random network ip's\t    [2]Choose network octet")
        c = int(input())
        if c == 1:
            while(1):
                print("How many ip addresses do you need? please select the amount less than or equals to 100")
                amount = int(input())
                if amount <= 100 :
                    for i in range(1, amount+1):
                        numbers = list(range(1,127))
                        excl = 10
                        if excl in numbers:
                            numbers.remove(excl)
                        first_octet = random.choice(numbers)
                        second_octet = random.randint(0,255)
                        third_octet = random.randint(0,255)
                        fourth_octet = random.randint(0,255)
                        ip = f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"
                        print(ip)
                else:
                    print("please select the amount less than or equals to 100")        
                print("press enter to take another set of ip's (or) type exit to quit")
                j = input()
                if j == "exit":
                    break
        elif c == 2:
            while(1):
                print("Choose the network octet")
                first_octet = int(input())
                if first_octet >= 1 and first_octet <= 127 :
                    if first_octet == 10:
                        print("It is a private network, please choose network in range of 1 to 127 excluding 10")
                    else:
                        print("How many ip addresses do you need? please select the amount less than or equals to 100")
                        amount = int(input())
                        if amount <= 100 :
                            for i in range(1, amount+1):
                                second_octet = random.randint(0,255)
                                third_octet = random.randint(0,255)
                                fourth_octet = random.randint(0,255)
                                ip = f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"
                                print(ip)
                        else:
                            print("please select the amount less than or equals to 100")
                        print("press enter to take another set of ip's (or) type exit to quit")
                        j = input()
                        if j == "exit":
                            break                           
                else:
                    print("Invalid input, please choose network in range of 1 to 127 excluding 10")
        else:
            print("Invalid input")
            A()

    elif i == 2: #Intranet A
        while(1):
            print("How many ip addresses do you need? please select the amount less than or equals to 100")
            amount = int(input())
            if amount <= 100 :
                for i in range(1, amount+1):
                    first_octet = 10
                    second_octet = random.randint(0,255)
                    third_octet = random.randint(0,255)
                    fourth_octet = random.randint(0,255)
                    ip = f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"
                    print(ip)
            else:
                print("please select the amount less than or equals to 100")  
            print("press enter to take another set of ip's (or) type exit to quit")
            j = input()
            if j == "exit":
                break
    elif i == 3: return
    else:
        print("Invalid input")
        A()

#class B                    
def B():
    print("What type of network do u need? \n[1] Internet \t[2]Intranet(Private internet) \t[3]Cancel")
    i = int(input())
    if i == 1: #Internet B
        print("[1]Generate Random network ip's\t    [2]Choose network octet")
        c = int(input())
        if c == 1:  #Internet Random B
            while(1):
                print("How many ip addresses do you need? please select the amount less than or equals to 100")
                amount = int(input())
                if amount <= 100 :
                    for i in range(1, amount+1):
                        numbers1 = list(range(128,192))
                        numbers2 = list(range(0,256))
                        ex_nums = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31] 
                        filtered_list = [num for num in numbers2 if num not in ex_nums]
                        first_octet = random.choice(numbers1)
                        second_octet = random.choice(filtered_list)
                        third_octet = random.randint(0,255)
                        fourth_octet = random.randint(0,255)
                        ip = f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"
                        print(ip)
                else:
                    print("please select the amount less than or equals to 100")
                print("press enter to take another set of ip's (or) type exit to quit")
                j = input()
                if j == "exit":
                    break
        elif c == 2: # Internet octet B
            while(1):
                print("Choose the first network octet")
                first_octet = int(input())
                if first_octet in range(128, 192):
                    print("Choose the second network octet")
                    second_octet = int(input())
                    if second_octet in range(1, 256):
                        if second_octet not in range(16, 32):
                            print("How many ip addresses do you need? please select the amount less than or equals to 100")
                            amount = int(input())
                            if amount <= 100 :
                                for i in range(1, amount+1):
                                    third_octet = random.randint(0,255)
                                    fourth_octet = random.randint(0,255)
                                    ip = f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"
                                    print(ip)
                            else: print("please select the amount less than or equals to 100")        
                        else:
                            print("It is a private network, please choose in range of 1 to 255 excluding [16 to 31]")    
                    else:
                        print("Invalid input, please choose in the range of 1 to 255")
                else: print("Invalid input, Choose in range of 128 to 191")        
                print("press enter to take another set of ip's (or) type exit to quit")
                j = input()
                if j == "exit":
                    break
        else:
            print("Invalid input")
            B()


    elif i == 2: #Intranet B
        print("[1]Generate Random network ip's\t    [2]Choose network octet")
        c = int(input())
        if c == 1: #Intranet Random B
            while(1):
                print("How many ip addresses do you need? please select the amount less than or equals to 100")
                amount = int(input())
                if amount <= 100 :
                    for i in range(1, amount+1):
                        first_octet = 172
                        second_octet = random.randint(16,31)
                        third_octet = random.randint(0,255)
                        fourth_octet = random.randint(0,255)
                        ip = f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"
                        print(ip)
                else: print("please select the amount less than or equals to 100")      
                print("press enter to take another set of ip's (or) type exit to quit")
                j = input()
                if j == "exit":
                    break
        elif c == 2: #Intranet choose B
            while(1):
                first_octet=172
                print("Choose the second octet value")
                second_octet = int(input())
                if second_octet in range(16, 32):
                    print("How many ip addresses do you need? please select the amount less than or equals to 100")
                    amount = int(input())
                    if amount <= 100 :
                        for i in range(1, amount+1):
                            third_octet = random.randint(0,255)
                            fourth_octet = random.randint(0,255)
                            ip = f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"
                            print(ip)
                    else: print("please select the amount less than or equals to 100")        
                else: print("Invalid, Please choose in the range of 16 to 31")
                print("press enter to take another set of ip's (or) type exit to quit")
                j = input()
                if j == "exit":
                    break
        else:
            print("Invalid input")
            B()                
    elif i == 3: return
    else:
        print("Invalid input")
        B()                             
#class C
def C():
    print("What type of network do u need? \n[1] Internet \t[2]Intranet(Private internet) \t[3]Cancel")
    i = int(input())
    if i == 1: #Internet C
        print("[1]Generate Random network ip's\t    [2]Choose network octet")
        c = int(input())
        if c == 1: #Internet Random C
            while(1):
                print("How many ip addresses do you need? please select the amount less than or equals to 100")
                amount = int(input())
                if amount <= 100 :
                    for i in range(1, amount+1):
                        numbers1 = list(range(192,224))
                        numbers2 = list(range(0,256))
                        excl = 168
                        numbers2.remove(excl) 
                        first_octet = random.choice(numbers1)
                        second_octet = random.choice(numbers2)
                        third_octet = random.randint(0,255)
                        fourth_octet = random.randint(0,255)
                        ip = f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"
                        print(ip)
                else: print("please select the amount less than or equals to 100")
                print("press enter to take another set of ip's (or) type exit to quit")
                j = input()
                if j == "exit":
                    break
        elif c == 2: #internet octet C
            while(1):
                print("Choose the first network octet")
                first_octet = int(input())
                if first_octet in range(192, 224):
                    print("Choose second octet")
                    second_octet = int(input())
                    if second_octet == 168 and first_octet == 192:
                        print("Error:192.168 is pvt network, please choose in range of 1 to 255 excluding 168 for second octet")     
                    else:
                        print("Choose the third octet")
                        third_octet = int(intput())
                        if third_octet in range(1, 256):
                            print("How many ip addresses do you need? please select the amount less than or equals to 100")
                            amount = int(input())
                            if amount <= 100:
                                for i in range(1, amount+1):
                                    fourth_octet = random.randint(0, 255)
                                    ip = f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"
                                    print(ip)
                            else: print("please select the amount less than or equals to 100")    
                        else: print("Please choose in the range of 1 to 255")        
                else: print("Error, Please choose in the range of 192 to 223")
                print("press enter to take another set of ip's (or) type exit to quit")
                j = input()
                if j == "exit":
                    break
        else:
            print("Invalid input")
            C()                        
    elif i == 2: #intranet C
        print("[1]Generate Random network ip's\t    [2]Choose network octet")
        c = int(input())
        if c == 1: #intranet random C
            while(1):
                print("How many ip addresses do you need? please select the amount less than or equals to 100")
                amount = int(input())
                if amount <= 100 :
                    for i in range(1, amount+1):
                        first_octet = 192
                        second_octet = 168
                        third_octet = random.randint(0,255)
                        fourth_octet = random.randint(0,255)
                        ip = f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"
                        print(ip)
                else: print("please select the amount less than or equals to 100")        
                print("press enter to take another set of ip's (or) type exit to quit")
                j = input()
                if j == "exit":
                    break
        elif c == 2: #intranet octet C
            first_octet = 192
            second_octet = 168
            while(1):
                print("Choose the 3rd octet value: ")
                third_octet = int(input())
                if third_octet in range(0, 255):
                    print("How many ip addresses do you need? please select the amount less than or equals to 100")
                    amount = int(input())
                    if amount <= 100 :
                        for i in range(1, amount+1):
                            fourth_octet = random.randint(0,255)
                            ip = f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}"
                            print(ip)
                    else: print("please select the amount less than or equals to 100")
                    print("press enter to take another set of ip's (or) type exit to quit")
                    j = input()
                    if j == "exit":
                        break
                else: print("Invalid input, PLease choose in the range of 0 to 255")
        else:
            print("Invalid input")
            C()        
    elif i == 3: return
    else:
        print("Invalid input")
        C()

#driver-code
print("WELCOME TO MY PORTAL")
print("==========================")
while(1):
    print("\nChoose the class u need: \n[1] class A\t [2] class B\t [3] class C\t [4]Quit \n please give either 1 or 2 or 3 as input || 4 to quit")
    b = int(input())
    if b == 1:
        A()
    elif b == 2:
        B()
    elif b == 3:
        C()     
    elif b == 4:
        print("Thank You!")
        break    
    else:
        print("Invalid input, please give either 1 or 2 or 3 or 4 as your input")            