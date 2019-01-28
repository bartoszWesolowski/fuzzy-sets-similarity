#really ugly but any other way did not work
import sys, os
print 'adding parent dir to path'
sys.path.insert(0, os.path.abspath('..'))