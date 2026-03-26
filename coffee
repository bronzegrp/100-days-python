mport time

#create a simulation of a coffee machine

#Menu cappuccino $5 quantity 5, latte $4 quantity 5 , espresso $10 quantity 5

transaction = True

balance = 50

coffe_machine ={
                
                "espresso" : {"price":30,
                              "water" :100,
                              "milk" : 40},

                "latte" : {"price":10,
                              "water" :100,
                              "milk" : 40
                           },

                "capuccino": {"price":10,
                              "water" :100,
                              "milk" : 40
                              
                              
                              }

                
                
                
                }



list_coffees = list(coffe_machine.keys())


while transaction:

    if balance < 10:
        print("sorry you dont have enough money!!")
        time.sleep(1)
        transaction=False
        break

    else:


        print(list_coffees)
        coffee_choice = str(input(f"what would you like to buy: "))

    if coffee_choice in list_coffees:
        for coffee in list_coffees:
            if coffee_choice == coffee:

                if coffe_machine [coffee] ["milk"] < 10 :
                    print("sorry the machine is out of milk :[")
                    transaction = False
                    time.sleep(0.5)
                    break

                elif coffe_machine [coffee] ["water"] <2:
                    print("out of water actually prob for the better")

                    transaction = False
                    time.sleep(0.5)
                    break

                else:

                    machine_status  = coffe_machine [coffee]

                    coffe_machine [coffee]["water"] -=25
                    coffe_machine [coffee]["milk"] -=10
                    balance -=10
                    print("preparing your coffee")
                    time.sleep(1)
                    print(f"Here's your {coffee} enjoy!!")

                    again = input(f"would you like to buy another coffe you have {balance} $ ,left ")

                    if again == "no":
                        transaction = False

                    elif again == "dev" :
                        print(machine_status)
                        time.sleep(1)
                        transaction = True

                    else:
                        print("preparing the next coffee ")
                        transaction= True

                

        
            











