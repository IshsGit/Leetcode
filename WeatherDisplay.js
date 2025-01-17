import React from 'react';

function WeatherDisplay({ weatherData }) {
  if (!weatherData || !weatherData.main) {
    return <p style={{ textAlign: 'center', color: 'red' }}>Error: Invalid weather data.</p>;
  }

  const { name, main, weather } = weatherData;

  return (
    <div style={displayStyle}>
      <h2>{name}</h2>
      <p>{weather[0].description}</p>
      <p>Temperature: {main.temp}°C</p>
      <p>Feels Like: {main.feels_like}°C</p>
    </div>
  );
}

const displayStyle = {
  textAlign: 'center',
  marginTop: '20px',
  fontSize: '1.2rem',
};

export default WeatherDisplay;
