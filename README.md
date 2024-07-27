# Philosopher Chatbot

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)
![React Version](https://img.shields.io/badge/react-18.3.1-blue.svg)

Philosopher Chatbot is an interactive web application that allows users to engage in conversations with simulations of famous historical philosophers in multiple languages (Spanish, English, and Catalan). The application uses the Anthropic API to generate responses based on the style and philosophical ideas of each thinker in the user's selected language.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Web-based user interface for easy interaction
- Multi-language support (Spanish, English, Catalan)
- Selection of historical philosophers
- Dynamic conversation using Anthropic's Claude API
- Personalized responses based on each philosopher's style and ideas
- Secure API key management
- Rate limiting to prevent abuse

## Technologies Used

### Backend
- Python 3.6+
- Flask
- Flask-CORS
- Flask-Session
- Flask-Limiter
- Anthropic API
- Gunicorn (for production deployment)

### Frontend
- React 18.3.1
- TypeScript
- Axios for API requests
- Tailwind CSS for styling

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/pma1999/philosopher_chatbot.git
   cd philosopher_chatbot
   ```

2. Set up the backend:
   ```sh
   cd backend
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```sh
   cd ../frontend
   npm install

4. Configure the environment variables. You can do this by adding them to your development environment or by creating a .env file in the backend directory. Here is an example of what the .env file should look like:
   ```env
   ANTHROPIC_API_KEY=sk-ant-api03-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   SECRET_KEY=$(python -c "import secrets; print(secrets.token_urlsafe(32))")
   ```

5. Start the backend server:
   ```sh
   cd backend
   python app.py

6. In a new terminal, start the frontend development server:
   ```sh
   cd frontend
   npm start

7. Open your browser and navigate to `http://localhost:3000`

8. Select your preferred language, enter your Anthropic API key, choose a philosopher, and start chatting!


## Project Structure

```
philosopher_chatbot/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── philosophers.py
│   ├── translations.py
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── contexts/
│   │   ├── services/
│   │   ├── App.tsx
│   │   └── index.tsx
│   ├── package.json
│   └── tsconfig.json
└── README.md
```

### Backend

- `app.py`: Main Flask application with API endpoints
- `config.py`: Configuration file for API keys and other settings
- `philosophers.py`: Database of philosophers and their information
- `translations.py`: Translations for user interface text

### Frontend

- `components/`: React components for the user interface
- `contexts/`: React context for managing application state
- `services/`: API service for communicating with the backend
- `App.tsx`: Main application component
- `index.tsx`: Entry point of the React application

## API Endpoints

- `GET /api/languages`: Get available languages
- `POST /api/validate-api-key`: Validate the Anthropic API key
- `GET /api/philosophers`: Get list of available philosophers
- `POST /api/start-conversation`: Initialize a conversation with a philosopher
- `POST /api/send-message`: Send a message to the philosopher and get a response

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

Pablo Miguel - pablomiguelargudo@gmail.com

Project Link: [https://github.com/pma1999/philosopher_chatbot](https://github.com/pma1999/philosopher-chatbot)