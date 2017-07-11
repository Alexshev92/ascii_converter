import Tkinter as tk
import tkMessageBox
import tkFileDialog
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os.path

class Window(tk.Tk): 
    def __init__(self, master):
        tk.Tk.__init__(self)
        self.title('ASCII Converter')
        self.geometry('400x200+300+200')
        self.resizable(False, False) 

        # Show Button
        self.show_button=tk.Button(self, text='View', width=8, state=tk.DISABLED, command=self.show)
        self.show_button.place(x=320, y=100)

        # Save Button
        self.save_button=tk.Button(self, text='Save', width=8, state=tk.DISABLED, command=self.save)
        self.save_button.place(x=320, y=140) 

        menu = tk.Menu(self)
        self.config(menu=menu)
        # File
        menu_file = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='File', menu=menu_file)
        menu_file.add_command(label='Open...', command=self.open_file)

        self.var=tk.IntVar()
        self.var.set(1)
        submenu = tk.Menu(menu_file, tearoff=0)
        submenu.add_radiobutton(label="png", variable=self.var, value=1)
        submenu.add_radiobutton(label="gif", variable = self.var, value=2)
        submenu.add_radiobutton(label="jpg", variable = self.var, value=3)
        submenu.add_radiobutton(label="bmp", variable = self.var, value=4)
        menu_file.add_cascade(label='Output File Format', menu=submenu, underline=0)
        menu_file.add_command(label='Exit', command=self.quit_program)

        # Help
        menu_help = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label='Help', menu=menu_help)
        menu_help.add_command(label='About Program')

        # Canvas
        self.canvas = tk.Canvas(self, width=149, height=149, bg='grey')
        self.canvas.place(x=125, y=15)
        
        self.path_to_file = None

    def convert(self):
        image = Image.open(self.path_to_file)
        try:
            fnt = ImageFont.truetype("cour.ttf", 12)
        except IOError:
            fnt = ImageFont.load_default()
        width = image.size[0] 
        height = image.size[1] 
        bw_image = image.convert("L")
        self.image2 = Image.new("1", (width, height))
        draw = ImageDraw.Draw(self.image2)
        pix_sum = 0
        for y in range(height/8):
            for x in range(width/6):
                temp = bw_image.crop((6*x, 8*y, 6*x+5, 8*y+7))
                for i in range(5):
                    for j in range(7):
                        pix = temp.load()
                        pix_sum = pix_sum + pix[i, j]
                pix_sum = pix_sum // 35
                if (pix_sum > 50 and pix_sum <= 60):
                    draw.text((6*x,8*y), ".", font=fnt, fill='white')
                elif (pix_sum > 60 and pix_sum <= 85):
                    draw.text((6*x,8*y), ",", font=fnt, fill='white')
                elif (pix_sum > 85 and pix_sum <= 100):
                    draw.text((6*x,8*y), ":", font=fnt, fill='white')
                elif (pix_sum > 100 and pix_sum <= 120):
                    draw.text((6*x,8*y), ";", font=fnt, fill='white')
                elif (pix_sum > 120 and pix_sum <= 140):
                    draw.text((6*x,8*y), "o", font=fnt, fill='white')            
                elif (pix_sum > 140 and pix_sum <= 180):
                    draw.text((6*x,8*y), "0", font=fnt, fill='white')
                elif (pix_sum > 180 and pix_sum <= 220):
                    draw.text((6*x,8*y), "8", font=fnt, fill='white')          
                elif pix_sum > 220:
                    draw.text((6*x,8*y), "@", font=fnt, fill='white')
                pix_sum = 0

    def open_file(self):
        self.path_to_file = tkFileDialog.askopenfilename()
        if (self.path_to_file != ''):
            try:
                image = Image.open(self.path_to_file)
                width = image.size[0] 
                height = image.size[1]
                resize_ratio = float(max(width, height)) / float(min(width, height))
                if width > height:
                    width = 150
                    height = int(width / resize_ratio)
                elif width < height:
                    height = 150
                    width = int(height / resize_ratio)
                elif width == height:
                    width = 150
                    height = 150
                image = image.resize((width, height), Image.ANTIALIAS)
                self.photo = ImageTk.PhotoImage(image)
                self.canvas.create_image(75, 75, anchor='center', image=self.photo)
                self.save_button['state'] = 'normal'
                self.show_button['state'] = 'normal'
            except IOError:
                tkMessageBox.showerror("Error", "Could not open file " + self.path_to_file)

    def quit_program(self):
        self.destroy()

    def save(self):
        self.convert()
        temp = os.path.split(self.path_to_file)
        filename = temp[1].split('.')
        file_ext = None
        if self.var.get() == 1:
            file_ext = '.png'
        elif self.var.get() == 2:
            file_ext = '.gif'
        elif self.var.get() == 3:
            file_ext = '.jpg'
        elif self.var.get() == 4:
            file_ext = '.bmp'
        final_filename = temp[0] + '/' + filename[0] + '_ascii' + file_ext
	print final_filename
        self.image2.save(final_filename)

    def show(self):
        self.convert()
        self.image2.show()
        
if __name__ == '__main__':
    root = Window(tk.Tk)
    root.mainloop()

