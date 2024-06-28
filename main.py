import random
import streamlit as st
import numpy as np
st.title("MY PROJECT")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("Tôi chẳng biết viết gì vào đây cả ")
st.caption("Sao đây lại là caption nhỉ")
st.divider()
st.header("This is a header")
st.markdown("[Đinh Cường](facebook.com/cuongcutee)")
st.markdown("""
    1. Machine Learning
    2. Deep Learning
    3. Cuong cute
            """)
st.latex("\sqrt{2x}")
st.divider()
st.write('AI Viet Nam')
st.write('[Google](https//)')
st.code("""
    import numpy as np
    import matplotlib.py as plt
    data = np.arange(1,10)
    print(data)
""")


def get_year():
    return "19"


with st.echo():
    st.write("This is a text")

    def get_name():
        return "Thai"
    name = get_name()
    year = get_year()
    st.write(name, year)
st.divider()
st.logo("./FTU_logo_2020.png")
st.image("image1.png", caption="Trạm cỏ may, đánh bay miền ký ức")
st.audio("./DLTTAD.mp3")
st.divider()


def get_fullname():
    return "Thai"


agree = st.checkbox("I agree")
if agree:
    st.write("Cuong so funny")
status = st.radio("Your Favorite Color: ", [
    "Yellow", "Blue"], captions=["Vàng", "Xanh"])
print(status)


st.selectbox("Your Contact", {'Email', "Address", "Age"})
st.multiselect("Colors", ['Red', 'Green', 'Blue', 'Pink'], "Red")
st.select_slider("Number", np.linspace(0, 100))
st.divider()

if st.button("Say Hello"):
    st.write("Hello")
else:
    st.write("Goodbye")

value = st.text_input("Your name", value="Cuong")
st.write(value)
st.divider()

uploaded_files = st.file_uploader("Choose Files", accept_multiple_files=True)

for uploaded_file in uploaded_files:
    read_f = uploaded_file.read()
    st.write("File Name: ", uploaded_file.name)


with st.form("My form"):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("Name")
    f_age = col2.text_input("Age")
    submited = st.form_submit_button("Submit")
    if submited:
        st.write(f"Name :{f_name}, Age:{f_age}")
st.divider()
value = random.randint(1, 10)
if 'key' not in st.session_state:
    st.session_state['key'] = value
st.write(st.session_state.key)
