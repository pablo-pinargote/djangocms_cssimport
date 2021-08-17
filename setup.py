import setuptools

REQUIREMENTS = [
    'django-cms>=3.7'
]

setuptools.setup(
    name="djangocms_cssimport",
    version="1.0.1",
    author="Pablo Pinargote",
    author_email="pablo.pinargote@outlook.com",
    description="Plugin for django CMS that allows you to add SVG images on your site.",
    url='https://github.com/pablo-pinargote/django_cssimport',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    include_package_data=True,
    python_requires='>=3.6',
)
