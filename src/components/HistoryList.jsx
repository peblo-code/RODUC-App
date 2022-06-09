import { Text, FlatList, View } from 'react-native';
import { useEffect, useState } from 'react';
import HistoryItem from './HistoryItem';
import useUserContext from '../hooks/useUserContext.js';
import axios from 'axios';

const HistoryList = () => {

    const { URL, user } = useUserContext();
    const initialState = [{
        carrera: '',
        asignatura: '',
        curso: '',
        plan: '',
        fecha: '',
        horaInicio: '',
        horaFin: '',
    }]
    const [reportes, setReportes] = useState([]);
    const [asignaturas, setAsignaturas] = useState([]);
    const [carreras, setCarreras] = useState([]);
    const [tipoClase, setTipoClase] = useState([]);
    const [planes, setPlanes] = useState([]);
    const [parsedReportes, setParseReportes] = useState(initialState);

    //Funcion para obtener una lista especifica de la API
    const getAPIData = (response, list, setList) => {
        const res = JSON.parse(response.data[list])
        setList(res.map(field => field))
    }

    useEffect(() => {
        axios.get(`${URL}/historial_reportes/${user.cod_usuario}`)
        .then(response => {
            getAPIData(response, 'lista_cabeceras', setReportes)
        })
        .catch(error => console.log(error))
        axios.get(`${URL}/listaFacultades_Carreras/${user.cod_usuario}`)
        .then(response => {
            getAPIData(response, 'lista_asignaturas', setAsignaturas)
            getAPIData(response, 'lista_carreras', setCarreras)
            getAPIData(response, 'lista_tipo_clase', setTipoClase)
            getAPIData(response, 'lista_planes', setPlanes)
            
        })
        .catch(error => console.log(error))
    },[])

    useEffect(() => {
        setParseReportes(reportes.map(reporte => {
            const asignatura = asignaturas.find(asignatura => asignatura.pk === reporte.fields.cod_asignatura)
            const tipo_clase = tipoClase.find(clase => clase.pk === reporte.fields.cod_tipo_clase)
            const carrera = carreras.find(carrera => carrera.pk === asignatura.fields.cod_carrera)
            const plan = planes.find(plan => plan.pk === asignatura.fields.cod_plan_estudio)

            const curso = asignatura.fields.curso
            const fecha = reporte.fields.fecha_clase
            const horaInicio = reporte.fields.hora_entrada
            const horaFin = reporte.fields.hora_salida
            console.log()
            return {
                asignatura: asignatura.fields.descripcion,
                carrera: carrera.fields.descripcion,
                plan: plan.fields.descripcion,
                curso: 'Curso: ' + curso,
                tipo_clase: reporte.fields.evaluacion == 0 ? tipo_clase.fields.descripcion : 'Evaluación',
                fecha: fecha,
                horaInicio: horaInicio,
                horaFin: horaFin
            }
        }))
    },[planes])

    return(
        <FlatList 
            data={parsedReportes}
            ItemSeparatorComponent={() => <View style={{ borderColor: "gray", borderWidth: .5, marginHorizontal: 15 }}/>}
            renderItem={({ item: repo }) => (
                <HistoryItem {...repo} />
            )}
        >
        </FlatList>
    )
}

export default HistoryList;