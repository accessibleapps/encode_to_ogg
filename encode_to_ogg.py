import os
import subprocess

import sound_lib
import resource_finder

def encode_to_ogg(filename, quality=4.5):
 subprocess.check_call(r'"%s" -q %r "%s"' % (resource_finder.find_application_resource('oggenc2.exe'), quality, filename))
 created_filename = '%s.ogg' % os.path.splitext(filename)[0]
 return created_filename

