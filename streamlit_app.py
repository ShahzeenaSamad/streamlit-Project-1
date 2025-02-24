import streamlit as st
import datetime
import requests
from hijri_converter import convert

# Function to calculate Zakat
def zakat_calculator(amount):
    return amount * 0.025  # 2.5% Zakat Calculation

# 99 Names of Allah
names_of_allah = {
    "Ar-Rahman": "The Most Gracious", "Ar-Rahim": "The Most Merciful", "Al-Malik": "The King and Owner of Dominion",
    "Al-Quddus": "The Absolutely Pure", "As-Salam": "The Source of Peace", "Al-Mu’min": "The Giver of Faith",
    "Al-Muhaymin": "The Preserver of Safety", "Al-Aziz": "The Almighty", "Al-Jabbar": "The Compeller",
    "Al-Mutakabbir": "The Supreme", "Al-Khaliq": "The Creator", "Al-Bari": "The Evolver",
    "Al-Musawwir": "The Fashioner", "Al-Ghaffar": "The Constant Forgiver", "Al-Qahhar": "The All-Prevailing One",
    "Al-Wahhab": "The Supreme Bestower", "Ar-Razzaq": "The Provider", "Al-Fattah": "The Supreme Solver",
    "Al-Alim": "The All-Knowing", "Al-Qabid": "The Withholder", "Al-Basit": "The Extender",
    "Al-Khafid": "The Reducer", "Ar-Rafi": "The Elevating One", "Al-Muizz": "The Honourer-Bestower",
    "Al-Mudhill": "The Dishonourer", "As-Sami": "The All-Hearing", "Al-Basir": "The All-Seeing",
    "Al-Hakam": "The Impartial Judge", "Al-Adl": "The Just One", "Al-Latif": "The Subtle One",
    "Al-Khabir": "The All-Aware", "Al-Halim": "The Most Forbearing", "Al-Azim": "The Magnificent One"
}
# Quranic Verses
quranic_verses = [
    "Indeed, prayer prohibits immorality and wrongdoing. (Surah Al-Ankabut 29:45)",
    "And whoever puts their trust in Allah, then He alone is sufficient for them. (Surah At-Talaq 65:3)",
    "So remember Me; I will remember you. (Surah Al-Baqarah 2:152)",
    "Indeed, with hardship comes ease. (Surah Al-Inshirah 94:6)",
    "And He found you lost and guided you. (Surah Ad-Duha 93:7)"
]

# Hadiths
hadiths = [
    "The best among you are those who have the best manners and character. (Bukhari)",
    "Allah does not look at your appearance or wealth, but He looks at your hearts and deeds. (Muslim)",
    "The strong person is not the one who can wrestle, but the one who can control himself in anger. (Bukhari)",
    "A Muslim is the one from whose tongue and hands other Muslims are safe. (Bukhari)"
]

# Function to get real-time prayer times
def get_prayer_times():
    city = "Makkah"
    country = "SA"
    url = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=2"
    response = requests.get(url).json()
    if response and "data" in response:
        return response["data"]["timings"]
    return {}

prayer_times = get_prayer_times()

# Get current Hijri date
current_date = datetime.datetime.now()
hijri_date = convert.Gregorian(current_date.year, current_date.month, current_date.day).to_hijri()
hijri_date_str = f"{hijri_date.day} {hijri_date.month_name()} {hijri_date.year} AH"

# Set page title and layout
st.set_page_config(page_title="🌙 Ramzan Islamic App", page_icon="🕌", layout="wide")

# Sidebar Menu
st.sidebar.header("🌙 Islamic Hub")  # Updated title to match app theme

