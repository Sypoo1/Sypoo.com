import React, { useState } from 'react';
import { addProject } from '../api/project';

function AddProjectForm() {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [githubUrl, setGithubUrl] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await addProject({ name, description, github_url: githubUrl });
      // Clear the form after successful submission
      setName('');
      setDescription('');
      setGithubUrl('');
      alert('Project added successfully!');
    } catch (error) {
      console.error('Error adding project:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="container mx-auto p-8 fade-in">
      <h2 className="text-2xl font-bold mb-4 text-primary">Add Project</h2>
      <div className="mb-4">
        <label className="block text-primary mb-2">Project Name</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="w-full p-2 border border-gray-300 rounded"
          required
        />
      </div>
      <div className="mb-4">
        <label className="block text-primary mb-2">Description</label>
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="w-full p-2 border border-gray-300 rounded"
          required
        />
      </div>
      <div className="mb-4">
        <label className="block text-primary mb-2">GitHub URL</label>
        <input
          type="url"
          value={githubUrl}
          onChange={(e) => setGithubUrl(e.target.value)}
          className="w-full p-2 border border-gray-300 rounded"
        />
      </div>
      <button type="submit" className="bg-primary text-white p-2 rounded">Add Project</button>
    </form>
  );
}

export default AddProjectForm;