from setuptools import setup, find_packages

setup(
    name="spsspro",
    version="0.1.0",
    description="统计分析和机器学习工具包",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="liyibing",
    author_email="liyibing666@gmail.com",  # 添加您的邮箱
    url="https://github.com/li-yibing/spsspro",  # 添加项目URL
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)