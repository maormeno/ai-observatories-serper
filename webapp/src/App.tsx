import React from 'react';
import LinkDetail from './components/LinkDetail';
import Links from './components/Links';
import { Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div>
      <Routes>
        <Route path="/" element={<Links />} />
        <Route path="/1" element={<LinkDetail />} />
      </Routes>
    </div>
  );
}

export default App;
