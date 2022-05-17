import { useEffect, useState } from 'react';
import { Route, Routes, useNavigate } from 'react-router-native';
import { View } from 'react-native';
import AppBar from './AppBar.jsx';
import Home from '../pages/Home.jsx';
import LoginInPage from '../pages/LogIn.jsx';
import useUserContext from '../hooks/useUserContext.js';

const Main = () => {

    const { user } = useUserContext();  //recuperar datos del contexto
    let navigate = useNavigate(); //funcion para navegar entre paginas

    useEffect(() => {
        user.cod_usuario == 0 ? navigate('/signin') : navigate('/') //si el usuario no esta logueado, redireccionar a la pagina de login
    }, [user.cod_usuario]);

    return(
        <View style={{flex: 1}}>
            { user.cod_usuario > 0 ? <AppBar /> : null }
            <Routes>
                <Route path='/' element={<Home />} />
                <Route path='/signin' element={<LoginInPage />} />
            </Routes>
        </View>
    )
}

export default Main;