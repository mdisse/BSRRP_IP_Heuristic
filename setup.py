from setuptools import setup, find_packages

setup(
    name="bsrrp",
    version="0.1.0",
    description="Buffer Storage, Retrieval, and Reshuffling Problem (BSRRP) Optimization",
    author="Max Disselnmeyer",
    author_email="max.disselnmeyer@kit.edu",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
        "matplotlib",
        "imageio",
        "gurobipy",
        "pandas",
        "seaborn",
        "ortools"
    ],
    python_requires=">=3.8",
)
