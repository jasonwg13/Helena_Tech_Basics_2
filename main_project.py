import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Welcome to PuzzlePortal")



# function for changing colors
def set_theme(theme_name):
    themes = {
        "Brown": {  # Warm brown tones
            "primary_color": "#8B4513",
            "background_color": "#F4E3D7",
            "text_color": "#4E342E",
            "header_color": "#6D4C41"
        },
        "Bright": {
            "primary_color": "#FFFFFF",
            "background_color": "#CBEDB1",
            "text_color": "#000000",
            "header_color": "#FFFFFF"
        },
        "Dark": {
            "primary_color": "#6C6C6C",
            "background_color": "#6C6C6C",
            "text_color": "#000000",
            "header_color": "#000000"
        },
        "Blue": {  # Blue-themed colors
            "primary_color": "#298897",
            "background_color": "#298897",
            "text_color": "#99F1FF",
            "header_color": "#99F1FF"
        },
        "Green": {  # Emerald-green inspired colors
            "primary_color": "#3F804E",
            "background_color": "#3F804E",
            "text_color": "#86CA96",
            "header_color": "#86CA96"
        },
        "Red": {  # Bordeaux-inspired deep reds
            "primary_color": "#BC6175",
            "background_color": "#F2CED1",
            "text_color": "#880924",
            "header_color": "#880924"
        }
    }

    if theme_name in themes:
        theme = themes[theme_name]
        custom_css = f"""
        <style>
            :root {{
                --primary-color: {theme['primary_color']};
                --background-color: {theme['background_color']};
                --text-color: {theme['text_color']};
                --header-color: {theme['header_color']};
            }}

            /* Apply background color and text color with higher specificity */
            html, body, div.stApp {{
                background-color: var(--background-color) !important;
                color: var(--text-color) !important;
            }}

            h1, h2, h3, h4, h5, h6 {{
                color: var(--header-color) !important;
            }}

            /* Streamlit-specific class adjustments */
            .css-18e3th9 {{
                background-color: var(--background-color) !important;
                color: var(--text-color) !important;
            }}

            .stButton > button {{
                background-color: var(--primary-color) !important;
                color: var(--text-color) !important;
            }}

            .stTextInput > div > div input {{
                background-color: var(--background-color) !important;
                color: var(--text-color) !important;
            }}

            .css-1cpxqw2 {{
                background-color: var(--background-color) !important;
            }}
        </style>
        """
        st.markdown(custom_css, unsafe_allow_html=True)


# create a side bar with different pages
st.sidebar.header("Menu")
options = ['Welcome to PuzzlePortal', 'Preferences', 'Animal of the day', 'Reviews']
page_selection = st.sidebar.selectbox("Choose the page", options)

# choosing the color in the menu
st.sidebar.header("Design")
theme_name = st.sidebar.selectbox("Which colour theme do you prefer", ["Brown", "Dark", "Blue", "Green", "Red", "Bright"], index=0)

set_theme(theme_name)


def random_message():
    # List of messages
    messages = [
        "Hey there! Just finished my puzzle—took me 15 minutes. What’s your time looking like?",
        "Pro tip: Start with the corners; it’s a game changer!",
        "How’s it going? I always find the edges first; works for me!",
        "Wow, I just unlocked a 6x6 grid. Have you tried it yet?",
        "Did you know the world’s largest jigsaw puzzle had over 500,000 pieces? Imagine that!",
        "Almost there? I can’t wait to see the finished puzzle!",
        "You’re doing amazing—keep it up! Don’t let that one tricky piece fool you.",
        "Fun fact: Puzzles were invented in the 1760s. You're part of a historic tradition!",
        "Think of it like life: one piece at a time, and it all fits together.",
        "Need a break? Sometimes a fresh perspective makes all the difference!",
        "I just unlocked a cat-themed puzzle—so adorable! What’s your favorite theme?",
        "Have you tried rotating pieces? Sometimes the solution’s simpler than you think.",
        "Challenge accepted! I’m trying to beat your time on the last puzzle.",
        "Puzzles are like meditation for the brain. Feeling zen yet?",
        "Wow, your puzzle looks great! Want to swap tips on tough spots?",
        "I love how satisfying it is when the final piece clicks. Almost there?",
        "You’re inspiring me! I might take on a harder level next.",
        "Stuck? Look at the colors and patterns—it always helps me!",
        "I just discovered there’s a world championship for puzzling. Should we enter?",
        "Way to go, puzzler extraordinaire! I’m cheering you on from here!",
    ]

    message = random.choice(messages)
    st.toast(message)



