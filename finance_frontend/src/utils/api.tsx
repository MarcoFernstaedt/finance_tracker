import React from 'react';
const baseUrl = 'http://localhost:5173/';

interface RequestOptions extends RequestInit {
    headers?: Record<string, string>;
    withAuth?: boolean,
}

const apiRequest = async (
    endpoint: string,
    options: RequestOptions = {},
): Promise<any> => {
    const { withAuth = true, ...fetchOptions } = options;

    const headers: Record<string, string> = {
        'Content-Type': 'application/json',
        ...(options.headers || {}),
    }

    if (withAuth) {
        const token = localStorage.getItem('token');
        if (token) headers['Authorization'] = `Bearer ${token}`;
    }

    try {
        const response = await fetch(`${baseUrl}${endpoint}`, {
            credentials: 'include',
            ...fetchOptions,
            headers,
        })

        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`Error: ${response.status} - ${errorText}`);
        }

        return await response.json();
    } catch (err) {
        console.error('API Error: ', err)
        throw err
    }
};
