import React, { useState, useEffect } from 'react';
import axiosInstance from '../../axiosInstance';
import moment from 'moment';

const NewAppointmentModal = ({ isOpen, onClose, onAppointmentCreated }) => {
  const [description, setDescription] = useState('');
  const [dateHour, setDateHour] = useState('');
  const [client, setClient] = useState('');
  const [clients, setClients] = useState([]);

  useEffect(() => {
    const fetchClients = async () => {
      try {
        const response = await axiosInstance.get('/clients/');
        setClients(response.data || []);
      } catch (error) {
        console.error('Erro ao buscar clientes:', error);
      }
    };

    fetchClients();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axiosInstance.post('/appointments/', {
        description,
        date_hour: moment(dateHour).toISOString(),
        client,
      });

      onAppointmentCreated(); // Atualiza a lista de appointments
      onClose(); // Fecha o modal
    } catch (error) {
      console.error('Erro ao criar o agendamento:', error);
    }
  };

  if (!isOpen) return null; // Não renderiza o modal se estiver fechado

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <h2>New Appointment</h2>
        <form onSubmit={handleSubmit}>
          <label>Description:</label>
          <input
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
          />

          <label>Date & Time:</label>
          <input
            type="datetime-local"
            value={dateHour}
            onChange={(e) => setDateHour(e.target.value)}
            required
          />

          <label>Client:</label>
          <select value={client} onChange={(e) => setClient(e.target.value)} required>
            <option value="">Select a client</option>
            {clients.map((c) => (
              <option key={c.id} value={c.id}>
                {c.name}
              </option>
            ))}
          </select>

          <div className="modal-buttons">
            <button type="submit" className="save-btn">Save</button>
            <button type="button" className="cancel-btn" onClick={onClose}>Cancel</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default NewAppointmentModal;
