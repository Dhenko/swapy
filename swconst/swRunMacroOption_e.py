from enum import IntEnum

class swRunMacroOption_e(IntEnum):
    """SOLIDWORKS RunMacro options (2025)."""

    swRunMacroDefault = 0
    swRunMacroUnloadAfterRun = 1

    def what(self):
        """Human-readable description of the macro run option."""
        return {
            0: "Run macro and leave it loaded",
            1: "Run macro and unload after run",
        }[self.value]