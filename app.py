# Question 1 - Resistors in Parallel 

def parallel(*resistors): # *resistors allows for multiple individual arguments
   sum_of_reciprocal = sum(1 / r for r in resistors) 
   total_resistance = 1 / sum_of_reciprocal if sum_of_reciprocal != 0 else float("inf")
   print(f"{total_resistance:.3f} ohms")
# example values   
parallel (330,1000,2200)

# Question 2 - Potential Divider
def potential_divider(voltage_supply, resistors):
    total_resistance = sum(resistors)
    for r in resistors:
        print(f"Voltage drop: {(voltage_supply*r)/ total_resistance:.2f} V")
# example values
potential_divider(9, [3000, 1000])

#Question 3 - Temperature Check 
def temperature_check(temp, degree ):
    if  degree == "F": 
#calulation from fahrenheit to celcius 
      temp =  (temp -32)*(5/9)
#Checking if the patient's temperature is normal, hypothermic or hyperthermic 
    if temp < 36:
        print("The patient is hypothermic.")
    elif 36 <= temp <= 37.5:
        print("The patient's temperature is normal.")
    else:
        print("The patient is hyperthermic.")
   
# example values  
temperature_check(14,"C")
temperature_check(37, "C")
temperature_check(37, "F")
temperature_check(38, "C")
 