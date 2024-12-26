import axios from 'axios';
import qs from 'qs'; 
const API_BASE_URL = 'http://0.0.0.0:8000/api/v1';

export const login = async (username, password) => {
  try {
    const response = await axios.post(
      `${API_BASE_URL}/auth/token`,
      qs.stringify({ username, password }), // URL-encode the payload
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      }
    );
    return response.data;
  } catch (error) {
    console.error('Error logging in:', error.response ? error.response.data : error.message);
    throw error;
  }
};
export const register = async (username, password) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/auth/register`, { username, password });
    return response.data;
  } catch (error) {
    console.error('Error registering:', error);
    throw error;
  }
};

export const getUserProfile = async (token) => {
  try {
    const response = await axios.get(`${API_BASE_URL}/users/me`, {
      headers: { Authorization: `Bearer ${token}` }
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching user profile:', error);
    throw error;
  }
};