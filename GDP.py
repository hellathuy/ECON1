prompt = "> "
loop = 1

print "Hello and welcome to the GDP calculator!"

def Y(C, I, GP, NX):
    Y = C + I + GP + NX
    print "\nGDP = %.2f\n" % Y

def consumption(Y, I, GP, NX):
    consumption = Y - I - GP - NX
    print "\nCONSUMPTION = %.2f\n" % consumption

def investment(Y, C, GP, NX):
    I = Y - C - GP - NX
    print "\nINVESTMENT = %.2f\n" % I

def government(Y, C, I, NX):
    GP = Y - C - I - NX
    print "\nGOVERNMENT PURCHASES = %.2f\n" % GP

def net_exports(Y, C, I, GP):
    NX = Y - C - I - GP
    print "\nNET EXPORTS = %.2f\n" % NX


if __name__=="__main__":
    while loop == 1:

        print "What are you trying to calculate? (To quit program, press CTRL + C.)"
        print "\t1. GDP (Y)"
        print "\t2. consumption (C)"
        print "\t3. investment (I)"
        print "\t4. government purchases (GP)"
        print "\t5. net exports (NX)"

        user_input = int(raw_input(prompt))

        if user_input == 1:
            print "\nCALCULATING GDP (Y):\n"
            print "How much is consumption?",
            C = float(raw_input(prompt))

            print "How much is investment?",
            I = float(raw_input(prompt))

            print "How much are government purchases?",
            GP = float(raw_input(prompt))

            print "How much are net exports?",
            NX = float(raw_input(prompt))

            Y(C, I, GP, NX)

        elif user_input == 2:
            print "\nCALCULATING CONSUMPTION (C):\n"
            print "How much is GDP?",
            Y = float(raw_input(prompt))

            print "How much is investment?",
            I = float(raw_input(prompt))

            print "How much are government purchases?",
            GP = float(raw_input(prompt))

            print "How much are net exports?",
            NX = float(raw_input(prompt))

            consumption(Y, I, GP, NX)

        elif user_input == 3:
            print "\nCALCULATING INVESTMENT (I):\n"
            print "How much is GDP?",
            Y = float(raw_input(prompt))

            print "How much is consumption?",
            C = float(raw_input(prompt))

            print "How much are government purchases?",
            GP = float(raw_input(prompt))

            print "How much are net exports?",
            NX = float(raw_input(prompt))

            investment(Y, C, GP, NX)

        elif user_input == 4:
            print "\nCALCULATING GOVERNMENT PURCHASES (GP):\n"
            print "How much is GDP?",
            Y = float(raw_input(prompt))

            print "How much is consumption?",
            C = float(raw_input(prompt))

            print "How much is investment?",
            I = float(raw_input(prompt))

            print "How much are net exports?",
            NX = float(raw_input(prompt))

            government(Y, C, I, NX)

        elif user_input == 5:
            print "\nCALCULATING NET EXPORTS (NX):\n"
            print "How much is GDP?",
            Y = float(raw_input(prompt))

            print "How much is consumption?",
            C = float(raw_input(prompt))

            print "How much is investment?",
            I = float(raw_input(prompt))

            print "How much are government purchases?",
            GP = float(raw_input(prompt))

            net_exports(Y, C, I, GP)

        else:
            print "Please input a valid option!"
