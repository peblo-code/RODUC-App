import { useState, useEffect } from 'react';
import { Route, Routes, useNavigate } from 'react-router-native';
import { View } from 'react-native';
import AppBar from './AppBar.jsx';
import Home from '../pages/Home.jsx';
import LoginInPage from '../pages/LogIn.jsx';

const Main = () => {
    const [isLoggedIn, setIsLoggedIn] = useState(false);
    let navigate = useNavigate();

    useEffect(() => {
        if (!isLoggedIn) {
            navigate('/signin');
        }
    }, []);

    return(
        <View style={{flex: 1}}>
            { isLoggedIn && <AppBar /> }
            <Routes>
                <Route path='/' element={<Home />} />
                <Route path='/signin' element={<LoginInPage />} />
            </Routes>
        </View>
    )
}

export default Main;