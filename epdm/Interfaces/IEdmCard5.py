"""
Wrapper for IEdmCard5 in Solidworks API. For more information: https://help.solidworks.com/2025/English/api/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmCard5.html?verRedirect=1

Allows you to access the file or folder data card that is created with the SOLIDWORKS PDM Professional's Card Editor.
"""

import IEdmObject5, IEdmCardControl5, IEdmPos5


class IEdmCard5(IEdmObject5):
    def __init__(self, comm_object):
        """
        Creates an instance of the IEdmCard5 wrapper from the Solidworks API, and its corresponding IEdmObject5 super
        :param comm_object: COM object representing IEdmCard5 instance from Solidworks API\n
        Obtained from:\n
        - IEdmFolder5::GetCard\n
        - IEdmVault5::GetObject\n
        """

        super().__init(comm_object)
        self.__comm_object = comm_object

    def GetControl(self, lControlID: int):
        """
        Gets a card control with the specified ID.
        :param lControlID: ID of card control to get
        :return: IEdmCardControl5
        """
        return IEdmCardControl5(self.__comm_object.GetControl(lControlID))

    def GetControlID(self, poVariableNameOrID):
        """
        Gets the ID of the control that is connected to the specified variable in this card.
        :param poVariableNameOrID: ID or name of the variable for which to get the control ID
        :return: Control ID; 0 if the variable isn't used by any control in this card
        """
        return self.__comm_object.GetControlID(poVariableNameOrID)

    def GetFirstControlPosition(self):
        """
        Starts an enumeration of the controls in this data card.\n

        After calling this method, pass the returned position of the first control to IEdmCard5::GetNextControl to get
        the first control in the list. Call IEdmCard5::GetNextControl repeatedly to get the rest of the controls in the list.
        :return:
        """
        return IEdmPos5(self.__comm_object.GetFirstControlPosition())

    def GetNextControl(self, poPos: IEdmPos5):
        """
        Gets the next control in the enumeration.\n

        Before calling this method the first time, you must populate poPos with the interface to the position of the
        first control, IEdmPos5. Call IEdmCard5::GetFirstControlPosition to obtain IEdmPos5.\n

        After calling this method the first time, poPos is automatically incremented every time it is called.
        Call this method repeatedly to obtain the rest of the controls.\n

        Be sure to call IEdmPos5::IsNull before you call this method to ensure you have not reached the end of the enumeration.
        :param poPos: IEdmPos5; position of the next control in the list
        :return: IEdmCardControl5
        """
        return IEdmCardControl5(self.__comm_object.GetNextControl(poPos))

    def GetSize(self):
        """
        Gets the size of this data card.
        :return: Width, Height
        """
        return self.__comm_object.GetSize()