Principal_amount = eval(input("Enter principle amount: "))
Rate_of_interest = eval(input("Enter annual rate: "))
Time = eval(input("Enter time (in years): "))
Amount = Principal_amount*(1+(Rate_of_interest/100)*Time)
print("Total ammount =",int(round(Amount,2)))
