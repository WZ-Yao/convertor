import PySimpleGUI as pg
import covertion

label1=pg.Text("Enter feet")
input1=pg.Input(key="feet")

label2=pg.Text("Enter inches")
input2=pg.Input(key="inches")

convert_button=pg.Button("Convert")
output_label=pg.Text(key="output")

window=pg.Window("Convertor",layout=[[label1,input1],
                                     [label2,input2],
                                     [convert_button,output_label]])
while True:
    event,values=window.read()
    match event:
        case "Convert":
            feet=float(values["feet"])
            inches=float(values["inches"])
            total=covertion.converting(feet,inches)
            window["output"].update(value=total)
        case pg.WIN_CLOSED:
            break
# window["output"].update(value="Numbers")

window.close()