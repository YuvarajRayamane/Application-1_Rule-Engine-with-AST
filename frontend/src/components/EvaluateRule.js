import React, { useState } from 'react';
import axios from 'axios';

function EvaluateRule() {
  const [ruleId, setRuleId] = useState('');
  const [data, setData] = useState('');
  const [result, setResult] = useState('');

  const evaluateRule = async () => {
    try {
      const jsonData = JSON.parse(data);
      const response = await axios.post('http://localhost:5000/api/evaluate_rule', {
        rule_id: ruleId,
        data: jsonData,
      });
      setResult(`Evaluation Result: ${response.data.result}`);
    } catch (error) {
      setResult(`Error: ${error.response.data.error}`);
    }
  };

  return (
    <div>
      <h2>Evaluate Rule</h2>
      <input
        type="text"
        value={ruleId}
        onChange={(e) => setRuleId(e.target.value)}
        placeholder="Enter rule ID"
      />
      <textarea
        value={data}
        onChange={(e) => setData(e.target.value)}
        placeholder='Enter data JSON (e.g. {"age": 35, "department": "Sales", "salary": 60000})'
      />
      <button onClick={evaluateRule}>Evaluate Rule</button>
      <p>{result}</p>
    </div>
  );
}

export default EvaluateRule;
