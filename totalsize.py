import os
totalsize = 0
for filename in os.listdir('C:\\Users\\mavic\\Documents\\Ebook'):
    totalsize = totalsize + os.path.getsize(os.path.join('C:\\Users\\mavic\\Documents\\Ebook', filename))

print(totalsize / 1024)