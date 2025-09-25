from enum import IntEnum


class EdmUnlockFlag(IntEnum):
    """Types of Unlock flags for the IEdmFile5.UnlockFile method"""
    EdmUnlock_FailOnRegenerationNeed = 16
    EdmUnlock_ForceUnlock = 256
    EdmUnlock_IgnoreCorruptFile = 4
    EdmUnlock_IgnoreReferences = 128
    EdmUnlock_IgnoreRefsNotLockedByCaller = 32
    EdmUnlock_IgnoreRefsOutsideVault = 8
    EdmUnlock_KeepLocked = 1
    EdmUnlock_OverwriteLatestVersion = 64
    EdmUnlock_RemoveLocalCopy = 2
    EdmUnlock_Simple = 0

    def what(self):
        return {
            16 : "Fail if the file needs to be regenerated in the CAD program ",
            256 : "Unlock the file even if it is not modified",
            4 : "Ignore files with file formats unrecognized by SOLIDWORKS PDM Professional; without this flag, SOLIDWORKS PDM Professional returns E_EDM_INVALID_FILE if it encounters a corrupt file or a file containing a newer format than SOLIDWORKS PDM Professional can handle",
            128: "Silently unlock parent files without their references",
            32 : "Ignore references not locked by caller",
            8 : "Ignore references to files outside the vault",
            1 : "Keep the file checked out after creating the new version in the archive",
            64 : "Do not create a new version; overwrite the last version of the file with new changes",
            2 : "Remove the local copy of the file from the hard disk after the file has been checked in",
            0 : "Check in the file using default behavior"
        }[self.value]
