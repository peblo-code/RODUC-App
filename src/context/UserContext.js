import { createContext, useState, useEffect } from 'react'
import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';

export const UserContext = createContext();

const initialState = {  //valores iniciales
    cod_usuario: 0,
    nombre_usuario: '',
    nombres_del_usuario: '',
    apellidos_del_usuario: '',
}

const storeData = async (value) => {    //funcion para persistir datos
    try {
      const jsonValue = JSON.stringify(value)
      await AsyncStorage.setItem('@storage_Key', jsonValue)
    } catch (e) {
      // saving error
    }
}


const getData = async () => {   //funcion para recuperar datos
    try {
        const jsonValue = await AsyncStorage.getItem('@storage_Key')
        return jsonValue != null ? JSON.parse(jsonValue) : null;
    } catch(e) {
        // error reading value
    }
}

export const UserProvider = ({ children }) => {

    const [user, setUser] = useState(initialState); //estado del usuario
    const [error, setError] = useState(false); //estado del error
    const [isLoading, setIsLoading] = useState(false); //estado del loading

    const closeSession = () => {    //funcion para cerrar sesion
        storeData(initialState);
        setUser(initialState);
    }

    useEffect(() => {
        getData().then(data => {    //recuperar datos
            if(data != null){
                setUser(data);
                console.log(data)
            }
        })
    }, [])

    function Auth(values) {
        axios.get(`http://26.247.235.244:8000/restapi/lista_usuarios/${values.email}`)
        .then(response => {
            if(response.data.nombre_usuario.length > 0) {
                if(response.data.nombre_usuario === values.email && response.data.contraseña === values.password) { 
                    setUser(response.data) //si el usuario existe, guardar datos en el contexto
                    storeData(response.data) //persistir datos
                } else {
                    console.log('Login Incorrecto')
                }
            }
        })
        .catch(error => {
            console.log(error);
            setError(true);
        });
        setIsLoading(false);
    }
    

    return (
        <UserContext.Provider value={{
            user,
            isLoading,
            error,
            setError,
            setUser,
            Auth,
            closeSession
        }}>
            { children }
        </UserContext.Provider>
    )
}