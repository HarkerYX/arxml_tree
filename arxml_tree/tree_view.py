import re
import xml.etree.ElementTree as ET
tree = ET.parse('newFile.arxml')
root = tree.getroot()
print(root.tag)
