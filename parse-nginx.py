import re
import pprint
print "Hell1"
dict1 = {}
dict2 = {}

# Intitialize minute variable, to be used as a flag to reset
# dictionary1
initial_min = None
for l in open("nginx.log"):
  # remove empty spaces caused \n
  l = l.strip()
  if re.search('^(\d+\.\d+\.\d+\.\d+) - - \[(\S+)\s.*\]\s+\"(\w+)\s+(\S+)\s+\S+\s+(\d+).*',l):
   m      = re.search('^(\d+\.\d+\.\d+\.\d+) - - \[(\S+)\s.*\]\s+\"(\w+)\s+(\S+)\s+\S+\s+(\d+).*',l)
   ip     =  m.group(1)
   ts     = m.group(2)
   # remove seconds
   ts     = ts[:-3]

   # split to get the minute
   ts_a   = ts.split(':')
   minute = ts_a[2]
   #print minute
   method = m.group(3)
   url    = m.group(4)
   code   =  m.group(5)
   
   # create return code dictionary
   # dict2 
   if not dict2.has_key(code):
      dict2[code] = 1
      continue
   dict2[code] = dict2[code] + 1
   if initial_min == None: 
      print "Hello"
      initial_min = minute 
      dict1[ts] = dict2
      continue
   # if next minute, reset return code dict and initialize key dict
   if initial_min != minute:
      dict1[ts] = dict2
      # reset dictionary
      dict2 = {}
      # reset to the new minute
      initial_min = minute

print dict2
pprint.pprint(dict1)

      
  
  
