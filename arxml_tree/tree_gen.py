import os, sys
#instruction: $ python setup.py install
from autosarfactory import autosarfactory as af
from autosarfactory import autosar_ui as ui
#Read the arxml file

files = ['sample1.arxml', 'ArcCore_Types.arxml']
root, status = af.read(files)
#ui.show_in_ui(root)
mod_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

#Creating new file

rootPack = af.new_file('newFile.arxml', defaultArPackage = 'RootPack', overWrite = True)
newPack = rootPack.new_ARPackage('NewPack')
signalsPack = newPack.new_ARPackage('signals')
systemsignalsPack = newPack.new_ARPackage('systemsignals')
syssig1 = systemsignalsPack.new_SystemSignal('syssig1')
sig1 = signalsPack.new_ISignal('sig1')
# #new application component

newcomp = newPack.new_ApplicationSwComponentType('newcomponent')
newcomp.new_PPortPrototype('outPort')

# #new senderRecever interface

# srIf = newPack.new_SenderReceiverInterface('srif1')
# srIf.new_DataElement('de1')

#save changes

af.save(['newFile.arxml'])
#af.saveAs('temp.arxml')

