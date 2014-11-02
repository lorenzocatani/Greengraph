from setuptools import setup, find_packages


setup(
    name = "Greengraph",
    version = "0.1",
    packages = find_packages(exclude=['*test']) 
	#install_requires = ['geopy']
	#install_requires = ['requests']
	#install_requires = ['png']
	#install_requires = ['itertools']
	#install_requires = ['StringIO']
	#install_requires = ['numpy']
	)