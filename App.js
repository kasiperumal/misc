import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import PieChartComponent from './Chart';
import Graph from './Graph';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/pie-chart" element={<PieChartComponent />} />
        <Route path="/graph" element={<Graph />} />
        <Route path="/" element={<Navigate replace to="/pie-chart" />} />
      </Routes>
    </Router>
  );
}

export default App;
