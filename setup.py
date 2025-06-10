from setuptools import setup, find_packages

setup(
    name="thumbcrafter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Pillow>=10.2.0",
        "requests>=2.31.0",
        "python-dotenv>=1.0.1",
        "numpy>=1.26.4",
        "scikit-learn>=1.4.1",
        "colorthief>=0.2.1",
        "transformers>=4.38.2",
        "torch>=2.2.1",
        "stability-sdk>=0.8.5"
    ],
    python_requires=">=3.8",
) 