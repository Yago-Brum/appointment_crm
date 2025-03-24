import React from 'react';
import { Outlet } from 'react-router-dom';
import Sidebar from '../Sidebar/Sidebar';

const MainLayout = () => {
  return (
    <div className="flex h-screen">
      {/* Sidebar fixa */}
      <Sidebar />

      {/* Conteúdo principal ocupando o espaço restante */}
      <div className="flex-1 p-4 overflow-auto">
        <Outlet />
      </div>
    </div>
  );
};

export default MainLayout;
