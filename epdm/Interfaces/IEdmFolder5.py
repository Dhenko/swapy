"""
Wrapper for IEdmFile5 in Solidworks API. For more information: https://help.solidworks.com/2025/english/api/epdmapi/epdm.interop.epdm~epdm.interop.epdm.iedmfolder5.html?verRedirect=1

Allows you to access the contents of a file system folder in the vault.
"""

import IEdmObject5, IEdmVault5, IEdmFolderData5, IEdmCard5, IEdmFile5, IEdmPos5, IEdmLabel5
from swapy.utils.helpers import VBNothing


class IEdmFolder5(IEdmObject5):
    def __init__(self, comm_object):
        """
        Creates an instance of the IEdmFolder5 wrapper from the Solidworks API, and its corresponding IEdmObject5 super
        :param comm_object: COM object representing IEdmFolder5 instance from Solidworks API\n
        Obtained from:\n
        - IEdmFile5::GetNextFolder\n
        - IEdmFile5::LockedInFolder\n
        - IEdmFolder5::AddFolder\n
        - IEdmFolder5::CreateFolderPath\n
        - IEdmFolder5::GetNextSubFolder\n
        - IEdmFolder5::GetSubFolder\n
        - IEdmFolder5::ParentFolder\n
        - IEdmLabel5::GetNextFolder\n
        - IEdmReference5::Folder\n
        - IEdmReference5::LockedInFolder\n
        - IEdmVault5::BrowseForFolder\n
        - IEdmVault5::GetFileFromPath\n
        - IEdmVault5::GetFolderFromPath\n
        - IEdmVault5::GetObject\n
        - IEdmVault5::GetFileFromPath\n
        - IEdmVault5::GetFolderFromPath\n
        - IEdmVault5::RootFolder
        """

        super().__init__(comm_object)
        self.__comm_object = comm_object
        self.ID = self.__comm_object.ID
        self.LocalPath = self.__comm_object.LocalPath
        self.Name = self.__comm_object.Name
        self.ObjectType = self.__comm_object.ObjectType
        self.ParentFolder = IEdmFolder5(self.__comm_object.ParentFolder)
        self.Vault = IEdmVault5(self.__comm_object.Vault)

    def AddFolder(self, lParentWnd: str, bsFolderName: str, poData: IEdmFolderData5 = None):
        """
        Creates a subfolder in this folder.\n

        To add more than one folder, use IEdmBatchAddFolders to add them all at once, which is much more efficient
        than using this method, which adds folders only one at a time.\n

        If poData is null, the user rights and file data card for the new folder are inherited from the parent folder.\n
        :param lParentWnd: Parent window handle
        :param bsFolderName: Name of the new folder
        :param poData: optional additional data
        :return:
        """
        if not poData:
            poData = VBNothing

        return self.__comm_object.AddFolder(lParentWnd, bsFolderName, poData)

    def DeleteFile(self, lParentWnd: int, lFileID: int, bRemoveLocalCopy: bool = True):
        """
        Deletes a file having the specified ID from this folder.\n

        If the specified file is shared to other folders, it is deleted only from this folder.\n
        :param lParentWnd: Parent window handle
        :param lFileID: ID of file to delete
        :param bRemoveLocalCopy: Optionally, true to erase the local copy of the file, false to not; default is true
        :return:
        """
        return self.__comm_object.DeleteFile(lParentWnd, lFileID, bRemoveLocalCopy)

    def DeleteFolder(self, lParentWnd: int, lSubfolderID: int, bRemoveLocalCopy: bool = True):
        """
        Deletes the specified subfolder from this folder.\n

        This method deletes only folders that are empty.\n
        :param lParentWnd: Parent window handle
        :param lSubfolderID: ID of folder to delete
        :param bRemoveLocalCopy: Optionally true to remove the folder from the local disk, false to not; default is true
        :return:
        """
        return self.__comm_object.DeleteFolder(lParentWnd, lSubfolderID, bRemoveLocalCopy)

    def GetCard(self, bsExtension: str):
        """
        Gets the interface to a data card of a file of the specified file type or the interface to the data card of this folder.
        :param bsExtension: Extension of file for which to get a data card; for example, "DWG" or "DOC" or "." to
        get the data card for this folder
        :return: IEdmCard5
        """
        return IEdmCard5(self.__comm_object.GetCard(bsExtension))

    def GetCardID(self, bsExtension: str):
        """
        Gets the ID of the data card of a file with the specified extension or the ID of the data card of this folder.
        :param bsExtension: Extension of file for which to get a data card ID; for example, "DWG" or "DOC" or "." to
        get the ID of the data card for this folder
        :return: ID of the data card (int); 0 if not found
        """
        return self.__comm_object.GetCardID(bsExtension)

    def GetFile(self, bsFileName: str):
        """
        Gets the interface to a file with the specified name in this folder.
        :param bsFileName: Name of file to get
        :return: IEdmFile5
        """
        return IEdmFile5(self.__comm_object.GetFile(bsFileName))

    def GetFirstFilePosition(self):
        """
        Starts an enumeration of the files in this folder.\n

        After calling this method, pass the returned first file position to IEdmFolder5::GetNextFile to get the first
        file in the list. Then call IEdmFolder5::GetNextFile repeatedly to get the rest of the files in the list.
        :return: IEdmPos5; position of the first file in this folder
        """
        return IEdmPos5(self.__comm_object.GetFirstFilePosition())

    def GetFirstLabelPosition(self):
        """
        Starts an enumeration of the labels in this folder.\n

        After calling this method, pass the returned first label position to IEdmFolder5::GetNextLabel to get the
        first label in the list. Then call IEdmFolder5::GetNextFile repeatedly to get the rest of the labels in the list.
        :return: IEdmPos5; position of the first label in this folder
        """
        return IEdmPos5(self.__comm_object.GetFirstLabelPosition())

    def GetFirstSubFolderPosition(self):
        """
        Starts an enumeration of the subfolders in this folder.\n

        After calling this method, pass the returned first subfolder position to IEdmFolder5::GetNextSubFolder to get
        the first subfolder in the list. Then call IEdmFolder5::GetNextSubFolder repeatedly to get the rest of the subfolders in the list.
        :return: IEdmPos5; position of the first sub-folder in this folder
        """
        return IEdmPos5(self.__comm_object.GetFirstSubFolderPosition())

    def GetNextFile(self, poPosition: IEdmPos5):
        """
        Gets the next file in the enumeration.\n

        Before calling this method the first time, you must populate poPosition with the interface to the position of
        the first file, IEdmPos5. Call IEdmFolder5::GetFirstFilePosition to obtain IEdmPos5.\n

        After calling this method the first time, poPos is automatically incremented every time it is called.
        Call this method repeatedly to obtain the rest of the files.\n

        Be sure to call IEdmPos5::IsNull before you call this method to ensure you have not reached the end of the enumeration.
        :param poPosition: IEdmPos5, position of file to retrieve
        :return: IEdmFile5
        """
        return IEdmFile5(self.__comm_object.GetNextFile(poPosition))

    def GetNextLabel(self, poPos: IEdmPos5):
        """
        Gets the next label in the enumeration.\n

        Before calling this method the first time, you must populate poPos with the interface to the position of the
        first label, IEdmPos5. Call IEdmFolder5::GetFirstLabelPosition to obtain IEdmPos5.\n

        After calling this method the first time, poPos is automatically incremented every time it is called.
        Call this method repeatedly to obtain the rest of the labels.\n

        Be sure to call IEdmPos5::IsNull before you call this method to ensure you have not reached the end of the enumeration.
        :param poPos: IEdmPos5, position of label to retrieve
        :return: IEdmLabel5
        """
        return IEdmLabel5(self.__comm_object.GetNextLabel(poPos))

    def GetNextSubFolder(self, poPosition: IEdmPos5):
        """
        Gets the next subfolder in the enumeration.\n

        Before calling this method the first time, you must populate poPosition with the interface to the position of
        the first subfolder, IEdmPos5. Call IEdmFolder5::GetFirstSubFolderPosition to obtain IEdmPos5.\n

        After calling this method the first time, poPos is automatically incremented every time it is called.
        Call this method repeatedly to obtain the rest of the subfolders.\n

        Be sure to call IEdmPos5::IsNull before you call this method to ensure you have not reached the end of the enumeration.
        :param poPosition: IEdmPos5, position of the subfolder to retrieve
        :return: IEdmFolder5
        """
        return IEdmFolder5(self.__comm_object.GetNextSubFolder(poPosition))

    def GetSubFolder(self, bsFolderName: str):
        """
        Gets the interface to the subfolder with the specified name.
        :param bsFolderName: Name of subfolder to get
        :return:
        """
        return IEdmFolder5(self.__comm_object.GetSubFolder(bsFolderName))
