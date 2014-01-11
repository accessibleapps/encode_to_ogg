import os
import subprocess

import sound_lib
import resource_finder

def find_datafiles():
 import sys
 path = os.path.split(os.path.abspath(sys.modules[find_datafiles.__module__].__file__))[0]
 return [(), [os.path.join(path, 'oggenc2.exe')]]

def encode_to_ogg(filename, quality=4.5):
 subprocess.check_call(r'"%s" -q %r "%s"' % (resource_finder.find_application_resource('oggenc2.exe'), quality, filename))
 created_filename = '%s.ogg' % os.path.splitext(filename)[0]
 return created_filename

