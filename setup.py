import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'Babel',
    'lingua',
    'plaster_pastedeploy',
    'pyramid',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'waitress',
    'alembic',
    'pyramid_retry',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'supervisor',
    'pymysql'
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest >= 3.7.4',
    'pytest-cov',
]

setup(
    name='app',
    version='0.0',
    description='app',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={
        'testing': tests_require,
    },
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = app:main',
        ],
        'console_scripts': [
            'initialize_app_db=app.scripts.initialize_db:main',
        ],
    },
    message_extractors = { 'app': [
        ('**.py', 'python', None ),
        ('**.pt', 'xml', None ),
        ('templates/**.py', 'python', None),
        ('templates/**.jinja2', 'jinja2', None),
        ('templates/submit_person_info/**.jinja2', 'jinja2', None),
        ('templates/status/**.jinja2', 'jinja2', None),
        ('templates/**.jinja2', 'jinja2', None),
        ('static/**', 'ignore', None)
        ],
    },
)
