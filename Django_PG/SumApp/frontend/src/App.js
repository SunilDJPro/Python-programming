//frontend/src/App.js
import React, { useState } from 'react';
import { calculateSum } from './services/api';
import './App.css';

function App() {
  // State for input values and result
  const [num1, setNum1] = useState('');
  const [num2, setNum2] = useState('');
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    
    // Validate inputs
    if (num1 === '' || num2 === '') {
      setError('Please enter both numbers');
      return;
    }

    try {
      setLoading(true);
      
      // Call the API service
      const data = await calculateSum(parseInt(num1), parseInt(num2));
      
      // Update result state
      setResult(data.result);
      setLoading(false);
    } catch (err) {
      setError(err.response?.data?.error || 'An error occurred');
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Simple Sum App</h1>
      </header>
      
      <main className="App-main">
        <form onSubmit={handleSubmit} className="sum-form">
          <div className="input-group">
            <div className="input-box">
              <input
                type="number"
                value={num1}
                onChange={(e) => setNum1(e.target.value)}
                placeholder="Enter number"
                aria-label="First number"
              />
            </div>
            
            <div className="operator">+</div>
            
            <div className="input-box">
              <input
                type="number"
                value={num2}
                onChange={(e) => setNum2(e.target.value)}
                placeholder="Enter number"
                aria-label="Second number"
              />
            </div>
            
            <div className="equals">=</div>
            
            <div className="result-box">
              {loading ? (
                <div className="loading">...</div>
              ) : (
                <div className="result">{result !== null ? result : ''}</div>
              )}
            </div>
          </div>

          <button type="submit" className="calculate-btn">
            Calculate
          </button>
          
          {error && <div className="error-message">{error}</div>}
        </form>
      </main>
    </div>
  );
}

export default App;