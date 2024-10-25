import React, { useState } from 'react';
import axios from 'axios';

function CreateRule() {
  const [rule, setRule] = useState('');
  const [message, setMessage] = useState('');

  const createRule = async () => {
    try {
      const response = await axios.post('http://localhost:5000/api/create_rule', { rule });
      setMessage(`Rule created successfully. Rule ID: ${response.data.rule_id}`);
    } catch (error) {
      setMessage(`Error: ${error.response.data.error}`);
    }
  };

  return (
    <div>
      <h2>Create Rule</h2>
      <input
        type="text"
        value={rule}
        onChange={(e) => setRule(e.target.value)}
        placeholder="Enter rule string"
      />
      <button onClick={createRule}>Create Rule</button>
      <p>{message}</p>
    </div>
  );
}

export default CreateRule;
