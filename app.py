import streamlit as st

# Function to generate bot response
def bot_response(user_input):
    # This is just a placeholder for the response logic
    responses = {
        "Hi": "Hello! How can I assist you today?",
        "How are you?": "I'm just a bot, but I'm here to help!",
        "What can you do?": "I can assist with various queries related to intents-based chatbot systems!"
    }
    return responses.get(user_input, "I'm sorry, I didn't understand that.")

# Setting up the Streamlit app
st.title("Intents-based Chatbot")

user_input = st.text_input("You:")

if user_input:
    response = bot_response(user_input)
    st.text_area("Bot:", value=response, height=200, max_chars=None, key=None)  
