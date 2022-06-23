import { TouchableOpacity, FlatList, View, Alert } from 'react-native';
import { useEffect, useState } from 'react';
import HistoryItem from './HistoryItem';
import useUserContext from '../hooks/useUserContext.js';
import axios from 'axios';
import TouchIcon from './TouchIcon'

const HistoryList = ({ navigation }) => {
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
    const parseAPIData = (response, list, setList) => {
        const res = JSON.parse(response.data[list])
        setList(res.map(field => field))
    }

    const getAPIData = () => {
        axios.get(`${URL}/historial_reportes/${user.cod_usuario}`)
            .then(response => {
                parseAPIData(response, 'lista_cabeceras', setReportes)
            })
            .catch(error => console.log(error))

        axios.get(`${URL}/listaFacultades_Carreras/${user.cod_usuario}`)
            .then(response => {
                parseAPIData(response, 'lista_asignaturas', setAsignaturas)
                parseAPIData(response, 'lista_carreras', setCarreras)
                parseAPIData(response, 'lista_tipo_clase', setTipoClase)
                parseAPIData(response, 'lista_planes', setPlanes)
                
            })
            .catch(error => console.log(error))
    }

    useEffect(() => {
        getAPIData()
    },[])

    useEffect(() => {
        setParseReportes(reportes.map(reporte => {
            const asignatura = asignaturas.find(asignatura => asignatura.pk === reporte.fields.cod_asignatura)
            const tipo_clase = tipoClase.find(clase => clase.pk === reporte.fields.cod_tipo_clase)
            const carrera = carreras.find(carrera => carrera.pk === asignatura.fields.cod_carrera)
            const plan = planes.find(plan => plan.pk === asignatura.fields.cod_plan_estudio)

            const curso = asignatura.fields.curso
            const fecha = reporte.fields.fecha_clase.split('-').reverse().join('/')
            const horaInicio = reporte.fields.hora_entrada
            const horaFin = reporte.fields.hora_salida

            return {
                editObj: {
                    cod_cabecera: reporte.pk,
                    cod_facultad: carrera.fields.cod_facultad,
                    cod_carrera: carrera.pk,
                    cod_plan: plan.pk,
                    cod_asignatura: asignatura.pk,
                    cod_tipo_clase: tipo_clase ? tipo_clase.pk : 0,
                    fecha: fecha,
                    horaInicio: horaInicio,
                    horaFin: horaFin
                },
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

    const confirmDelete = (cod_cabecera) => {
        Alert.alert("Eliminar Registro", "Estas seguro/a de eliminar este registro?",[
            {
                text: 'Cancelar',
                style: 'cancel',
            },
            {
                text: 'Si',
                onPress: () => {
                    axios.get(`${URL}/borrar_reporte/${cod_cabecera}/${user.nombre_usuario}`)
                    .then(res => {
                        Alert.alert("Eliminar Registro", "El registro fue eliminado exitosamente")
                        getAPIData()
                    })
                    .catch(err => Alert.alert("Error", "No se pudo eliminar el registro"))
                }
            }
        ])
    }

    return(
        <FlatList 
            data={parsedReportes}
            ItemSeparatorComponent={() => <View style={{ borderColor: "gray", borderWidth: .5, marginHorizontal: 15 }}/>}
            renderItem={({ item: repo }) => (
                <View style={{flexDirection: 'row'}}>
                    <View style={{flex: 1}}>
                        <HistoryItem {...repo} />
                    </View>
                    <View style={{justifyContent: 'space-around', marginRight: 10}}>
                        { repo.tipo_clase != 'Evaluación' ? <TouchIcon name="edit" size={24} color="black" onPress={() => navigation.navigate('Detalle del Registro', {
                            editObj: repo.editObj,
                        })}/>: null }
                        <TouchIcon name="trash" size={24} color="red" onPress={() => confirmDelete(repo.editObj.cod_cabecera)}/>
                    </View>
                </View>
            )}
        >
        </FlatList>
    )
}

export default HistoryList;