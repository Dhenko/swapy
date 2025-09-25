"""
Declares helpers (functions or variables) that are useful for the communication with Solidworks API
"""

import pythoncom
import win32com.client
import os

# Create a wrapper for the Nothing variable in VB
VBNothing = win32com.client.VARIANT(pythoncom.VT_DISPATCH, None)

# Prepare placeholders for errors and warnings
errors = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)
warnings = win32com.client.VARIANT(pythoncom.VT_BYREF | pythoncom.VT_I4, 0)

