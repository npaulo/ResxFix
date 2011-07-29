from distutils.core import setup
import py2exe

options = {'py2exe': {'compressed':1, 'bundle_files': 2, 'dll_excludes': ['w9xpopen.exe']}}
setup(console=['ResxFix.py'], options=options)
