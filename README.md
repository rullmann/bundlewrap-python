# bundlewrap-python

`bundlewrap-python` installs python, pip as well as the required tools to install python packages.
It allows to install additional pip packages from a nodes metdata.

## Metadata

    'metadata': {
        'python': {
            'pip_packages': ["thefuck"], # optional
        },
    }
