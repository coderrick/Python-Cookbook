'''
This is an example from CTCI; reverse a string
'''

def reverse_str(str):
    s = list(str)
    start_idx = 0
    end_idx = len(s) - 1
    #Loop through all chars and swap first idx with the last
    for i in range(len(s)):
      s[start_idx], s[end_idx] = s[end_idx], s[start_idx]
      start_idx += 1
      end_idx -= 1
    print(s)

reverse_str('hello')
