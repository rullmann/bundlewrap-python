pkg_yum = {
    "python": {},
    "python-setuptools": {},
    "python-devel": {},
    "python-tools": {},
    "python-virtualenv": {},
}

if node.has_bundle("epel"):
    pkg_yum['python-pip'] = {
        'needs': [
            "pkg_yum:epel-release",
            "pkg_yum:python-setuptools",
        ],
    }
else:
    pkg_yum['python-pip'] = {
        'needs': [
            "pkg_yum:python-setuptools",
        ],
    }

pkg_pip = {}

for package in node.metadata.get('python', {}).get('pip_packages', {}):
    pkg_pip['{}'.format(package)] = {
        'needs': [
            "pkg_yum:python-pip",
        ],
    }
