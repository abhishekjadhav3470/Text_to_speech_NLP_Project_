from setuptools import find_packages, setup

def get_requirements(file_path):
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.read().splitlines()

    return requirements

setup(
    name='YourNLPProject',
    version='0.1',
    author='Abhishek Jadhav',
    author_email='abhishekjadhav3470@gmail.com',
    description='Your NLP Project Description',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
