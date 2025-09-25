"""
Wrapper for IEdmObject5 in Solidworks API. For more information: https://help.solidworks.com/2025/english/api/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmObject5.html?_gl=1*1u62hmp*_up*MQ..*_ga*MTUxMTY3NzUyOC4xNzQ4OTMyMTIy*_ga_XQJPQWHZHH*czE3NDg5Mzg3MzUkbzIkZzEkdDE3NDg5Mzg3NjkkajI2JGwwJGgw

Almost all objects that are stored in SOLIDWORKS PDM Professional's database inherit from this parent interface. See EmdObjectType for a list of all of the interfaces that inherit from IEdmObject5.

You can retrieve all objects inheriting from IEdmObject5 using IEdmVault5::GetObject if you know the type and the database ID.

This interface inherits from IDispatch. See IDispatch Interface (Automation).
"""

from ..Enumerations import EdmObjectType


class IEdmObject5:
    def __init__(self, comm_object):
        """
        Creates an instance of the IEdmObject5 wrapper from the Solidworks API
        :param comm_object: COM object representing IEdmObject5 instance from Solidworks API\n
        Obtained from:\n
        - IEdmVault5::GetObject\n
        Properties:\n
        - ID	        - Gets the database ID of this object.\n
        - Name	    - Gets the name of the object.\n
        - ObjectType	- Gets the type of object.\n
        - Vault	    - Gets the file vault to which this object belongs.\n
        """
        self.__comm_object = comm_object
        self.ID = self.__comm_object.ID
        self.Name = self.__comm_object.Name
        self.ObjectType = self.__comm_object.ObjectType
        self.Vault = self.__comm_object.Vault

    def IsKindOf(self, __MIDI__IEdmObject50000: EdmObjectType):
        """
        Checks whether the object is of a certain type.
        :param __MIDI__IEdmObject500: Type of object as defined in EdmObjectType
        :return: True if the object is of the specified type, false if not
        """
        return self.__comm_object.IsKindOf(__MIDI__IEdmObject50000)

    def Refresh(self):
        """
        Re-reads cached properties from the database.
        In a multi-user implementation, the object may change as you are working on it. Call this method to ensure that you are seeing the latest state of the object.
        For performance reasons, some object properties might be cached in the object itself. This method ensures that cached properties are re-read from the database.
        :return:S_OK: The method successfully executed.
                S_EDM_DATABASE_ACCESS: General error accessing the database.
        """
        return self.__comm_object.Refresh()
