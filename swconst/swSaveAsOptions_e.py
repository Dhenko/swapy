from enum import IntEnum


class swSaveAsOptions_e(IntEnum):
    """Save As options (extended)."""

    swSaveAsOptions_Silent = 1
    swSaveAsOptions_Copy = 2
    swSaveAsOptions_SaveReferenced = 4
    swSaveAsOptions_AvoidRebuildOnSave = 8
    swSaveAsOptions_UpdateInactiveViews = 16
    swSaveAsOptions_OverrideSaveEmodel = 32
    swSaveAsOptions_IgnoreBiography = 256
    swSaveAsOptions_CopyAndOpen = 512
    swSaveAsOptions_IncludeVirtualSubAsmComps = 1024
    swSaveAsOptions_ExportTo2DPdfFromInspection = 2048
    # swSaveAsOptions_DetachedDrawing is obsolete
    # swSaveAsOptions_SaveEmodelData is obsolete

    def what(self):
        return {
            1: "Silent save (no dialogs).",
            2: "Save the document as a copy and continue editing.",
            4: "Save all referenced components (sub-assemblies, parts, drawings).",
            8: "Avoid rebuild on save.",
            16: "Update views on inactive sheets in drawings (not valid for IPartDoc::SaveToFile2).",
            32: "Save eDrawings-related data into the file, overriding system option (not valid for IPartDoc::SaveToFile2).",
            256: "Ignore biography (prune revision history to just the current file name).",
            512: "Save the document as a copy and open it.",
            1024: "Include regular components in virtual subassemblies.",
            2048: "Export drawing sheets from Inspection to 2D PDF.",
        }[self.value]
