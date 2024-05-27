


from tkinter import *
import _mysql_connector
conexion = _mysql_connector.connect( user="root", password="", host="localhost",db="formulario")
 

def send_data():
  Nombre_info = Nombre.get()
  Edad_info = Edad.get()
  Apellido_info = Apellido.get()
  Correo_info = Correo.get()
  Celular_info = Celular.get()
  print(Nombre_info,"\t", Apellido_info,"\t", Correo_info,"\t")
 

  file = open("user.txt", "a")
  file.write(Nombre_info)
  file.write("\t")
  file.write(Edad_info)
  file.write("\t")
  file.write(Apellido_info)
  file.write("\t")
  file.write(Correo_info)
  file.write("\t")
  file.write(Celular_info)
  file.write("\t")
  file.close()
  print(" Usuario Registrado. Nombre: {} | Apellido: {} | Correo: {} | Edad: {}  ".format(Nombre_info,Edad_info, Apellido_info, Correo_info, Celular_info))
 

  Nombre_entry.delete(0, END)
  Apellido_entry.delete(0, END)
  Correo_entry.delete(0, END)



mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("Registration Form - Python + Tkinter")
mywindow.resizable(False,False)
mywindow.config(background = "#213141")
main_title = Label(text = "Bienvenido Al Formulario Del Grupo Ingenierios Tecnicos", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()


Nombre_label = Label(text = "Nombre", bg = "#FFEEDD")
Nombre_label.place(x = 22, y = 70)
Edad_label = Label(text = "Edad", bg = "#FFEEDD")
Edad_label.place(x = 22, y = 130)
Apellido_label = Label(text = "Apellido", bg = "#FFEEDD")
Apellido_label.place(x = 22, y = 190)
Correo_label = Label(text = "Correo", bg = "#FFEEDD")
Correo_label.place(x = 22, y = 250)
Celular_label = Label(text = "Celular", bg = "#FFEEDD")
Celular_label.place(x = 22, y = 310)
label = Label(text=" Autores: Jose Jaimes, Fausto Calderon")
label.place(x = 22, y = 370)

Nombre = StringVar()
Edad = StringVar()
Apellido = StringVar()
Correo = StringVar()
Celular = StringVar()


 
Nombre_entry = Entry(textvariable = Nombre, width = "40")
Edad_entry = Entry(textvariable = Nombre, width = "40")
Apellido_entry = Entry(textvariable = Apellido, width = "40")
Correo_entry = Entry(textvariable = Correo, width = "40")
Celular_entry = Entry(textvariable = Celular, width = "40")
 
Nombre_entry.place(x = 22, y = 100)
Edad_entry.place(x = 22, y = 160)
Apellido_entry.place(x = 22, y = 220)
Correo_entry.place(x = 22, y = 280)
Celular_entry.place(x = 22, y = 340)
 

submit_btn = Button(mywindow,text = "Enviar", width = "30", height = "2", command = send_data, bg = "#00CD63")
submit_btn.place(x = 22, y = 430)

submit_btn = Button(mywindow,text = "Salir", width = "30", height = "2", command = exit, bg = "#00CD63")
submit_btn.place(x =370, y = 430)

mywindow.mainloop()

