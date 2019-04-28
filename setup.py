from distutils.core import setup
setup(
  name='pdftobb',
  packages=['pdftobb'],
  version='0.1',
  license='MIT',
  description='Parse bounding boxes from PDFs',
  author='Sam Zhang',
  author_email='shimian.zhang@gmail.com',
  url='https://github.com/samzhang111/pdftobb',
  download_url='https://github.com/samzhang111/pdftobb/archive/v_01.tar.gz',
  entry_points = {
      'console_scripts': [
          'pdftobb=pdftobb.pdftobb:run_pdftobb'
      ]
  },
  keywords=['pdf', 'parser'],
  install_requires=[
          'lxml',
          'bs4',
          'pdfminer3k',
          'pandas'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
  ],
)