def main_page():
    get_random_puzzle()
    st.title("Welcome to PuzzlePortal!")
    random_message()


# Function to get today's puzzle

def get_random_puzzle():

    # List of puzzle types
    puzzles = ["Riddle", "Question", "Word Puzzle"]

    # Randomly pick a puzzle type
    puzzle_type = random.choice(puzzles)

    if puzzle_type == "Riddle":
        return {
            "type": "Riddle",
            "content": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
        }

    elif puzzle_type == "Question":
        return {
            "type": "Question",
            "content": "What is the capital city of France?",
            "answer": "Paris",
        }

    elif puzzle_type == "Word Puzzle":
        scrambled_word = "EFDOR"
        return {
            "type": "Word Puzzle",
            "content": f"Unscramble this word: {scrambled_word}",
            "answer": "FRODE",
        }





def preference_page():
    # title
    st.title("Multiple-Choice Quiz")
    st.write("Answer the questions about what you prefer to puzzle!")
    random_message()

    # title
    st.title("Quiz for puzzling preferences")
    st.write("Answer the questions about what you prefer to puzzle!")

    def random_images():
        # List of images
        image_urls = [
            "https://m.media-amazon.com/images/I/81hAdEFf+EL._AC_UF894,1000_QL80_.jpg",
            "https://spielwaren-kroemer.de/844665-large_default/prachtvolle-blumenliebe-100.jpg",
            "https://images.thimbletoys.com/images/items/2142015a.jpg",
            "https://data.puzzle-online.de/ravensburger.5/planetensystem-puzzle-5000-teile.91802-2.fs.jpg",
            "https://www.galaxus.ch/im/productimages/5/1/1/8/7/2/3/2/5/0/0/5/5/3/9/8/6/9/5/70eef960-9b28-465e-b2fd-6155164cc995_cropped.jpg",
            "https://spielwaren-kroemer.de/844665-large_default/prachtvolle-blumenliebe-100.jpg",
            "https://www.1001puzzles.de/2641164-large_default/ravensburger-100009-pokemon-puzzle-pokemon-allstars-5000-teile.jpg",
        ]

        random_image = random.choice(image_urls)

        st.image(random_image, caption=f"Bild von {random_image}", use_column_width=True)

    # Questions for preference quiz
    question1 = st.radio("Do you prefer Landscape or Ocean?",
                         ["Landscape", "Ocean", "Mountains", "Desert"])

    question2 = st.radio("Do you prefer detailed or undetailed?",
                         ["Detailed", "Undetailed"])

    question3 = st.radio("Do you prefer city or nature?",
                         ["City", "Nature", "Coastal town"])

    question4 = st.radio("Do you prefer a lot of pieces or fewer pieces?",
                         ["A lot of pieces", "Fewer pieces"])

    question5 = st.radio("Do you prefer a realistic image or a cartoon image?",
                         ["Realistic", "Cartoon"])

    question6 = st.radio("Do you prefer colourful or monochrome?",
                         ["Colourful", "Monochrome", "Earth tones"])

    button_results = st.button("Click here for results")

    if button_results:
        if question1 == "Landscape" and question2 == "Detailed" and question3 == "Nature" and question4 == "Fewer pieces" and question5 == "Realistic" and question6 == "Colourful":
            st.image("https://m.media-amazon.com/images/I/61qBAseyBBL._AC_UF1000,1000_QL80_.jpg")
        elif question1 == "Landscape" and question2 == "Detailed" and question3 == "City" and question4 == "A lot of pieces" and question5 == "Realistic" and question6 == "Monochrome":
            st.image("https://m.media-amazon.com/images/I/611tjCHSSoL._AC_UF1000,1000_QL80_.jpg")
        elif question1 == "Landscape" and question2 == "Detailed" and question3 == "Nature" and question4 == "A lot of pieces" and question5 == "Realistic" and question6 == "Earth tones":
            st.image("https://m.media-amazon.com/images/I/61OpG-BKUwL._AC_UF894,1000_QL80_.jpg")
        elif question1 == "Landscape" and question2 == "Undetailed" and question3 == "Nature" and question4 == "Fewer pieces" and question5 == "Cartoon" and question6 == "Earth tones":
            st.image("https://ravensburger.cloud/images/produktseiten/520x445/12000685.webp")
        elif question1 == "Landscape" and question2 == "Detailed" and question3 == "Coastal town" and question4 == "Fewer pieces" and question5 == "Cartoon" and question6 == "Earth tones":
            st.image("https://m.media-amazon.com/images/I/91adAe-LBkL.jpg")
        elif question1 == "Ocean" and question2 == "Detailed" and question3 == "City" and question4 == "A lot of pieces" and question5 == "Realistic" and question6 == "Earth tones":
            st.image("https://m.media-amazon.com/images/I/71EGLaamQcL.jpg")
        elif question1 == "Ocean" and question2 == "Detailed" and question3 == "Nature" and question4 == "A lot of pieces" and question5 == "Cartoon" and question6 == "Colourful":
            st.image("data:image/jpeg;base64,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")
        elif question1 == "Ocean" and question2 == "Undetailed" and question3 == "Nature" and question4 == "Fewer pieces" and question5 == "Realistic" and question6 == "Earth tones":
            st.image("https://www.sooonah.com/uploads/vendor-images/ravensburger-gesmbh/15154.jpg")
        elif question1 == "Ocean" and question2 == "Detailed" and question3 == "Coastal town" and question4 == "Fewer pieces" and question5 == "Realistic" and question6 == "Earth tones":
            st.image("data:image/jpeg;base64,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")
        elif question1 == "Ocean" and question2 == "Undetailed" and question3 == "Nature" and question4 == "Fewer pieces" and question5 == "Cartoon" and question6 == "Monochrome":
            st.image("https://i.pinimg.com/736x/cb/5a/03/cb5a038c26f04bd30b73bbd53be4becc.jpg")
        elif question1 == "Mountains" and question2 == "Detailed" and question3 == "Nature" and question4 == "A lot of pieces" and question5 == "Realistic" and question6 == "Colorful":
            st.image("https://scale.coolshop-cdn.com/product-media.coolshop-cdn.com/23JB8Y/8326844d67cc442bbaf1bc8f6aaf5510.jpg/f/ravensburger-puzzle-foto-city-landscape-3000p-12000809.jpg")
        elif question1 == "Mountains" and question2 == "Detailed" and question3 == "Nature" and question4 == "Fewer pieces" and question5 == "Realistic" and question6 == "Monochrome":
            st.image("https://m.media-amazon.com/images/I/81PNofvq0jL._AC_UF894,1000_QL80_.jpg")
        elif question1 == "Mountains" and question2 == "Detailed" and question3 == "Nature" and question4 == "Fewer pieces" and question5 == "Realistic" and question6 == "Colorful":
            st.image("https://m.media-amazon.com/images/I/71zg-x0qpmL._AC_UF894,1000_QL80_.jpg")
        elif question1 == "Mountains" and question2 == "Undetailed" and question3 == "City" and question4 == "Fewer pieces" and question5 == "Realistic" and question6 == "Earth tones":
            st.image("https://media1.jpc.de/image/w1155/front/0/4005555002543.jpg")
        elif question1 == "Mountains" and question2 == "Undetailed" and question3 == "Coastal town" and question4 == "Fewer pieces" and question5 == "Cartoon" and question6 == "Earth tones":
            st.image("https://m.media-amazon.com/images/I/7188dhMSPsL.jpg")
        elif question1 == "Desert" and question2 == "Detailed" and question3 == "Nature" and question4 == "A lot of pieces" and question5 == "Realistic" and question6 == "Colorful":
            st.image("https://m.media-amazon.com/images/I/81rnDyCqnkL.jpg")
        elif question1 == "Desert" and question2 == "Detailed" and question3 == "Nature" and question4 == "Fewer pieces" and question5 == "Realistic" and question6 == "Earth tones":
            st.image("https://m.media-amazon.com/images/I/81-4l9-nVaL.jpg")
        elif question1 == "Desert" and question2 == "Undetailed" and question3 == "Nature" and question4 == "Fewer pieces" and question5 == "Realistic" and question6 == "Monochrome":
            st.image("https://spielwaren-kroemer.de/898924-large_default/pzthe-huntington-desert-garden-1000-t.jpg")
        elif question1 == "Desert" and question2 == "Undetailed" and question3 == "City" and question4 == "A lot of pieces pieces" and question5 == "Cartoon" and question6 == "Earth tones":
            st.image("https://m.media-amazon.com/images/I/71VcfM3aBLL.jpg")
        elif question1 == "Desert" and question2 == "Undetailed" and question3 == "Coastal town" and question4 == "Fewer pieces" and question5 == "Realistic" and question6 == "Earth tones":
            st.image("https://m.media-amazon.com/images/I/91MMqfZH-AL.jpg")
        else:
            st.title("We couldn't find the perfect fit for your preferences but maybe you like this!")
            random_images()


