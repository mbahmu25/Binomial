import math
strt = int(input("Jumlah Sampel / X = "))
c = input("Peluang benar = ")
a = strt + 1

for i in c:

    if i == '/':
        g = 0
        c1 = 0
        c2 = 0
        c = str(c)
        for i in c:
            g +=1
            if i =='/':
                g -= 1
                c1  =  c[:g]
                g = 0 
                c1 = int(c1)
                break
        pass
        c = c[::-1]
        for i in c:
            g +=1
            if i =='/':
                g -= 1
                c2  =  c[:g]
                c2 = int(c2[::-1])
                break
        c = round(float(c1/c2),4)
        break

    elif i == '.' :
        c = float(c)
        pass

print("----------------------------------------")
pilihan = int(input("1. Sebaran Distribusi Binomial \n2. Distribusi Binomial \n3. Distribusi Binomial Kumulatif\nPilihan = "))
print("----------------------------------------")
if pilihan == 1:
    x = 0
    while x<a:
        result = (math.comb(strt,x)*(c**x)*((1-c)**(strt-x)))
        result = round(result,4)
        print("f(",x,") = ",result)
        x += 1
        if x==a :
            break
elif pilihan == 2:
    x = int(input("x = "))
    result = (math.comb(strt,x)*(c**x)*((1-c)**(strt-x)))
    result = round(result,4)
    print("f(",x,") = ", result)

elif pilihan == 3:
    x = int(input("x = "))
    tanda = input("< / > = ")
    p = 0
    xt = x + 1
    temp = 0
    if tanda == '<':
        while p<xt:
            result = (math.comb(strt,p)*(c**p)*((1-c)**(strt-p)))
            temp = temp + result
            p += 1
            if p==xt :
                temp = round(temp,4)
                print("P(X <=",x,") = ", temp)
                break
    elif tanda == '>':
        while p<xt:
            result = (math.comb(strt,p)*(c**p)*((1-c)**(strt-p)))
            temp = temp + result
            p += 1
            if p==x :
                temp = 1 - temp
                temp = round(temp,4)
                print("P(X >",x,") = ", temp)
                break
        pass
else :
    pass
