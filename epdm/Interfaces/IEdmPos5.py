"""
Wrapper for IEdmPos5 in Solidworks API. For more information: https://help.solidworks.com/2025/english/api/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmPos5_members.html?_gl=1*8c5y7g*_up*MQ..*_ga*MTgyMTMxOTQ5My4xNzQ5MDQ1NDg2*_ga_XQJPQWHZHH*czE3NDkwNDU0ODUkbzEkZzAkdDE3NDkwNDU0ODUkajYwJGwwJGgw

Allows you to access a position in SOLIDWORKS PDM Professional.
"""


class IEdmPos5:
    def __init__(self, comm_object):
        """
        Allows you to identify the position of an element in a list of elements.
        :param comm_object: COM object representing IEdmFile5 instance from Solidworks API\n
        """
        self.__comm_object = comm_object
        self.IsNull = self.__comm_object.IsNull

    def Clone(self):
        pass
