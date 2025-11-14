# demonstration of data compression
# in Lecture 16 of CIE6020

from math import comb
from numpy import random, log2, ceil, floor

# representing bit string by integer

def encode_bits_to_int(x : list [int]):   # input x is a list of 0 and 1
  """  transform a list of 0 and 1 into an integer  
  """
  loc = [i for i , m in enumerate(x) if m==1]  # locations of 1
  return sum([comb(m,i+1) for i,m in enumerate(loc)])

def decode_int_to_bits(a : int, n : int, k : int):
  """  the reverse transform for combinatorial number system
       return a list of length n containing k ones
  """
  d=[]    # initialize to empty list
  for i in range(n-1,-1,-1):  
    binom_coeff = comb(i,k)  # compute binomial coefficient i choospythone k
    if binom_coeff <= a:   # if this binomial coeff is less than a
      d.append(i)          # there is a 1 located at i
      a -= binom_coeff     # update variable a
      k -= 1               # update variable k
  return  [1 if j in d else 0 for j in range(n)]

#n = 5
#k = 3
#print("Binary string    | Locations of 1 | integral representation")
#print("-----------------+----------------+-----------------")
#for i in range(comb(n,k)):
#  x = decode_int_to_bits(i,n,k)
#  loc = [i for i in range(n) if x[i]==1]
#  print(f"{x}  |  {loc}     |    {i}")
 

# encode bit string to an integer
def encode (bits : list[int], n : int, max_no_of_bits: int) ->int:
  """ bits : a list of zero and one
      n    : length of bits
      max_no_of_bits : maximum number of bits
  """
  k = sum(bits)  # number of 1 in k
  if k > max_no_of_bits:  # if the number of 1 in c exceeds the limit
    W = sum([comb(n,i) for i in range(max_no_of_bits+1)]) # the error index
  else:
    W = encode_bits_to_int(bits)
    W += sum([comb(n,i) for i in range(k)])
  return W


# Recover the original bits
def decode(n : int , W : int ) -> list[int]:
  """
   n is the block length and W is the integral representation
   return a list of length n
  """
  k = 0  # determine the number of 1
  while W >= comb(n,k):
    W -= comb(n,k)
    k += 1
  return decode_int_to_bits(W,n,k)

bits =[1,1,1,0,1,0,0,1,1,1]
mb = 5  # maximum number of bits
n = len(bits)  # block length
encoded_bits = encode(bits, n, mb)   # encode bits to an integer 
decoded_bits = decode(n,encoded_bits)
print(f"Original bits = {bits}")
print(f"Encoded bits = {encoded_bits}")
print(f"Decoded bits = {decoded_bits}")
