pkg_yum = {
    "python": {},
    "python-devel": {},
    "python-tools": {},
}

if node.has_bundle("epel"):
    pkg_yum['python-setuptools'] = {}
    pkg_yum['python-pip'] = {
        'needs': [
            "pkg_yum:epel-release",
            "pkg_yum:python-setuptools",
        ],
    }
else:
    pkg_yum['python2-setuptools'] = {}
    pkg_yum['python3-setuptools'] = {}
    pkg_yum['python2-virtualenv'] = {}
    pkg_yum['python3-virtualenv'] = {}
    pkg_yum['python-pip'] = {
        'needs': [
            "pkg_yum:python2-setuptools",
            "pkg_yum:python3-setuptools",
        ],
    }

pkg_pip = {}

for package in node.metadata.get('python', {}).get('pip_packages', {}):
    pkg_pip['{}'.format(package)] = {
        'needs': [
            "pkg_yum:python-pip",
        ],
    }
