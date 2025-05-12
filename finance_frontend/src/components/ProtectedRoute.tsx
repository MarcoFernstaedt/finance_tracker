import React from 'react'
import { Navigate } from 'react-router-dom';

interface ProtectedRouteProps {
    isLoggedIn: boolean;
    children: React.ReactNode;
}

const ProtectedRoute: React.FC<ProtectedRouteProps> = ({ children, isLoggedIn }) => {
    if (!isLoggedIn) {
        return <Navigate to='/' />
    }
    return <>{children}</>
}

export default ProtectedRoute