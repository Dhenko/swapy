from enum import IntEnum


class swFileSaveError_e(IntEnum):
    """File Save error codes."""

    swGenericSaveError = 1
    swReadOnlySaveError = 2
    swFileNameEmpty = 4
    swFileNameContainsAtSign = 8
    swFileLockError = 16
    swFileSaveFormatNotAvailable = 32
    swFileSaveAsDoNotOverwrite = 128
    swFileSaveAsInvalidFileExtension = 256
    swFileSaveAsNoSelection = 512
    swFileSaveAsBadEDrawingsVersion = 1024
    swFileSaveAsNameExceedsMaxPathLength = 2048
    swFileSaveAsNotSupported = 4096
    swFileSaveRequiresSavingReferences = 8192
    swFileSaveAsDetachedDrawingsNotSupported = 16384
    # swFileSaveWithRebuildError is obsolete, see swFileSaveWarning_e

    def what(self):
        return {
            1: "Generic save error.",
            2: "Read-only save error.",
            4: "File name cannot be empty.",
            8: "File name cannot contain the at symbol (@).",
            16: "File lock error.",
            32: "Save As file type is not valid.",
            128: "Do not overwrite an existing file.",
            256: "File name extension does not match the document type.",
            512: "Save the selected bodies in a part document (valid for IPartDoc::SaveToFile2, not valid for IModelDocExtension::SaveAs).",
            1024: "Invalid eDrawings version.",
            2048: "File name cannot exceed 255 characters.",
            4096: (
                "Save As not supported, or operation executed incorrectly; "
                "resulting file might not be complete (check if SOLIDWORKS is visible)."
            ),
            8192: "Saving an assembly with renamed components requires saving the references.",
            16384: "Detached drawing Save As option is not supported.",
        }[self.value]
