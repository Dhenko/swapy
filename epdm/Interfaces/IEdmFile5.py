"""
Wrapper for IEdmFile5 in Solidworks API. For more information: https://help.solidworks.com/2025/english/api/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmFile5.html?id=4dc9b4803a8b40669f3aa85748110afa&_gl=1*16bbfdg*_up*MQ..*_ga*MTUxMTY3NzUyOC4xNzQ4OTMyMTIy*_ga_XQJPQWHZHH*czE3NDg5Mzg3MzUkbzIkZzAkdDE3NDg5Mzg3MzUkajYwJGwwJGgw#Pg0

Allows you to access a file in SOLIDWORKS PDM Professional.
"""

import IEdmObject5, IEdmPos5, IEdmEnumeratorVariable5, IEdmStrList5
from swapy.utils.helpers import VBNothing


class IEdmFile5(IEdmObject5):
    def __init__(self, comm_object):
        """
        Creates an instance of the IEdmFile5 wrapper from the Solidworks API, and its corresponding IEdmObject5 super
        :param comm_object: COM object representing IEdmFile5 instance from Solidworks API\n
        Obtained from:\n
        - IEdmFolder5::GetFile\n
        - IEdmFolder5::GetNextFile\n
        - IEdmLabel5::GetNextFile\n
        - IEdmReference5::File\n
        - IEdmState5::GetNextFle\n
        - IEdmVault5::GetFileFromPath\n
        - IEdmVault5::GetObject\n\n

        Properties\n
        - CurrentRevision   - Gets the file's current revision.\n
        - CurrentState	    - Gets the file's current workflow state.\n
        - CurrentVersion  	- Gets the file's current version number.\n
        - ID	            - Gets the database ID of this file.\n
        - IsLocked	        - Gets whether the file is checked out.\n
        - LockedByUser	    - Gets the user who has the file checked out.\n
        - LockedByUserID    - Gets the ID of the user who has the file checked out.\n
        - LockedInFolder  	- Gets the folder in which this file is checked out.\n
        - LockedInFolderID	- Gets the ID of the folder in which this file is checked out.\n
        - LockedOnComputer	- Gets the name of the computer to which the file is checked out.\n
        - LockPath          - Gets the full path to the checked-out file.\n
        - Name	            - Gets the name of the file.\n
        - ObjectType	    - Gets the type of object.\n
        - Vault	            - Gets the file vault to which this file belongs.\n
        """
        super().__init__(comm_object)
        self.__comm_object = comm_object
        self.CurrentRevision = self.__comm_object.CurrentRevision
        self.CurrentState = self.__comm_object.CurrentState
        self.CurrentVersion = self.__comm_object.CurrentVersion
        self.IsLocked = self.__comm_object.IsLocked
        self.LockedByUser = self.__comm_object.LockedByUser
        self.LockedByUsedID = self.__comm_object.LockedByUserID
        self.LockedInFolder = self.__comm_object.LockedInFolder
        self.LockedInFolderID = self.__comm_object.LockedInFolderID
        self.LockedOnComputer = self.__comm_object.LockedOnComputer
        self.LockPath = self.__comm_object.LockPath

    def GetConfigurations(self):
        """
        Gets a list of names of the configurations for the specified version of this file.
        :return: IEdmStrList5
        """
        return IEdmStrList5(self.__comm_object.GetConfigurations())

    def GetEnumeratorVariable(self, bsOptionalPath: str = None):
        """
        Gets an interface to this file's data card variables.\n

        You must check out a file in order to write variables in its data card.
        :param bsOptionalPath: Optional; full file path to the file to access; if not specified, uses location where this file is checked out
        :return:
        """
        if self.IsLocked:
            bsOptionalPath = self.LockedInFolder if not bsOptionalPath else bsOptionalPath
        else:
            raise ValueError("File is not locked out.")

        return IEdmEnumeratorVariable5(self.__comm_object.GetEnumeratorVariable(bsOptionalPath))

    def GetFileCopy(self):
        pass

    def GetFirstFolderPosition(self):
        pass

    def GetLocalFileDate(self):
        pass

    def GetLocalPath(self):
        pass

    def GetLocalRevisionName(self):
        pass

    def GetNextFolder(self, poPosition: IEdmPos5):
        """
        Gets the next parent folder of this file.
        Before calling this method the first time, you must populate poPosition with the interface to the
        position of the first parent folder, IEdmPos5. Call IEdmFile5::GetFirstFolderPosition to obtain IEdmPos5. \n
        After calling this method the first time, poPos is automatically incremented every time it is called.
        Call this method repeatedly to obtain the rest of the folders.\n

        Be sure to call IEdmPos5::IsNull before you call this method to ensure you have not reached the end of the enumeration.\n

        C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmFolder5.\n
        :param poPosition: IEdmPos5; position of next parent folder of this file
        :return: IEdmFolder5
        """
        return self.__comm_object.GetNextFolder(poPosition)

    def GetReferenceTree(self, lParentFolderID: int, lVersionNo: int = 0):
        """
        Gets an interface to the files that reference or are referenced by this file.\n
        Some file types, such as files from AutoCAD, SOLIDWORKS, MS Word, etc., contain references to other files.
        You can also set up your own references via SOLIDWORKS PDM Professional's User Defined File References dialog box.
        SOLIDWORKS PDM Professional manages all of these references for you, and they appear in the check-in
        dialog box in the form of a reference tree.\n

        To specify lParentFolderID, inspect all of the parent folders of this file by calling
        IEdmFile5::GetFirstFolderPosition and IEdmFile5::GetNextFolder.\n

        Use IEdmReference5 that is returned in ppoRetRoot to enumerate referenced files
        and referencing files and set up user-defined references.\n

        C++ programmers not using smart-pointer wrapper functions must release the returned interface, IEdmReference5.

        Return:\n
        - S_OK: The method successfully executed.\n
        - S_FALSE: An argument is invalid.\n
        :param lParentFolderID: ID of the file's parent folder (see Remarks)
        :param lVersionNo: Version of the file for which to get references; 0 to get the latest version
        """
        return self.__comm_object.GetReferenceTree(lParentFolderID, lVersionNo)

    def GetRevisionGeneratorInfo(self):
        pass

    def IncrementRevision(self):
        pass

    def LockFile(self, lParentFolderID: int, lParentWnd: int, lEdmLockFlags: int = 0):
        """
        Checks out this file from the vault to which the user is currently logged in.\n
        Return:\n
        - S_OK: The method successfully executed.\n
        - E_EDM_FILE_IS_LOCKED: The file is already checked out.\n
        - E_EDM_PERMISSION_DENIED: The user lacks permission to check out this file.\n
        - E_EDM_OPERATION_REFUSED_BY_PLUGIN: One of the installed EdmCmdType.EdmCmd_PreLock hooks did not permit the operation.\n
        - E_EDM_FILE_NOT_FOUND: The file was not found in the vault.\n
        :param lParentFolderID: ID of parent folder to which to check out the file
        :param lParentWnd: Parent window handle
        :param lEdmLockFlags: Optional combination of EdmLockFlag bits; default is EdmLockFlag.EdmLock_Simple
        """
        if self.IsLocked:
            raise PermissionError(f"The file is already checked out by {self.LockedByUser}")
        else:
            return self.__comm_object.LockFile(lParentFolderID, lParentWnd, lEdmLockFlags)

    def Refresh(self):
        """
        Refreshes the file.
        :return:
        """
        self.__comm_object.Refresh()

    def UndoLockFile(self):
        pass

    def UnlockFile(self, lParentWnd: int, bsComment: str, lEdmUnlockFlags: int = 0, poIEdmRefCallback = VBNothing):
        """
        Checks in this file.\n
        Return: \n
        - S_OK: The method successfully executed.\n
        - S_FALSE: The method successfully executed, but as no file is modified, SOLIDWORKS PDM Professional did not create a new version.\n
        - E_EDM_FILE_NOT_LOCKED_BY_YOU: The file is not checked out by the logged-in user.\n
        - E_EDM_LOCKED_ON_OTHER_COMPUTER: The file is not checked out on the client machine where you tried to check it in.\n
        - E_EDM_FILE_NOT_FOUND: The file is not part of the vault.\n
        - E_EDM_LOCAL_FILE_NOT_FOUND: There is no copy of the file in the cache folder on the client machine.\n
        - E_EDM_FILE_SHARE_ERROR: The file is open exclusively in another program.\n
        - E_EDM_CANCELLED_BY_USER: Not implemented.\n
        - E_EDM_INVALID_FILE: The file format is not recognized, and you have specified to not check in such files.\n
        - E_EDM_MISSING_MANDATORY_VALUE: The file lacks a value for a required file data card variable.\n
        - E_EDM_OPERATION_REFUSED_BY_PLUGIN: One of the loaded EdmCmdType.EdmCmd_PreUndoLock hooks did not permit the operation.\n
        - E_EDM_FILE_NOT_REGENERATED: The file needs to be rebuilt.\n
        - E_EDM_NO_WORKFLOW: The document does not meet the conditions of any workflow.\n
        - E_EDM_CIRCULAR_XREF: A cyclic file reference was detected.\n
        - E_EDM_SWDRW_SETTO_USE_INDEPENDENT_REV_TABLE: An independent type revision setting is used in the drawing.\n
        - E_EDM_NO_DOCTYPE: The document does not meet the conditions of any category.\n
        - E_EDM_LOCKED_IN_OTHER_FOLDER: The file is checked out in another folder.\n
        - E_EDM_FILE_NAME_NOT_GLOBALLY_UNIQUE: The file name is not unique.\n
        - E_EDM_TOOLBOX_FILE_LOCATED_IN_NONTOOLBOX_FOLDER: Toolbox file must be located in a Toolbox folder.\n
        :param lParentWnd: Parent window handle
        :param bsComment: Version comment to show in the history dialog box
        :param lEdmUnlockFlags: Optional combination of EdmUnlockFlag bits; default is EdmUnlockFlag.EdmUnlock_Simple
        :param poIEdmRefCallback: Optional Nothing or null
        """
        if poIEdmRefCallback is not VBNothing:
            raise ValueError("poIEdmRefCallback is not the correct type. Make sure it is a viable 'nothing' variable for Visual Basic")
        if not self.IsLocked:
            print(f"File is already checked in")
        else:
            return self.__comm_object.UnlockFile(lParentWnd, bsComment, lEdmUnlockFlags, poIEdmRefCallback)
