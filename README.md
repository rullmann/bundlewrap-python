# bundlewrap-python

`bundlewrap-python` installs python, pip as well as the required tools to install python packages.
It allows to install additional pip packages from a nodes metdata.

## Compatibility

This bundle has been tested on the following systems:

| OS          | `[x]` |
| ----------- | ----- |
| Fedora 25   | `[x]` |
| Fedora 26   | `[x]` |

## Metadata

    'metadata': {
        'python': {
            'pip_packages': ["thefuck"], # optional
        },
    }
