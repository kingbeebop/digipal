// auth.ts
import { apiUrl } from './config'; 
import { LoginData, AuthResponse } from '../types'

export const loginRequest = async (data: LoginData): Promise<AuthResponse> => {
  try {
    const response = await fetch(`${apiUrl}/login/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      const responseData = await response.json();
      return responseData;
    } else {
      throw new Error('Invalid credentials');
    }
  } catch (error: any) {
    console.error('Login error:', error.message);
    throw error;
  }
};

export const logoutRequest = async (): Promise<void> => {
  try {
    const response = await fetch(`${apiUrl}/logout/`, {
      method: 'POST',
      credentials: 'include',
    });

    if (!response.ok) {
      throw new Error('Failed to logout');
    }
  } catch (error: any) {
    console.error('Logout error:', error.message);
    throw error;
  }
};

export const refreshToken = async (refreshToken: string): Promise<AuthResponse> => {
  try {
    const response = await fetch(`${apiUrl}/token/refresh/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ refresh: refreshToken }),
    });

    if (response.ok) {
      const responseData = await response.json();
      return responseData;
    } else {
      throw new Error('Failed to refresh token');
    }
  } catch (error: any) {
    console.error('Refresh token error:', error.message);
    throw error;
  }
};

export const getRefreshToken = (): string | null => {
  // Retrieve the refresh token from localStorage
  const refreshToken = localStorage.getItem('refreshToken');
  return refreshToken;
};
