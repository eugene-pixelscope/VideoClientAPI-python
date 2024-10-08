from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension
import os


project_root = os.path.abspath(os.path.dirname(__file__))
lib_dir = os.path.join(project_root, "VideoClientAPI", "linux_out", "lib")
include_dir = os.path.join(project_root, "VideoClientAPI", "linux_out", "include")

ext_modules = [
    Pybind11Extension(
        "pxgrabapi_python.pxgrabapi_python",
        ["src/plugins.cpp"],
        include_dirs=[include_dir],
        library_dirs=[lib_dir],
        libraries=["VideoClientAPI", "NvDecoder"],
        runtime_library_dirs=[lib_dir],
        extra_link_args=[f"-Wl,-rpath,{lib_dir}"],
    ),
]

setup(
    name='pxgrabapi_python',
    version='0.0.1',
    python_requires='>=3.6',
    packages=['pxgrabapi_python'],
    ext_modules=ext_modules,
    package_data={'pxgrabapi_python': ['../VideoClientAPI/linux_out/lib/*.so*']},
    include_package_data=True,
    install_requires=["easydict", "pydantic==1.8.2"]
)
