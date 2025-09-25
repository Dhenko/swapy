from enum import IntEnum

class EdmBrowseFlag(IntEnum):
    """EPDM.BrowseForFile options (bitmask), EPDM.Interop.epdm EdmBrowseFlag (2025)."""

    EdmBws_ForOpen = 0
    EdmBws_ForSave = 1
    EdmBws_PermitMultipleSel = 2
    EdmBws_PermitLocalFiles = 4
    EdmBws_PermitVaultFiles = 8
    EdmBws_PermitExternalFiles = 16
    EdmBws_Help = 32

    def what(self):
        """Returns a human-readable description of this browse flag."""
        return {
            0: "Display the Open dialog box",
            1: "Display a Save As dialog box",
            2: "Permit the user to select more than one file",
            4: "Permit user to select files inside vault tree but not checked-in",
            8: "Permit user to select files that are part of the vault",
            16: "Permit user to select files outside the vault folder tree",
            32: "Display Help button in the dialog box",
        }[self.value]