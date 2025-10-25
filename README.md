# 🗂 Django Task Manager

A simple task manager web app built with Django.  
Users can register, log in, and manage their personal task list.

Features

- User authentication
  - Register / Login / Logout
- Personal tasks
  - Each user sees ONLY their own tasks
- Task CRUD
  - Create / Edit / Delete tasks
- Status tracking
  - `To Do`, `In Progress`, `Done`
- Optional deadline with calendar picker
- Admin panel (Django admin)
  

Tech Stack

Python 3.11

Django 5

SQLite (локальная база)

Django Crispy Forms + Bootstrap 5 (UI форм)

config/            # Django project settings, urls, etc.
tasks/
  models.py        # Task model
  forms.py         # TaskForm + RegisterForm
  views.py         # Auth + CRUD logic
  urls.py          # Routes
  templates/tasks/ # HTML templates (Bootstrap)
manage.py          # Django entry point
db.sqlite3         # Local dev database


Auth flow

/register/ – create account

/login/ – sign in

/logout/ – sign out

/ – your personal tasks

/create/ – create task

/admin/ – admin panel (superuser only)
