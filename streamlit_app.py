import streamlit as st
from accessing_models import get_caption, story_generation

# Title of the website
st.markdown(
    """
    <div style="text-align: center; font-weight: bold; font-size: 36px; color: #d90368;">
        PicTale
    </div>
    """,
    unsafe_allow_html=True
)
st.divider()

st.markdown(
    """
    <div style="text-align: left; font-weight: bold; font-size: 22px; color: #147df5;">
        Upload a picture to get a story
    </div>
    """,
    unsafe_allow_html=True
)

# upload image
image = st.file_uploader(label='upload a picture', label_visibility='hidden')
# show the image
st.image(image)
st.divider()

# create caption
caption = get_caption(image)
# generate a story
story = story_generation(caption)
story = story.replace('\n\n','\n')

st.markdown(
    """
    <div style="text-align: left; font-weight: bold; font-size: 22px; color: #147df5;">
        Here is the story for you
    </div>
    <br><br>
    """,
    unsafe_allow_html=True
)


st.markdown(
    f"""
    <div style="text-align: left; font-size: 18px; color: #22333b;">
        {story}
    </div>
    """,
    unsafe_allow_html=True
)

