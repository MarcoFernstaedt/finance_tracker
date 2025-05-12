import { useState } from 'react'
import Footer from '../Footer/Footer'
import Header from '../Header/Header'
import './App.css'
import { Navigate, Route, Routes } from 'react-router-dom'
import ProtectedRoute from '../ProtectedRoute'
import SignInPage from '../SignInPage/SignInPage'

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
        <Route
          path='/dashboard'
          element={
            <ProtectedRoute isLoggedIn={isLoggedIn}>
              {/* <Dashboard /> */}
              <h1>Dashbaord</h1>
            </ProtectedRoute>
          }
        />
        <Route
          path='/account'
          element={
            <ProtectedRoute isLoggedIn={isLoggedIn}>
              {/* <Account /> */}
              <h1>Account</h1>
            </ProtectedRoute>
          }
        />
        <Route
          path='/transactions'
          element={
            <ProtectedRoute isLoggedIn={isLoggedIn}>
              {/* <Transactions /> */}
              <h1>Transactions</h1>
            </ProtectedRoute>
          }
        />
        <Route
          path='/sign-in'
          element={
            <SignInPage />
          }
        />
        <Route path='*' element={<Navigate to='/' replace />} />
      </Routes>
      <Footer />
    </>
  )
}

export default App