pkg_dnf = {
    "python": {},
    "python-devel": {},
    "python-tools": {},
    "python2-setuptools": {},
    "python3-setuptools": {},
    "python2-virtualenv": {},
    "python3-virtualenv": {},
    "python-pip": {
        'needs': [
            "pkg_dnf:python2-setuptools",
            "pkg_dnf:python3-setuptools",
        ],
    },
}

pkg_pip = {}

for package in node.metadata.get('python', {}).get('pip_packages', {}):
    pkg_pip['{}'.format(package)] = {
        'needs': [
            "pkg_dnf:python-pip",
        ],
    }
