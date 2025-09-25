"""
Wrapper for IEdmReference5 in Solidworks API. For more information: https://help.solidworks.com/2025/english/api/epdmapi/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmReference5_members.html?_gl=1*ytd808*_up*MQ..*_ga*MTgyNTUxNTUyMC4xNzQ5MDQxNzc2*_ga_XQJPQWHZHH*czE3NDkwNDE3NzYkbzEkZzEkdDE3NDkwNDE3OTMkajQzJGwwJGgw
It includes all the methods and variables from IEdmReference6, IEdmReference7, IEdmReference8, IEdmReference9
and IEdmReference10 to simplify swapy structure

Allows you to access a reference in SOLIDWORKS PDM Professional.
"""

import IEdmPos5
import win32com.client


class IEdmReference5:
    def __init__(self, comm_object):
        """
        Creates an instance of the IEdmFile5 wrapper from the Solidworks API
        :param comm_object: COM object representing IEdmReference5 instance from Solidworks API\n
        Obtained from:\n
        - IEdmFile5::GetReferenceTree\n
        - IEdmReference5::GetNextChild\n
        - IEdmReference5::GetNextParent\n

        Properties:\n
        - File	            - Gets the file.
        - FileID	        - Gets the ID of the file.
        - Folder	        - Gets the file's parent folder.
        - FolderID	        - Gets the ID of the file's parent folder.
        - FoundPath	        - Gets the file system path where the file was found.
        - IsLocked	        - Gets whether the file is checked out.
        - LockedByUser	    - Gets the the user who checked out the file.
        - LockedInFolder	- Gets the folder in which the file is checked out.
        - LockedOnComputer	- Gets the name of the computer on which the file is checked out.
        - LockPath	        - Gets the file's check-out path.
        - Name	            - Gets the name of the file.
        - ReferencedAs	    - Gets how the file is included by the referencing file.
        - VersionLocal	    - Gets the local version number of the file.
        - VersionRef	    - Gets the referenced version number of the file.
        """
        self.__comm_object = comm_object
        self.File = self.__comm_object.File
        self.FileID = self.__comm_object.FileID
        self.Folder = self.__comm_object.Folder
        self.FolderID = self.__comm_object.FolderID
        self.FoundPath = self.__comm_object.FoundPath
        self.IsLocked = self.__comm_object.IsLocked
        self.LockedByUser = self.__comm_object.LockedByUser
        self.LockedImFolder = self.__comm_object.LockedInFolder
        self.LockedOnComputer = self.__comm_object.LockedOnComputer
        self.LockPath = self.__comm_object.LockPath
        self.Name = self.__comm_object.Name
        self.ReferencedAs = self.__comm_object.ReferencedAs
        self.VersionLocal = self.__comm_object.VersionLocal
        self.VersionRef = self.__comm_object.VersionRef

    def GetCustomData(self):
        pass

    def GetFirstChildPosition(self,
                              bIsTopParent: bool,
                              bPermitReadLocal: bool,
                              bGetSuppressedComponent: bool,
                              lEdmRefFlags: int,
                              bsConfiguration: str,
                              lVersion: int = 0):
        """
        Starts an enumeration of child references for the specified configuration.\n
        You should maintain and pass in a string, by reference, in this argument for all calls to this method in a reference tree.
        The project name can be allocated and returned by the topmost node in the tree and is used by its children.\n

        IEdmReference6::RefCount and IEdmReference8::RefCountEdited for child references return values for corresponding
        referenced configurations. If an empty string is passed to bsConfiguration, then the file's common configuration is used.\n

        Pass the position returned by this method to IEdmReference5::GetNextChild to continue to enumerate the referenced files.\n

        C++ programmers not using smart-pointer wrapper functions must release the position.\n

        Return code S_OK indicates that the method successfully executed.\n
        :param bIsTopParent: True if this is the topmost node in the reference tree, false if not
        :param bPermitReadLocal: True to allow SOLIDWORKS PDM Professional to read reference information if it is not
        already present in the database, false to disallow SOLIDWORKS PDM Professional to read reference information if
        it is not already present in the database
        :param bGetSuppressedComponent: True to get a suppressed reference, false to not
        :param lEdmRefFlags: Types of references that you want enumerated as defined in EdmRefFlags
        :param bsConfiguration: Configuration name for which to get child references (see Remarks)
        :param lVersion: Version for which to get references; use 0 for latest version (Default)
        :return: Position of the first file referenced by this file (see Remarks) and Project Name
        """
        _IEdmReference10_com = win32com.client.CastTo(self.__comm_object, "IEdmReference10")
        return _IEdmReference10_com.GetFirstChildPosition(bIsTopParent, bPermitReadLocal, bGetSuppressedComponent, lEdmRefFlags, bsConfiguration, lVersion)

    def GetFirstParentPosition(self, lVersionOrZero: int, bGetAllParentVersion: bool, lEdmRefFlags: int):
        """
        Starts an enumeration of parent references.\n
        Pass the position to IEdmReference5::GetNextParent to continue to enumerate all of the parent files.\n

        C++ programmers not using smart-pointer wrapper functions must release the position.\n

        Return code S_OK indicates that the method successfully executed.\n
        :param lVersionOrZero: Non-0 value enumerates the files referencing the specified version of the file; argument is ignored if value is 0
        :param bGetAllParentVersion: True to return all versions, of all parents, referencing this file; false to return on the latest referencing version
        :param lEdmRefFlags: Types of references that you want enumerated as defined in EdmRefFlags
        :return: Position of first file referencing this file
        """
        _IEdmReference7_com = win32com.client.CastTo(self.__comm_object, "IEdmReference7")
        return _IEdmReference7_com.GetFirstParentPosition2(lVersionOrZero, bGetAllParentVersion, lEdmRefFlags)

    def GetNextChild(self, poPos: IEdmPos5):
        """
        Enumerates the files referenced by this file.\n
        Call IEdmReference5::GetFirstChildPosition to get the position of the first referenced child file,
        before you call IEdmReference5::GetNextChild for the first time.\n

        After calling this method the first time, poPos is automatically incremented every time it is called.
        Call this method repeatedly to obtain the rest of the referenced child files.\n

        Return code S_OK indicates that the method successfully executed.\n
        :param poPos: Position of next child file to get
        :return: Child file
        """
        return self.__comm_object.GetNextChild(poPos)

    def GetNextParent(self, poPos: IEdmPos5):
        """
        Enumerates the files referencing this file.\n
        Call IEdmReference5::GetFirstParentPosition to get the position of the first referenced parent file,
        before you call this method the first time.\n

        After calling this method the first time, poPos is automatically incremented every time this method is called.
        Call this method repeatedly to obtain the rest of the referenced parent files.\n

        Return code S_OK indicates that the method successfully executed.\n
        :param poPos: Position of the next parent file to get
        :return: Parent file
        """
        return self.__comm_object.GetNextParent(poPos)

    def SetCustomData(self):
        pass
