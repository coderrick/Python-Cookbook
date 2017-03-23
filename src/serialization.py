# Credit: TheNewBoston
from struct import *

# Store as bytes data
struct_data = pack('iif', 19, 90, 8.99)
print(struct_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# To deserialize byte data and read original data
original_data = unpack('iif', struct_data)
print(original_data)
# Or the foolowing
#print(unpack('iif', b'\x13\x00\x00\x00Z\x00\x00\x00\n\xd7\x0fA)\\x)