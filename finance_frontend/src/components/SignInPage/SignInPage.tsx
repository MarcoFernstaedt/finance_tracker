import React from 'react';

const SignInPage = () => {
    return (
        <main className="min-h-screen bg-black flex flex-col justify-center items-center px-4">
            <form className="p-6 pb-10 border border-4 justify-center items-center rounded shadow-md flex flex-col w-full max-w-sm">
                <h1 className="my-2 text-4xl text-white">Sign In</h1>
                <input
                    type="email"
                    placeholder="Enter email"
                    className="pl-6 py-2 text-white placeholder-white bg-black border border-gray-300 rounded-full w-full"
                />
                <input
                    type="password"
                    placeholder="Enter password"
                    className="pl-6 py-2 text-white placeholder-white bg-black border border-gray-300 rounded-full w-full"
                />
                <button type="submit" className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600">
                    Sign In
                </button>
                <p className="text-black mt-4 text-center">
                    Don't have an account? <a href="/sign-up" className="text-red-500">Sign up</a>
                </p>
            </form>
        </main>
    );
};

export default SignInPage;
