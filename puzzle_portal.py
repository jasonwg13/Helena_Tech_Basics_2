import streamlit as st
import pandas as pd
import random
from rapidfuzz import fuzz



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
options = ['Welcome to PuzzlePortal', 'Preferences', 'Animal of the day', 'Reviews', 'Inspiration']
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

# List of puzzles with their answers
puzzles = [
    {"question": "What has to be broken before you can use it?", "answer": "egg"},
    {"question": "What has keys but can’t open locks?", "answer": "piano"},
    {"question": "The more of me you take, the more you leave behind. What am I?", "answer": "footsteps"},
    {"question": "What can fill a room but takes up no space?", "answer": "light"},
    {"question": "I’m light as a feather, yet the strongest person can’t hold me for long. What am I?",
     "answer": "breath"},
    {"question": "What comes once in a minute, twice in a moment, but never in a thousand years?", "answer": "m"},
    {"question": "What has a head, a tail, is brown, and has no legs?", "answer": "penny"},
    {"question": "I am not alive, but I can grow. I don’t have lungs, but I need air. What am I?", "answer": "fire"}
]

# session state for selected puzzle and score
if "selected_puzzle" not in st.session_state:
    st.session_state.selected_puzzle = random.choice(puzzles)
if "score" not in st.session_state:
    st.session_state.score = 0


def welcome_page():
    st.title("Welcome to PuzzlePortal!")

    st.title("Daily dose of using your brain🧩")
    st.write("Solve the puzzle below and input your answer:")

    # Display puzzle question
    st.subheader(st.session_state.selected_puzzle["question"])

    # Input field for user's answer
    user_answer = st.text_input("Your Answer:")

    # Check answer when button is clicked
    if st.button("Submit"):
        correct_answer = st.session_state.selected_puzzle["answer"]
        similarity = fuzz.ratio(user_answer.strip().lower(), correct_answer.lower())

        if similarity >= 80:
            st.success(f"Correct! Great job! The answer is indeed: {correct_answer}")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect. The correct answer was: {correct_answer}")

        new_game_button = st.button("new game")
        # Pick a new puzzle for the next interaction
        st.session_state.selected_puzzle = random.choice(puzzles)

    # Display the user's score
    st.write(f"**Your Score:** {st.session_state.score}")


