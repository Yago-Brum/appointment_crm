import React, { useEffect, useState } from 'react';
import axiosInstance from '../../axiosInstance';
import moment from 'moment';
import { FaUserAlt, FaRegCalendarAlt, FaEdit, FaTrash } from 'react-icons/fa'; // Ícones
import './Dashboard.css';

const Dashboard = () => {
  const [appointments, setAppointments] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchAppointments = async () => {
      try {
        setLoading(true);

        const appointmentsResponse = await axiosInstance.get('/appointments/');
        const appointmentsData = appointmentsResponse.data.results || [];

        const clientsResponse = await axiosInstance.get('/clients/');
        const clientsData = clientsResponse.data || [];

        const clientsMap = {};
        clientsData.forEach((client) => {
          clientsMap[client.id] = client;
        });

        const appointmentsWithClientNames = appointmentsData.map((appointment) => ({
          ...appointment,
          clientName: clientsMap[appointment.client] ? clientsMap[appointment.client].name : 'Desconhecido',
        }));

        setAppointments(appointmentsWithClientNames); // Atualizar os agendamentos com o nome do cliente
      } catch (error) {
        setError(error);
        console.error("Erro ao buscar dados:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchAppointments();
  }, []);

  if (loading) return <div className="loading">Loading...</div>;
  if (error) {
    return (
      <div>
        <h2>Error Loading Appointments</h2>
        <p>Error: {error.message}</p>
        <p>Check your network connection and authentication.</p>
      </div>
    );
  }

  return (
    <div className="dashboard">
      <h2>Appointments</h2>
      {appointments.length === 0 ? (
        <p>No appointments found.</p>
      ) : (
        <div className="appointments-list">
          {appointments.map((appointment) => (
            <div className="appointment-card" key={appointment.id}>
              <div className="appointment-header">
                <h3>{appointment.description}</h3>
                <span className="appointment-date">
                  {moment(appointment.date_hour).format('DD MMM YYYY, h:mm A')}
                </span>
              </div>
              <div className="appointment-body">
                <p>
                  <FaUserAlt /> Client: {appointment.clientName}
                </p>
                <p>
                  <FaRegCalendarAlt /> Date: {moment(appointment.date_hour).format('MMMM Do YYYY')}
                </p>
              </div>
              <div className="appointment-actions">
                <button className="edit-btn">
                  <FaEdit /> Edit
                </button>
                <button className="delete-btn">
                  <FaTrash /> Delete
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default Dashboard;
