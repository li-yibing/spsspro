from setuptools import setup, find_packages

setup(
    name="spsspro",
    version="0.1.0",
    description="统计分析和机器学习工具包",
    author="SPSS Pro",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn",
    ],
    python_requires=">=3.6",
)