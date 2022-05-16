import { createContext, useState } from 'react'

export const UserContext = createContext();

const initialState = {
    id_usuario: '',
    nombre_usuario: '',
    nombres_usuario: '',
    apellidos_usuario: '',
}

export const UserProvider = ({ children }) => {

    const [user, setUser] = useState(initialState);

    return (
        <UserContext.Provider value={{
            user,
            setUser
        }}>
            { children }
        </UserContext.Provider>
    )
}