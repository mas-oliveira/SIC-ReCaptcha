import os
import PIL
from PIL import Image, ImageTk
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from time import sleep
from datetime import datetime

dirs = [
    'None',
    'a fire hydrant',
    'bicycles',
    'boats',
    'bridges',
    'bus',
    'cars',
    'chimneys',
    'crosswalks',
    'motorcycles',
    'mountains or hills',
    'palm trees',
    'parking meters',
    'stairs',
    'taxis',
    'tractors',
    'traffic lights',
    'None'
    ] 

# variables

root = Tk()
root.geometry ('2000x2000')
list_dir = os.listdir ()
current_path = os.getcwd ()
dir = 'palm trees' #change along the directories - chimneys(casas sem escada), tractors(carros e barcos e fire hydrants e parking meters(cenas com relva), montes e colunas), stairs(casas sem escada), palm trees dar arvores (none e carros henrique)
""" VER SE CONSIGO MUDAR AUTO LINHA ACIMA """  
os.chdir (current_path + '/' + dir)

def cut (img_np):
    cropped = []
    for i in range (0, 9):
        cropped.append (img_np[(i//3)*100:((i+3)//3)*100-1, (i%3)*100:((i+1)%3)*100-1])
    return cropped

def save_file (variables, w, cropped, button):
    for i in range (9):
        os.chdir(current_path + '/' + str(variables[i].get()))
        image = PIL.Image.fromarray (np.uint8(cropped[i])).convert('RGB')
        image.save('filtered ' + str(variables[i].get()) + str(datetime.now()).replace (':', '-') + '.png')
        os.chdir(current_path)
        w[i].destroy()
        button.destroy()

def task():
    os.chdir (current_path + '/' + dir) # havent solved the auto dir chenged so had to onclude dir to the path, remove later
    for im in os.listdir ():
        if 'filtered' not in str(im):
            image = im
    #image = os.listdir ()[0] #name of the first image
    image_test = PIL.Image.open (current_path + '/' + dir + '/' + image.replace(':', ':'))
    teste = ImageTk.PhotoImage(image_test)
    img_np= np.array(image_test)

    label1 = tk.Label(image=teste)
    label1.image = teste

    label1.place(x=300, y=0) #sitio onde ta a imagem
    expression_field = Entry(root)
    
    cropped = cut (img_np)

    variables = []
    w = []

    for i in range (9):
        variables.append (StringVar (root))
        variables[i].set (dirs[0])
        w.append (OptionMenu (root, variables[i], *dirs))
        w[i].pack ()


    button = Button (root, text = 'OK', command = lambda : save_file (variables, w, cropped, button))
    button.pack ()

    os.remove(current_path + '/' + dir + '/' + image)

    root.after(30000, task)  # reschedule event in 20s (adjust for you) seconds // recursion


#main

root.after(1000, task) #first recursion
root.mainloop()