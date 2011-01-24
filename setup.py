from distutils.core import setup
import os

from mcc2 import get_version


# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('mcc2'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[13:] # Strip "mcc2/" or "mcc2\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(name='mcc2',
      version=get_version().replace(' ', '-'),
      description='Mandriva control center 2',
      author='Mandriva',
      author_email='',
      url='',
      download_url='',
      package_dir={'mcc2': 'mcc2'},
      packages=packages,
      package_data={'mcc2': data_files},
      classifiers=['Development Status :: 1 - Planning',
                   'Intended Audience :: Developers',
                   'License :: ',
		   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python',
                   'Topic :: Libraries :: Python Modules',]
      )

