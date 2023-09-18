#
# setup.py for maxarcat
#
# Increment the version stored in the file maxarcat/version.txt.
# Then build a wheel to the dist directory.
#

import os.path
import setuptools

# Read version from maxarcat/version.txt
root_dir = os.path.dirname(__file__)
version_file = os.path.join(root_dir, 'maxarcat', 'version.txt')
print(f'Reading version from {version_file}')
with open(version_file, 'r') as file:
    version = file.read().strip()
print(f'Building version {version}')

long_description = '''
Maxarcat is a Python client for searching the
[Maxar Catalog](https://doc.content.maxar.com).
'''

setuptools.setup(
    name="maxarcat",
    version=version,
    author="Maxar",
    description="Maxar Catalog Python client",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/Maxar-Corp/maxarcat",
    packages=[
        'maxarcat',
        'maxarcat_client',
        'maxarcat_client.api',
        'maxarcat_client.models'],
    package_dir = {
        'maxarcat': 'maxarcat',
        'maxarcat_client': 'maxarcat_client/maxarcat_client',
        'maxarcat_client.api': 'maxarcat_client/maxarcat_client/api',
        'maxarcat_client.models': 'maxarcat_client/maxarcat_client/models'
    },
    package_data={
        'maxarcat': ['version.txt']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: GIS"
    ],
    install_requires=[
        # Required by maxarcat
        'requests',

        # Required by maxarcat_client.  See maxarcat_client/setup.py
        'certifi',
        'python-dateutil',
        'six',
        'urllib3'
    ],
    python_requires='>=3.8'
)
