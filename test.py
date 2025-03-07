import streamlit as st

def main():
    # Set page title
    st.title("My Simple Streamlit App")
    
    # Add a header
    st.header("Welcome to the app!")
    
    # Add text input
    user_input = st.text_input("Enter your name:", "")
    
    # Add a selectbox
    favorite_color = st.selectbox(
        "What's your favorite color?",
        ["Red", "Blue", "Green", "Yellow"]
    )
    
    # Add a slider
    age = st.slider("How old are you?", 0, 100, 25)
    
    # Add a button
    if st.button("Click me!"):
        # Show results when button is clicked
        st.write(f"Hello {user_input}!")
        st.write(f"Your favorite color is {favorite_color}")
        st.write(f"You are {age} years old")
        
        # Add a balloons animation
        st.balloons()
    
    # Add sidebar content
    st.sidebar.header("About")
    st.sidebar.text("This is a simple demo app")
    st.sidebar.text("Built with Streamlit")

if __name__ == "__main__":
    main()
