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


window = tk.Tk()
window.geometry('2000x2000')

list_dir = os.listdir()

"""def cut_img(img, dir): #dir - ex: a fire hydrant
    for i in range(9):
        if array_flag[i] is True:
            cropped = img_np[(i//3)*100:((i+3)//3)*100-1, (i%3)*100:((i+1)%3)*100-1]    
            plt.imsave('filtered ' + dir + str(datetime.now()) + '.png', cropped)
"""

for dir in list_dir:
    if '.' in dir or '_' in dir:
        list_dir.remove(dir)

for dir in list_dir:
    current_path = os.getcwd()
    os.chdir(current_path + '/' + dir)
    for image in os.listdir(): #listdir contem as imagens de cada uma das diretorias (todas do mesmo tipo)
        image_test = open(current_path + '/' + dir + '/' + image)
        image_test = PIL.Image.open(current_path + '/' + dir + '/' + image)
        teste = ImageTk.PhotoImage(image_test)

        img_np= np.array(image_test)

        label1 = tk.Label(image=teste)
        label1.image = teste

        label1.place(x=300, y=0) #sitio onde ta a imagem

        expression_field = Entry(window)

        i = 0

        variable1 = StringVar(window)
        variable1.set(dirs[0]) # default value
        cropped1 = img_np[(i//3)*100:((i+3)//3)*100-1, (i%3)*100:((i+1)%3)*100-1]
        i += 1

        w1 = OptionMenu(window, variable1, *dirs)
        w1.pack()

        variable2 = StringVar(window)
        variable2.set(dirs[0]) # default value
        cropped2 = img_np[(i//3)*100:((i+3)//3)*100-1, (i%3)*100:((i+1)%3)*100-1]
        i += 1

        w2 = OptionMenu(window, variable2, *dirs)
        w2.pack()
        print ("value is:" + variable2.get())

        variable3 = StringVar(window)
        variable3.set(dirs[0]) # default value
        cropped3 = img_np[(i//3)*100:((i+3)//3)*100-1, (i%3)*100:((i+1)%3)*100-1]
        i += 1

        w3 = OptionMenu(window, variable3, *dirs)
        w3.pack()
        print ("value is:" + variable3.get())

        variable4 = StringVar(window)
        variable4.set(dirs[0]) # default value
        cropped4 = img_np[(i//3)*100:((i+3)//3)*100-1, (i%3)*100:((i+1)%3)*100-1]
        i += 1

        w4 = OptionMenu(window, variable4, *dirs)
        w4.pack()
        print ("value is:" + variable4.get())

        variable5 = StringVar(window)
        variable5.set(dirs[0]) # default value
        cropped5 = img_np[(i//3)*100:((i+3)//3)*100-1, (i%3)*100:((i+1)%3)*100-1]
        i += 1

        w5 = OptionMenu(window, variable5, *dirs)
        w5.pack()
        print ("value is:" + variable5.get())

        variable6 = StringVar(window)
        variable6.set(dirs[0]) # default value
        cropped6 = img_np[(i//3)*100:((i+3)//3)*100-1, (i%3)*100:((i+1)%3)*100-1]
        i += 1

        w6 = OptionMenu(window, variable6, *dirs)
        w6.pack()
        print ("value is:" + variable6.get())

        variable7 = StringVar(window)
        variable7.set(dirs[0]) # default value
        cropped7 = img_np[(i//3)*100:((i+3)//3)*100-1, (i%3)*100:((i+1)%3)*100-1]
        i += 1

        w7 = OptionMenu(window, variable7, *dirs)
        w7.pack()
        print ("value is:" + variable7.get())

        variable8 = StringVar(window)
        variable8.set(dirs[0]) # default value
        cropped8 = img_np[(i//3)*100:((i+3)//3)*100-1, (i%3)*100:((i+1)%3)*100-1]
        i += 1

        w8 = OptionMenu(window, variable8, *dirs)
        w8.pack()
        print ("value is:" + variable8.get())

        variable9 = StringVar(window)
        variable9.set(dirs[0]) # default value
        cropped9 = img_np[(i//3)*100:((i+3)//3)*100-1, (i%3)*100:((i+1)%3)*100-1]
        i += 1

        w9 = OptionMenu(window, variable9, *dirs)
        w9.pack()
        print ("value is:" + variable9.get())

        def save_file():
            os.chdir(current_path + '/' + str(variable1.get()))
            plt.imsave('filtered ' + str(variable1.get()) + str(datetime.now()) + '.png', cropped1)
            os.chdir(current_path)
            os.chdir(current_path + '/' + str(variable2.get()))
            plt.imsave('filtered ' + str(variable2.get()) + str(datetime.now()) + '.png', cropped2)
            os.chdir(current_path)
            os.chdir(current_path + '/' + str(variable3.get()))
            plt.imsave('filtered ' + str(variable3.get()) + str(datetime.now()) + '.png', cropped3)
            os.chdir(current_path)
            os.chdir(current_path + '/' + str(variable4.get()))
            plt.imsave('filtered ' + str(variable4.get()) + str(datetime.now()) + '.png', cropped4)
            os.chdir(current_path)
            os.chdir(current_path + '/' + str(variable5.get()))
            plt.imsave('filtered ' + str(variable5.get()) + str(datetime.now()) + '.png', cropped5)
            os.chdir(current_path)
            os.chdir(current_path + '/' + str(variable6.get()))
            plt.imsave('filtered ' + str(variable6.get()) + str(datetime.now()) + '.png', cropped6)
            os.chdir(current_path)
            os.chdir(current_path + '/' + str(variable7.get()))
            plt.imsave('filtered ' + str(variable7.get()) + str(datetime.now()) + '.png', cropped7)
            os.chdir(current_path)
            os.chdir(current_path + '/' + str(variable8.get()))
            plt.imsave('filtered ' + str(variable8.get()) + str(datetime.now()) + '.png', cropped8)
            os.chdir(current_path)
            os.chdir(current_path + '/' + str(variable9.get()))
            plt.imsave('filtered ' + str(variable9.get()) + str(datetime.now()) + '.png', cropped9)


        os.remove(current_path + '/' + dir + '/' + image)

                
        button = Button(window, text="OK", command=save_file)  # , command=ok)
        button.pack()
 
    window.mainloop()

    os.chdir(current_path)