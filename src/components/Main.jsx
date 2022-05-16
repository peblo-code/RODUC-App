import { useEffect, useContext } from 'react';
import { Route, Routes, useNavigate } from 'react-router-native';
import { View } from 'react-native';
import { UserContext } from '../context/UserContext.js';
import AppBar from './AppBar.jsx';
import Home from '../pages/Home.jsx';
import LoginInPage from '../pages/LogIn.jsx';

const Main = () => {

    const {user, setUser} = useContext(UserContext)
    
    let navigate = useNavigate();

    useEffect(() => {
        if (!user.id_usuario) {
            navigate('/signin');
        }
    }, []);

    return(
        <View style={{flex: 1}}>
            { user.id_usuario && <AppBar /> }
            <Routes>
                <Route path='/' element={<Home />} />
                <Route path='/signin' element={<LoginInPage />} />
            </Routes>
        </View>
    )
}

export default Main;