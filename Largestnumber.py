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
st.sidebar.title("Largest among three numbers") 
form=st.sidebar.form(key="form",clear_on_submit=False) 
num1=form.number_input('Enter the first number',step=1) 
num2=form.number_input('Enter the second number',step=1) 
num3=form.number_input('Enter the third number',step=1) 
submitted=form.form_submit_button('Submit') 
if submitted: 
  st.header('Result:') 
  result=largest_num(num1,num2,num3) 
  st.write(f'The largest number is {result}') 
else: 
  st.header('Result:') 
  st.write('Waiting for submiting the numbers')
