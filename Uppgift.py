S1 = 2
n = int(input("Ange n: "))

def f(x):
  for k in range (1,n+1):
    S12 = pow(S1,k)
    S13 = S1 + S12
  #print (S13-2)
  t = S13 - 2
  return t

startvärde = int(input("ange startvärde: "))
slutvärde = int(input("ange slutvärde: "))
steglängd = int(input("ange steglängd: "))
k = startvärde
while k <= slutvärde+1:
  print ("x =",k, ", f(x) =",f(k))
  k=k+steglängd  
