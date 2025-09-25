"""
Wrapper for IFeature in Solidworks API. For more information: https://help.solidworks.com/2025/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html

Allows access to the feature type, name, parameter data, and the next feature in the FeatureManager design tree.
"""


class IFeature:
    def __init__(self, comm_object):
        """
        Creates an instance of the IFeature wrapper from the Solidworks API
        :param comm_object: COM object representing IFeatureE instance from Solidworks API\n
        """
        self.__comm_object = comm_object
        self.Name = self.__comm_object.Name

    def Select2(self, Append: bool, Mark: int):
        """
        Selects and marks this feature.

        If an object is already selected with a mark of x and you attempt to select the same object again using this
        method with Append = true and Mark = y, then that object remains selected with a mark with x.
        Reselecting a previously selected object does not assign a new mark value.
        :param Append: True appends the feature to the current selection list, false replaces the current selection list
        :param Mark: Value you want to use as a mark; this number is used by functions that require ordered selection
        :return: True if the feature was selected, false if not
        """
        return self.__comm_object.Select2(Append, Mark)
