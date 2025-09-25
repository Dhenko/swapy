from enum import IntEnum


class swFileLoadError_e(IntEnum):
    """File load errors (bitmask), SolidWorks swFileLoadError_e (2025)"""

    swGenericError = 1
    swFileNotFoundError = 2
    swInvalidFileTypeError = 1024
    swFutureVersion = 8192
    swFileWithSameTitleAlreadyOpen = 65536
    swLiquidMachineDoc = 131072
    swLowResourcesError = 262144
    swNoDisplayData = 524288
    swFileRequiresRepairError = 2097152
    swFileCriticalDataRepairError = 4194304
    swAddinInteruptError = 1048576
    swApplicationBusy = 8388608
    swConnectedIsOffline = 16777216

    def what(self):
        """Returns a human-readable description of this error."""
        return {
            1: "Another error was encountered.",
            2: "Unable to locate the file; the file is not loaded or referenced component suppressed.",
            1024: "File type argument is not valid.",
            8192: "The document was saved in a future version of SOLIDWORKS.",
            65536: "A document with the same name is already open.",
            131072: "File encrypted by Liquid Machines.",
            262144: "File is open and blocked due to low system resources (memory/GDI handles).",
            524288: "File contains no display data.",
            2097152: "The document has non-critical custom property data corruption.",
            4194304: "The document has critical data corruption.",
            1048576: "The user interrupted the file-open routine to open another file.",
            8388608: "File open is blocked because the application is busy.",
            16777216: "User is offline in SOLIDWORKS Connected environment.",
        }[self.value]
