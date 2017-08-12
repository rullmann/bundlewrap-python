pkg_dnf = {
    "python3": {},
    "python3-devel": {},
    "python3-tools": {},
    "python3-setuptools": {},
    "python3-virtualenv": {},
    "python3-pip": {
        'needs': [
            "pkg_dnf:python3-setuptools",
        ],
    },
}

pkg_pip = {}

for package in node.metadata.get('python', {}).get('pip_packages', {}):
    pkg_pip['{}'.format(package)] = {
        'needs': [
            "pkg_dnf:python3-pip",
        ],
    }