def preference_page():
    # title
    st.title("Preference Quiz")
    st.write("Answer the questions about what you prefer to puzzle!")
    random_message()

    # title
    st.title("Quiz for puzzling preferences")
    st.write("Answer the questions about what you prefer to puzzle!")

    # Puzzles database
    puzzles = [
        {
            "name": "Lavendelfeld zur goldenen Sonne 16724",
            "image_url": "https://m.media-amazon.com/images/I/61qBAseyBBL._AC_UF1000,1000_QL80_.jpg",
            "attributes": ["Landscape", "Detailed", "Nature", "Fewer pieces", "Realistic", "Colourful"]
        },
        {
            "name": "Guanajuato in Mexiko 17442",
            "image_url": "https://m.media-amazon.com/images/I/611tjCHSSoL._AC_UF1000,1000_QL80_.jpg",
            "attributes": ["Landscape", "Detailed", "City", "A lot of pieces", "Realistic", "Monochrome"]
        },
        {
            "name": "Magische Stimmung über dem Leuchtturm von Akranes, Island 12000732",
            "image_url": "https://m.media-amazon.com/images/I/61OpG-BKUwL._AC_UF894,1000_QL80_.jpg",
            "attributes": ["Landscape", "Detailed", "Coastal town", "A lot of pieces", "Realistic", "Earth tones"]
        },
        {
            "name": "Schlacht auf hoher See 13969",
            "image_url": "https://m.media-amazon.com/images/I/71EGLaamQcL.jpg",
            "attributes": ["Ocean", "Detailed", "Coastal town", "A lot of pieces", "Cartoon", "Earth tones"]
        },
        {
            "name": "Geheimnisvolle Unterwasserwelt 16661",
            "image_url": "https://i.pinimg.com/736x/cb/5a/03/cb5a038c26f04bd30b73bbd53be4becc.jpg",
            "attributes": ["Ocean", "Undetailed", "Nature", "A lot of pieces", "Cartoon", "Monochrome"]
        },
        {
            "name": "Almbock mit Baby 12000809",
            "image_url": "https://scale.coolshop-cdn.com/product-media.coolshop-cdn.com/23JB8Y/8326844d67cc442bbaf1bc8f6aaf5510.jpg/f/ravensburger-puzzle-foto-city-landscape-3000p-12000809.jpg",
            "attributes": ["Mountains", "Detailed", "Nature", "A lot of pieces", "Realistic", "Colourful"]
        },
        {
            "name": "Regenbogenberge, China 17324",
            "image_url": "https://m.media-amazon.com/images/I/71zg-x0qpmL._AC_UF894,1000_QL80_.jpg",
            "attributes": ["Mountains", "Detailed", "Nature", "Fewer pieces", "Realistic", "Colorful"]
        },
        {
            "name": "Zauberhafte Wüste 15069",
            "image_url": "https://m.media-amazon.com/images/I/81-4l9-nVaL.jpg",
            "attributes": ["Desert", "Detailed", "Nature", "Fewer pieces", "Realistic", "Earth tones"]
        },
        {
            "name": "In den Dünen 146130",
            "image_url": "https://m.media-amazon.com/images/I/91MMqfZH-AL.jpg",
            "attributes": ["Ocean", "Undetailed", "Coastal town", "Fewer pieces", "Realisitc", "Earth tones"]
        },
        {
            "name": "Wasserfall von Kirkjufell, Island 19539",
            "image_url": "https://m.media-amazon.com/images/I/61WOdfMmGrL.jpg",
            "attributes": ["Mountains", "Undetailed", "Coastal town", "Fewer pieces", "Realistic", "Earth tones"]
        },
        {
            "name": "Pokémon Classics 12000726",
            "image_url": "https://data.puzzle.de/.5/pokemon-classics-1500-teile--puzzle.91804-2.fs.jpg",
            "attributes": ["Landscape", "Undetailed", "City", "A lot of pieces", "Cartoon", "Colorful"]
        },
    ]

    # Helper function for fuzzy matching
    def find_best_puzzle(user_preferences, puzzles, threshold=70):
        best_match = None
        highest_score = 0

        for puzzle in puzzles:
            # Compare each attribute of the puzzle to user preferences
            scores = [fuzz.ratio(user_attr, puzzle_attr) for user_attr, puzzle_attr in
                      zip(user_preferences, puzzle["attributes"])]
            avg_score = sum(scores) / len(scores)

            if avg_score > highest_score and avg_score >= threshold:
                highest_score = avg_score
                best_match = puzzle

        return best_match, highest_score

    # Streamlit app
    def preference():
        st.title("Find Your Perfect Puzzle!")
        st.write("Answer the following questions to find the best puzzle for you!")

        # Questions for user preferences
        question1 = st.radio("Do you prefer Landscape or Ocean?", ["Landscape", "Ocean", "Mountains", "Desert"])
        question2 = st.radio("Do you prefer detailed or undetailed?", ["Detailed", "Undetailed"])
        question3 = st.radio("Do you prefer city or nature?", ["City", "Nature", "Coastal town"])
        question4 = st.radio("Do you prefer a lot of pieces or fewer pieces?", ["A lot of pieces", "Fewer pieces"])
        question5 = st.radio("Do you prefer a realistic image or a cartoon image?", ["Realistic", "Cartoon"])
        question6 = st.radio("Do you prefer colourful or monochrome?", ["Colourful", "Monochrome", "Earth tones"])

        # Collect user preferences
        user_preferences = [question1, question2, question3, question4, question5, question6]

        # Find the best puzzle match when the button is clicked
        if st.button("Find My Puzzle!"):
            best_match, score = find_best_puzzle(user_preferences, puzzles)

            if best_match:
                st.write(f"We found a match for you!🧩 ({score:.2f}% match)")
                st.image(best_match["image_url"], caption=best_match["name"], use_column_width=True)
            else:
                st.write("No perfect match found, but here’s a random suggestion!")
                random_puzzle = random.choice(puzzles)
                st.image(random_puzzle["image_url"], caption=random_puzzle["name"], use_column_width=True)

    if __name__ == "__main__":
        preference()
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

def inspiration_page():
    # Titel der Anwendung
    st.title("Inspiration Page")
    st.write("Here is some inspiration")
    random_message()
    st.image("https://www.japanwelt.de/media/image/origami-figuren-tiere-falten.jpg")
    st.write("Origami")
    st.image("https://nimble-needles.com/wp-content/uploads/2021/09/how-to-knit-for-beginners-720x720.jpg")
    st.write("Knitting")
    st.image("https://sudoku-puzzles.net/wp-content/puzzles/butterfly-sudoku/easy/1.png")
    st.write("Sudoku")
    st.image("https://www.treevalleyacademy.com/wp-content/uploads/6th-Grade-Fall-Crossword-791x1024.png.webp")
    st.write("Crossword")
    st.image("https://i.insider.com/60144316a7c0c4001991dde6?width=800&format=jpeg&auto=webp")
    st.write("Coding")
    st.image("https://magicholz.de/cdn/shop/files/LKB01-Classic-Gramophone-Robotime-ROKR-v10.png?v=1699300249&width=960")
    st.image("https://www.kastner-oehler.de/metal+earth-3d+metallbausatz+-+star+wars+-+sith+tie+fighter-1-768_1024_75-7429781_1.webp")
    st.write("Mechanical Puzzles")
    st.image("https://lego.storeturkey.com.tr/millennium-falcon-v29-star-wars-lego-24646-33-B.jpg")
    st.write("Lego")


# when the user selects a page, show the new content
if page_selection == "Welcome to PuzzlePortal":
    welcome_page()
elif page_selection == "Preferences":
    preference_page()
elif page_selection == "Reviews":
    review_page()
elif page_selection == "Inspiration":
    inspiration_page()
elif page_selection == "Animal of the day":
    st.write("HI!")
    st.image("https://www.pandaclub.ch/wp-content/uploads/2019/09/Header_Ronny-Overhate-auf-Pixabay-768x512.jpg",
             caption="spider")
    random_message()




