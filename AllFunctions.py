import random

## Autres

def puiss_rec(a,n,p):
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            b = a*a % p
            return puiss_rec(b,n//2,p)
        else:
            b = a*a % p
            return a*puiss_rec(b,(n-1)//2,p) % p

def pgcd(a,b):
    if a < b :
        return pgcd(b,a)
    elif a % b == 0:
        return b
    else:
        return pgcd(b, a % b)

## Nombres premiers

def valuation(p):
    s = 0
    m = p - 1
    while m % 2 == 0:
        s += 1
        m = m//2
    return (s,m)

def Temoin_Miller(a,p) :
    s,m = valuation(p)
    x = puiss_rec(a,m,p)
    if x == 1 :
            return True
    else:
        for i in range(s) :
            t = puiss_rec(a,m,p)
            if t == -1 % p:
                return True
            else :
                m = 2*m
    return False

def Rabin_Miller(p,k):
    for i in range(k):
        a = random.randrange(2,p-2)
        if not Temoin_Miller(a,p):
            return False
    return True

def premier(n):
    while not (Rabin_Miller(n,30) and Rabin_Miller((n-1)//2,30)):
        n += 2
    return n

## Générateur (p-1/2 premier)

def est_generateur(a,p):
    return(puiss_rec(a,(p-1)//2,p) == p-1)

def generateur(p):
    g = 2
    while not est_generateur(g,p):
        g = g + 1
    return(g)

## Décomposition en facteurs premiers

def facteurs_premiers(N):
    L = []                      #La liste de tous les facteurs premiers #
    p = 2                       #Le facteur premier #
    while p*p <= N:
        while (N % p) == 0:
            L.append(p)
            N //= p
        p += 1
    if N > 1:
       L.append(N)
    return L

def count_puiss (p,L) :         #le nombre premier que l'on compte#
    a=0
    n=len(L)
    for i in range (0,n):
        if L[i] == p :
            a+=1
    return a

def decompo_finale (N) :
    P= facteurs_premiers (N)     #Liste des facteurs premiers#
    n=len(P)
    a=0
    X=[]
    i=0
    while i<n :
        a=count_puiss (P[i],P)
        X.append([P[i],a])
        i+=a
    return X

## Decomposition du problème du logarithme discret

def deci(p,g,y,q,m):
    L = []
    x = (p-1)//q
    a = puiss_rec(y,x,p)
    d = 0
    while (puiss_rec(g,x*d,p)) != a :
        d += 1
    L.append(d)
    for i in range(1,m):
        k = 0
        x = x//q
        y = y*inverse_modulaire(puiss_rec(g,q**(i-1)*L[i-1],p),p) % p
        u = puiss_rec(y,x,p)
        while puiss_rec(g,((p-1)//q)*k,p) != u:
            k += 1
        L.append(k)
    return L

def rassemble_decimal (g,y,p) :
    J = decompo_finale(p-1)
    D = []
    for i in range (len(J)) :
        L = deci(p,g,y,J[i][0],J[i][1])
        xi = 0
        for j in range (J[i][1]) :
            xi += L[j]*(J[i][0]**j)
        D.append(xi)
    return D

## Euclide étendu et Théorème chinois

def euclide_etendu (a,b) :
    r, u, v = a, 1, 0
    r1, u1, v1 = b, 0, 1
    while r1 != 0 :
        q = r//r1
        r, u, v, r1, u1, v1 = r1, u1, v1, r-q*r1, u-q*u1, v-q*v1
    return (u,v)

def reste_chinois(g,y,p) :
    P = decompo_finale(p-1)
    D = rassemble_decimal(g,y,p)
    s = 0
    e = []
    for i in range (len(D)) :
        ni = P[i][0]**P[i][1]
        mi = (p-1)/ni
        v = inverse_modulaire(mi,ni)
        ei = v*mi
        e.append(ei)
        s += D[i]*ei
    return int(s % (p-1))

def euclide_rec(a,b):
    if b == 0 :
        return 1,0
    else :
        u,v = euclide_rec(b, a%b)
        return (v, u - (a//b)*v)

def inverse_modulaire(x,p):
    u,v = euclide_rec(x,p)
    return u % p