import React from 'react';

const SignInPage = () => {
    return (
        <main className="min-h-screen bg-black flex flex-col justify-center items-center px-4">
            <form className="px-6 py-10 border border-4 justify-center items-center rounded shadow-md flex flex-col w-full max-w-sm">
                <h1 className="mb-10 text-4xl text-white">Sign In</h1>
                <input
                    type="email"
                    placeholder="Enter email"
                    className="px-4 py-2 mb-5 text-white placeholder-white bg-black border border-gray-300 rounded-full w-full"
                />
                <input
                    type="password"
                    placeholder="Enter password"
                    className="px-4 py-2 mb-10 text-white placeholder-white bg-black border border-gray-300 rounded-full w-full"
                />
                <button type="submit" className="mb-5 bg-red-500 text-white px-4 py-2 rounded-full w-30 hover:bg-red-600">
                    Sign In
                </button>
                <p className="text-white text-center">
                    Don't have an account? <a href="/sign-up" className="text-blue-500">Sign up</a>
                </p>
            </form>
        </main>
    );
};

export default SignInPage;
