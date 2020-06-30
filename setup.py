import setuptools

setuptools.setup(
    name='webloc',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages(),
    scripts=['scripts/.webloc.sh','scripts/webloc']
)
