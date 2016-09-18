pkg_yum = {
    "python": {},
    "python-devel": {},
    "python-tools": {},
    "python2-setuptools": {},
    "python3-setuptools": {},
    "python2-virtualenv": {},
    "python3-virtualenv": {},
    "python-pip": {
        'needs': [
            "pkg_yum:python2-setuptools",
            "pkg_yum:python3-setuptools",
        ],
    },
}

pkg_pip = {}

for package in node.metadata.get('python', {}).get('pip_packages', {}):
    pkg_pip['{}'.format(package)] = {
        'needs': [
            "pkg_yum:python-pip",
        ],
    }
