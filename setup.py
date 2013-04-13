from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np
import os.path

libs = ['pcl-1.7', 'eigen3', 'vtk-5.10']

def unix_paths(libs):
    paths = []
    for l in libs:
        paths = paths + [os.path.join("/usr/include", l), os.path.join("/usr/local/include", l)]
    return paths

setup(name='python-pcl',
      description='pcl wrapper',
      url='http://github.com/strawlab/python-pcl',
      version='0.1',
      author='John Stowers',
      author_email='john.stowers@gmail.com',
      license='BSD',
      ext_modules=[Extension(
                   "pcl",
                   ["pcl.pyx", "minipcl.cpp"],
                    include_dirs=[np.get_include()] + unix_paths(libs),
                    libraries=["pcl_segmentation", "pcl_io", "OpenNI",
                               "usb-1.0", "pcl_filters", "pcl_sample_consensus",
                               "pcl_features", "pcl_surface", "pcl_search", "pcl_kdtree", "pcl_octree",
                               "flann_cpp", "pcl_common", "pcl_visualization"],
                    language="c++")],
      cmdclass={'build_ext': build_ext}
)
