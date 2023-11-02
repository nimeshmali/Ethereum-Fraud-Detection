import React from 'react'
import ReactSpeedometer from "react-d3-speedometer"
import { BiUpArrow } from "react-icons/bi"

let threat = "";

const Meter = ({ fraud }) => {
  if (fraud <= 0.4) {
    threat = "Fraudulent account";
  }
  else if (fraud >= 0.6) {
    threat = "Safe account";
  }
  console.log(threat);

  return (
    <div className='mt-[4em] flex flex-col items-center w-full Poppins meter'>
      {/* <div className='w-[100%] flex flex-col items-center'>
        <div className='Poppins w-[50%] h-[3em] rounded-full flex justify-between items-center bg-gradient-to-r from-green-400 to-red-400'>
        <h1 className='pl-4'>0</h1>
        <h1>0.5</h1>
        <h1 className='pr-4'>1</h1>
        </div>
        </div>      
        <div className='w-[70%]'>
            <BiUpArrow className={`text-[25px] ml-[${temp}%] text-white`}/>
            <h1 className={`text-white ml-[${temp}%]`}>{temp2}</h1>
        </div> */}
      <ReactSpeedometer
        width={500}
        height={300}
        minValue={0}
        maxValue={1}
        value={fraud}
        currentValueText="Fraud Index"
        customSegmentLabels={[
          {
            text: "Fraudulent",
            position: "INSIDE",
            color: "black",
          },
          {
            text: "Unsafe",
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
            text: "Safe",
            position: "INSIDE",
            color: "black",
          },
          {
            text: "Very Safe",
            position: "INSIDE",
            color: "black",
          },



        ]}
      />
      <h3 className='text-white text-center font-bold Poppins'>{threat}</h3>


    </div>
  )
}

export default Meter;