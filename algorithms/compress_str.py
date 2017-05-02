'''
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become
a2blc5a3. If the "compressed" string would not become smaller than the original
string, your method should return the original string.
'''
def compress_str(str):
  s = list(str)
  lettercnt = 1
  i = 1
  for i in range(len(s)-1):
    if s[i] == s[i + 1]:
      lettercnt += 1
      print(f"current count {i}")#Using f-string for string interpolation
    else:
      #Push to new list 
      s[i] = lettercnt 
      #Reset the count
      lettercnt = 0

  print(s)

compress_str("aabcccccaaa")
