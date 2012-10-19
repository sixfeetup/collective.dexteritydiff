from Products.CMFDiffTool.CMFDTHtmlDiff import CMFDTHtmlDiff


class RichTextDiff(CMFDTHtmlDiff):
    """diff p.a.textfield rich text fields
    """
    def _parseField(self, value, filename=None):
        if not value:
            value = ''
        else:
            value = value.raw
        # the output here is unicode, it is unclear if CMFDTHtmlDiff can 
        # handle that directly, but it seems to work.  Keep eyes open for 
        # encoding/decoding errors.
        return CMFDTHtmlDiff._parseField(self, value, filename)
