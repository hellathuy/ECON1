from sys import argv

prompt = "> "
loop = 1

print """
Hello and welcome to the Microeconomics elasticity calculator!
All calculations will be made using the midpoint method.
"""

def PED(Q1, Q2, P1, P2):
    # calculating percent change in quantity
    Qchange = Q2 - Q1
    Qaverage = (Q2 + Q1)/float(2)
    percentageChangeQD = Qchange/float(Qaverage)
    print percentageChangeQD

    # calculating percent change in price
    Pchange = P2 - P1
    Paverage = (P2 + P1)/float(2)
    percentageChangeP = Pchange/float(Paverage)

    PED = percentageChangeQD / float(percentageChangeP)

    print "\nPercentage Change in Quantity Demanded: %d" % (percentageChangeQD * 100)
    print "Percentage Change in Price: %d" % (percentageChangeP * 100)
    print "Price Elasticity of Demand: %d" % abs(PED)

#def PES():

#def IED():

#def CPED():

if __name__== "__main__":
    while loop == 1:

        print "What would you like to calculate? (To quit program, press CTRL + C.)"
        print "\t1. price elasticity of demand"
        print "\t2. price elasticity of supply"
        print "\t3. income elasticity of demand"
        print "\t4. cross-price elasticity of demand"

        user_input = int(raw_input(prompt))

        if user_input == 1:
            print "\nCALCULATING PRICE ELASTICITY OF DEMAND:\n"
            print "What is the initial quantity demanded? ",
            Q1 = int(raw_input())

            print "What is the new quantity demanded? ",
            Q2 = int(raw_input())

            print "What is the initial price? ",
            P1 = int(raw_input())

            print "What is the new price? ",
            P2 = int(raw_input())

            PED(Q1, Q2, P1, P2)

        elif user_input == 2:
            print "2"
        elif user_input == 3:
            print "3"
        elif user_input == 4:
            print "4"
        else:
            print "Please input a valid option!"
