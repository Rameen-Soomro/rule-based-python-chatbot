import customtkinter as ctk
from tkinter import END
from datetime import datetime
import random

# ----------------------------
# Window Settings
# ----------------------------

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Professional Rule-Based Chatbot")
app.geometry("700x650")
app.resizable(False, False)

# ----------------------------
# Title
# ----------------------------

title = ctk.CTkLabel(
    app,
    text="🤖 Rule-Based Chatbot",
    font=("Arial", 24, "bold")
)
title.pack(pady=15)

# ----------------------------
# Chat Area
# ----------------------------

chat_area = ctk.CTkTextbox(
    app,
    width=650,
    height=430,
    font=("Arial", 14),
    wrap="word"
)

chat_area.pack(pady=10)
chat_area.configure(state="disabled")

# ----------------------------
# Chat Colors
# ----------------------------



chat_area.tag_config(
    "bot",
    foreground="#66CCFF"
)

chat_area.tag_config(
    "name",
    foreground="white"
)

# ----------------------------
# Time Function
# ----------------------------

def current_time():
    return datetime.now().strftime("%I:%M %p")


# ----------------------------
# Display Message
# ----------------------------

def display_message(sender, message):

    chat_area.configure(state="normal")

    if sender == "user":
        icon = "👤"
    else:
        icon = "🤖"

    chat_area.insert(
        END,
        f"{icon} {sender.title()} ({current_time()})\n",
        "name"
    )

    chat_area.insert(
        END,
        message + "\n\n",
        sender
    )

    chat_area.configure(state="disabled")
    chat_area.see(END)


# ----------------------------
# Rule-Based Chatbot
# ----------------------------

def chatbot_response(message):

    message = message.lower().strip()

    # Greetings
    if message in ["hi", "hello", "hey", "hii", "helo"]:
        responses = [
            "Hello! How can I help you?",
            "Hi there! Nice to meet you.",
            "Hey! What can I do for you?"
        ]
        return random.choice(responses)

    # How are you
    elif "how are you" in message:
        return "I'm doing great! Thanks for asking. 😊"

    # Name
    elif "your name" in message or "who are you" in message:
        return "I am a Rule-Based Chatbot created using Python and CustomTkinter."

    # Time
    elif "time" in message:
        return f"The current time is {current_time()}."

    # Date
    elif "date" in message or "today" in message:
        today = datetime.now().strftime("%A, %d %B %Y")
        return f"Today's date is {today}."

    # Python
    elif "python" in message:
        return "Python is a popular programming language used for web development, AI, automation, data science, and more."

    # Programming
    elif "programming" in message or "coding" in message:
        return "Programming is the process of writing instructions that tell a computer what to do."

    # Thanks
    elif "thank" in message or "thanks" in message:
        return "You're welcome! 😊"

    # Help
    elif "help" in message:
        return "Sure! You can ask me about Python, programming, the date, the time, or simply say hello."

    # Goodbye
    elif message in ["bye", "goodbye", "see you", "exit", "quit"]:
        return "Goodbye! Have a great day! 👋"

    # Default response
    else:
        return "Sorry, I don't understand that yet. Please try another question."


# ----------------------------
# Send Message
# ----------------------------

def send_message():

    message = entry.get().strip()

    if message == "":
        return

    # Display user message
    display_message("user", message)

    # Get chatbot response
    response = chatbot_response(message)

    # Display bot response
    display_message("bot", response)

    # Clear entry box
    entry.delete(0, END)


# ----------------------------
# Clear Chat
# ----------------------------

def clear_chat():

    chat_area.configure(state="normal")
    chat_area.delete("1.0", END)
    chat_area.configure(state="disabled")


# ----------------------------
# Bottom Frame
# ----------------------------

bottom_frame = ctk.CTkFrame(app)

bottom_frame.pack(
    fill="x",
    padx=15,
    pady=10
)

# ----------------------------
# Message Entry
# ----------------------------

entry = ctk.CTkEntry(
    bottom_frame,
    width=470,
    placeholder_text="Type your message..."
)

entry.pack(
    side="left",
    padx=10,
    pady=10
)

# ----------------------------
# Send Button
# ----------------------------

send_button = ctk.CTkButton(
    bottom_frame,
    text="Send",
    command=send_message,
    width=80
)

send_button.pack(
    side="left",
    padx=5
)

# ----------------------------
# Clear Button
# ----------------------------

clear_button = ctk.CTkButton(
    bottom_frame,
    text="Clear Chat",
    fg_color="red",
    hover_color="#8B0000",
    command=clear_chat,
    width=100
)

clear_button.pack(
    side="left",
    padx=5
)

# ----------------------------
# Enter Key
# ----------------------------

entry.bind(
    "<Return>",
    lambda event: send_message()
)

# ----------------------------
# Welcome Message
# ----------------------------

display_message(
    "bot",
    "Hello! I am your Rule-Based Chatbot.\nHow can I help you today?"
)

# ----------------------------
# Start Application
# ----------------------------

app.mainloop()