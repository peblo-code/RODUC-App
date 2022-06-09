import { StyleSheet, Alert } from 'react-native';
import Home from '../pages/Home.jsx';
import LoginInPage from '../pages/LogIn.jsx';
import NewForm from './NewForm.jsx';
import HistoryList from './HistoryList.jsx';
import About from '../pages/About.jsx';
import UserView from '../pages/UserView.jsx';
import TouchIcon from './TouchIcon.jsx';
import useUserContext from '../hooks/useUserContext.js';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { NavigationContainer } from '@react-navigation/native';

const Stack = createNativeStackNavigator();

const Main = () => {
    const { user, closeSession } = useUserContext();  //recuperar datos del contexto

    const createTwoButtonAlert = () =>
        Alert.alert('Cerrar Sesión', '¿Estas seguro/a de cerrar tu sesión?', [
            {
                text: 'Cancelar',
                style: 'cancel',
            },
            { text: 'Sí!', onPress: () => closeSession() },
        ]);

    const styles = StyleSheet.create({
        headerStyle: {
            backgroundColor: '#0d3498',
        },
        headerTintColor: '#fff',
        headerTitleStyle: {
            fontWeight: 'bold',
        },
        headerRight: () => (
            <TouchIcon
                name="sign-out"
                size={24}
                color="#fff"
                onPress={() => createTwoButtonAlert()} 
            />
        ),
    });

    return (
        <NavigationContainer style={{ flex: 1 }}>
            {
                user.cod_usuario == 0 ? <LoginInPage /> :
                    <Stack.Navigator>
                        <Stack.Screen
                            name='Inicio'
                            component={Home}
                            options={styles} />
                        <Stack.Screen
                            name='Iniciar Sesion'
                            component={LoginInPage}
                            options={styles} />
                        <Stack.Screen
                            name='Nuevo Informe'
                            component={NewForm}
                            options={styles} />
                        <Stack.Screen
                            name='Historial'
                            component={HistoryList}
                            options={styles} />
                        <Stack.Screen
                            name='Mi Perfil'
                            component={UserView}
                            options={styles} />
                            <Stack.Screen
                            name='Acerca de'
                            component={About}
                            options={styles} />
                    </Stack.Navigator>
            }
        </NavigationContainer>
    )

}


export default Main;