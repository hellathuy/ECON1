print "Employed?"
employed = float(raw_input())

print "Unemployed?"
unemployed = float(raw_input())

labor_force = employed + unemployed
rate = unemployed / labor_force

print "%r" % (rate * 100)
