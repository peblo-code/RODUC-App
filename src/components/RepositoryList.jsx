import { Text, FlatList, View } from 'react-native';
import { useEffect, useState } from 'react';
import repositories from '../data/repositories.js';
import RepositoryItem from './RepositoryItem';
import useUserContext from '../hooks/useUserContext.js';
import axios from 'axios';

const RepositoryList = () => {

    const { URL, user } = useUserContext();
    const initialState = {
        carrera: '',
        asignatura: '',
        curso: '',
        plan: '',
        fecha: '',
        horaInicio: '',
        horaFin: '',
    }
    const [reportes, setReportes] = useState([]);
    const [asignaturas, setAsignaturas] = useState([]);
    const [carreras, setCarreras] = useState([]);
    const [planes, setPlanes] = useState([]);
    const [parsedReportes, setParseReportes] = useState([]);

    //Funcion para obtener una lista especifica de la API
    const getAPIData = (response, list, setList) => {
        const res = JSON.parse(response.data[list])
        setList(res.map(field => field))
    }

    useEffect(() => {
        axios.get(`${URL}/historial_reportes/${user.cod_usuario}`)
        .then(response => {
            getAPIData(response, 'lista_cabeceras', setReportes)
            getAPIData(response, 'lista_asignaturas', setAsignaturas)
            getAPIData(response, 'lista_carreras', setCarreras)
            getAPIData(response, 'lista_planes', setPlanes)
        })
        .catch(error => console.log(error))
    },[])

    return(
        <FlatList 
            data={reportes}
            ItemSeparatorComponent={() => <View style={{ borderColor: "gray", borderWidth: .5, marginHorizontal: 15 }}/>}
            renderItem={({ item: repo }) => (
                <RepositoryItem {...repo} />
            )}
        >
        </FlatList>
    )
}

export default RepositoryList;