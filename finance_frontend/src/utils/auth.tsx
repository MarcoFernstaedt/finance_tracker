import { apiRequest } from './api';

// Login: sends email and password, expects access token and user info
export const login = async (email: string, password: string) => {
    return await apiRequest('/login/', {
        method: 'POST',
        body: JSON.stringify({ email, password }),
        withAuth: false,
    });
};

// Signup/Register
export const register = async (name: string, email: string, password: string) => {
    return await apiRequest('/register/', {
        method: 'POST',
        body: JSON.stringify({ name, email, password }),
        withAuth: false,
    });
};

// Verify token is still valid
export const verifyToken = async (token: string) => {
    return await apiRequest('/token/verify/', {
        method: 'POST',
        body: JSON.stringify({ token }),
        withAuth: false,
    });
};

// Refresh access token using cookie-stored refresh token
export const refreshToken = async () => {
    return await apiRequest('/refresh/', {
        method: 'POST',
        withAuth: false,
    });
};

// Logout: removes the refresh token cookie on backend
export const logout = async () => {
    return await apiRequest('/logout/', {
        method: 'POST',
        withAuth: false,
    });
};

// Get current user info (requires auth)
export const fetchUser = async () => {
    return await apiRequest('/me/', {
        method: 'GET',
        withAuth: true,
    });
};
