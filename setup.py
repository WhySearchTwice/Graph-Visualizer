from distutils.core import setup

setup(
    name='GraphVisualizer',
    version='0.0.1',
    author='Tony Grosinger',
    author_email='tony@grosinger.net',
    packages=['graphvisualizer', 'graphvisualizer.test'],
    scripts=[],
    url='https://github.com/WhySearchTwice/Graph-Visualizer/',
    license='LICENSE.txt',
    description='Create a graphical representation of the WhySearchTwice graph information by connecting to a running Ubigraph instance.',
    long_description=open('README.md').read(),
    install_requires=[
        "xmlrpclib",
    ],
)
