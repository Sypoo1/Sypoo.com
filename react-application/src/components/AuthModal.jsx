import React, { useState, useContext } from 'react';
import { login, register } from '../api/auth';
import { UserContext } from '../context/UserContext';

function AuthModal({ isOpen, onClose }) {
  const [isLogin, setIsLogin] = useState(true);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const { login: loginUser } = useContext(UserContext);

  const handleAuth = async (e) => {
    e.preventDefault();
    try {
      const userData = isLogin ? await login(username, password) : await register(username, password);
      loginUser(userData);
      onClose();
    } catch (error) {
      console.error(isLogin ? 'Error logging in:' : 'Error registering:', error);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
      <div className="bg-white p-8 rounded shadow-md w-96">
        <h2 className="text-2xl font-bold mb-4">{isLogin ? 'Login' : 'Register'}</h2>
        <form onSubmit={handleAuth}>
          <div className="mb-4">
            <label className="block text-primary mb-2">Username</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded"
              required
            />
          </div>
          <div className="mb-4">
            <label className="block text-primary mb-2">Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="w-full p-2 border border-gray-300 rounded"
              required
            />
          </div>
          <button type="submit" className="bg-primary text-white p-2 rounded w-full">
            {isLogin ? 'Login' : 'Register'}
          </button>
        </form>
        <button onClick={() => setIsLogin(!isLogin)} className="mt-4 text-blue-500">
          {isLogin ? 'Need an account? Register' : 'Have an account? Login'}
        </button>
        <button onClick={onClose} className="mt-4 text-red-500">Close</button>
      </div>
    </div>
  );
}

export default AuthModal;