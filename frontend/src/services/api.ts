import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

axios.defaults.withCredentials = true;

export const getLanguages = async () => {
  const response = await axios.get(`${API_URL}/languages`);
  return response.data;
};

export const validateApiKey = async (apiKey: string) => {
  try {
    const response = await axios.post(`${API_URL}/validate-api-key`, 
      { api_key: apiKey },
      {
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': apiKey
        }
      }
    );
    return response.data.valid;
  } catch (error) {
    if (axios.isAxiosError(error) && error.response) {
      throw new Error(error.response.data.error || 'Failed to validate API key');
    } else {
      throw new Error('An unexpected error occurred');
    }
  }
};

export const getPhilosophers = async (language: string, apiKey: string) => {
  try {
    const response = await axios.get(`${API_URL}/philosophers`, {
      params: { language },
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': apiKey
      }
    });
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error) && error.response) {
      throw new Error(error.response.data.error || 'Failed to fetch philosophers');
    } else {
      throw new Error('An unexpected error occurred');
    }
  }
};

export const startConversation = async (language: string, philosopherId: string, apiKey: string) => {
  try {
    const response = await axios.post(`${API_URL}/start-conversation`, 
      { language, philosopher_id: philosopherId },
      {
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': apiKey
        }
      }
    );
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error) && error.response) {
      throw new Error(error.response.data.error || 'Failed to start conversation');
    } else {
      throw new Error('An unexpected error occurred');
    }
  }
};

export const sendMessage = async (message: string, apiKey: string) => {
  try {
    const response = await axios.post(`${API_URL}/send-message`, 
      { message },
      {
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': apiKey
        }
      }
    );
    return response.data.response;
  } catch (error) {
    if (axios.isAxiosError(error) && error.response) {
      throw new Error(error.response.data.error || 'An error occurred while sending the message');
    } else {
      throw new Error('An unexpected error occurred');
    }
  }
};