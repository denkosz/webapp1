import streamlit as st
import functions1
# streamlit run C:\PythoProjects\pythonProject3\webapp\web.py
# pip freeze > requirements.txt
todos = functions1.get_todos()




def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions1.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

st.text_input(label="Enter todo:", placeholder="Enter here",
              on_change=add_todo, key="new_todo")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions1.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()
