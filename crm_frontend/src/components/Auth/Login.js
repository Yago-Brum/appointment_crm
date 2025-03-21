import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './Login.css';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState(''); // Add email for registration
  const [isRegistering, setIsRegistering] = useState(false); // Control registration mode
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');
    try {
      console.log("Attempting login with:", { username, password }); // Log login data
      const response = await axios.post('http://127.0.0.1:8000/auth/login/', { username, password });
      console.log("Login response:", response.data); // Log the entire response
      localStorage.setItem('token', response.data.access);
      navigate('/dashboard');
    } catch (error) {
      handleError(error);
    }
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    setError('');
    try {
      const response = await axios.post('http://127.0.0.1:8000/auth/register/', { username, password, email });
      // Handle successful registration (e.g., redirect to login)
      alert('Registration successful! Please log in.');
      setIsRegistering(false); // Switch back to login mode
    } catch (error) {
      handleError(error);
    }
  };

  const handleError = (error) => {
    console.error('Error:', error);
    if (error.response && error.response.data) {
      setError(error.response.data.detail || error.response.data.non_field_errors?.[0] || 'Registration/Login failed.');
    } else {
      setError('Network error. Please try again later.');
    }
  };

  return (
    <div className="login-container">
      <div className="login-box">
        <h2 className="login-title">{isRegistering ? 'Register' : 'Login'}</h2>
        <form onSubmit={isRegistering ? handleRegister : handleLogin} className="login-form">
          <div className="input-group">
            <label htmlFor="username">Username</label>
            <input type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)} required />
          </div>
          <div className="input-group">
            <label htmlFor="password">Password</label>
            <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
          </div>
          {isRegistering && (
            <div className="input-group">
              <label htmlFor="email">Email</label>
              <input type="email" id="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
            </div>
          )}
          {error && <div className="error-message">{error}</div>}
          <button type="submit" className="login-button">
            {isRegistering ? 'Register' : 'Login'}
          </button>
          <button type="button" onClick={() => setIsRegistering(!isRegistering)} className="switch-button">
            {isRegistering ? 'Go back to Login' : 'Register instead'}
          </button>
        </form>
      </div>
    </div>
  );
};

export default Login;
