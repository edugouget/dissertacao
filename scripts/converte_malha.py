import csv
with open('SENHAS.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='"')
    x = list(spamreader)
filedata = None

with open('Malha02.dxf', 'r') as file :
    filedata = file.read()

# Replace the target string
for row in x:
    print(row[0],row[1])
    filedata = filedata.replace(row[0],row[1])

# Write the file out again
with open('Malha02_saida.dxf', 'w') as file:
    file.write(filedata)
