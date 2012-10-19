from Products.CMFDiffTool.TextDiff import TextDiff
from Products.CMFDiffTool.ListDiff import ListDiff


class DictRowListDiff(ListDiff):
    """diff of DataGrid dict rows"""
    # XXX: This could be __much__ more interesting if we iterated over the
    #      schema of the dictrow and provided appropriate diffs of the contained
    #      values.  
    
    same_fmt = """<div class="%s">%s</div>"""
    inlinediff_fmt = TextDiff.inlinediff_fmt
    
    def __init__(self, obj1, obj2, field, id1=None, id2=None, field_name=None, field_label=None, 
        schemata=None):
        ListDiff.__init__(self, obj1, obj2, field, id1, id2, field_name, field_label, schemata)
        
        old_values = list(self.oldValue or [])
        new_values = list(self.newValue or [])
        
        self.same = True        
        if len(old_values) != len(new_values):
            self.same = False
        else:                
            for (old, new) in zip(old_values, new_values):
                if not is_same(old, new):
                    self.same = False
                    break

    def _parseField(self, value, filename=None):
        # convert dicts to strings for simplest possible comparison
        return [repr(row) for row in value]


def is_same(old_dict, new_dict):
    """compare keys and values to determine if the dicts are the same"""
    return old_dict == new_dict
