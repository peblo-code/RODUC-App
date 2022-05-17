import { createContext, useState } from 'react'
import axios from 'axios';

export const UserContext = createContext();

const initialState = {
    cod_usuario: 1,
    nombre_usuario: '',
    nombres_del_usuario: 'Pablo Vilmar',
    apellidos_del_usuario: 'Benedix Cañete',
}

export const UserProvider = ({ children }) => {

    const [user, setUser] = useState(initialState);

    function Auth(values) {
        axios.get(`http://26.247.235.244:8000/restapi/lista_usuarios/${values.email}`)
        .then(response => {
            if(response.data.nombre_usuario.length > 0) {
                response.data.nombre_usuario === values.email && response.data.contraseña === values.password ? setUser(response.data) : console.log('Login Incorrecto')
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
            Auth
        }}>
            { children }
        </UserContext.Provider>
    )
}