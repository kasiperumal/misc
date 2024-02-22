import React, { useState } from 'react';
import { Pie } from 'react-chartjs-2';
import { Chart, ArcElement, Tooltip, Legend } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import "chart.js-plugin-labels-dv";
import { useNavigate } from 'react-router-dom';

// Register the components
Chart.register(ArcElement, Tooltip, Legend,ChartDataLabels);

const PieChartComponent = () => {
  // const [tableData, setTableData] = useState(null);
  const navigate = useNavigate();

  const data = {
    labels: ['Technical Glitches', 'Password Issues', 'Fraud Victims', 'Duplicate Profiles', 'Biometric Issues', 'RSA Device', 'OTP Issues', 'Accessibility Denial'],
    datasets: [
      {
        data: [15.3, 21.1, 2.9, 4.2, 2.4, 1.8, 19.8, 32.6],      backgroundColor: [
          "#FDBAAB",
          "#FFEBA5",
          "#99C3E1",
          "#90D1C5",
          "#66AAEE",
          "#33EEFF",
          "#33aaaa",
          "#cccccc"
        ]
      },
    ],
  };

  const options = {
    plugins: {
      datalabels: {
        // color: '#fff',
        textAlign: 'center',
        responsive: true,
        maintainAspectRatio: true, // or false, depending on your layout needs
        font: {
          size: 10,
          weight: 'bold',
        },
        anchor: 'middle', // Anchors the labels to the end of the arcs
        align: 'end', // Aligns the labels outside of the arcs
        offset:93, // Adjusts the distance of the labels from the arcs
        formatter: (value, context) => {
          return `${context.chart.data.labels[context.dataIndex]}\n${value}%`;
        },
      },
      legend: {
        display: false,
      },
      title: {
        display: true,
        text: "VOC Report Topic Modelling"
      }
    },
    onClick: (evt, element) => {
      if (element.length > 0) {
        navigate('/graph');
      }
    },
  };

return (
  <div style={{ display: 'flex', width: '100%', justifyContent: 'center' }}>
    <div style={{width: '50%', height: '50%' }}>
      <Pie data={data} options={options} plugins={[ChartDataLabels]} />
    </div>
  </div>
);
};

export default PieChartComponent;
