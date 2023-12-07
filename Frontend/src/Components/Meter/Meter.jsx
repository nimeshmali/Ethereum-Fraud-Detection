import React from 'react'
import ReactSpeedometer from "react-d3-speedometer"

let threat = "";

const Meter = (props) => {
  if (props.fraud <= 0.4) {
    threat = "Fraudulent account";
  }
  else if (props.fraud >= 0.6) {
    threat = "Safe account";
  }
  console.log(threat);
  let prob = (1 - props.fraud).toFixed(3);


  return (
    <div className='mt-[4em] flex flex-col items-center w-full Poppins meter'>
      <ReactSpeedometer
        width={500}
        height={300}
        minValue={0}
        maxValue={1}
        value={prob}
        currentValueText="Fraud Index"
        segmentColors={['#6ad72d', '#aee228', '#ecdb23', '#f6961e', '#ff471a']}
        customSegmentLabels={[


          {
            text: "Very Safe",
            position: "INSIDE",
            color: "black",
            backgroundColor: "#fff"
          },
          {
            text: "Safe",
            position: "INSIDE",
            color: "black",
          },
          {
            text: "Uncertain",
            position: "INSIDE",
            color: "black",
            fontSize: "15px",
          },
          {
            text: "Unsafe",
            position: "INSIDE",
            color: "black",
          },
          {
            text: "Fraudulent",
            position: "INSIDE",
            color: "black",
          },
        ]}
      />
      <h3 className='text-white text-center font-bold Poppins'>Probablity of this Account being Fraudulent is {prob}</h3>
    </div>
  )
}

export default Meter;