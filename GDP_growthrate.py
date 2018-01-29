print "Current average income?"
current_income = float(raw_input())

print "Growth rate?"
growth_rate = float(raw_input())

print "Years projected for?"
n = float(raw_input())

average_income = current_income * ((1 + growth_rate) ** n)

print "%.2f" % average_income
