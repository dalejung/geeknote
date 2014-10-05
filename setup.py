from distutils.core import setup

DISTNAME='geeknote'
FULLVERSION='0.1'

setup(
    name=DISTNAME,
    version=FULLVERSION,
    packages=['geeknote'],
    entry_points={
        'console_scripts':
            [
                'gnsync = geeknote.gnsync:main',
                'geeknote = geeknote.geeknote:main',
            ]
    }
      )
