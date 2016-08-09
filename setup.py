from setuptools import setup, find_packages
import os

version = '1.1'

setup(name='collective.tinymceplugins.latex',
      version=version,
      description="",
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
      ],
      keywords='',
      author='Eric Wohnlich',
      author_email='wohnlice@imsweb.com',
      url='https://git.imsweb.com/plone/collective.tinymceplugins.latex',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective','collective.tinymceplugins'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.jquery',
          #'matplotlib',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      extras_require={
          'test': ['plone.app.testing', 'plone.mocktestcase'],
      },
      )
