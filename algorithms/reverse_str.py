'''
This is an example from CTCI; reverse a string
'''

def reverse_str(str):
    start_idx = 0
    end_idx = len(str)-1
    #Loop through all chars and swap first idx with the last
