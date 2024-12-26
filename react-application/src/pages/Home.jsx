import React from 'react';
import { FaGithub, FaLinkedin, FaTelegram, FaPython, FaDocker, FaRust } from 'react-icons/fa';
import { SiNodedotjs, SiPostgresql, SiMongodb } from 'react-icons/si';

function Home() {
  return (
    <div className="container mx-auto p-8 fade-in">
      <h1 className="text-4xl font-bold mb-4 text-primary">About Me</h1>
      <p className="mb-6">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
      </p>
      <h2 className="text-2xl font-semibold mb-4">Skills</h2>
      <ul className="list-disc pl-5 mb-6">
        <li className="flex items-center"><FaPython className="mr-2 text-blue-500" /> Python</li>
        <li className="flex items-center"><FaRust className="mr-2 text-orange-500" /> Rust</li>
        <li className="flex items-center"><FaDocker className="mr-2 text-blue-600" /> Docker</li>
        <li className="flex items-center"><SiNodedotjs className="mr-2 text-green-500" /> Node.js</li>
        <li className="flex items-center"><SiPostgresql className="mr-2 text-blue-700" /> PostgreSQL</li>
        <li className="flex items-center"><SiMongodb className="mr-2 text-green-600" /> MongoDB</li>
      </ul>
      <h2 className="text-2xl font-semibold mb-4">Social Links</h2>
      <ul className="list-disc pl-5">
        <li>
          <a href="https://github.com/Sypoo1" target="_blank" rel="noopener noreferrer" className="flex items-center text-black hover:text-gray-700 transition duration-300">
            <FaGithub className="mr-2" /> GitHub
          </a>
        </li>
        <li>
          <a href="https://www.linkedin.com/in/sypoo/" target="_blank" rel="noopener noreferrer" className="flex items-center text-blue-700 hover:text-blue-800 transition duration-300">
            <FaLinkedin className="mr-2" /> LinkedIn
          </a>
        </li>
        <li>
          <a href="https://t.me/Sypoo" target="_blank" rel="noopener noreferrer" className="flex items-center text-blue-500 hover:text-blue-600 transition duration-300">
            <FaTelegram className="mr-2" /> Telegram
          </a>
        </li>
      </ul>
    </div>
  );
}

export default Home;