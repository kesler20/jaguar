from tkinter import Tk, Label, Button, TOP, LEFT, RIGHT
from PIL import ImageTk, Image
from PIL.ImageTk import PhotoImage
from workflow_automation import initialize_workflow
from main_logging import logger

class Gui(object):
    
    def __init__(self, title='GUI', root_height=900, root_width=700):
        self.root = Tk()
        self.root.title = title
        self.root.geometry(f'{root_height}x{root_width}')
        self.crossed = self.create_image(30,30,r'assets\crossed.jpg')
        self.n_routines = 3
        self.selected_routines = [False for _ in range(self.n_routines)]

    def create_image(self,width, height, filename):
        image = Image.open(filename)
        resize_image = image.resize((width, height))
        img = PhotoImage(resize_image)
        return img

    # the only images within the guy are the boxes that are either ticked or not
    def add_image(self, task, image_to_add: PhotoImage, row, column, grid=True, padx=0, pady=0, side=TOP):
        if grid == True:
            my_img = Label(self.root, image=image_to_add)
            my_img.grid(row=row, column=column)
        else:
            my_img = Label(self.root, image=image_to_add)
            my_img.pack(side=side, padx=padx, pady=pady)
        if task == 'task0':
            self.ticked_box0 = my_img
        elif task == 'task1':
            self.ticked_box1 = my_img
        else:
            pass
    
    def select_task0(self):
        self.ticked_box0.config(image=self.crossed)
        self.selected_routines.remove(self.selected_routines[0])
        self.selected_routines.insert(0, True)
    
    def select_task1(self):
        self.ticked_box1.config(image=self.crossed)
        self.selected_routines.remove(self.selected_routines[1])
        self.selected_routines.insert(1, True)
    
    def add_text(self, text, font_style, font_size, row, column, grid=True, padx=0, pady=0, side=TOP):
        if grid == True:
            Label(self.root, text=text, font=(font_style, font_size)).grid(row=row, column=column)
        else:
            Label(self.root, text=text, font=(font_style, font_size)).pack(side=side, padx=padx, pady=pady)
    
    def add_btn(self, text, func,  row, column, grid=True, padx=0, pady=0, side=TOP):
        if grid == True:
            Button(self.root, text=text, command=func).grid(row=row, column=column)
        else:
            Button(self.root, text=text, command=func).pack(side=side, padx=padx, pady=pady) 

    def start(self):
        self.root.mainloop()

launch = []
def select_tasks():
    launch.append('tasks.docx')

def select_data_structures_docx():
    launch.append('data structures & Oh.docx')

def select_refactoring_notes():
    launch.append('refactoring notes.docx')

def select_clean_code_docx():
    launch.append('clean code.docx')

def select_maths_for_cs():
    launch.append('mathematics for cs.docx')

def select_why_stopped():
    launch.append('why stopped log.docx')

def select_routine_modified():
    launch.append('routine modified.xlsx')

def select_web_developement():
    launch.append('web development notes.docx')

gui = Gui()

# gym routine section
tick_box = gui.create_image(30,30,r'assets\tick.jpg')
gui.add_text('                                                          ','Helvetica',17,0,0)
gui.add_text('Gym Routine','Helvetica',17,0,1)
gui.add_image('task0', tick_box,0,2)
gui.add_btn('select gym routine', gui.select_task0,1,1)

# Diet routine section
gui.add_text('                                                          ','Helvetica',17,2,0)
gui.add_text('                                                          ','Helvetica',17,3,0)
gui.add_text('Diet Routine','Helvetica',17,3,1)
gui.add_image('task1', tick_box,3,2)
gui.add_btn('select diet routine', gui.select_task1,4,1)

# Workflow automation section
gui.add_text('                                                          ','Helvetica',17,5,0)
gui.add_text('                                                          ','Helvetica',17,6,0)
gui.add_text('Workflow Automation','Helvetica',17,6,1)
gui.add_btn('tasks.docx', select_tasks,7,1)

gui.add_btn('data structures & Oh.docx', select_data_structures_docx,8,1)

gui.add_btn('refactoring notes.docx', select_refactoring_notes,9,1)

gui.add_btn('clean code.docx', select_clean_code_docx,10,1)

gui.add_btn('mathematics for cs.docx', select_maths_for_cs,11,1)

gui.add_btn('why stopped log.docx', select_why_stopped,12,1)

gui.add_btn('routine modified.xlsx', select_routine_modified,13,1)

gui.add_btn('web development notes.docx', select_web_developement,14,1)

gui.start()

if gui.selected_routines[0]:
    logger.info('LAUNCH GYM ROUTINE')
    try:
        gym_routine()
    except:
        pass
elif gui.selected_routines[1]:
    logger.info('LAUNCH diet ROUTINE')
    diet_routine()
elif gui.selected_routines[2]:
    logger.info('launch workflow routine')
else:
    pass

initialize_workflow(launch)