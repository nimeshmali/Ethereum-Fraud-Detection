import React, { useState } from 'react'
import Meter from "../Meter/Meter"
import Invalid from '../Invalid'
import Valid from '../Valid';
import Loading from '../Loading';
//CSS Files
// import "./input.css"


const Input = (props) => {

  const [address, setAddress] = useState("");
  const [fraud, setFraud] = useState(-2)
  const data = props.data;
  const [ld, setld] = useState(false);

  const handlePrediction = async () => {
    setld(true);
    await fetch("http://127.0.0.1:5000/predict", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      body: JSON.stringify(address)
    }).then(async (res) => {
      const vari = await res.json();
      console.log(vari.result)
      setFraud(vari.result);
      console.log(fraud);
    })
    setld(false);
    // console.log(fraud); 
  }


  return (
    <div>
      <h1 className='text-white text-[3rem] text-center font-bold Poppins my-[2em]'>Ethereum Fraud Detection</h1>
      <div className='flex justify-center w-full Poppins'>
        <input className='w-1/2 p-2 rounded-sm input font-bold bg-slate-800 text-white' type="text" placeholder='Address' onChange={(e) => { setAddress(JSON.stringify(e.target.value)) }} required="required" />
        <button className='mx-2 p-2 text-white bg-cyan-600 rounded md font-bold' onClick={handlePrediction} >Predict</button>
      </div>
      {ld ? <Loading /> : fraud == -2 ? <Valid /> : fraud != -1 ? < Meter fraud={fraud} /> : <Invalid />}
    </div>
  )
}

export default Input