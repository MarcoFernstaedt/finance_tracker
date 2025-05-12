import { useState } from 'react'
import Footer from '../Footer/Footer'
import Header from '../Header/Header'
import './App.css'
import { Route, Routes } from 'react-router-dom'
import ProtectedRoute from '../ProtectedRoute'

const App = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <>
      <Header loggedIn={isLoggedIn} />
      <Routes>
        <Route
          path='/'
          element={
            <main className='min-h-screen flex flex-col justify-center items-center w-screen h-screen bg-black'>
              <h1 className="text-4xl text-red-500">Hello</h1>
            </main>
          }
        />
        {/* <Route
          path='/dashboard'
          element={
            <ProtectedRoute isLoggedIn={isLoggedIn}>
              <Dashboard />
            </ProtectedRoute>
          }
        /> */}
        {/* <Route
          path='/account'
          element={
            <ProtectedRoute isLoggedIn={isLoggedIn}>
              <Account />
            </ProtectedRoute>
          }
        /> */}
        {/* <Route
          path='/transactions'
          element={
            <ProtectedRoute isLoggedIn={isLoggedIn}>
              <Transactions />
            </ProtectedRoute>
          }
        /> */}
      </Routes>
      <Footer />
    </>
  )
}

export default App