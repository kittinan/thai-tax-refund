import setuptools

import thaitaxrefund

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='thaitaxrefund',
    version=thaitaxrefund.VERSION,
    author="Kittinan Srithaworn",
    description="Thai tax refund checker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    install_requires=['requests', 'docopt'],
    scripts=['bin/thaitaxrefund'],
    keywords='thai tax refund',
    url="https://github.com/kittinan/thai-tax-refund",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],

    project_urls={
        'Bug Reports': 'https://github.com/kittinan/thai-tax-refund/issues',
        'Source': 'https://github.com/kittinan/thai-tax-refund',
    },
)
