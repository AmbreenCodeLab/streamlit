import streamlit as st
import datetime
import json
import os

# Page configuration
st.set_page_config(
    page_title="Growth Mindset Challenge",
    page_icon="🌱",
    layout="wide"
)

# Initialize session state for user data
if 'reflections' not in st.session_state:
    st.session_state.reflections = []

def save_reflection(date, challenge, approach, learning):
    st.session_state.reflections.append({
        'date': date.strftime("%Y-%m-%d"),
        'challenge': challenge,
        'approach': approach,
        'learning': learning
    })

# Main header
st.title("🌱 Growth Mindset Challenge")
st.markdown("""
    Welcome to your personal growth mindset journey! This tool will help you develop
    and maintain a growth mindset through daily reflection and practical exercises.
""")

# Sidebar navigation
page = st.sidebar.radio(
    "Navigate",
    ["Learn", "Daily Reflection", "Progress Tracker", "Mindset Tips"]
)

if page == "Learn":
    st.header("Understanding Growth Mindset")
    
    st.subheader("What is a Growth Mindset?")
    st.write("""
        A growth mindset is the belief that your abilities can be developed through 
        dedication, hard work, and learning from feedback. It's about seeing challenges 
        as opportunities and viewing effort as a path to mastery.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Fixed vs Growth Mindset")
        st.markdown("""
        | Fixed Mindset | Growth Mindset |
        |--------------|----------------|
        | "I'm not good at this" | "I can learn this" |
        | "This is too hard" | "This may take time" |
        | "I made a mistake" | "Mistakes help me learn" |
        | "This is good enough" | "I can always improve" |
        """)
    
    with col2:
        st.subheader("Benefits of Growth Mindset")
        st.markdown("""
        - Enhanced problem-solving abilities
        - Greater resilience in face of challenges
        - Improved learning outcomes
        - Better relationships and collaboration
        - Increased motivation and achievement
        """)

elif page == "Daily Reflection":
    st.header("Daily Growth Reflection")
    
    today = datetime.date.today()
    date = st.date_input("Date", today)
    
    challenge = st.text_area("What challenge did you face today?")
    approach = st.text_area("How did you approach this challenge? What growth mindset principles did you apply?")
    learning = st.text_area("What did you learn from this experience?")
    
    if st.button("Save Reflection"):
        if challenge and approach and learning:
            save_reflection(date, challenge, approach, learning)
            st.success("Reflection saved successfully!")
        else:
            st.error("Please fill in all fields")

elif page == "Progress Tracker":
    st.header("Your Growth Journey")
    
    if st.session_state.reflections:
        for reflection in reversed(st.session_state.reflections):
            with st.expander(f"Reflection from {reflection['date']}"):
                st.write("**Challenge:**", reflection['challenge'])
                st.write("**Approach:**", reflection['approach'])
                st.write("**Learning:**", reflection['learning'])
    else:
        st.info("Start your journey by adding daily reflections!")

else:  # Mindset Tips
    st.header("Growth Mindset Tips")
    
    tips = {
        "Embrace Challenges": "View challenges as opportunities to learn and grow.",
        "Learn from Mistakes": "Analyze mistakes to understand what went wrong and how to improve.",
        "Persist Through Difficulties": "Stay committed even when things get tough.",
        "Seek Feedback": "Ask for constructive criticism and use it to improve.",
        "Celebrate Progress": "Acknowledge small wins and improvements along the way."
    }
    
    for title, description in tips.items():
        with st.expander(title):
            st.write(description)
            
    st.markdown("""
    ### Daily Affirmation
    Remember: Your abilities and intelligence can be developed through dedication,
    hard work, and a willingness to learn from feedback.
    """)

# Footer
st.markdown("---")
st.markdown("*Developed with ❤️ to support your growth journey*")