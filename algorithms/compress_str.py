'''
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become
a2blc5a3. If the "compressed" string would not become smaller than the original
string, your method should return the original string.
'''
def compress_str(str):
  s = list(s)
  lettercnt = 1
  i = 1
  for i in range(len(s)):
    if s[i] == s[i + 1]:
      lettercnt += 1
      print(f"current count {i}")
    else:
      #Push to new list 
      #Reset the count
      lettercnt = 0
