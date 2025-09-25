from enum import IntEnum

class swRunMacroError_e(IntEnum):
    """SOLIDWORKS VBA macro run errors (2025)."""

    swRunMacroError_InvalidArg = 1
    swRunMacroError_MacrosAreDisabled = 2
    swRunMacroError_NotInDesignMode = 3
    swRunMacroError_OnlyCodeModules = 4
    swRunMacroError_OutOfMemory = 5
    swRunMacroError_InvalidProcname = 6
    swRunMacroError_InvalidPropertyType = 7
    swRunMacroError_BadParmCount = 9
    swRunMacroError_BadVarType = 10
    swRunMacroError_Overflow = 13
    swRunMacroError_ParmNotOptional = 15
    swRunMacroError_Busy = 17
    swRunMacroError_ConnectionTerminated = 18
    swRunMacroError_CallRejected = 19
    swRunMacroError_CallFailed = 20
    swRunMacroError_Invalidindex = 22
    swRunMacroError_NoPermission = 23
    swRunMacroError_CantSave = 27
    swRunMacroError_DiskError = 26

    def what(self):
        """Returns a human-readable description of this macro run error."""
        return {
            1: "Invalid argument to macro call",
            2: "VBA macros are disabled",
            3: "Not in design mode",
            4: "Procedure not in code module",
            5: "Out of memory",
            6: "Invalid procedure name",
            7: "Invalid property type",
            9: "Bad parameter count",
            10: "Bad variable type",
            13: "Overflow error",
            15: "Parameter not optional",
            17: "Macro is busy",
            18: "Connection terminated",
            19: "Call rejected",
            20: "Call failed",
            22: "Invalid index specified",
            23: "No permission to run macro",
            27: "Cannot save macro or document",
            26: "Disk error encountered",
        }[self.value]