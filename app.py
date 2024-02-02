import streamlit as st
st.title('hello world')
st.header('this is the headermarkdown')
st.markdown('hi is the  markdown') 
st.subheader('hi is the subheader')
st.markdown("<h1>colorful</h1>")
st.latex('x+ 50 ')
st.image("https://www.hopkinsmedicine.org/-/media/images/health/1_-conditions/brain/brain-lobes-anatomy.jpg")
st.select_slider('pick a mark ' , ['bad' , 'good' , 'exellent'])
gender = st.radio('pick your gender ' , ['male' , 'female' ])
if gender == 'male' : 
    st.write('hello mr')
else : 
    st.write('hello mrs ' )
gender2 = st.selectbox('pick your gender ' , ['male' , 'female' ])
if gender == 'male' : 
    st.write('hello mr')
else : 
    st.write('hello mrs ' )    
st.slider("your age ", 0 , 50 , step = 10)