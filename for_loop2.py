student_grades={"Ananth": 9.1 , "Priya" :8.8 , "Kirithik" :7.5}

for grades in student_grades.items():
    print(grades)
"""""""""""""""""""""
#print keys
for grades in student_grades.keys():
    print(grades)

#print values
for grades in student_grades.values():
    print(grades)

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for value in phone_numbers.values():
    print(value.replace('+',"0"))

"""""""""""""""""""""""""""""""""""