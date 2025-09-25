"""
Wrapper for ISldWorks in Solidworks API. For more information: https://help.solidworks.com/2025/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html?id=c08057475f4b41f58893ba90503547fd&_gl=1*1gdphrr*_up*MQ..*_ga*MTQzNzM3OTU2NC4xNzUzMjc3Mzc2*_ga_XQJPQWHZHH*czE3NTMyNzczNzUkbzEkZzEkdDE3NTMyNzczNzgkajU3JGwwJGgw#Pg0

Provides direct and indirect access to all other interfaces exposed in the SOLIDWORKS API.
"""

from ..swconst.swRebuildOnActivation_e import swRebuildOnActivation_e
from swapy.sldworks import IModelDoc2


class ISldWorks:
    def __init__(self, comm_object):
        """
        This interface is the highest-level object in the SOLIDWORKS API. This interface provides a general set of
        functions that allow application-level operations such as create, open, close, and quit documents, arrange icons
        and windows, change the active document, and create attribute definitions.
        """
        self.__comm_object = comm_object
        self.ApplicationType = self.__comm_object.ApplicationType
        self.CommandInProgress = self.__comm_object.CommandInProgress
        self.EnableBackgroundProcessing = self.__comm_object.EnableBackgroundProcessing
        self.EnableFileMenu = self.__comm_object.EnableFileMenu
        self.FrameHeight = self.__comm_object.FrameHeight
        self.FrameLeft = self.__comm_object.FrameLeft
        self.FrameState = self.__comm_object.FrameState
        self.FrameTop = self.__comm_object.FrameTop
        self.FrameWidth = self.__comm_object.FrameWidth
        self.StartupProcessCompleted = self.__comm_object.StartupProcessCompleted
        self.TaskPaneIsPinned = self.__comm_object.TaskPaneIsPinned
        self.UserControl = self.__comm_object.UserControl
        self.UserControlBackground = self.__comm_object.UserControlBackground
        self.UserTypeLibReferences = self.__comm_object.UserTypeLibReferences
        self.Visible = self.__comm_object.Visible

    def GetActiveDoc(self):
        """
        Getter for self.__comm_object.ActiveDoc property, to wrap it into a IModelDoc2 class
        :return:
        """
        return IModelDoc2.IModelDoc2(self.__comm_object.ActiveDoc)

    def ActivateDoc3(self, Name: str, UseUserPreferences: bool = True, Option: swRebuildOnActivation_e = swRebuildOnActivation_e.swUserDecision):
        """
        Activates a loaded document and rebuilds it as specified.\n
        This method brings the document specified in Name to the foreground of SOLIDWORKS and returns a pointer to the document.\n\n

        If you do not specify a file extension in Name, the document activated is based on its filename without the
        file extension. This can cause problems if you have loaded two different document types with the same name
        (e.g., 12345.sldprt and 12345.sldasm). To avoid this problem, specify the file extension in Name or check the
        document type after it is activated using IModelDoc2::GetType.
        :param Name: Name of the loaded document to activate
        :param UseUserPreferences: True to rebuild as per the swRebuildOnActivation system option; false to rebuild as per Option
        :param Option: Rebuild option as defined in swRebuildOnActivation_e
        :return:
        """
        self.__comm_object.ActivateDoc3(Name, UseUserPreferences, Option)

    def ActivateTaskPane(self):
        pass

    def AddCallback(self):
        pass

    def AddFileOpenItem3(self):
        pass

    def AddFileSaveAsItem2(self):
        pass

    def AddItemToThirdPartyPopupMenu(self):
        pass

    def AddItemToThirdPartyPopupMenu2(self):
        pass

    def AddMenu(self):
        pass

    def AddMenuItem5(self):
        pass

    def AddMenuPopupItem3(self):
        pass

    def AddMenuPopupItem4(self):
        pass

    def AddToolbar5(self):
        pass

    def AddToolbarCommand2(self):
        pass

    def AllowFailedFeatureCreation(self):
        pass

    def ArrangeIcons(self):
        pass

    def ArrangeWindows(self):
        pass

    def BlockSkinning(self):
        pass

    def CallBack(self):
        pass

    def CheckpointConvertedDocument(self):
        pass

    def CloseAllDocuments(self, IncludeUnsaved: bool):
        """
        Closes all open documents in the SOLIDWORKS session.
        :param IncludeUnsaved:True if clase all documents, including dirty ones. False if close all documents, excluding dirty ones
        :return: True if successful, False if not successful
        """
        return self.__comm_object.CloseAllDocuments(IncludeUnsaved)

    def CloseAndReopen(self, Doc: IModelDoc2, Option: int):
        """
        Closes and reopens the specified drawing document without unloading its references from memory.\n\n
        Before a third-party application can process a drawing document that is open in SOLIDWORKS,
        it must close the document. Usually when a drawing document is closed, its references are unloaded from memory,
        and reopening the drawing document takes a lot of time. This method closes a drawing document,
        keeps its references in memory, and quickly reopens it.
        :param Doc: IModelDoc2; drawing document to close and reopen
        :param Option: Reopen options as defined in swCloseReopenOption_e
        :return: IModelDoc2; reopened drawing document
        """
        return self.__comm_object.CloseAndReopen(Doc, Option)

    def CloseAndReopen2(self, Doc: IModelDoc2, Option: int):
        """
        Closes and reopens the specified drawing document without unloading its references from memory.\n\n
        Before a third-party application can process a drawing document that is open in SOLIDWORKS,
        it must close the document. Usually when a drawing document is closed, its references are unloaded from memory,
        and reopening the drawing document takes a lot of time. This method closes a drawing document,
        keeps its references in memory, and quickly reopens it.
        :param Doc: IModelDoc2; drawing document to close and reopen
        :param Option: Reopen options as defined in swCloseReopenOption_e
        :return: IModelDoc2; reopened drawing document
        """
        return IModelDoc2.IModelDoc2(self.__comm_object.CloseAndReopen2(Doc, Option))

    def CloseDoc(self, Name: str):
        """
        Closes the specified document.\n
        :param Name: Name of document
        :return:
        """
        self.__comm_object.CloseDoc(Name)

    def CloseUserNotification(self):
        pass

    def Command(self):
        pass

    def CopyAppearance(self):
        pass

    def CopyDocument(self):
        pass

    def CreateNewWindow(self):
        pass

    def CreatePropertyManagerPage(self):
        pass

    def CreateTaskpaneView3(self):
        pass

    def DefineAttribute(self):
        pass

    def DefineMessageBar(self):
        pass

    def DefineUserNotification(self):
        pass

    def EnumDocuments2(self):
        """
        Gets a list of documents currently open in the application.
        """
        return self.__comm_object.EnumDocuments2()

    def ExitApp(self):
        """
        Shuts down SOLIDWORKS.
        """
        self.__comm_object.ExitApp()

    def Frame(self):
        """
        Gets the SOLIDWORKS main frame.
        """
        return self.__comm_object.Frame()

    def GetActiveConfigurationName(self, FilePathName: str):
        """
        Gets the name of the active configuration in the specified SOLIDWORKS document.
        :param FilePathName: Path for the SOLIDWORKS document
        :return: Name of the active configuration
        """
        return self.__comm_object.GetActiveConfigurationName(FilePathName)

    def GetConfigurationNames(self, FilePathName: str):
        """
        Gets the names of the configuration in this SOLIDWORKS document, whether the document is opened or closed.
        :param FilePathName: Path and file name for the SOLIDWORKS document
        :return: Array of strings containing the names of the configurations in this SOLIDWORKS document
        """
        return self.__comm_object.GetConfigurationNames(FilePathName)

    def GetCurrentWorkingDirectory(self):
        """
        Gets the current working directory being used by the SOLIDWORKS application.\n\n
        The current working directory is used when opening documents containing references. If explicit search folders
        are not set (see ISldWorks::SetSearchFolders), then the SOLIDWORKS application initially tries to locate file
        references (for example, assembly component parts) in the current working directory. Interactively,
        the current working directory is used by the File Open dialog and is set when you choose the Open dialog button.
        :return: str: Current working directory with trailing backslash
        """
        return self.__comm_object.GetCurrentWorkingDirectory()

    def GetMassProperties2(self, FilePathName: str, ConfigurationName: str, Accuracy: int):
        """
        Gets the mass properties from the specified document for the specified configuration.\n\n
        Consistent with all other functions, this method returns metric units unless otherwise specified.
        :param FilePathName: Document path and file name
        :param ConfigurationName: Name of the configuration to use
        :param Accuracy: 0 - as is, 1 - default, 2 - maximum
        :return: Array of doubles of size 13; last element is the accuracy at which mass properties are calculated
        """
        return self.__comm_object.GetMassProperties2(FilePathName, ConfigurationName, Accuracy)

    def GetMaterialDatabases(self):
        """
        Gets the names of the material databases.
        :return: Array of strings of the names of the material databases
        """
        return self.__comm_object.GetMaterialDatabases()

    def IActivateDoc3(self, Name: str, Silent: bool, Errors: int):
        """
        Activates a document that has already been loaded. This file becomes the active document, and this method returns a pointer to that document object.\n\n

        This file becomes the active document, and this method returns a pointer to that document object.\n\n

        If you do not specify a file extension in the name parameter, the document activated is based on its name and
        ignores the file extension. This can cause problems if you have two different document types with the same name
        loaded; for example, 12345.sldprt and 12345.sldasm.\n\n

        If you do not specify the filename extension in your call to this method, then you cannot be sure which document
        is activated. To avoid this problem, you can specify the file name extension in the name parameter or you can
        check the document type after it is activated using IModelDoc2::GetType.\n\n

        In some instances, a document requires a rebuild when it is activated. If this is the case and you have passed
        True for the silent argument, then the activated document is not rebuilt and swDocNeedsRebuildWarning is
        returned in the errors argument. You can then programmatically rebuild the document using the IModelDoc2::EditRebuild3 method.\n\n

        :param Name: Name of document to activate
        :param Silent: True if dialogs and warning messages should be avoided; false if dialogs and warning messages should be displayed to the end-user
        :param Errors: Status of the document activate operation as defined in swActivateDocError_e; if no errors or warnings are encountered, this value is set to 0
        :return: Model document
        """
        return IModelDoc2.IModelDoc2(self.__comm_object.IActivateDoc3(Name, Silent, Errors))

    def LoadFile4(self, FileName: str, ArgString: str, ImportData):
        """
        Loads a third-party native CAD file into a new SOLIDWORKS document using 3D Interconnect.
        :param FileName: Full path and file name of the third-party native CAD part or assembly document to import
        :param ArgString:Space-separated string that allows optional arguments to be specified when opening a third-party native CAD file; empty string if 3D Interconnect is enabled (see Remarks)
        :param ImportData: IImportIgesData, IImportDxfDwgData, or IImportStepData object; null or Nothing if 3D Interconnect is not enabled (see Remarks)
        :return: Model document and error
        """
        return IModelDoc2.IModelDoc2(self.__comm_object.LoadFile4(FileName, ArgString, ImportData))

    def MoveDocument(self, SourceDoc: str, DestDoc: str, FromChildren, ToChildren, Option: int):
        """
        Moves a document and optionally updates references to it.
        :param SourceDoc: Full path and filename of the document to move
        :param DestDoc: Full path and filename of the new document to which to move the document specified for SourceDoc
        :param FromChildren: Array of strings containing the full path and filenames of the child documents dependent on the document specified for SourceDoc
        :param ToChildren: Array of strings containing the new full path and filenames for the child documents to which to move the documents specified for FromChildren
        :param Option: Move options as defined by swMoveCopyOptions_e
        :return: Success or error code as defined by swMoveCopyError_e
        """
        return self.__comm_object.MoveDocument(SourceDoc, DestDoc, FromChildren, ToChildren, Option)

    def NewDocument(self, TemplateName: str, PaperSize: int, Width: float, Height: float):
        """
        Creates a new document based on the specified template.
        :param TemplateName: Fully qualified path and name of the template to use for creating the new document
        :param PaperSize: Size of paper as defined in swDwgPaperSizes_e
        :param Width: Width of paper; used only when PaperSize is swDwgPapersUserDefined
        :param Height: Height of paper; used only when PaperSize is swDwgPapersUserDefined
        :return: Newly created document or NULL if the operation fails
        """
        return IModelDoc2.IModelDoc2(self.__comm_object.NewDocument(TemplateName, PaperSize, Width, Height))
        if self.__comm_object.NewDocument(TemplateName, PaperSize, Width, Height) is not None:
            return IModelDoc2.IModelDoc2(self.__comm_object.NewDocument(TemplateName, PaperSize, Width, Height))
        else:
            return None

    def OpenDoc6(self, FileName: str, Type: str, Options: int, Configuration: str, Errors: int, Warnings: int):
        """
        Opens an existing document and returns a pointer to the document object.\n\n
        As of SOLIDWORKS 2008, ISldWorks::OpenDoc7 performs the same work as this method, but also:\n\n

        Allows you to open a document with a specified display state.\n\n
        Uses IDocumentSpecification to specify input parameters.\n\n
        :param FileName: Document name or full path if not in current directory, including extension
        :param Type: Document type as defined in swDocumentTypes_e
        :param Options: Mode in which to open the document as defined in swOpenDocOptions_e
        :param Configuration: Model configuration in which to open this document
        :param Errors: Load errors as defined in swFileLoadError_e
        :param Warnings: Warnings or extra information generated during the open operation as defined in swFileLoadWarning_e
        :return: Newly loaded model document or NULL if document failed to open
        """
        return IModelDoc2.IModelDoc2(self.__comm_object.OpenDoc6(FileName, Type, Options, Configuration, Errors, Warnings))

    def OpenDoc7(self, Specification):
        """
        Opens an existing document and returns a pointer to the document object.\n\n

        Calling ISldWorks::OpenDoc7 does not change the current working directory to that of the opened file, whereas,
        interactively using the File Open dialog box does. This may affect documents with references.\n\n

        Because the user may have interactively opened files from some random directory, you cannot be certain that the
        current working directory is pointing to the desired location. This may affect the referenced documents that
        ultimately get loaded when using ISldWorks::OpenDoc7 versus performing File Open interactively.
        You may want to set the current working directory before calling ISldWorks::OpenDoc7. This can be done using
        the ISldWorks::SetCurrentWorkingDirectory method.
        :param Specification: Document specification (IDocumentSpecification Interface)
        :return: Document (IModelDoc2 Interface)
        """
        return IModelDoc2.IModelDoc2(self.__comm_object.OpenDoc7(Specification))

    def QuitDoc(self, Name: str):
        """
        Closes the specified document without saving changes.
        :param Name: Name of document to close
        """
        self.__comm_object.QuitDoc(Name)

    def RunMacro2(self, FilePathName: str, ModuleName: str, ProcedureName: str, Options: int):
        """
        Runs a macro from a project file.
        :param FilePathName: Path and filename of the project file containing the macro
        :param ModuleName: Name of the module in the macro
        :param ProcedureName: Name of the procedure in the module
        :param Options: Option as defined swRunMacroOption_e
        :return: Error as defined by swRunMacroError_e; True if macro runs, False if not
        """
        return self.__comm_object.RunMacro2(FilePathName, ModuleName, ProcedureName, Options)

    def SetCurrentWorkingDirectory(self, CurrentWorkingDirectorty: str):
        """
        Sets the current working directory to be used by SOLIDWORKS.
        :param CurrentWorkingDirectorty: Directory to set as the current working directory
        :return: True if specified direction is set as the current working directory, false if not
        """
        return self.__comm_object.SetCurrentWorkingDirectory(CurrentWorkingDirectorty)
