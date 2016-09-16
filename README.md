# bundlewrap-python

`bundlewrap-python` installs python, pip as well as the required tools to install python packages.
It allows to install additional pip packages from a nodes metdata.

## Compatibility

This bundle has been tested on the following systems:

| OS          | `[x]` |
| ----------- | ----- |
| CentOS 7    | `[x]` |
| Fedora 24   | `[x]` |
| RHEL 7      | `[ ]` |
| Fedberry 23 | `[ ]` |

## Requirements

* Bundles:
  * [epel](https://github.com/rullmann/bundlewrap-centos-epel)
    * Required for RHEL and CentOS, but not Fedora

## Metadata

    'metadata': {
        'python': {
            'pip_packages': ["thefuck"], # optional
        },
    }
