import React, { useState, useEffect, useContext } from 'react';
import { addProject } from '../api/project';
import { UserContext } from '../context/UserContext';
import { getUserProfile } from '../api/auth';

function AddProjectForm() {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [githubUrl, setGithubUrl] = useState('');
  const [isAdmin, setIsAdmin] = useState(false);
  const { user } = useContext(UserContext);

  useEffect(() => {
    const fetchUserProfile = async () => {
      if (user) {
        try {
          const profileData = await getUserProfile(localStorage.getItem('token'));
          setIsAdmin(profileData.is_admin); 
        } catch (error) {
          console.error('Error fetching user profile:', error);
        }
      }
    };

    fetchUserProfile();
  }, [user]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await addProject({ name, description, github_url: githubUrl });
      // Очистка формы после успешной отправки
      setName('');
      setDescription('');
      setGithubUrl('');
      alert('Project added successfully!');
    } catch (error) {
      console.error('Error adding project:', error);
    }
  };

  if (!isAdmin) {
    return (
      <div className="container mx-auto p-8 fade-in">
        <h2 className="text-2xl font-bold mb-4 text-primary">Access Denied</h2>
        <p>You do not have permission to add projects.</p>
      </div>
    );
  }

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