import sys


print "Version information of installed Python and extensions:"
print "-------------------------------------------------------\n"


print "Python:      %s" % sys.version 


try:
    import numpy
except ImportError:
    print "numpy not installed!"
else:
    print "numpy:      ", numpy.version.version


try:
    import scipy
except ImportError:
    print "scipy not installed!"
else:
    print "scipy:      ", scipy.version.version


try:
    import win32api
except ImportError:
    print "PyWin32 not installed!"
else:
    pw32_info = win32api.GetFileVersionInfo(win32api.__file__, '\\')
    print "PyWin32:    ", pw32_info['FileVersionLS'] >> 16


try:
    import matplotlib
except ImportError:
    print "matplotlib not installed!"
else:
    print "matplotlib: ", matplotlib.__version__


try:
    import wxversion
except ImportError:
    print "wxPython not installed!"
else:
    print "wxPython:   ",
    for elem in wxversion.getInstalled():
        print elem
