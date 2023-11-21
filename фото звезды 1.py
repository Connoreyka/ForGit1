import astropy.io.fits as pyfits
import matplotlib.pyplot as plt
hdulist = pyfits.open("v523cas60s-001(1).fit")
hdulist.info()
#exp = hdulist[0].header['exptime']
#obj = hdulist[0].header['object']
scidata = hdulist[0].data #обращение к изображению
print(scidata)
x = int(input())
y = int(input())
s = scidata[y-1][x-1] #чисто проверить value
r = int(input()) #радиус звезды(для нас - предполагаемый)
Value_x = []
Value_y = []
Ox = []
Oy = []
for i in range(x-r, x+r+1):
    Value_x.append(scidata[y-1][i-1]) #-1 потому что массив с 0, а изображение с 1
    Ox.append(i)
for i in range(y-r, y+r+1):
    Value_y.append(scidata[i-1][x-1])
    Oy.append(i)
plt.subplot(2, 1, 1)
plt.plot(Ox, Value_x)
plt.xlabel('x')
plt.ylabel('Value')
plt.title(f'Value(x) при y={y}')

plt.subplot(2, 1, 2)
plt.plot(Oy, Value_y)
plt.xlabel('y')
plt.ylabel('Value')
plt.title(f'Value(y) при x={x}')

plt.show()
hdulist.close()
