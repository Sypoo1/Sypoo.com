import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { getProjectById } from '../api/project';
import { FaGithub } from 'react-icons/fa';

function ProjectDetail() {
  const { projectId } = useParams();
  const [project, setProject] = useState(null);

  useEffect(() => {
    getProjectById(projectId)
      .then(data => setProject(data))
      .catch(error => console.error('Error fetching project details:', error));
  }, [projectId]);

  if (!project) {
    return <div className="container mx-auto p-8">Loading...</div>;
  }

  return (
    <div className="container mx-auto p-8 fade-in">
      <h1 className="text-4xl font-bold mb-4 text-primary">Project: {project.name}</h1>
      <p className="mb-4">Description: {project.description}</p>
      <a href={project.github_url} className="flex items-center text-primary hover:text-secondary transition duration-300">
        <FaGithub className="mr-2" /> GitHub
      </a>
    </div>
  );
}

export default ProjectDetail;