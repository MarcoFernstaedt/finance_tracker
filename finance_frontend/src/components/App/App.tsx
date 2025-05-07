import { useState } from 'react'
import Footer from '../Footer/Footer'
import Header from '../Header/Header'
import './App.css'

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <>
      <Header loggedIn={isLoggedIn} />
      <main className='min-h-screen flex flex-col justicy-center items-center w-screen h-screen bg-black'>
        <h1 className="text-4xl text-red-500">Hello</h1>
      </main>
      <Footer />
    </>
  )
}

export default App
