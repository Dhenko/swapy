from enum import IntEnum

class swDwgPaperSizes_e(IntEnum):
    """Drawing paper sizes, SolidWorks swDwgPaperSizes_e (2025)."""

    swDwgPaperAsize = 0
    swDwgPaperAsizeVertical = 1
    swDwgPaperBsize = 2
    swDwgPaperCsize = 3
    swDwgPaperDsize = 4
    swDwgPaperEsize = 5
    swDwgPaperA4size = 6
    swDwgPaperA4sizeVertical = 7
    swDwgPaperA3size = 8
    swDwgPaperA2size = 9
    swDwgPaperA1size = 10
    swDwgPaperA0size = 11
    swDwgPapersUserDefined = 12

    def what(self):
        """Returns a human-readable description of this paper size."""
        return {
            0: "ANSI A (landscape)",
            1: "ANSI A (portrait)",
            2: "ANSI B size",
            3: "ANSI C size",
            4: "ANSI D size",
            5: "ANSI E size",
            6: "A4 (landscape)",
            7: "A4 (portrait)",
            8: "A3 size",
            9: "A2 size",
            10: "A1 size",
            11: "A0 size",
            12: "User-defined paper size",
        }[self.value]