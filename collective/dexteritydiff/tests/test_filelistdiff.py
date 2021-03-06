import unittest2 as unittest
from collective.dexteritydiff.testing import INTEGRATION_TESTING, TEST_CONTENT_TYPE_ID
from Products.CMFCore.utils import getToolByName
from ..filelistdiff import DexterityFileListDiff
from plone.app.testing import setRoles, TEST_USER_ID
from Products.CMFDiffTool.interfaces import IDifference
from datetime import date
from plone.namedfile import NamedFile

class DummyType(object):
    def __init__(self, files):
        """`files` is a sequence of (data, filename) tuples."""
        self.files = files and [NamedFile(data=d, filename=fn) for (d, fn) in files]

class AsTextDiffTestCase(unittest.TestCase):
    
    def setUp(self):
        pass    
            
    def test_should_diff_file_lists_correctly(self):                        
        self._test_diff_files(
            [('data1', u'filename1')], 
            [('data2', u'filename2')], 
            False
        )
        self._test_diff_files(
            [('data1', u'filename1'), ('datax', u'filenamex')], 
            [('data1', u'filename1'), ('datay', u'filenamey')], 
            False
        )
        self._test_diff_files(
            [('data1', u'filename1'), ('datax', u'filenamex')], 
            [('datax', u'filenamex'), ('data1', u'filename1')], 
            False
        )
        self._test_diff_files(
            [('data1', u'filename1')], 
            [('data1', u'filename1'), ('datax', u'filenamex')], 
            False
        )                        
        self._test_diff_files(
            [('data1', u'filename1')], 
            [('data1', u'filename1')], 
            True
        )
        self._test_diff_files(
            [('data1', u'filename1'), ('datax', u'filenamex')], 
            [('data1', u'filename1'), ('datax', u'filenamex')], 
            True
        )
        self._test_diff_files(
            [('data1', u'filename1'), ('datax', u'filenamex')], 
            None, 
            False
        )        
        self._test_diff_files(
            [('data1', u'filename1'), ('datax', u'filenamex')], 
            [], 
            False
        )        
        self._test_diff_files(None, None, True)
        self._test_diff_files([], [], True)
        self._test_diff_files([], None, True)
    
    def _test_diff_files(self, files1, files2, same):
        diff = DexterityFileListDiff(DummyType(files1), DummyType(files2), 'files')
        self.assertTrue(IDifference.providedBy(diff))
        self.assertEqual(diff.same, same)
        self.assertNotEqual(bool(diff.inline_diff()), same)