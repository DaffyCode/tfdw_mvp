import React from 'react';
import { Routes, Route } from 'react-router-dom';
import SpendenTestRequest from './components/home/SpendenTestRequest';
import Login from './components/Login';
import DonationDetails from './components/DonationDetails';
import Layout from './components/Layout';
import Home from './components/home';


function App() {
    return (

        <Routes>
            <Route path='/' element={<Layout />}>
                <Route index element={< Home />} />
                <Route path='/login' element={<Login />}></Route>
                <Route path='/donation' element={<DonationDetails />}></Route>
                <Route path='/spenden' element={<SpendenTestRequest />}></Route>
            </Route>
        </Routes>

    );
}

export default App;