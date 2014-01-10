from setuptools import setup

__version__ = "0.1"
__doc__ = """Encode a wav file to .ogg"""

setup(
 name = 'encode_to_ogg',
 version = __version__,
 description = __doc__,
 data_files = [
  ('', ['oggenc2.exe']),
 ],
 py_modules = ['encode_to_ogg'],
 zip_safe = False,
 classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'License :: OSI Approved :: MIT License',
  'Topic :: Software Development :: Libraries',
 ],
)
