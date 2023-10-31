from distutils.core import setup

setup(name="bilinear_infft_filter",
      version="0.0.1",
      description="spectral filtering for irregular time-series data",
      license='GNU v3.0',
      author="Michael Sorochan Armstrong",
      author_email="mdarmstr(at)go.ugr.es",
      url='https://github.com/mdarmstr/bilinear_infft_filter',
      package_dir={"bilinear_infft_filter":"."},
      packages=['bilinear_infft_filter'],
      install_requires=[
            'nfft',
            'scipy',
            'numpy',
            'intrp_infft_1d @ git+https://github.com/mdarmstr/intrp_infft_1d'
      ]
     )
