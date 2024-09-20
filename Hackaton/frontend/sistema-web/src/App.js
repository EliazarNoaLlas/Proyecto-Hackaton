import React from 'react';
import MapView from './components/MapView';
import EmergencyInfo from './components/EmergencyInfo';
import './styles/App.css';

const App = () => {
  return (
    <div className="App">
      <header>
        <h1>Monitoreo y Prevención de Incendios Forestales en Perú y Bolivia</h1>
      </header>
      <main>
        <MapView />
        <EmergencyInfo />
      </main>
    </div>
  );
};

export default App;
