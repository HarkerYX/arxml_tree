import re
import xml.etree.ElementTree as ET
tree = ET.parse('sample1.arxml')
root = tree.getroot()
root.tag
'{http://autosar.org/schema/r4.0}AUTOSAR'
#root's all AR-PACKAGE child tag
for child in root:
    print(child)
#The first AR-PACKAGE data
root1 = root[0]
# SHORT-NAME tags in the first AR-PACKAGE
root1.find("./{http://autosar.org/schema/r4.0}SHORT-NAME")
#root1.find("./{http://autosar.org/schema/r4.0}SHORT-NAME").text

#AR-PACKAGES tags in the first AR-PACKAGE
root1.findall("./{http://autosar.org/schema/r4.0}AR-PACKAGES/{http://autosar.org/schema/r4.0}AR-PACKAGE/{http://autosar.org/schema/r4.0}ELEMENTS/{http://autosar.org/schema/r4.0}SYSTEM/*")

#Find FIBEX-ELEMENT-REF-CONDITIONAL contain FRAME,PDU,GROUP,SIGNAL
root1.findall(".//{http://autosar.org/schema/r4.0}FIBEX-ELEMENT-REF-CONDITIONAL")

#The second AR-PACKAGE data
#root2 = root[1]

#Get all frame

# Communication = root2.findall("./{http://autosar.org/schema/r4.0}AR-PACKAGES/{http://autosar.org/schema/r4.0}AR-PACKAGE")
# ELEMENTS = Communication[0].findall(".//{http://autosar.org/schema/r4.0}ELEMENTS/*")
# for child in ELEMENTS:
#     print(child[0].text)
#frames = [child[0].text for child in ELEMENTS]

#Get signal_group

#siganls_group = root_signal_group.findall("./{http://autosar.org/schema/r4.0}ELEMENTS/{http://autosar.org/schema/r4.0}SYSTEM-SIGNAL-GROUP/{http://autosar.org/schema/r4.0}SHORT-NAME")

#get all signal_group signal names

#siganls_group_ref = root_signal_group.findall("./{http://autosar.org/schema/r4.0}ELEMENTS/{http://autosar.org/schema/r4.0}SYSTEM-SIGNAL-GROUP/{http://autosar.org/schema/r4.0}SYSTEM-SIGNAL-REFS")
# all_signal_list=[]
# for signal_each_group in siganls_group_ref: 
#     signal_list =[]
#     for content_signal in signal_each_group:     
#         signal_text = content_signal.text
#         signal=signal_text.split(r"/")[-1] #split get the last one
#         signal_list.append(signal)
#     all_signal_list.append(signal_list)
# print(all_signal_list)
# print(len(all_signal_list))