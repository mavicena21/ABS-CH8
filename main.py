import shelve, os, re
a = open('C:\\latihan\\hello.txt')
b = a.read()
print(b)

a.close()
print(os.getcwd())

shelf1 = shelve.open('datakyu')
aa = list(shelf1.keys())
print(aa)
shelf1.close()

oleholehu = {'Andi': {'Apel': 12, 'Bakpao': 5, 'Coklat': 4},
             'Budi': {'Apel': 14, 'Bakpao': 4, 'Coklat': 8},
             'Cia': {'Apel': 14, 'Bakpao': 1, 'Coklat': 18},}

def printall(namadik, namakey):
    totalu = 0
    for k, v in oleholehu.items():
        totalu += v.get(namakey, 0)
    return totalu
print('Total oleh olehu')
print('Apel ' + str(printall(oleholehu, 'Apel')))
print('Bakpao ' + str(printall(oleholehu, 'Bakpao')))
print('Coklat ' + str(printall(oleholehu, 'Coklat')))

listo = ['skripsi.txt', 'skripsi final.txt', 'skripsi final final.txt', 'skripsi final final final.txt']
for i in listo:
    print(os.path.join('C:\\Users\\mavic', i))

regeksu = re.compile(r'Agent \w+')
moan = regeksu.sub('Agent xxx', 'Agent dona tidak tahu kalau Agent doni tahu kalau Agent Dona ganda dan jadinya Agent Dono mencret')
print(moan)
print(os.listdir('C:\\Users\\mavic\\Documents\\Ebook\\Chess Book'))

ab = '****Inventory*****'
print(ab.strip("*"))
print(ab.lstrip("*"))
print(ab.rstrip("*"))

for i in os.listdir('C:\\Users\\mavic\\Documents\\Ebook\\Chess Book'):
    sizef = 0
    print('Total size :')
    sizef += os.path.getsize(os.path.join('C:\\Users\\mavic\\Documents\\Ebook\\Chess Book', i))
    print(sizef)
