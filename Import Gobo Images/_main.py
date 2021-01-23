import vs
import ui.dlgHandler
import ui.importGobo

def execute():
    #import pydevd
    #pydevd.settrace(suspend=False)
    
    data = ui.dlgHandler.DialogData()
    data.operationValue = "value"
    data.operationValue1 = 11
    
    if ui.dlgHandler.RunDialog( data ):
        # ok updates the 'data' from the local dialog data
        data = ui.dlgHandler.dialogData

        symCreated = ui.importGobo.ImportSym(data.gSize, data.gScale)
        vs.AlrtDialog( 'Done! Created ', symCreated , ' symbols.')

        #vs.AlrtDialog( "The dialog was confirmed. The value is: ",  )
        
    else:
        # cancel keeps the 'data' unchanged
        # vs.AlrtDialog( "The dialog was CANCELED. The value is: ", data.operationValue )
        return
    
    
    