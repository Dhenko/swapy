"""
Wrapper for IEdmVault5 in Solidworks API. For more information: https://help.solidworks.com/2025/english/api/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmVault5.html?id=31d027e9333745cc8a66b4af12822ae2&_gl=1*ygrlz8*_up*MQ..*_ga*Mzk2ODgxMDIuMTc1MzI3NTYzOA..*_ga_XQJPQWHZHH*czE3NTMzNjkxOTEkbzIkZzAkdDE3NTMzNjkxOTEkajYwJGwwJGgw#Pg0

Allows you to access a file vault.
"""

from ..Enumerations import EdmBrowseFlag, EdmObjectType
from swapy.utils.helpers import VBNothing
import IEdmStrList5, IEdmFolder5, IEdmFile5, IEdmObject5
import os


class IEdmVault5:
    def __init__(self, comm_obj):
        """
        This interface represents a SOLIDWORKS PDM Professional file vault.
        It is the highest-level interface within this API;
        most of the other interfaces in this API are retrieved from this interface either directly or indirectly.
        :param comm_obj: COM object representing IEdmVault5 instance from Solidworks API\n
        """
        self.__comm_obj = comm_obj
        self.CommandID = self.__comm_obj.CommandID
        self.IsLoggedIn = self.__comm_obj.IsLoggedIn
        self.Languange = self.__comm_obj.Language
        self.Name = self.__comm_obj.Name
        self.RootFolder = self.__comm_obj.RootFolder
        self.RootFolderID = self.__comm_obj.RootFolderID
        self.RootFolderPath = self.__comm_obj.RootFolderPath
        self.SilentMode = self.__comm_obj.SilentMode

    def BrowseForFile(self, hParentWnd,
                      lEdmBrowseFlags: int = EdmBrowseFlag.EdmBws_ForOpen,
                      bsFilter: str = "",
                      bsDefaultExtension: str = "",
                      bsDefaultFileName: str = "",
                      bsDefaultFolder: str = "",
                      bsCaption: str = ""):
        """
        Displays an Open (default) or Save As dialog box in which the user can click one or more files.
        :param hParentWnd: Parent window handle
        :param lEdmBrowseFlags: Optional combination of EdmBrowseFlag bits
        :param bsFilter: Optional filter string that limits the types of files displayed in the dialog box
        :param bsDefaultExtension: Optional default file extension to append if the user does not specify an extension
        :param bsDefaultFileName: Optional default file name to display in the file name field of the dialog box
        :param bsDefaultFolder: Optional path to the folder on which the dialog box should initially open
        :param bsCaption: Optional caption for the dialog box
        :return: IEdmStrLst5; list of paths to multi-selected files; Null if the user clicks Cancel
        """
        file_list = self.__comm_obj.BrowseForFile(hParentWnd,
                                             lEdmBrowseFlags,
                                             bsFilter,
                                             bsDefaultExtension,
                                             bsDefaultFileName,
                                             bsDefaultFolder,
                                             bsCaption)
        if file_list:
            return IEdmStrList5(file_list)

        else:
            return None

    def GetFileFromPath(self, bsFilePath: str, ppoRetParentFolder: IEdmFolder5 = None):
        """
        Gets an interface to the file with the specified file system path.
        :param bsFilePath: File system path to the file for which to get an interface
        :return: IEdmFile5; Null if file specified in bsFilePath does not exist
        """

        if not ppoRetParentFolder:
            ppoRetParentFolder = VBNothing
        file = self.__comm_obj.GetFileFromPath(bsFilePath, ppoRetParentFolder)

        if os.path.isfile(bsFilePath) and bsFilePath.lower().endswith(('sldprt', 'sldasm', 'slddrw')):
            return IEdmFile5(file)
        else:
            return None

    def GetFolderFromPath(self, bsFolderPath: str):
        """
        Gets an interface to a folder on the specified file system path.
        :param bsFolderPath: File system path to the folder
        :return: IEdmFolder5; Null if the folder in bsFolderPath is not found
        """

        if os.path.isdir(bsFolderPath):
            return IEdmFolder5(self.__comm_obj.GetFileFromPath(bsFolderPath))
        else:
            return None

    def GetObject(self, eType: EdmObjectType, lObjectID: int):
        """
        Gets an interface to a SOLIDWORKS PDM Professional object of the specified type and having the specified ID.
        :param eType: Type of object to get as defined in EdmObjectType
        :param lObjectID: ID of object to get
        :return:
        """
        if eType in EdmObjectType:
            return IEdmObject5(self.__comm_obj.GetObject(eType, lObjectID))
        else:
            return None

    def GetVaultNameFromPath(self, bsPath: str):
        """
        Gets the name of the vault where the specified file or folder resides.\n

        You do not need to call IEdmVault5::Login or IEdmVault5::LoginAuto before calling this method.
        :param bsPath: Full system path to a file or folder
        :return:
        """
        if os.path.isdir(bsPath) or os.path.isfile(bsPath):
            return self.__comm_obj.GetVaultNameFromPath(bsPath)
        else:
            return None

    def Login(self, bsUserName: str, bsPasswd: str, bsVaultName: str):
        """
        Logs in to the specified vault using the specified user name and password.
        :param bsUserName: User name of user created in the SOLIDWORKS PDM Professional User Manager
        :param bsPasswd: Password for bsUserName
        :param bsVaultName: Vault name
        :return:
        """
        return self.__comm_obj.Login(bsUserName, bsPasswd, bsVaultName)

    def LoginAuto(self, bsVaultName: str, hParentWnd: int):
        """
        Logs in to the specified vault.
        :param bsVaultName: Vault name
        :param hParentWnd: Parent window handle; used when the login dialog box displays to ensure it remains visible
        :return:
        """
        return self.__comm_obj.LoginAuto(bsVaultName, hParentWnd)

    def RefreshFolder(self, bsFolderPath: str):
        """
        Refreshes the file listing in the specified folder.
        :param bsFolderPath: File system path to the folder to refresh
        :return:
        """
        return self.__comm_obj.RefreshFolder(bsFolderPath)
