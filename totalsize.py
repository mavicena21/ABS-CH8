import os, re
totalsize = 0
for filename in os.listdir('C:\\Users\\mavic\\Documents\\Ebook'):
    totalsize = totalsize + os.path.getsize(os.path.join('C:\\Users\\mavic\\Documents\\Ebook', filename))

print(totalsize / 1024)

a = {'apel': 3, 'donat': 2, 'coklat': 5, 'roti': 2}
def hargabarang(namadik, kiri, kanan):
    print('Harga'.center(kiri + kanan, '-'))
    for k, v in namadik.items():
        print(k.ljust(kiri, '-') + str(v).rjust(kanan, '-'))

hargabarang(a, 10, 5)

b = re.compile(r'bat(wo)?man')
bmo = b.search('za adventuro of batwoman')
print(bmo.group())

c = re.compile(r'bat(man|car|plane)')
cmo = c.search('batman batcar batplane')
cfindal = c.findall('batman batcar batplane lololol')
print(cmo.group())
print(cfindal)
listu = [1, 9, 2, 4, 6, 7, 3]
d = listu.sort()
print(d)