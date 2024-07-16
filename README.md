# Legal Assistant Chatbot - LegalAI

    Welcome to the Legal Assistant Chatbot project! This project aims to provide users with instant legal advice and answers to their legal queries through a user-friendly chat interface.

## Introduction

    The Legal Assistant Chatbot utilizes Flask, Google's GenerativeAI, and other libraries to offer users a platform to seek legal guidance and information. The chatbot analyzes user queries, matches them with relevant legal information, and provides responses accordingly.

## Features

 **Instant Legal Advice**: Users can ask legal questions and receive immediate responses.
 **Keyword Matching**: The chatbot matches user queries with relevant legal information stored in a CSV file.
 **User-Friendly Interface**: The web interface is designed to be intuitive and easy to use.
 **Dataset**: The dataset is stored at this location "static/ipc_sections.csv"

## Installation

1. Clone the repository:
    git clone <[repository_url](https://github.com/Barathvec-005/AI-POWERED-LEGAL-ASSISTANT.git)>
   
2. Install dependencies:
     pip install -r requirements.txt

3. Configure API Key:
     Obtain an API key from GenerativeAI and set it in the app.py file.
   
4. Generate Session Key:
     Run session.py to generate a session management secret key.

5.Run the application:
    python app.py

6. Usage:
     Navigate to the application URL in your web browser.
     Click on "Start Chatting" to access the chat interface.
     Enter your legal query in the input field and click "Send".
     The chatbot will analyze your query and provide a response based on relevant legal information.
7. Contributing:
     Contributions to the Legal Assistant Chatbot project are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.
