import streamlit as st 
def largest_num(num1,num2,num3): 
  result=0 
  if num1>num2 and num1>num3: 
    result=num1 
  elif num2>num1 and num2>num3: 
    result=num2 
  else: 
    result=num3 
  return result 
st.set_page_config(page_title='Largest number',layout='wide') 
st.sidebar.title("Largest number") 
form=st.sidebar.form(key="form",clear_on_submit=False) 
num1=form.number_input('Enter the 1st number',step=1) 
num2=form.number_input('Enter the 2nd number',step=1) 
num3=form.number_input('Enter the 3rd number',step=1) 
submitted=form.form_submit_button('Submit') 
if submitted: 
  st.header('Result:') 
  result=largest_num(num1,num2,num3) 
  st.write(f'The largest number is {result}') 
else: 
  st.header('Result:') 
  st.write('Click on submit button')
