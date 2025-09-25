"""
Wrapper for IModelDocExtension in Solidworks API. For more information: https://help.solidworks.com/2021/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension.html

Allows access to the model.
"""


class IModelDocExtension:
    def __init__(self, comm_object, Document):
        """
        Creates an instance of the IModelDocExtension wrapper from the Solidworks API
        :param comm_object: COM object representing IModelDocExtension instance from Solidworks API\n
        """
        self.__comm_object = comm_object
        self.Document = Document

    def SelectByID2(self, Name: str, Type: str, X: float, Y: float, Z: float,
                    Append: bool, Mark: int, Callout, SelectOption: int):
        """
        Selects the specified entity.
        :param Name: Name of object to select or an empty string
        :param Type: Type of object (uppercase) as defined in swSelectType_e or an empty string
        :param X: X selection location or 0
        :param Y: Y selection location or 0
        :param Z: Z selection location or 0
        :param Append: check documentation
        :param Mark: Value that you want to use as a mark; this value is used by other functions that require ordered selection
        :param Callout: Pointer to the associated callout
        :param SelectOption: Selection option as defined in swSelectOption_e
        :return: True if item was successfully selected, false if not
        """
        return self.__comm_object.SelectByID2(Name, Type, X, Y, Z, Append, Mark, Callout, SelectOption)

    def SaveAs3(self, Name: str, Version: int, Options: int, ExportData, AdvancedSystemOptions, Errors, Warnings):
        """
        Saves the active document to the specified name with advanced options.\n

        To specify the AdvancedSaveAsOptions parameter of this method, call IModelDocExtension::GetAdvancedSaveAsOptions
        to create an IAdvancedSaveAsOptions object.\n

        This method:\n
        - Overwrites existing files unless they are read only.\n

        To save as an IGES, STL, or STEP file, the document to convert must be the active document. Before calling this method:\n

        - Call ISldWorks::ActivateDoc3 to make the document to convert the active document.\n
        - Call ISldWorks::ActiveDoc to get the active document.\n

        If the file is saved successfully, then the returned value is true and Errors is 0. If the save is not successful,
        then the returned value is false and Errors contains a bitwise OR of the error codes that were generated in
        saving the document. Check the masks against the Errors enumeration. If you do not want SOLIDWORKS to return
        error information, set Errors to Nothing or null.
        :param Name: Full pathname of the document to save; the file extension indicates any conversion that should be performed
        :param Version: Format in which to save this document as defined in swSaveAsVersion_e
        :param Options: Option indicating how to save the document as defined in swSaveAsOptions_e
        :param ExportData: IExportPdfData object for exporting drawing sheets to PDF
        :param AdvancedSystemOptions: IAdvancedSaveAsOptions
        :param Errors: Errors that caused the save to fail as defined in swFileSaveError_e
        :param Warnings: Warnings or extra information generated during the save operation as defined in swFileSaveWarning_e
        :return:
        """
        return self.__comm_object.SaveAs3(Name, Version, Options, ExportData, AdvancedSystemOptions, Errors, Warnings)
