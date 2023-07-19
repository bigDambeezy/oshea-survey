from PIL import Image
import requests
import streamlit as st
import st_lottie

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Edikan Webpage", page_icon=":mage:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    return r.json()


# Use Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css('style/style.css.css')

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_wqypnpu5.json")
img_lottie_animation = Image.open("images/yt_lottie_animation.png.png")
img_contact_form = Image.open("images/yt_contact_form.png.png")

# ---- HEADER SECTION ----
st.subheader("Hi, I am Edikan :wave:")
st.title("A Graphic Designer And Electrical Engineer From Nigeria")
st.write(
    "I am passionate about finding ways to use python to improve digital designs and to design data collection systems that are both accurate and efficient in business settings. ")
st.write(
    "[Learn More >](https://docs.google.com/document/d/1dsWFIkWgZqnqzhaxWaPG_B872f7bU6f3/edit?usp=drive_link&ouid=106100842998567487877&rtpof=true&sd=true)")

# --- WHAT I DO ---
st.write("---")
left_column, right_column = st.columns(2)
with left_column:
    st.header("What I Do")
    st.write("##")
    if st.write(
            """
            I am building websites for companies and firms who:
            - are looking to use python to design data collection systems
            - wish to alleviate poverty with provision of scholarships and grants 
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses 
            - want to use python for graphic designing and illustrations.
            - modeling agencies that want to showcase their brands, or foundation for promotions
            
            If this sounds interesting to you, consider reaching us on our Email Address, so you can learn more about us 
            """
    ):
        st.write("[Email Address >](Ebukansonpp@outlook.com)")
    with right_column:
        st_lottie(lottie_coding)

    # ---- PROJECTS ----
    with st.container():
        st.write("---")
        st.header("My Projects")
        st.write("##")
        image_column, text_column = st.columns((1, 2))
        with image_column:
            st.image(img_lottie_animation)
        with text_column:
            st.subheader("Dog Myths and Misconceptions You Should Stop Believing")
            st.write(
                """
                Learn the misconceptions and myths behind dogs
                Dog myths are common beliefs or stories about dogs that are not accurate or true. Some myths are about their color vison, agression, or eating habits, all misconceptions we wish to clarify for you.
                """
            )
            st.markdown("[Watch Video...](https://www.youtube.com/watch?v=9DUpjx1tprQ)")
with st.container():
    image_column, text_column = st.columns((1, 2))
with image_column:
    st.image(img_contact_form)
with text_column:
    st.subheader("Contact us and subscribe for more info so you don't miss out")
    st.write(
        """
        Do you have a proposal that needs graphical presentation for your website?
        In this contact form you will find our email and number, if you want spontaneous work why not come to us and experience delivery and integrity
        """
    )
    st.markdown(
        "[Open Image...](https://drive.google.com/file/d/1fyjrkFYKcaVpW95QMtuNw2Y2iRO1OFJP/view?usp=drive_link)")

    # ---- CONTACT ----
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/ebukansonpp@outlook.com" method="POST">
             <input type="hidden" name="_captcha" value="false">
             <input type="text" name="name" placeholder="Your name" required>
             <input type="email" name="email" placeholder="Your email" required>
             <textarea name="message" placeholder="Your message here" required></textarea>
             <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
