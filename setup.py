from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy as np

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
                    include_dirs=[np.get_include(), "/usr/local/include/pcl-1.7", "/usr/local/include/eigen3/"],
                    libraries=["pcl_segmentation", "pcl_io", "OpenNI",
                               "usb-1.0", "pcl_filters", "pcl_sample_consensus",
                               "pcl_features", "pcl_surface", "pcl_search", "pcl_kdtree", "pcl_octree",
                               "flann_cpp", "pcl_common"],
                    language="c++")],
      cmdclass={'build_ext': build_ext}
)


