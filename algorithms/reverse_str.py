'''
This is an example from CTCI; reverse a string
'''
import math, sys

def reverse_str(str):
    s = list(str) # Converting string to an "array"
    start_idx = 0
    end_idx = len(s) - 1
    #Loop through all chars and swap first idx with the last
    for i in range(math.floor(len(s)/2)):
      s[start_idx], s[end_idx] = s[end_idx], s[start_idx]
      start_idx += 1
      end_idx -= 1
    print(s)

if __name__ == "__main__":
  reverse_str(sys.argv[1])

