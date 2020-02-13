# Public Key Cryptography

## Part I - XOR Review
Use the key (K) given below to “encrypt” the message (S) using the XOR operation.

S = 101100010100100001010010
K = 001001101001110100110101

E = 

Now apply the same key (K) to the encrypted message (E).

## Part II - PRNG
A pseudo-random-number generator is a way to generate data in a way where the pattern is not immediately obvious and can be difficult to distinguish from random data

X(n+1) = [A*X(n) + B]mod(N)

X(0) is known as the “seed” of the pseudo-random-number generator.

example:
A=533, B=277, N=64, and X(0) = 125

X(1) =  
X(2) =  
X(3) =  
X(4) = 

Now, combine these four 6-bit sequences together to get a three byte key.



## Part III - Public Key Cryptography

choose integer C between 0 and N-1
sender chooses large integer I as private key
recipient chooses large integer J as private key

Sender calculates public key P and recipient computes public key Q

P = CI mod(N)

Q = CJ mod(N)

They swap public keys and each calculates encryption key (or seed for PRNG) which will be equal

QI mod(N) = PI mod(N)


### Examples:

1. Let C = 5; compare the first 6 powers of C modulo N for N = 16 and N = 17 - i.e. compute CJ mod(N) for J = {1,...,5} for both N = 16 and then again for N=17.

2. Suppose N = 32, I = 5, and J = 7 are chosen. Additionally, the value of C is chosen to be 11. Compute the public keys P and Q, and show that these can be used to generate the same X(0) seed value to be used to produce the same encryption key.


## Part IV - Implementation

Let us try to implement something similar in a python program. Try:
 
1. Create a function that will take a string of bits and perform an XOR operation on the string with some given binary key. Check out this: https://stackoverflow.com/questions/19414093/how-to-xor-binary-with-python

2. Create a function which will take in a seed value and implement a PRNG similar to the one given as an example. 
 
3. Finally, let's put this all together to try to create a function which will exchange key values with someone else and generate the same seed value using PK encryption.


 

