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
    
def prime(n):
    while not Rabin_Miller(n,30):
        n += 2
    return n
    

## Générateur
    
def est_generateur(a,p):
    return(puiss_rec(a,(p-1)//2,p) == p-1)

def generateur(p):
    g = 2
    while not est_generateur(g,p):
        g = g + 1
    return(g)
    
## Chiffrement

def gen_cle(p,g,xa):
    ya = puiss_rec(g,xa,p)
    return((p,g,ya))
    

def cryptage(msg, xb, p, ya, g): 
  
  
    a = msg*puiss_rec(ya, xb, p) 
    b = puiss_rec(g, xb, p)
    
    return((a,b))
    
    
    
## Programme El Gamal avec nombres
p=10**100+43723
g=generateur(p)

print("Génération de la clé publique")
print(" ")

print("Nombre premier utilisé:",p)
print("Le générateur est:",g)
xa=int(input("Clé secrete du récépteur: "))
ya=puiss_rec(g,xa,p)
print("La clé secrète du récepteur est:",xa)
print ("La clé publique est:", gen_cle(p,g,xa))

print(" ")
print("Chiffrement du message:")
print(" ")

msg=int(input("Message à transmettre: "))
xb=int(input("Clé personnelle de l'émétteur: "))


print ("Le message chiffré transmis est:", cryptage(msg,xb,p,ya,g))

(ms,b)=cryptage(msg,xb,p,ya,g)


print(" ")

print ("Déchiffrement du message: ",ms//puiss_rec(b,xa,p))


##Cryptage / decryptage de message

def cryptage_message(mess,xb,p,ya,g):
    
    mess_code=[]
    
    for i in range(0, len(mess)): 
        mess_code.append(mess[i])
    
        
    for i in range(0, len(mess_code)): 
        mess_code[i] = puiss_rec(ya, xb, p)*ord(mess_code[i])
        
        
    info = puiss_rec(g, xb, p)
        
    return(mess_code,info)
    
    


def decrypt(mess_code,info,xa, p): 
  
    mess_decrypt = []
    m = ""  
    for i in range(0, len(mess_code)): 
        mess_decrypt.append(chr(int(mess_code[i]/puiss_rec(info,xa,p)))) 
    for j in range (0,len(mess_decrypt)):
        m += mess_decrypt[j]
    return (m) 
 
##Programme El Gamal avec message
p=10**100+43723
g=2
print("Génération de la clé publique")
print(" ")

print("Nombre premier utilisé:",p)
print("Le générateur est:",g)
xa=int(input("Clé secrete du récépteur: "))
ya=puiss_rec(g,xa,p)
print("La clé secrète du récepteur est:",xa)
print ("La clé publique est:", gen_cle(p,g,xa))

print(" ")
print("Chiffrement du message:")
print(" ")

mess=input("Message à transmettre: ")
xb=int(input("Clé personnelle de l'émétteur: "))


print ("Le message chiffré transmis est:", cryptage_message(mess,xb,p,ya,g))

(ms,inf)=cryptage_message(mess,xb,p,ya,g)


print(" ")

print ("Déchiffrement du message: ",decrypt(ms,inf,xa, p))



