import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './components/Auth/Login';
import Dashboard from './components/Dashboard/Dashboard';
import Calendar from './components/Calendar/Calendar';
import Clients from './components/Clients/Clients';
import Appointments from './components/Appointments/Appointments';
import ProtectedRoute from './components/ProtectedRoute';
import MainLayout from './components/Layout/MainLayout'; // Novo layout com Sidebar


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Navigate to="/login" />} />
        <Route path="/login" element={<Login />} />

        {/* Rotas protegidas dentro do layout */}
        <Route 
          path="/" 
          element={<ProtectedRoute><MainLayout /></ProtectedRoute>}
        >
          <Route path="dashboard" element={<Dashboard />} />
          <Route path="clients" element={<Clients />} />
          <Route path="calendar" element={<Calendar />} />
          <Route path="appointments" element={<Appointments />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;
