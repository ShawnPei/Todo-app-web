import os
import time

import streamlit as st
from streamlit.errors import DuplicateWidgetID

import functions

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state['new_todo'] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)
    st.session_state['new_todo'] = ""


# The order of the code is important
st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    try:
        checkbox = st.checkbox(todo, key=todo)
        if checkbox:
            todos.pop(index)
            functions.write_todos(todos)
            del st.session_state[todo]
            st.experimental_rerun()
    except DuplicateWidgetID:
        todos.pop(index)
        functions.write_todos(todos)

        st.warning("You already have this todo, please type in a new one")

st.text_input(label=" ", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
