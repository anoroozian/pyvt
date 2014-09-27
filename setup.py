from setuptools import setup, find_packages

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

setup(
    name='pyvt',
    version='0.1a1',
    maintainer='Arman Noroozian',
    maintainer_email='arman.noroozian.developer@gmail.com',
    url='https://github.com/anoroozian/pyvt',
    description='Python VirusTotal Private API 2.0 Implementation.',
    long_description=read_md('README.md'),
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Security',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    keywords='virustotal api private',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    install_requires=[],
    tests_require=['nose', 'coverage'],
    zip_safe=False,
    test_suite='nose.collector',
    # data_files=[],
    # scripts=[],
    # setup_requires=[],
    # **extra_kwargs
)


