import { createContext, useState, useEffect } from 'react'
import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';

export const UserContext = createContext();

const initialState = {
    cod_usuario: 0,
    nombre_usuario: '',
    nombres_del_usuario: '',
    apellidos_del_usuario: '',
}

const storeData = async (value) => {
    try {
      const jsonValue = JSON.stringify(value)
      await AsyncStorage.setItem('@storage_Key', jsonValue)
    } catch (e) {
      // saving error
    }
}


const getData = async () => {
    try {
        const jsonValue = await AsyncStorage.getItem('@storage_Key')
        return jsonValue != null ? JSON.parse(jsonValue) : null;
    } catch(e) {
        // error reading value
    }
}

export const UserProvider = ({ children }) => {

    const [user, setUser] = useState(initialState);

    const closeSession = () => {
        storeData(initialState);
        setUser(initialState);
    }

    useEffect(() => {
        getData().then(data => {
            if(data != null){
                setUser(data);
            }
        })
    }, [])

    function Auth(values) {
        axios.get(`http://26.247.235.244:8000/restapi/lista_usuarios/${values.email}`)
        .then(response => {
            if(response.data.nombre_usuario.length > 0) {
                if(response.data.nombre_usuario === values.email && response.data.contraseña === values.password) { 
                    setUser(response.data)
                    storeData(response.data)
                } else {
                    console.log('Login Incorrecto')
                }
            }
        })
    
        .catch(error => {
            console.log(error);
        });
    }
    

    return (
        <UserContext.Provider value={{
            user,
            setUser,
            Auth,
            closeSession
        }}>
            { children }
        </UserContext.Provider>
    )
}