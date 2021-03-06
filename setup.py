from setuptools import setup

setup(name='acpc_intercomparison',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      description='ACPC deep convection intercomparison setup',
      url='http://github.com/mheikenfeld/acpc_intercomparison',
      author='Max Heikenfeld',
      author_email='max.heikenfeld@physics.ox.ac.uk',
      license='GNU',
      packages=['acpc_intercomparison','acpc_intercomparison.load_models','acpc_intercomparison.plot_functions'],
      install_requires=[],
      zip_safe=False)
