from enum import IntEnum


class swCloseReopenOption_e(IntEnum):
    """File close and reopen options."""
    swCloseReopenOption_ReadOnly = 1
    swCloseReopenOption_DiscardChanges = 2
    swCloseReopenOption_MatchSheet = 4
    swCloseReopenOption_ExitDetailingMode = 8

    def what(self):
        return {
            1: "include this option to open the drawing document in read-only mode",
            2: "include this option to discard any changes to the document before reopening it; if you exclude this option and there are changes, ISldWorks::CloseAndReopen fails and returns swCloseReopenError_e.swCloseReopenModifiedError",
            4: "include this option to open the same sheet that was active during closing",
            8: " include this option to reopen model drawings as resolved; if excluded by ISldWorks::CloseAndReopen2, keeps a model drawing in detailing mode on reopen"
        }[self.value]
