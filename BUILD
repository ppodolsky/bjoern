load('//tools/package:python.bzl', 'python_package', 'python_venv')
load('//tools/testing:python.bzl', 'python_test')


python_package(
    name = 'bjoern-wheel',
    package_name = 'bjoern',
    version = '1.4.3',
    python_tag = 'cp27',
    abi_tag = 'cp27mu',
    platform_tag = 'linux_x86_64',
    python_binary = 'python2',
    visibility = ["//visibility:public"],
)

python_venv(
    name = 'venv',
    wheels = [':bjoern-wheel'],
    python_binary = 'python2',
)

python_test(
    name = 'bjoern-tests',
    venv = ':venv',
    tests = 'tests',
)