def review_page():

    # Titel der Anwendung
    st.title("Review Page")
    st.write("Give your review!")
    random_message()


    df_reviews =  pd.DataFrame(columns=["Number of article", "Name", "Review", "Comment"])
    # Initialisierung oder Laden der Daten
    if "df_reviews" not in st.session_state:
        st.session_state.df_reviews = pd.DataFrame(columns=["Number of article", "Name", "Review", "Comment"])

    # Formular für neue Reviews
    with st.form("review_form"):
        st.subheader("Add a new review!")
        artikelnummer = st.text_input("Number of article", placeholder="e.g. 123456")
        name = st.text_input("Name", placeholder="Your Name")
        bewertung = st.slider("Review", min_value=1, max_value=5, step=1)
        kommentar = st.text_area("Comment", placeholder="Write your comment here...")
        submit_button = st.form_submit_button("Save")



    # Speicherung der Daten
    if submit_button:
        if artikelnummer and name and kommentar:
            new_review = {
                "Number of article": artikelnummer,
                "Name": name,
                "Review": bewertung,
                "Comment": kommentar
            }
            new_review = pd.DataFrame([new_review])
            st.session_state.df_reviews = pd.concat([st.session_state.df_reviews, new_review], ignore_index=True)
            #st.session_state["reviews"] = st.session_state["reviews"].append(new_review, ignore_index=True)
            st.success("Review saved successfully!")
        else:
            st.error("Please fill out everything.")

    # Anzeige der gespeicherten Reviews
    st.subheader("Saved Review")
    if not st.session_state.df_reviews.empty:
        st.dataframe(st.session_state["df_reviews"])
    else:
        st.write("No reviews yet.")


# when the user selects a page, show the new content
if page_selection == "Welcome to PuzzlePortal":
    main_page()
elif page_selection == "Preferences":
    preference_page()
elif page_selection == "Reviews":
    review_page()
elif page_selection == "Animal of the day":
    st.write("HI!")
    st.image("https://www.pandaclub.ch/wp-content/uploads/2019/09/Header_Ronny-Overhate-auf-Pixabay-768x512.jpg",
             caption="spider")
    random_message()




