from setuptools import setup, find_packages

setup(
    name='pulp_docker_extensions_admin',
    version='2.0.0b1',
    packages=find_packages(),
    url='http://www.pulpproject.org',
    license='GPLv2+',
    author='Pulp Team',
    author_email='pulp-list@redhat.com',
    description='pulp-admin extensions for docker image support',
    entry_points={
        'pulp.extensions.admin': [
            'repo_admin = pulp_docker.extensions.admin.pulp_cli:initialize',
        ]
    }
)
