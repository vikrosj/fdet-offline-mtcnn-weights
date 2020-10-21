"""The setup script"""

from setuptools import setup, find_packages

AUTHOR = 'Viktoria R.'
EMAIL = 'viktoria.rosjo@gmail.com'
VERSION = '0.0.1'

setup(
    name='fdet-offline-mtcnn-weights',
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    maintainer=AUTHOR,
    maintainer_email=EMAIL,
    url='https://github.com/vikrosj/fdet-offline-mtcnn-weights',
    download_url='https://github.com/vikrosj/fdet-offline-mtcnn-weights/archive/0.0.1.tar.gz',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Other Audience',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 8',
        'Operating System :: Microsoft :: Windows :: Windows 8.1',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries'
    ],
    description='Weights for the models in fdet-offline.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # This is important!
    keywords='face recognition detection biometry',
    packages=find_packages(),
    zip_safe=False,
    python_requires='>=3.5',
    install_requires=[
                        'future==0.18.2',
                        'numpy==1.19.2',
                        'torch==1.6.0'
                    ]
)