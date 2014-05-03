from setuptools import setup, find_packages

__version__ = "0.2"
__doc__ = """Encode a wav file to .ogg"""

setup(
 name = 'encode_to_ogg',
 version = __version__,
 description = __doc__,
 packages = find_packages(),
 package_data = {
  'encode_to_ogg': ['oggenc2.exe'],
 },
 zip_safe = False,
 classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'License :: OSI Approved :: MIT License',
  'Topic :: Software Development :: Libraries',
 ],
)
