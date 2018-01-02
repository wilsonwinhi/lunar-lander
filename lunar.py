#Wei-Cheng Lin
#42130057
#The assignment was done alone without help

cond = True 
t = False

while cond:
    altitude = 1000
    velocity = 0
    fuel = 1000
    c = 0.15
    i=0


    while (altitude >0):
        #1. initial value
        print("Altitude:", altitude, "Current velocity:", velocity, "Fuel left", fuel)
        #2. fuel
        burn_fuel = float(input("How many liters of fuel to burn now?"))
        if burn_fuel > fuel:
            burn_fuel = fuel
            print("you don't have that many fuel left.")
        elif burn_fuel < 0:
            burn_fuel = 0
            print("you entered a number less than zero. \nIt will be 0 anyway.")
        #3. calculation                  
        velocity = velocity + 1.6 - c * burn_fuel
        altitude = altitude - velocity * 1
        fuel = fuel - burn_fuel
        i+=1

    #4. Win? Lose?
    if velocity < 10:
        print("The landing was safe.")
    else:
        print("The landing was not safe.")

    print("The landing velocity was:", velocity)
    print("The landing took", i, "seconds.")
    print("You have", fuel, "liter of fuel left.")

    #5. continue?
    while (not t):
        again = input("Again? \n'y' to continue \n'n' to end \n")
        conti = again[0]
        print(conti)
        
        if conti == "y" or conti == "Y":
            cond = True
            t = True
        elif conti == "n" or conti == "N":
            cond = False
            t = True
        else:
            t = False
            print("please enter 'n' or 'y'")
    
