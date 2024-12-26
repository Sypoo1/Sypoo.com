import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home.jsx';
import Projects from './pages/Projects';
import ProjectDetail from './pages/ProjectDetail';
import AddProjectForm from './components/AddProjectForm';
import { UserProvider } from './context/UserContext';

function App() {
  return (
    <UserProvider>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/projects" element={<Projects />} />
          <Route path="/projects/:projectId" element={<ProjectDetail />} />
          <Route path="/add-project" element={<AddProjectForm />} />
        </Routes>
      </Router>
    </UserProvider>
  );
}

export default App;