from setuptools import setup, find_packages

setup(
    name='legionx',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scikit-learn',
        'pandas',
        'PyYAML',
        'grpcio',
        'fastapi',
        'uvicorn',
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'legionx=legionx.cli:main'
        ]
    }
)
