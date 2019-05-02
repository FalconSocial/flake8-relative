from setuptools import setup
from flake8_relative import __version__


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='flake8-relative',
    version=__version__,
    description='Flake8 plugin checking for relative imports',
    long_description=readme(),
    long_description_content_type='text/markdown',
    keywords='flake8 relative import',
    install_requires=['flake8>=3.0.0'],
    author='Tue Haulund',
    author_email='tue.haulund@gmail.com',
    url='https://github.com/TueHaulund/flake8-relative',
    license='MIT License',
    py_modules=['flake8_relative'],
    zip_safe=False,
    entry_points={"flake8.extension": ["R100 = flake8_relative:RelativeImportChecker"]},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Framework :: Flake8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ],
)
