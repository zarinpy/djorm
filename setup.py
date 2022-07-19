from setuptools import setup, find_packages

setup(
    name="djorm",
    version="0.0.1",
    packages=find_packages(exclude=['tests', 'tests.*']),
    url="https://github.com/zarinpy/djorm",
    license="MIT License",
    author="Omid Zarinmahd Ziaabadi",
    author_email="zarinpy@gmail.com",
    description="a tool for django ORM, brings some useful features to django ORM",
    install_requires=["django>=3.0"],
    include_package_data=True,
    python_requires=">=3.7",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
