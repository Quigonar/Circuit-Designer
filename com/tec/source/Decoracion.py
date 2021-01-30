from PySide2.QtGui import QFont

font3 = QFont()
font3.setFamily(u"OCR A Extended")
def getFontLabel():
    font3.setPointSize(12)
    return font3
def getnormalfont():
    font3.setPointSize(20)
    return font3