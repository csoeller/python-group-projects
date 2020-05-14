i = 0;
k = [];
q = [];
for i in range (x.shape[0]):
    j = i-1;
    j4 = i-4;
    m = i+1;
    m4 = i+4;
    if i > 2 and (y[i] > y[j] or y[i] == y[j]) and y[i] > y[m] and y[i] > y[j4] and y[i] > y[m4]:
        k.append(x[i]);
        q.append(i);
print(k)

plt.plot(x,y)
for i in range (len(k)):
    plt.axvline(x=k[i], color = 'red')
plt.show()

for i in range (len(k)-1):
    print ("The distance between peak", i+1, "and peak", i+2, "is: %.1f nm" %((k[i+1]-k[i])*1000))