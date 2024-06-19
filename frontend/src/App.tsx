import React from 'react';
import logo from './logo.svg';
import './App.css';
import Livros from './components/Books';

const App: React.FC = () => {
  return (
    <div className="App">
      <Livros />
    </div>
  );
};

export default App;