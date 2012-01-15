import fnmatch
import os
for fileName in os.listdir ( '/' ):
   if fnmatch.fnmatch ( fileName, '*.txt' ):
      print open ( fileName ).read()
   elif fnmatch.fnmatch ( fileName, '*.exe' ):
      print fileName 

