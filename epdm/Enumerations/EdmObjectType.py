from enum import IntEnum


class EdmObjectType(IntEnum):
    """Type of objects returned by IEdmObject5.ObjectType, IEdmFile5.ObjectType and IEdmFolder5.ObjectType"""
    EdmObject_Attribute = 10
    EdmObject_BOM = 15
    EdmObject_Card = 5
    EdmObject_CardControl = 6
    EdmObject_Category = 14
    EdmObject_Dictionary = 12
    EdmObject_File = 1
    EdmObject_Folder = 2
    EdmObject_Invalid = 0
    EdmObject_Item = 16
    EdmObject_ItemFolder = 17
    EdmObject_ItemRootFolder = 18
    EdmObject_Label = 11
    EdmObject_State = 3
    EdmObject_Transition = 4
    EdmObject_User = 7
    EdmObject_UserGroup = 8
    EdmObject_Variable = 9
    EdmObject_Workflow = 13

    def what(self):
        return {
            10: "The object is an attribute, used in variables, and it supports the IEdmAttribute5 interface",
            15: "The object is a Bill of Materials; see IEdmBom",
            5: "The object is a file/folder data card, and it supports the IEdmCard5 interface",
            6: "The object is a control in a file/folder data card, and it supports the IEdmCardControl5 interface",
            14: "The object is a category; see IEdmCategory6",
            12: "The object is a dictionary, and it supports the IEdmDictionary5 interface",
            1: "The object is a file, and it supports the IEdmFile5 interface",
            2: "The object is a folder, and it supports the IEdmFolder5 interface",
            0: "This is not an object type; it is an error code",
            16: "The object is an item; see IEdmItem",
            17: "The object is a parent folder of an item; see IEdmFolder6",
            18: "The object is the invisible root folder of all item folders; see IEdmFolder6",
            11: "The object is a label, and it supports the IEdmLabel5 interface",
            3: "The object is a workflow state, and it supports the IEdmState5 interface",
            4: "The object is a transition (i.e., a workflow state change), and it supports the IEdmTransition5 interface",
            7: "The object is a user, and it supports the IEdmUser5 interface",
            8: "The object is a user group, and it supports the IEdmUserGroup5 interface",
            9: "The object is a variable (for file/folder data cards), and it supports the IEdmVariable5 interface",
            13: "The object is a workflow; see IEdmWorkflow5 and IEdmWorkflow6"
        }[self.value]
