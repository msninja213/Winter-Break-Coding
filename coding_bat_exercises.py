def not_string(str):
  if len(str) >= 3 and str[:3] == 'not': #str[:3] pulls the first 3 characters instead of having to go through an interated array
    return str
  return 'not ' + str

def missing_char(str, n):
  front = str[:n] #up to n
  back = str[n+1:] #after n
  return front + back

#Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
  result = ""
  n = len(str)
  i = 0
  for i in range(0, n, 2):
    result += str[i]
  return result

#or 
def string_bits(str):
  result = ""
  n = len(str)
  for i in range(n):
    if i % 2 == 0:
      result += str[i]
  return result

def array_front9(nums):
  for i in range(min(4, len(nums))): #iterates to either up to the 4th index or length of array, whichever one is smaller
    if nums[i] == 9:
      return True
  return False

def string_match(a, b):
  count = 0 
  for i in range(min(len(a), len(b))-1): #-1 to say that i iterates up to the second to last index to avoid out of range 
    a_str = a[i:i+2] #characters up to i+2
    b_str = b[i:i+2]
  
    if a_str == b_str:
      count += 1
  return count 

#get last 2 characters of string
def extra_end(str):
    chars = str[-2:]
    return(chars+chars+chars)

def has23(nums):
   return 2 in nums or 3 in nums #if array nums has a 2 or 3
 
 
def cigar_party(cigars, is_weekend):
  if is_weekend == True:
     return(cigars >= 40)
  else:
    return(cigars>=40 and cigars<=60) 

def caught_speeding(speed, is_birthday):
    # Adjust speed limit based on birthday
    if is_birthday:
        speed -= 5
    
    # Check speed and return the appropriate result
    if speed <= 60:
        return 0  # No ticket
    elif 61 <= speed <= 80:
        return 1  # Small ticket
    else:
        return 2  # Big ticket



def make_bricks(small, big, goal):
 #WHEN DOES THIS FAIL?
 #1: NOT ENOUGH BRICKS
  if(small + 5*big < goal):
   return False
 #2: NOT ENOUGH SMALL BRICKS
  elif((goal % 5) > small and goal//5 <= big):
    return False
  else:
    return True
  
#no teen
def no_teen_sum(a, b, c):
  return(fix_teen(a) + fix_teen(b) + fix_teen(c))
  
def fix_teen(n):
  if(13<= n <=14 or 17<= n <= 19):
    return 0
  return n