# Apply Custom CSS for Full Theme
st.markdown("""
    <style>
            
         /* Sidebar Navigation Headings */
        [data-testid="stSidebar"] h2 {
            color: #2B1B58 !important; /* Darker shade of #E5D9F2 */
            font-weight: bold !important;
            text-decoration: underline !important;
        }

        /* Main Section Headings (Global) */
        h1, h2, h3, h4, h5, h6 {
            color: #2B1B58 !important; /* Darker shade */
            font-weight: bold !important;
            text-decoration: underline !important;
        }

        /* Specific Custom Titles (If Any) */
        .main-title, .section-title {
            color: #2B1B58 !important;
            font-size: 26px !important;
            font-weight: bold !important;
            text-decoration: underline !important;
        }    
                
        [data-testid="stSidebar"] {
            background-color: #E5D9F2 !important;
        }

        div[data-testid="stAppViewContainer"] {
            background-color: #F5EFFF !important;
        }

        html, body, [data-testid="stAppViewContainer"] {
            background-color: #F5EFFF !important;
            height: 100%;
        }

        header {
            display: none !important;
        }

        .main-title {
            color: #5E3A9B !important;
            font-size: 32px !important;
            font-weight: bold !important;
            text-align: center;
            text-decoration: underline !important;
        }

        .section-title {
            color: #4A297C !important;
            font-size: 26px !important;
            font-weight: bold !important;
            text-decoration: underline !important;
        }
            
        /* Styling for content boxes */
        .stAlert, .content-box {
            background-color: #E5D9F2 !important;
            padding: 15px !important;
            border-radius: 8px !important;
            border-left: 5px solid #2B1B58 !important;
        }   

         /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #E5D9F2 !important;
        }

        /* Sidebar Text and Labels */
        [data-testid="stSidebar"] * {
            font-size: 18px !important; /* Increase font size */
            font-weight: bold !important;
            color: #2B1B58 !important;
        }

        /* Sidebar Headers */
        [data-testid="stSidebar"] h2 {
            font-size: 22px !important; /* Even larger for headers */
        }

        /* Sidebar Radio Buttons Labels */
        label {
            font-size: 18px !important;
        }        

        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }
        th {
    background-color: #5E3A9B !important; /* Keep a consistent theme */
    color: white !important; /* Make text white */
    font-weight: bold !important;
    padding: 10px !important;
    text-align: center !important;
}

            
        /* Mobile Specific Fixes */
    @media screen and (max-width: 768px) {
        [data-testid="stAppViewContainer"] {
            background-color: #F5EFFF !important;
        }

        /* Beautiful Names of Allah Text Fix */
    h2, h3, h4, h5, h6, p {
        color: #2B1B58 !important; /* Dark Purple for Readability */
        font-weight: bold !important;
    }

    /* If the text is inside a specific div */
    div:has(> h2) {
        color: #2B1B58 !important;
    }

    /* Forcefully fix specific section if needed */
    [data-testid="stAppViewContainer"] h2 {
        color: #2B1B58 !important;
    }

        /* Ensure all text remains visible */
        body, p, span, label {
            color: #2B1B58 !important;
        }

        /* Reduce Sidebar Size */
        [data-testid="stSidebar"] {
            font-size: 16px !important;
        }

        /* Improve Button Visibility */
        button {
            background-color: #5E3A9B !important;
            color: white !important;
            font-size: 16px !important;
            font-weight: bold !important;
        }
        }      
    </style>
""", unsafe_allow_html=True)

menu_options = [
    "🏠 Home",  # Added Home as the default page
    "🕌 Prayer Times",  # Renamed to a more Islamic theme
    "📿 Beautiful Names of Allah",  # More descriptive
    "💰 Zakat Estimator",  # Alternative wording
    "📖 Quranic Guidance",  # More spiritual
    "📜 Daily Hadith",  # More refined wording
    "📿 Digital Tasbeeh",  # Clearer name
    "📅 Ramadan Planner"  # More interactive title
]
selection = st.sidebar.radio("Choose a Section", menu_options)  # Updated wording

