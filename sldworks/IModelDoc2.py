"""
Wrapper for IModelDoc2 in Solidworks API. For more information: https://help.solidworks.com/2025/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html?id=9eb963a1f38745d0946c490b68d9df2e&_gl=1*1m1fnqu*_up*MQ..*_ga*NzQyMjIyNjEuMTc0OTYyOTg5MA..*_ga_XQJPQWHZHH*czE3NDk2MzkyMzAkbzIkZzEkdDE3NDk2MzkyMzckajUzJGwwJGgw#Pg0

Allows access to SOLIDWORKS documents: parts, assemblies, and drawings.
"""

from swapy.sldworks import ISketchManager, IModelDocExtension, IEquationMgr


class IModelDoc2:
    def __init__(self, comm_object):
        """
        :param comm_object: COM object representing IModelDoc2 instance from Solidworks API\n
        There are three main SOLIDWORKS document types:\n
        - parts
        - assemblies
        - drawings
        Each document type has its own object (IPartDoc, IAssemblyDoc, and IDrawingDoc) with its own set of related
        functions. For example, the IAssemblyDoc::AddComponent4 method exists on the IAssemblyDoc object because
        adding components is specific to assembly documents.\n
        The SOLIDWORKS API also has functions that are common to all document types. For example, printing, saving,
        or determining the file name associated with a document would be common operations. To expose common
        document-level functions, the SOLIDWORKS API uses the IModelDoc2 object.\n
        """
        self.__comm_object = comm_object
        self.ActiveView = self.__comm_object.ActiveView
        self.ConfiguratorManager = self.__comm_object.ConfigurationManager
        self.Extension = IModelDocExtension.IModelDocExtension(self.__comm_object.Extension, self)
        self.FeatureManager = self.__comm_object.FeatureManager
        # self.IActiveView = self.__comm_object.IActiveView
        # self.ILightSourcePropertyValues = self.__comm_object.ILightSourcePropertyValues
        # self.IMaterialPropertyValues = self.__comm_object.IMaterialPropertyValues
        # self.IPageSetup = self.__comm_object.IPageSetup
        # self.ISelectionManager = self.__comm_object.ISelectionManager  # To be replaced with ISelectionManager object
        self.SketchManager = ISketchManager.ISketchManager(self.__comm_object.SketchManager, self)

    def ClearSelection2(self, All: bool):
        """
        Clears the selection list.
        :param All: True clears the entire existing selection list, false clears only the items in the active selection list
        :return:
        """
        return self.__comm_object.ClearSelection2(All)

    def CreateArcByCenter(self, XC, YC, ZC, X1, Y1, Z1, X2, Y2, Z2, Direction):
        """

        :param XC: X coordinate of the circle center point in meters
        :param YC: Y coordinate of the circle center point in meters
        :param ZC: Z coordinate of the circle center point in meters
        :param X1: X coordinate of the start point of the arc in meters
        :param Y1: Y coordinate of the start point of the arc in meters
        :param Z1: Z coordinate of the start point of the arc in meters
        :param X2: X coordinate of the end point of the arc in meters
        :param Y2: Y coordinate of the end point of the arc in meters
        :param Z2: Z coordinate of the end point of the arc in meters
        :param Direction: +1 : Go from the start point to the end point in a counter-clockwise direction //
        -1 : Go from the start point to the end point in a clockwise direction
        :return:
        """
        return self.__comm_object.CreateArcByCenter(XC, YC, ZC, X1, Y1, Z1, X2, Y2, Z2, Direction)

    def EditRebuild3(self):
        """
        Rebuilds only those features that need to be rebuilt in the active configuration in the model.
        :return:
        """
        return self.__comm_object.EditRebuild3

    def EditSketch(self):
        """
        Allows the currently selected sketch to be edited.\n

        This method corresponds to SOLIDWORKS menu > Edit > Sketch. If the selection is a feature,
        its underlying sketch is placed in edit mode.\n

        After a sketch is in edit mode, you can add or delete geometry from the sketch and perform other standard
        sketch operations.
        :return:
        """
        return self.__comm_object.EditSketch

    def GetEquationMgr(self):
        """
        Gets the equation manager.
        :return:
        """
        return IEquationMgr.IEquationMgr(self.__comm_object.GetEquationMgr)

    def Save3(self, Options, Errors, Warnings):
        """
        Saves the current document.
        :param Options: Mode in which to save the document as defined in swSaveAsOptions_e
        :param Errors: Errors that caused the save operation to fail as defined in swFileSaveError_e
        :param Warnings: Warnings or extra information generated during the save operation as defined in swFileSaveWarning_e
        :return:
        """
        return self.__comm_object.Save3(Options, Errors, Warnings)

    def ShowNamedView2(self, VName: str, ViewId: int = -1):
        """
        Shows the specified view.
        :param VName: Name of the view to display or an empty string to use ViewId instead
        :param ViewId: ID of the view to display as defined by swStandardViews_e or -1 to use the VName argument instead;
        if you specify both VName and ViewId, then ViewId takes precedence if the two arguments do not resolve to the same view
        :return:
        """
        return self.__comm_object.ShowNamedView2(VName, ViewId)

    def ViewZoomtofit2(self):
        """
        Zooms the currently active view to fit the screen.
        :return:
        """
        return self.__comm_object.ViewZoomtofit2()
