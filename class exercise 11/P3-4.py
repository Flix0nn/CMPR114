import sqlite3



conn = sqlite3.connect('/Users/tobisho/cmpr114/class exercise 9/CLSEX9.db')
cur = conn.cursor()

cur.execute('''SELECT * FROM patients;''')
results = cur.fetchall()

print("Patients:\n")
print(f'{"PatientId":<9} {"Name":<8} {"Birthdate":<8} {"Doctorid"}')
for row in results:
    print(f'{row[0]:<9} {row[1]:<8} {row[2]:<9} {row[3]}')


print("-------------------------------------------------------------------------")

cur.execute('''SELECT * FROM prescriptions''')
results1 = cur.fetchall()

print("Prescriptions:\n")
print(f'{"PrescriptionsId":<12} {"PatientID":<10} {"DoctorId":<8} {"PerscriptionDate":<3} {"DrugCode"}')
for row in results1:
    print(f'{row[0]:<15} {row[1]:<10} {row[2]:<8} {row[3]:<16} {row[4]}')

print("-------------------------------------------------------------------------")

cur.execute('''SELECT * FROM doctors''')
results2 = cur.fetchall()

print("Doctors:\n")
print(f'{"Doctorid":<9} {"Name":<8} {"Birthdate":<10} {"License"}')
for row in results:
    print(f'{row[0]:<9} {row[1]:<8} {row[2]:<10} {row[3]}')

conn.close()