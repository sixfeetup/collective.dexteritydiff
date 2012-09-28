from setuptools import setup, find_packages
import os


def get_git_version(abbrev=4):
    from subprocess import Popen, PIPE
    try:
        p = Popen(['git', 'rev-parse', 'HEAD'],
                  stdout=PIPE, stderr=PIPE)
        p.stderr.close()
        line = p.stdout.readlines()[0]
        return '-' + line.strip()[:abbrev]
    except:
        return ''

version = '0.1b4' + get_git_version()

setup(name='collective.dexteritydiff',
      version=version,
      description='Provide the DexterityCompoundDiff diff type for Products.CMFEditions, '
          'analogous to ATCompoudDiff.',
      long_description=open(os.path.join('collective', 'dexteritydiff', 'README.txt')).read() + "\n" +
                       open(os.path.join('docs', 'HISTORY.txt')).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='plone dexterity',
      author='Rafael Oliveira',
      author_email='rafaelbco@gmail.com',
      url='http://svn.plone.org/svn/collective/collective.dexteritydiff',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.autoinclude',
          'Products.CMFDiffTool',
          'plone.dexterity',
          'zope.i18nmessageid',
      ],
      extras_require = {
        'test': [
            'Plone',
            'plone.app.dexterity',
            'plone.app.testing',
            'plone.namedfile',
            'plone.formwidget.namedfile',
        ]
      },
      entry_points="""
      # -*- Entry points: -*-
      """,
)
