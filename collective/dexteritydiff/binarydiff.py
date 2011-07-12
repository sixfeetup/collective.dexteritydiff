from Products.CMFDiffTool.BinaryDiff import BinaryDiff
from plone.dexterity.interfaces import IDexterityFTI
from z3c.form.interfaces import IDataManager
from zope.component import getMultiAdapter, getUtility
from zope.schema import getFields
from plone.namedfile.utils import stream_data

class DexterityBinaryDiff(BinaryDiff):
    
    def __init__(self, obj1, obj2, field, id1=None, id2=None, field_name=None, field_label=None, 
        schemata=None):
        
        self.field = field
        self.label = field_label or field
        self.schemata = schemata or 'default'
        self.field_name = field_name or field
        
        old_field = getattr(obj1, field)
        new_field = getattr(obj2, field)
                
        self.oldValue = getattr(old_field, 'data', None)
        self.newValue = getattr(new_field, 'data', None)
                
        self.id1 = id1 or getattr(obj1, 'getId', lambda: None)()
        self.id2 = id2 or getattr(obj2, 'getId', lambda: None)()
                
        self.oldFilename = getattr(old_field, 'filename', None)
        self.newFilename = getattr(new_field, 'filename', None)
        
        self.same = (self.oldValue == self.newValue)
        if (self.oldFilename is not None) and (self.newFilename is not None) and self.same:
            self.same = (self.oldFilename == self.newFilename)
    
#    def _get_data(self, obj):
#        fti = getUtility(IDexterityFTI, name=obj.portal_type)
#        schema = fti.lookupSchema()
#        field_obj = getFields(schema)[self.field_name]        
#        dm = getMultiAdapter((obj, field_obj), IDataManager)
#        return dm.get().file