import React, { useState } from 'react';
import { Pie } from 'react-chartjs-2';
// Import Chart.js components
import { Chart, ArcElement, Tooltip, Legend } from 'chart.js';
// import 'chartjs-plugin-datalabels'; // Import the datalabels plugin
import ChartDataLabels from 'chartjs-plugin-datalabels';
// import "chart.js-plugin-labels-dv";
import "./Chart.css";

// Register the components
Chart.register(ArcElement, Tooltip, Legend);
Chart.register(ChartDataLabels);

// import axios from 'axios';

const PieChartComponent = () => {
  const [tableData, setTableData] = useState(null);

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
        const index = element[0].index;
        const label = data.labels[index];
        loadTableData(label);
      }
    },
  };

  const loadTableData = async (label) => {
    alert('You clicked on ' + label);
    // try {
    //   const response = await axios.get(`/your-backend-endpoint/${label}`);
    //   setTableData(response.data);
    // } catch (error) {
    //   console.error('Error fetching data: ', error);
    // }
  };

//   return (
//     <div style={{
//       width: '600px', /* Increase width */
//       height: '600px', /* Increase height */
//       display: 'flex',
//       justifyContent: 'center',
//       alignItems: 'center',
//       height: '100vh' // This makes the container take up the full viewport height
//     }}>
//       <div style={{width: '400px', height: '400px'}}>
//         <Pie data={data} options={options} plugins={[ChartDataLabels]} />
//         {/* Render your table data here */}
//       </div>
//     </div>
//   );
// };

// return (
//   <div style={{
//     // width: '600px', /* Increase width */
//     // height: '600px', /* Increase height */
//     display: 'flex',
//     justifyContent: 'center',
//     alignItems: 'center',
//     height: '100vh' // This makes the container take up the full viewport height
//     // width: 'au' // This makes the container take up the full viewport height
//   }}>
//   <div className="chart-container">
//     <Pie data={data} options={options} plugins={[ChartDataLabels]} />
//   </div>
//   </div>
// );

// return (
  // <div className="chart-container">
  //   <Pie data={data} options={options} plugins={[ChartDataLabels]} />
  // </div>
// );

return (
  <div style={{ display: 'flex', width: '100%', justifyContent: 'center' }}>
    <div style={{width: '50%', height: '50%' }}>
      <Pie data={data} options={options} plugins={[ChartDataLabels]} />
    </div>
  </div>
);
};

export default PieChartComponent;
