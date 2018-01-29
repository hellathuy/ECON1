print "Unemployed?"
unemployed = float(raw_input())

print "Discouraged?"
discouraged = float(raw_input())

print "Labor force?"
labor_force = float(raw_input())

U4 = (unemployed + discouraged) / (labor_force + discouraged)

print "%.2f" % (U4 * 100)
