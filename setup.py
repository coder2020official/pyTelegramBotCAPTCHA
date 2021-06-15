try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pyTelegramBotCAPTCHA',
    packages=['pyTelegramBotCAPTCHA'],
    version='0.0.7',
    license='gpl-3.0',
    description='An easy to use an (hopefully useful) captcha solution for pyTelegramBotAPI.',
    author='SwissCorePy',
    author_email='swisscore.py@gmail.com',
    include_package_data=True,
    
    package_dir={'': '/Volumes/Macintosh SSD/Users/fredi/Documents/GitHub/pyTelegramBotCAPTCHA'},
    url='https://github.com/SwissCorePy/pyTelegramBotCAPTCHA',
    download_url='https://github.com/SwissCorePy/pyTelegramBotCAPTCHA/archive/refs/heads/main.zip',

    keywords=['Telegram', 'Captcha', 'pyTelegramPotAPI'],
    install_requires=['pyTelegramBotAPI', 'captcha', 'Pillow'],
    extras_require={'json': 'ujson'},
    
    classifiers=[
        # "3 - Alpha", "4 - Beta", "5 - Production/Stable"
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3'
    ],
)