# Main Content Based on Selection
if selection == "🏠 Home":
    st.markdown("<p class='main-title'>🌙 Welcome to the Ramzan Islamic App</p>", unsafe_allow_html=True)
    st.markdown("<p class='extra-info'>Stay connected with your faith this Ramadan with helpful tools and reminders! 🤲</p>", unsafe_allow_html=True)
    
    # Sehri & Iftar Reminder
    st.markdown("<p class='section-title'>🌅 Sehri & Iftar Time</p>", unsafe_allow_html=True)
    st.write(f"**🌙 Sehri Time:** {prayer_times.get('Fajr', 'N/A')}")
    st.write(f"**🌇 Iftar Time:** {prayer_times.get('Maghrib', 'N/A')}")
    
    # Islamic Duas
    st.markdown("<p class='section-title'>🤲 Daily Islamic Duas</p>", unsafe_allow_html=True)
    st.write("**Sehri Dua:** وَبِصَوْمِ غَدٍ نَّوَيْتُ مِنْ شَهْرِ رَمَضَانَ")
    st.write("**Iftar Dua:** اللَّهُمَّ إِنِّي لَكَ صُمْتُ وَبِكَ آمَنْتُ وَعَلَيْكَ تَوَكَّلْتُ وَعَلَى رِزْقِكَ أَفْطَرْتُ")
    st.write("**Dua for Forgiveness:** اللَّهُمَّ إِنَّكَ عَفُوٌّ تُحِبُّ الْعَفْوَ فَاعْفُ عَنِّي")
    st.write("**Dua for Guidance:** اللّهُمَّ اهْدِني وَسَدِّدْنِي")
    st.write("**Dua for Protection:** بِسْمِ اللَّهِ الَّذِي لَا يَضُرُّ مَعَ اسْمِهِ شَيْءٌ فِي الْأَرْضِ وَلَا فِي السَّمَاءِ وَهُوَ السَّمِيعُ الْعَلِيمُ")

 

elif selection == "🕌 Prayer Times":
    st.write("### 🕌 Prayer Times")
    for prayer, timing in prayer_times.items():
        st.write(f"**{prayer}:** {timing}")

elif selection ==  "📿 Beautiful Names of Allah":
    st.write("### 📿 Beautiful Names of Allah")
    st.markdown("""
     <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }
        th {
            background-color: #5E3A9B;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)
    table_html = "<table><tr><th>Arabic Name</th><th>Meaning</th></tr>"
    for name, meaning in names_of_allah.items():
        table_html += f"<tr><td>{name}</td><td>{meaning}</td></tr>"
    table_html += "</table>"
    st.markdown(table_html, unsafe_allow_html=True)


elif selection == "💰 Zakat Estimator":
    st.write("### 💰 Zakat Estimator")
    amount = st.number_input("Enter Your Total Savings (in currency)", min_value=0, step=1)
    if st.button("Calculate Zakat"):
        zakat_amount = zakat_calculator(amount)
        st.success(f"Your calculated Zakat is: {zakat_amount:.2f}")

elif selection == "📖 Quranic Guidance":
    st.write("### 📖 Quranic Guidance")
    for verse in quranic_verses:
        st.info(verse)

elif selection == "📜 Daily Hadith":
    st.write("### 📜 Hadith of the Day")
    for hadith in hadiths:
        st.info(hadith)

elif selection == "📿 Digital Tasbeeh":
    if "count" not in st.session_state:
        st.session_state.count = 0
    st.write("### 📿 Digital Tasbeeh")
    st.write(f"**Count:** {st.session_state.count}")
    if st.button("+1 SubhanAllah"):
        st.session_state.count += 1
    if st.button("+1 Alhamdulillah"):
        st.session_state.count += 1
    if st.button("+1 Allahu Akbar"):
        st.session_state.count += 1
    if st.button("Reset Counter"):
        st.session_state.count = 0

elif selection == "📅 Ramadan Planner":
    st.write("### 📅 Ramadan Planner")
    st.write("Ramzan Calendar for the current year:")
    st.table({
        "Day": [i for i in range(1, 31)],
        "Hijri Date": [f"{i} {hijri_date.month_name()} {hijri_date.year} AH" for i in range(1, 31)],
        "Sehri Time": ["04:30 AM" for _ in range(1, 31)],
        "Iftar Time": ["06:45 PM" for _ in range(1, 31)]
    })

st.sidebar.write(f"📅 **Current Date:** {current_date.strftime('%Y-%m-%d')}")
st.sidebar.write(f"🕌 **Hijri Date:** {hijri_date_str}")
