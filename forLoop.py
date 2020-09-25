for letter in 'hello':
    print(letter.title())

monday_temperatures=[9.1,8.8,7.6]

for temperature in monday_temperatures:
    print(round(temperature))

print("****celsius to kelvin*************")
def celsius_to_kelvin(cels):
    return cels + 273.15

monday_temperatures = [9.1, 8.8, -270.15]
 
for temperature in monday_temperatures:
    print(celsius_to_kelvin(temperature))