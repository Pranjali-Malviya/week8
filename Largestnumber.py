import streamlit as st

def largest_num(number_1,number_2,number_3):
  l=[number_1,number_2,number_3]
  l.sort()
  return (l[2])

st.set_page_config(page_title="Largest Number")
st.sidebar.title("Largest Number")
form.st.sidebar.form(key="form", clear_on_submit=False)
number_1=form.number.input("Enter the 1st number:",step=1)
number_2=form.number.input("Enter the 2nd number:",step=1)
number_3=form.number.input("Enter the 3rd number:",step=1)
submitted=form.form_submit_button("Find the Largest")

if submitted:
  st.header('Result:')
  result=largest_num(number_1,number_2,number_3)
  st.Write(f'The largest number is {result}')
else:
  st.header('Result:')
  st.write("Waiting for submiting")
