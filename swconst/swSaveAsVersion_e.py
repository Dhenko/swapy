from enum import IntEnum


class swSaveAsOptions_e(IntEnum):
    """Save As options."""

    swSaveAsCurrentVersion = 0
    swSaveAsFormatProE = 2
    swSaveAsStandardDrawing = 3
    swSaveAsDetachedDrawing = 4
    # swSaveAsSW98plus is obsolete and no longer supported

    def what(self):
        return {
            0: "This is the typical save behavior (current version).",
            2: "Save in Pro/ENGINEER format.",
            3: "Save as a standard drawing.",
            4: "Save as a detached drawing.",
        }[self.value]
