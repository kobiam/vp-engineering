import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [data, setData] = useState('');

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get('http://localhost:5000/v1/data');
      setData(response.data.message);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div style={{ textAlign: 'center', marginTop: '50px' }}>
      <h1>Data from Python Backend:</h1>
      <p>{data}</p>
      <button onClick={fetchData}>Refresh Data</button>
    </div>
  );
};

export default App;
