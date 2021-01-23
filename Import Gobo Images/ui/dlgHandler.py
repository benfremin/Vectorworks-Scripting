import copy
import vs
import ui.dlg

class DialogData:
    gSize = 24 
    gScale = 1.05
    
dialog = 0
dialogData = None
    
def DialogHandler(item, data):
    if item == 12255: # Setup event
        vs.SetItemText( dialog, ui.dlg.ksize, dialogData.gSize )
        vs.SetItemText( dialog, ui.dlg.kscale1, dialogData.gScale )
        pass
        
    elif item == ui.dlg.ksize:
        dialogData.gSize = float(vs.GetItemText( dialog, ui.dlg.ksize, dialogData.gSize ))
        pass

    elif item == ui.dlg.kscale1:
        dialogData.gScale = float(vs.GetItemText( dialog, ui.dlg.kscale1, dialogData.gScale ))
        pass
    
    return item    

def RunDialog(dlgData):
    # make a copy of the dialog data
    # so the dialog will edit the copy
    global dialogData;
    #dialogData = DialogData()
    #dialogData.operationValue = dlgData.operationValue
    #dialogData.operationValue1 = dlgData.operationValue1
    dialogData = copy.copy( dlgData )
    
   
    global dialog
    dialog = ui.dlg.CreateDialog()
    result = False
    if vs.RunLayoutDialog( dialog, DialogHandler ) == ui.dlg.kOK:
        result = True
        
    return result
    