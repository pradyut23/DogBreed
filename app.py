import streamlit as st
from PIL import Image, ImageOps
from classifier import image_classification

st.set_option('deprecation.showfileUploaderEncoding', False)

st.markdown('<style>body{background-image: url("https://www.jigsawstore.com.au/assets/full/RB15633-7.jpg?20200726170018"); background-repeat: no-repeat; background-attachment: fixed; background-size: 100% 100%;} body::before{content: ""; position: absolute; top: 0px; right: 0px; bottom: 0px; left: 0px; background-color: rgba(1,1,1,0.80);}</style>',unsafe_allow_html=True)
st.markdown('<style>body{color: white; text-align: center;}</style>',unsafe_allow_html=True)

st.title("DOG BREED IDENTIFIER")
st.text("Upload an image of a dog to identify it's breed")

st.write("")
st.write("")
st.write("")
st.write("")
st.write("Choose a dog image...")
uploaded_file = st.file_uploader("", type=["jpg","png","jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded image.', use_column_width=True)
    st.write("")
    with st.spinner('Identifying...'):
        label = image_classification(image, 'my_dog_model.h5')
    st.info(label)
