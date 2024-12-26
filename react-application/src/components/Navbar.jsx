import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav className="bg-blue-600 p-4 shadow-md flex justify-center">
      <div className="flex w-full max-w-screen-lg justify-between">
        <Link to="/" className="text-white font-bold text-lg hover:text-gray-200 transition duration-300">Home</Link>
        <Link to="/projects" className="text-white font-bold text-lg hover:text-gray-200 transition duration-300">Projects</Link>
      </div>
    </nav>
  );
}

export default Navbar;