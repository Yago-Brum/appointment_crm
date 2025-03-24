import React, { useEffect, useState } from 'react';
import axiosInstance from '../../axiosInstance';
import './Dashboard.css';

const Dashboard = () => {
  const [totalCustomers, setTotalCustomers] = useState(0);
  const [appointmentsToday, setAppointmentsToday] = useState(0);
  const [recentCustomers, setRecentCustomers] = useState([]);
  const [upcomingAppointments, setUpcomingAppointments] = useState([]);

  useEffect(() => {
    const fetchDashboardData = async () => {
      try {
        const customersResponse = await axiosInstance.get('/clients/');
        setTotalCustomers(customersResponse.data.length);

        const appointmentsResponse = await axiosInstance.get('/appointments/');
        const appointments = appointmentsResponse.data.results || [];
        const today = new Date().toISOString().split('T')[0];

        const todayAppointments = appointments.filter((appointment) =>
          appointment.date_hour.startsWith(today)
        );
        setAppointmentsToday(todayAppointments.length);

        setRecentCustomers(customersResponse.data.slice(0, 4));

        const upcoming = appointments.filter(
          (appointment) => new Date(appointment.date_hour) > new Date()
        );
        setUpcomingAppointments(upcoming);
      } catch (error) {
        console.error('Error fetching dashboard data:', error);
      }
    };

    fetchDashboardData();
  }, []);

  return (
    <div className="dashboard">
      <h2>Dashboard</h2>
      <div className="dashboard-summary">
        <div className="summary-card">
          <h3>Total Customers</h3>
          <p>{totalCustomers}</p>
          <span>+12% from last month</span>
        </div>
        <div className="summary-card">
          <h3>Appointments Today</h3>
          <p>{appointmentsToday}</p>
          <span>3 completed, 5 upcoming</span>
        </div>
      </div>
      <div className="dashboard-details">
        <div className="upcoming-appointments">
          <h3>Upcoming Appointments</h3>
          <ul>
            {upcomingAppointments.slice(0, 3).map((appointment) => (
              <li key={appointment.id}>
                <div>
                  <p><strong>{appointment.clientName}</strong></p>
                  <span>{appointment.serviceType}</span>
                </div>
                <div>
                  <span>
                    {new Date(appointment.date_hour).toLocaleDateString('en-US', {
                      weekday: 'short',
                      year: 'numeric',
                      month: 'short',
                      day: 'numeric',
                    })}{' '}
                    at{' '}
                    {new Date(appointment.date_hour).toLocaleTimeString([], {
                      hour: '2-digit',
                      minute: '2-digit',
                    })}
                  </span>
                  <span>Duration: 30 min</span>
                </div>
              </li>
            ))}
          </ul>
        </div>
        <div className="recent-customers">
          <h3>Recent Customers</h3>
          <p>New customers from the past week</p>
          <ul>
            {recentCustomers.map((customer) => (
              <li key={customer.id}>
                <p>{customer.name}</p>
                <span>Added {Math.floor(Math.random() * 7) + 1} days ago</span>
              </li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
