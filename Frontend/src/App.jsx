import React, { useState, useEffect } from "react";

//Components
import Input from "./Components/Input/Input";
import Background from "./Components/Background/Background";

//CSS files
import "./App.css";

function App() {
  const [data, setdata] = useState({});

  console.log(data)

  return (
    <div className="App">
      <Background className="back" />
      <div className="cont">
        <Input data={data} />
      </div>

    </div>);
}

export default App;
