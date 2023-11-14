import matplotlib.pyplot as plt
f1 = open('PZ_Mon_v_radial_1__1.dat', 'r')
f0 = []
for line in f1:
    f = line.split()
    f0.append(f)
del f0[0]
MJD = []
Vr = []
for i in range(len(f0)):
    MJD.append(float(f0[i][0]))
    Vr.append(float(f0[i][1]))
plt.scatter(MJD, Vr, color = 'green')
plt.xlabel('MJD')
plt.ylabel('Vr')
plt.title('Vr(MJD)')
plt.show()
