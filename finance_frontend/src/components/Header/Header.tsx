import React from 'react'

interface HeaderProps {
    loggedIn: boolean
}

const Header: React.FC<HeaderProps> = ({ loggedIn }) => {
    return (
        <header>
            {loggedIn ? (
                <button>Sign Out</button>
            ) : (
                <button>Sign In</button>
            )}
        </header>
    )
}

export default Header
