from setuptools import setup

setup(
    name="comp0034-week9-complete",
    packages=["paralympic_app", "iris_app"],
    include_package_data=True,
    install_requires=[
        "flask",
        "flask-wtf",
        "flask-sqlalchemy",
        "Flask-WTF",
        "flask-marshmallow",
        "marshmallow-sqlalchemy",
        "pandas",
        "requests",
        "scikit-learn",
    ],
)
