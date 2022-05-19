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
    const [error, setError] = useState(''); //estado del error

    const closeSession = () => {    //funcion para cerrar sesion
        storeData(initialState);
        setUser(initialState);
    }

    useEffect(() => {
        getData().then(data => {    //recuperar datos
            if(data != null){
                setUser(data);
            }
        })
    }, [])

    function Auth({ username, password }) {
        const URL = 'http://26.247.235.244:8000/restapi'; //url del servidor

        axios.get(`${URL}/lista_usuarios/${username}`)
        .then(response => {
            if(response.data.nombre_usuario.length > 0) {
                if(response.data.nombre_usuario === username && response.data.contraseña === password) {

                    const codUser = response.data.cod_usuario;  //recuperar codigo del usuario
                    axios.get(`http://26.247.235.244:8000/restapi/usuario_rol/${codUser}`)
                    .then(responseCod => {
                        if(responseCod.data.cod_rol_usuario == 2) {   //si es profesor
                            setUser(response.data) //si el usuario existe y es profesor, guardar datos en el contexto
                            storeData(response.data) //persistir datos
                        } else {
                            setError('El usuario no es un profesor.') //si el usuario no es profesor, mostrar error
                        }
                    })
                    .catch(error => {
                        console.log(error);
                    })

                } else {
                    setError('Nombre de usuario o contraseña incorrectas.') //si los datos son incorrectos, mostrar error
                }
            }
        })
        .catch(error => {
            if(error.response.status == 404) {
                setError('El usuario no existe.') //si el usuario no existe, mostrar error
            } else {
                setError('Error al conectar con el servidor.') //si hay error, mostrar error
            }
        });
    }
    

    return (
        <UserContext.Provider value={{
            user,
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