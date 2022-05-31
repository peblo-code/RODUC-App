import { useEffect } from 'react';
import { Route, Routes, useNavigate } from 'react-router-native';
import { View } from 'react-native';
import AppBar from './AppBar.jsx';
import Home from '../pages/Home.jsx';
import LoginInPage from '../pages/LogIn.jsx';
import NewForm from './NewForm.jsx';
import useUserContext from '../hooks/useUserContext.js';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { NavigationContainer } from '@react-navigation/native';

const Stack = createNativeStackNavigator();

const Main = () => {

    const { user } = useUserContext();  //recuperar datos del contexto
    let navigate = useNavigate(); //funcion para navegar entre paginas

    useEffect(() => {
        user.cod_usuario == 0 ? navigate('/signin') : navigate('/') //si el usuario no esta logueado, redireccionar a la pagina de login
    }, [user.cod_usuario]);

    return(
        <NavigationContainer style={{flex: 1}}>
            {/* { user.cod_usuario > 0 ? <AppBar /> : null } */}
            <Stack.Navigator>
                <Stack.Screen name='Inicio' component={ Home } />
                <Stack.Screen name='Iniciar Sesion' component={ LoginInPage } />
                <Stack.Screen name='Nuevo Formulario' component={ NewForm }/>
            </Stack.Navigator>
        </NavigationContainer>
    )
}

export default Main;