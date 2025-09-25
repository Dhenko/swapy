"""
Wrapper for IEdmEnumeratorVariable5 in Solidworks API. For more information: https://help.solidworks.com/2025/english/api/epdmapi/epdm.interop.epdm~epdm.interop.epdm.iedmenumeratorvariable5.html

Allows you to access the contents of a file or folder data card.

This interface:

inherits from IDispatch. See IDispatch Interface (Automation).
is extended by IEdmEnumeratorVariable6 which adds the ability to read a variable directly from the database.
The IEdmEnumeratorVariablen interface is a pointer to a file. If this pointer is not released, then other operations on the file can fail with a sharing violation. The recommendation in SOLIDWORKS PDM Professional 2008 and later is to always call IEdmEnumeratorVariable8::CloseFile when you are finished updating a file to make it possible for other applications and API functions to access the file. This replaces the earlier work-around to explicitly clear IEdmEnumeratorVariable pointers (set them to Nothing in Visual Basic and call Marshal.ReleaseComObject in .NET).

IEdmEnumeratorVariablen interfaces on the following do not need calls to IEdmEnumeratorVariable8::CloseFile:

folders (cast IEdmFolder5 to this interface)
file data cards (for add-ins, this interface is stored in EdmCmd::mpoExtra of the poCmd argument returned in IEdmAddIn5::OnCmd only when EdmCmd::meCmdType = EdmCmdType.EdmCmd_CardButton or EdmCmdType.EdmCmd_CardInput)
"""


class IEdmEnumeratorVariable5:
    def __init__(self, comm_object):
        """
        Creates an instance of the IEdmEnumeratorVariable5 wrapper from the Solidworks API
        :param comm_object: COM object representing IEdmEnumeratorVariable5 instance from Solidworks API\n
        Obtained from:\n
        - IEdmAddIn5::OnCmd\n
        - IEdmFile5::GetEnumeratorVariable\n
        - IEdmFolder5\n
        """
        self.__comm_object = comm_object

    def Flush(self):
        """
        Saves data to a file or folder.\n

        You must call this method after calling IEdmEnumeratorVariable5::SetVar to ensure that new data gets properly saved.\n

        Return codes:\n
        - S_OK: The method successfully executed.\n
        - E_EDM_FILE_SHARE_ERROR: The file is opened exclusively in another application.\n
        """
        return self.__comm_object.Flush()

    def GetThumbnail(self):
        pass

    def GetUpdateVars(self, lFolderID: int, ):
        """
        Gets values for the variables that can be updated in this file.\n
        :param lFolderID: ID of the file's parent folder
        Return codes:\n
        - S_OK: The method successfully executed.\n
        - E_EDM_FILE_NOT_LOCKED_BY_YOU: The file is not checked out. \n
        :return:
        """
        return self.__comm_object.GetUpdateVars(lFolderID)

    def GetVar(self, bsVarName: str, bsCfgName: str):
        """
        Gets the value of the specified variable from this file or folder.
        :param bsVarName: Name of variable to read
        :param bsCfgName: Name of configuration or layout from which to get the variable value;
        empty string for folders and file types that do not support configurations\n
        To specify bsCfgName:

        Call IEdmFile5::GetConfigurations to get the available configuration names for this file.
        If this method is used in your add-in's implementation of IEdmAddIn5::OnCmd,
        then a list of configuration names for the data card is returned in ppoData that can be cast to EdmCmdData.
        EdmCmdData.mpoExtra contains an IEdmStrLst5 of configuration names.
        :return: Variable value; data type as specified in IEdmVariable5:VariableType
        """
        return self.__comm_object.GetVar(bsVarName, bsCfgName)

    def SetVar(self, bsVarName: str, bsCfgName: str, poValue, bOnlyIfPartOfCard: bool = False):
        """
        Sets the value of the specified variable in this file or folder.\n
        To specify bsCfgName:

        Call IEdmFile5::GetConfigurations to get the available configuration names for this file.
        If this method is used in your add-in's implementation of IEdmAddIn5::OnCmd,
        then a list of configuration names for the data card is returned in ppoData that can be cast to EdmCmdData.
        EdmCmdData.mpoExtra contains an IEdmStrLst5 of configuration names.\n

        After calling this method to update the variables that can be updated, you must call
        IEdmEnumeratorVariable5::Flush or IEdmEnumeratorVariable8::CloseFile with the bFlush argument set to true
        in order to ensure that the changes are saved properly to the file or folder.
        :param bsVarName: Name of variable to write
        :param bsCfgName: Name of configuration or layout to which to store the variable value; empty string for folders and file types that do not support configurations
        :param poValue: Variable value
        :param bOnlyIfPartOfCard:
        :return: Optional - True to store the variable only if it is part of the file or folder data card, false to store the variable as hidden data if it is not part of the file or folder data card (default)
        """
        return self.__comm_object.SetVar(bsVarName, bsCfgName, poValue, bOnlyIfPartOfCard)

    def StoreValuesFromDatabase(self, lFolderID: int, bOnlyMissingValues: bool):
        pass
