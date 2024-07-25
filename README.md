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
   ```
   git clone https://github.com/yourusername/philosopher-chatbot.git
   cd philosopher-chatbot
   ```

2. Set up the backend:
   ```
   cd backend
   pip install -r requirements.txt
   ```

3. Set up the frontend:
   ```
   cd ../frontend
   npm install
   ```

4. Create a `config.py` file in the `backend` directory and add your Anthropic API key:
   ```python
   ANTHROPIC_API_KEY = 'your_api_key_here'
   ```

## Usage

1. Start the backend server:
   ```
   cd backend
   python app.py
   ```

2. In a new terminal, start the frontend development server:
   ```
   cd frontend
   npm start
   ```

3. Open your browser and navigate to `http://localhost:3000`

4. Select your preferred language, enter your Anthropic API key, choose a philosopher, and start chatting!

## Project Structure

```
philosopher-chatbot/
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

Your Name - [@your_twitter](https://twitter.com/your_twitter) - email@example.com

Project Link: [https://github.com/yourusername/philosopher-chatbot](https://github.com/yourusername/philosopher-chatbot)
