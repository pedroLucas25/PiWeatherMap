from setuptools import setup, find_packages

setup(
    name='PiWeatherMap',
    version='0.0.1',
    author='Pedro Souza',
    description='Retorno de previsões do tempo utilizando OpenWeatherMap',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'requests >= 2.25.1',
        'pytest >= 8.1.1'
    ],
    # entry_points={
    #     'console_scripts': [
    #         'meu_comando=meu_sdk.modulo:funcao_principal',
    #     ],
    # },
)