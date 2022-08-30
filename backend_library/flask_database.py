from datetime import timedelta
from flask import Flask, redirect, url_for, render_template, request, session, send_from_directory, flash
import os
from os import path as ps
import threading
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
import datetime
import openpyxl as xl
import selenium
from selenium import webdriver as wb
import time 
from tkinter import Tk
from tkinter import filedialog
import pandas as pd

create_engine("mysql+pymysql://user:pw@host/db", pool_pre_ping=True)
ROOT_DIR = os.path.dirname(os.getcwd())
app = Flask(
    __name__, 
    template_folder=ps.join(ROOT_DIR, 'expertsystem-gh-pages', 'templates'),
    static_folder=ps.join(ROOT_DIR, 'expertsystem-gh-pages', 'static')
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'top secret!'
app.secret_key = 'password'
app.permanent_session_lifetime = timedelta(minutes=50)
db = SQLAlchemy(app)

#------------------------------ BACKEND FUNCTIONALITY-----------------------------------------------

def get_specific_file_extensions_in_cwd(file_extension):
    _dir = os.path.curdir
    files = os.listdir(f'{_dir}')
    specific_files = []
    for file in files:
        if file.endswith(f'{file_extension}'):
            specific_files.append(file)
    return specific_files

def create_session_data(filename, x, y, z):
    
    db.create_all()
    session_data = SessionDataModel(
        session_id=increment_id(), 
        user_id=2, 
        filename=filename,
        x_simulation=x, 
        y_simulation=y, 
        z_simulation=z
    )
    db.session.add(session_data)
    db.session.commit()
    return session_data

def update_session_data(index,filename, x, y, z):
    db.create_all()
    datasess = db.session.query(SessionDataModel).all()
    datasess[1].filename = filename
    if x == '':
        pass
    else:
        datasess[1].x_simulation = x
        datasess[1].y_simulation = y
        datasess[1].z_simulation = z
    print(datasess)
    db.session.commit()

def upload_file():

    current_working_directory = os.path.curdir
    root = Tk()
    root.title('Web Crawler GUI')
    root_height = 500
    root_width = 500
    root.geometry(f'{root_height}x{root_width}')
    root.iconbitmap(r'static\img\favicon.ico')
    root.filename = filedialog.asksaveasfilename(initialdir=f'{current_working_directory}', title='upload a file')
    df = pd.read_csv(r'{}'.format(root.filename))
    variables = df.columns 
    x_y_z = []
    for var in variables:
        if var.startswith('Unnamed'):
            pass
        elif var == 0:
            pass
        elif var.startswith('0'):
            pass
        else:
            x_y_z.append(var)
    print(x_y_z)
    create_session_data(r'{}'.format(root.filename),x=x_y_z[0],y=x_y_z[1],z=x_y_z[2])
    root.mainloop()

def reset(reset_all_users=False, reset_all_posts=False):
    if 'username' in session:
        print('          loading reset .....')
        db.create_all()
        all_users = db.session.query(UserAccount).all()
        all_posts = db.session.query(Post).all()
        if reset_all_users:
            for user in all_users:
                users_to_delete = UserAccount.query.filter_by(name=user.participant_id).first()
                db.session.delete(users_to_delete)
                db.session.commit()
        else:
            pass
        if reset_all_posts:
            for post in all_posts:
                posts_to_delete = users_to_delete = Post.query.filter_by(session_id=post.session_id).first()
                db.session.delete(posts_to_delete)
                db.session.commit()
        else:
            pass
        print(all_users)
        session.pop('username', None) 
        session.pop('Node', None) 
        session.pop('date', None) 
    else:
        pass  
    
def increment_id():
    db.create_all()
    users = db.session.query(UserAccount).all()
    return len(users) + 1

def initialize_web_app():
    try:
        x = ps.abspath('msedgedriver.exe')
        driver = wb.Edge(x)
        driver.get('http://127.0.0.1:5500/')
    except selenium.common.exceptions.WebDriverException:
        print(threading.active_count())
        time.sleep(200000)
        
def init_session_(number_of_attributes, attribute_values):
    for i in range(number_of_attributes):
        session[attribute_values[i]] = request.form[attribute_values[i]]     

def modify_workbook_in_session(node, participant_id, date=datetime.datetime.now(),):
    if session.permanent:
        try:
            wb = xl.load_workbook('Expert_System_Session.xlsx', False)
        except PermissionError:
            flash('Close the Expert System file for 5 seconds')
            time.sleep(4)
            wb = xl.load_workbook('Expert_System_Session.xlsx', False)

        date_cell = wb['User Information']['C8'] 
        node_cell = wb['User Information']['C9']
        participant_cell = wb['User Information']['C10'] 
        node_cell.value = node
        participant_cell.value = participant_id
        date_cell.value = date
        
        wb.save('Expert_System_Session.xlsx')
        os.system('start Expert_System_Session.xlsx')

def check_database_column(column_objct):
    db.create_all()
    datasess = db.session.query(column_objct).all()
    print(datasess)

def get_session_by_index(index):
    db.create_all()
    datasess = db.session.query(SessionDataModel).all()
    print(datasess)
    session_data = datasess[index]
    return session_data
# -------------------------------- DATABASE MODEL OBJECTS----------------------------------------------
class UserAccount(db.Model):
    __tablename__ = 'user_account'
    participant_id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String(80), nullable=False, default=f'username{participant_id}', unique=True)
    post = relationship('Post', backref='author', lazy=True)
    session_data = relationship('SessionDataModel', backref='creator', lazy=True)


    def __repr__(self):
        return f'''
        UserAccount(
                username : {self.username},
                participant id : {self.participant_id},
                session activity: {self.post}
            )
        '''
    
class Post(db.Model):

    session_id = Column(Integer, primary_key=True, nullable=False)
    content = Column(String(80), nullable=False, default='start session')
    user_id = Column(Integer, ForeignKey('user_account.participant_id'), nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow())

    def __repr__(self):
        return f'''
            Post(
                date : {self.date},
                session id : {self.session_id},
                content: {self.content},
                author : {self.user_id}
            )
        '''

class SessionDataModel(db.Model):

    session_id = Column(Integer, primary_key=True, nullable=False)
    filename = Column(String(80), nullable=False, default=f'{ROOT_DIR}')
    user_id = Column(Integer, ForeignKey('user_account.participant_id'), nullable=False)
    x_simulation = Column(String(80), nullable=False, default=f'{ROOT_DIR}')
    y_simulation = Column(String(80), nullable=False, default=f'{ROOT_DIR}')
    z_simulation = Column(String(80), nullable=False, default=f'{ROOT_DIR}')
    consequence = Column(String(80), nullable=False, default=f'{ROOT_DIR}')
    consequence_value = Column(Integer, nullable=False, default=0)
    event_tree_probability = Column(Integer, nullable=False, default=0)
    initiating_event = Column(String(80), nullable=False, default=f'{ROOT_DIR}')

    def __repr__(self):
        return f'''
            SessionDataModel(
                session id : {self.session_id},
                filename: {self.filename},
                author : {self.user_id},
                x : {self.x_simulation},
                y : {self.y_simulation},
                z : {self.z_simulation},
                consequence : {self.consequence},
                consequence value : {self.consequence_value},
                event tree probability : {self.event_tree_probability},
                initiating event : {self.initiating_event}
            )
        '''
db.create_all()
ts = threading.Thread(target=initialize_web_app)
ts.start()