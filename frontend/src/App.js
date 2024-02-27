import React from "react";
import { Routes, Route } from 'react-router-dom';
//import Link from 'react-router-dom';
import Search from './components/Search';
// import SignUp from './components/SignUp';
// import { Navbar } from './components/Navbar';



function App() { 
  return (
    <div>
      {/* <Navbar></Navbar> */}
      <Routes>
        <Route path='/' element={<Search/>}></Route>

      </Routes>

    </div>
  );
}

export default App;
