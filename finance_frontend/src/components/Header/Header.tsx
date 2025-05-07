import React from 'react'

interface HeaderProps {
    loggedIn: boolean
}

const Header: React.FC<HeaderProps> = ({ loggedIn }) => {
    return (
        <header>
            {loggedIn ? (
                
            )}
        </header>
    )
}

export default Header
