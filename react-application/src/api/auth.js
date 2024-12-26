import axios from 'axios';

const API_BASE_URL = 'http://0.0.0.0:8000/api/v1';

export const login = async (username, password) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/auth/login`, { username, password });
    return response.data;
  } catch (error) {
    console.error('Error logging in:', error);
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
    const response = await axios.get(`${API_BASE_URL}/auth/profile`, {
      headers: { Authorization: `Bearer ${token}` }
    });
    return response.data;
  } catch (error) {
    console.error('Error fetching user profile:', error);
    throw error;
  }
};