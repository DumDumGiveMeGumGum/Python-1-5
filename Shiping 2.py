Tax1 = 1.05
Tax2 = 1.13                                         #shiping tax
Tax3 = 1.11
Tax4 = 1.12

inputNumber = float (input("Cost of your item: "))                      #cost input
country = input("What country: ")                                                  #country input
if country.lower() == "canada" :
    province = input ("What provence: ")                                        #provence input

if country.lower() == "usa" :
    print ("free 2 day shipping")
    print ("The cost of your item is ${0:.2f}".format(inputNumber))
    print ("have a nice day")


if province.lower() == "alberta" :
    Output = inputNumber*Tax1                                                       #uses your country input multipies by the tax
    print ("The cost of your item is ${0:.2f}".format(Output))
    print ("have a nice day")


if province.lower() == "ontario" :
    Output = inputNumber*Tax2
    print ("The cost of your item is ${0:.2f}".format(Output))
    print ("have a nice day")


if province.lower() == "quebec" :
    Output = inputNumber*Tax3
    print ("The cost of your item is ${0:.2f}".format(Output))
    print ("have a nice day")


if province.lower() == "bc" :
    Output = inputNumber*Tax4
    print ("The cost of your item is ${0:.2f}".format(Output))
    print ("have a nice day")


