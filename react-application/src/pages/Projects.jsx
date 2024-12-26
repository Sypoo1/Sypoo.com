import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { getAllProjects } from '../api/project';

function Projects() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    getAllProjects()
      .then(data => setProjects(data))
      .catch(error => console.error('Error fetching projects:', error));
  }, []);

  return (
    <div className="container mx-auto p-8 fade-in">
      <h1 className="text-4xl font-bold mb-4 text-primary">Projects</h1>
      <ul className="space-y-4">
        {projects.map(project => (
          <li key={project.id} className="p-4 bg-gray-100 rounded shadow hover:bg-secondary transition duration-300">
            <Link to={`/projects/${project.id}`} className="flex items-center text-primary hover:text-white text-xl">
              {project.name}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Projects;