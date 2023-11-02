import React, { useState, useEffect } from "react";

//Components
import Input from "./Components/Input/Input";
import Background from "./Components/Background/Background";

//CSS files
import "./App.css";

function App() {
  const [data, setdata] = useState({});

  // // Using useEffect for single rendering
  // useEffect(() => {
  //   // Using fetch to fetch the api from
  //   // flask server it will be redirected to proxy
  //   fetch("http://127.0.0.1:5000/data").then((res) =>
  //     res.json().then((data) => {
  //       // Setting a data from api
  //       console.log(data);
  //       setdata({
  //         Output: data.Output
  //       });
  //     })
  //   );
  // }, []);

  console.log(data)

  return (
  <div className="App">
    <Background className="back"/>
    <div className="cont">
    <Input data = {data}/>
    </div>
   
  </div>);
}

export default App;
