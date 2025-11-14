he original bits
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
