import React from 'react'
import { Link } from 'react-router-dom'
import { Button } from '../ui/button'
import { LayoutDashboard, PenBox } from 'lucide-react'

interface HeaderProps {
    loggedIn: boolean
}

const Header: React.FC<HeaderProps> = ({ loggedIn }) => {
    return (
        <header className='fixed top-0 bg-gray-900 w-full bg-black/80 backdrop-blur-md z-50 border-b border-gray-500'>
            <nav className='container mx-auto px-4 py-4 flex items-center justify-between'>
                <Link to='/'>
                    <div className='text-white text-4xl h-12 w-auto object-contain'>
                        {/* height: 60px
                        width: 200px */}
                        Logo
                    </div>
                </Link>
                <div className='flex items-center space-x-4'>
                    {loggedIn ? (
                        <>
                            <Link to='/dashboard' className='flex items-center gap-2'>
                                <Button variant='outline' className='bg-black text-gray-500 border-gray-500 hover:bg-gray-800 hover:text-blue-600'>
                                    <LayoutDashboard size={18}></LayoutDashboard>
                                    <span className='hidden md:inline'>Dashboard</span>
                                </Button>
                            </Link>
                            <Link to='/transaction' className='flex items-center gap-2'>
                                <Button variant='outline' className='bg-black text-gray-500 border-gray-500 hover:bg-gray-800 hover:text-blue-600'>
                                    <PenBox size={18}></PenBox>
                                    <span className='hidden md:inline'>Transaction</span>
                                </Button>
                            </Link>
                            <Button variant='outline' className='h-10 w-10 rounded-full bg-black text-gray-500 border-gray-500 hover:bg-gray-800 hover:text-blue-600' >M</Button>
                        </>
                    ) : (
                        <Button variant='outline' className='bg-black text-white border-gray-500 hover:bg-gray-500 hover:text-black' >Login</Button>
                    )}
                </div>
            </nav>
        </header>
    )
}

export default Header
