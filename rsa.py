def gcd(p, q):
    if q > p:
      return gcd(q, p)
    if p % q == 0:
      return q
    return gcd(q, p % q)

P = 53
Q = 59
M = 89
F = (P - 1) * (Q - 1)
print ("Calculate the Euler function F(n)=(p-1)*(Q-1)")
print ("F =",F)

# Use first simple number.
Ko = 0
i = 2
while i < F:
  e = gcd(F, i)
  if e == 1:
    Ko = i;
    break;
  i += 1

print ("Select the value of the public key Ko with the conditions")
print ("1<Кo<F(n), Кo и F(n) – mutually prime numbers (their greatest common divisor=1)")
print ("Ko =",Ko)

i = 2
while i < 3127:
  if (i * Ko) % F == 1:
    Kc = i
    break
  i += 1

print ("Find Kc =",Kc)

C = M**Ko % 3127
print ("Encryption: C =",C)

Md = C**Kc % 3127
print ("Decryption: M =",Md)
