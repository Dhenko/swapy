"""
Wrapper for IEdmStrLst5 in Solidworks API. For more information: https://help.solidworks.com/2025/english/api/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmStrLst5.html?id=c0ea1c02f937410faad349b08b03035b&_gl=1*1ngrod9*_up*MQ..*_ga*Mzk2ODgxMDIuMTc1MzI3NTYzOA..*_ga_XQJPQWHZHH*czE3NTMzNjkxOTEkbzIkZzAkdDE3NTMzNjkxOTEkajYwJGwwJGgw#Pg0

Allows you to access a list of arbitrary strings.
"""

import IEdmPos5


class IEdmStrLst5:
    def __init__(self, comm_object):
        """
        Allows you to access a list of arbitrary strings.
        :param comm_object: COM object representing IEdmStrLst5 instance from Solidworks API\n
        """
        self.__comm_object = comm_object
        self.Count = self.__comm_object.Count
        self.IsEmpty = self.__comm_object.IsEmpty

    def AddTail(self, bsString):
        """
        Adds a string to the end of this list.
        :param bsString: String to add to the end of this list
        :return:
        """
        return self.__comm_object.AddTail(bsString)

    def GetHeadPosition(self):
        """
        Starts an enumeration of the strings in this list.\n\n

        After calling this method, pass the returned position of the first string to IEdmStrLst5::GetNext to get the
        first string in this list. Then call IEdmStrLst5::GetNext repeatedly to get the rest of the strings in this list.
        :return: IEdmPos5; position in the list of the first string (see Remarks)
        """
        return IEdmPos5(self.__comm_object.GetHeadPosition())

    def GetNext(self, poPos: IEdmPos5):
        """
        Gets the next string in this list.
        :param poPos: position of the next string in this list
        :return: Next string in this list
        """
        return self.__comm_object.GetNext(poPos)
