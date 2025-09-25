from enum import IntEnum

class swDocumentTypes_e(IntEnum):
    """SOLIDWORKS document types enumeration (2025), excluding obsoletes."""

    swDocNONE = 0
    swDocPART = 1
    swDocASSEMBLY = 2
    swDocDRAWING = 3
    swDocSDM = 4
    swDocLAYOUT = 5
    swDocIMPORTED_PART = 6
    swDocIMPORTED_ASSEMBLY = 7

    def what(self):
        """Returns a human-readable description of this document type."""
        return {
            0: "No document type specified",
            1: "Part document (.sldprt)",
            2: "Assembly document (.sldasm)",
            3: "Drawing document (.slddrw)",
            4: "SDM document (Smart Dimension ?)",
            5: "Layout document",
            6: "Imported part",
            7: "Imported assembly",
        }[self.value]