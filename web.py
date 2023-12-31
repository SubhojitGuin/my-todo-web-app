import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state['new_todo']
    if not new_todo == '':
        todos.append(new_todo + "\n")
        functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my Todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='Enter a todo:', placeholder="Add a new todo...",
              label_visibility='hidden', on_change=add_todo, key='new_todo')
