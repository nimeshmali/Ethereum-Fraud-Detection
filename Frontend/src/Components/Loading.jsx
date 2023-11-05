
import React from 'react';
import ReactLoading from 'react-loading';

const Loading = ({ type, color }) => (
    <div className="pt-8 flex justify-center w-full Poppins">
        <ReactLoading type={"cubes"} color={"#ffffff"} height={150} width={150} />
    </div >
);

export default Loading;