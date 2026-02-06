import { useState } from "react";
import { analyzeCity } from "./api";

export default function Dashboard() {
  const [result, setResult] = useState(null);

  async function runAnalysis() {
    const data = await analyzeCity({
      population: 120000,
      green_space_pct: 35,
      public_transport: 70,
      carbon_emissions: 25,
      jobs_created: 3000,
      local_business_boost: 60,
    });
    setResult(data);
  }

  return (
    <div>
      <h2>City Development Assistant</h2>
      <button onClick={runAnalysis}>Run Analysis</button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}
