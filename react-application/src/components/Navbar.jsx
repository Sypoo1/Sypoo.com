import React, { useState, useContext } from 'react';
import { Link } from 'react-router-dom';
import AuthModal from './AuthModal';
import { UserContext } from '../context/UserContext';

function Navbar() {
  const [isAuthModalOpen, setAuthModalOpen] = useState(false);
  const { user } = useContext(UserContext);

  return (
    <nav className="bg-blue-600 p-4 shadow-md flex items-center justify-between">
      <span className="text-white font-bold text-lg ml-4">Sypoo.com</span>
      <div className="flex-grow flex justify-center space-x-24">
        <Link to="/" className="text-white font-bold text-lg hover:text-gray-200 transition duration-300">Home</Link>
        <Link to="/projects" className="text-white font-bold text-lg hover:text-gray-200 transition duration-300">Projects</Link>
        <Link to="/add-project" className="text-white font-bold text-lg hover:text-gray-200 transition duration-300">Add project</Link>
      </div>
      <div className="mr-4">
        {user ? (
          <span className="text-white font-bold">{user.username}</span>
        ) : (
          <button onClick={() => setAuthModalOpen(true)} className="text-white font-bold hover:text-gray-200 transition duration-300">
            Login/Register
          </button>
        )}
      </div>
      <AuthModal isOpen={isAuthModalOpen} onClose={() => setAuthModalOpen(false)} />
    </nav>
  );
}

export default Navbar;