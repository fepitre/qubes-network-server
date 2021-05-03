import os
import setuptools

if __name__ == '__main__':
    version = open(os.path.join(os.path.dirname(__file__), 'version')).read().strip()
    setuptools.setup(
        name='qubesnetworkserver',
        version=version,
        author='Manuel Amador (Rudd-O)',
        author_email='rudd-o@rudd-o.com',
        description='Qubes network server dom0 component',
        license='GPL2+',
        url='https://github.com/Rudd-O/qubes-network-server',

        packages=('qubesnetworkserver',),

        entry_points={
            'qubes.ext': [
                'qubesnetworkserver = qubesnetworkserver:QubesNetworkServerExtension',
            ],
        }
    )
