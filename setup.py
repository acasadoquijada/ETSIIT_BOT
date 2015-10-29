from setuptools import setup

setup(name='ETSIITBOT',
	version='0.8',
	description='Bot de telegram sobre la ETSIIT-UGR',
	url='https://github.com/acasadoquijada/ETSIIT_BOT',
	author='Alejandro Casado Quijada',
	author_email='acasadoquijada@gmail.com',
	license='GNU GPL',
	install_requires=['beautifulsoup4','py','pyTelegramBotAPI','pytest','requests','six','wheel'],
	zip_safe=False)