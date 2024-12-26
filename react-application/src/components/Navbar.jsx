import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <nav className="bg-blue-600 p-4 shadow-md flex items-center justify-between">
      <span className="text-white font-bold text-lg ml-4">Sypoo.com</span>
      <div className="flex-grow flex justify-center space-x-24">
        <Link to="/" className="text-white font-bold text-lg hover:text-gray-200 transition duration-300">Home</Link>
        <Link to="/projects" className="text-white font-bold text-lg hover:text-gray-200 transition duration-300">Projects</Link>
        <Link to="/add-project" className="text-white font-bold text-lg hover:text-gray-200 transition duration-300">Add project</Link>
      </div>
    </nav>
  );
}

export default Navbar;