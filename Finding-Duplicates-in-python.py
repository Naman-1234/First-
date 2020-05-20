#First we will write a function to check whether it contains dupliacte or not For this i will remember that a set is a data structure in which duplicates are not allowed.
def check(list):
  if len(list)==len(set(list)):
    return 0
  else:
    return 1
  
 # Now this function will give the frequency of each element and for this i will use another data structure called Dictionary
def freq(list):
  x=dict()
  for i in list:
    x[i]=x.get(i,0)+1
  return x
  
#This is returning a dictionary in which name-value pairs are there.
    
    
  

