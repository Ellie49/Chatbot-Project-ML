# Chatbot Project Report

## Project Problem Description
The objective of this project is to build an end-to-end chatbot system that integrates a machine
learning powered backend with a simple user interface. The chatbot provides users with a way to
query information and receive automated responses from a predefined knowledge base. This
project was chosen because chatbots represent a practical real-world application of machine
learning and natural language processing, and they are widely used in customer service,
healthcare, education, and more.

## Solution Overview
The project consists of two main parts:
1. **Backend:** Implemented using Flask, the backend hosts the chatbot model. The model loads
responses from a knowledge base (stored as JSON) and matches user queries. Flask-CORS is
enabled so that the frontend can directly communicate with the backend.
2. **Frontend:** A simple interface built using HTML, CSS, and JavaScript. The user enters queries
into the interface, which sends them via HTTP requests to the backend API.

### Workflow
- User enters a query in the frontend.
- The frontend sends the query to the Flask backend.
- The backend processes the query using the chatbot model and returns a suitable response.
- The frontend displays the chatbot’s reply in real time.

## Challenges and Learnings
During development, a few challenges were encountered:
- **Environment Setup:** Installing and managing dependencies such as Flask and scikit-learn
required attention to detail.
- **CORS Issues:** Initially, connecting the frontend and backend caused cross-origin errors, which
were resolved by enabling Flask-CORS.
- **Model Simplicity:** Since this was a lightweight project, the chatbot relied on a knowledge-base
approach rather than a large-scale deep learning model. This helped to keep the project efficient
and runnable on local machines.

### Learnings
- Gained hands-on experience in integrating frontend and backend systems.
- Understood the importance of API design and testing endpoints.
- Learned how to deploy and test a local ML-powered application end-to-end.

## References
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Flask-CORS](https://flask-cors.readthedocs.io/)
- [scikit-learn](https://scikit-learn.org/stable/)
- [NumPy](https://numpy.org/)
