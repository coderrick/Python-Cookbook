'''
Method to replace all spaces in a string with'%20'
'''
def replace_str(str):
  s = list(str)# Convert to char "array"
  #Loop through the array
  for i in range(len(s)):
    if s[i] == ' ':
      s[i] = '%20'
  print(''.join(s))#convert list to string. What is the Time complexity

replace_str('dun dun duunnn')