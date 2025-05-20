import axios from 'axios';

// Create axios instance with base URL
const api = axios.create({
  baseURL: 'http://localhost:8000/api/',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Function to calculate the sum
export const calculateSum = async (num1, num2) => {
  try {
    const response = await api.post('calculate/', { num1, num2 });
    return response.data;
  } catch (error) {
    console.error('Error calculating sum:', error);
    throw error;
  }
};

export default api;