import { View, StyleSheet, Button, Platform, ScrollView, Alert } from 'react-native';
import { useEffect, useState } from 'react'
import StyledText from './StyledText';
import PickerSelect from './PickerSelect';
import useUserContext from '../hooks/useUserContext.js';
import DateTimePicker from '@react-native-community/datetimepicker';
import axios from 'axios';
import SectionedMultiSelect from 'react-native-sectioned-multi-select';
import { CheckBox } from '@rneui/themed';


const NewForm = ({ navigation }) => {
    //Context
    const { user, URL } = useUserContext();

    //Estados para almacenar los datos de la API
    const [facultades, setFacultades] = useState([]);
    const [carreras, setCarreras] = useState([]);
    const [clases, setClases] = useState([]);
    const [planes, setPlanes] = useState([]);
    const [asignaturas, setAsignaturas] = useState([]);
    const [unidades, setUnidades] = useState([]);
    const [contenidos, setContenidos] = useState([]);
    const [semestres, setSemestres] = useState([]);

    //Variable que contiene las listas de la API y su correspondiente estado
    const listsAndSetters = [
        { list: 'lista_facultades', setter: setFacultades },
        { list: 'lista_carreras', setter: setCarreras },
        { list: 'lista_planes', setter: setPlanes },
        { list: 'lista_asignaturas', setter: setAsignaturas },
        { list: 'lista_unidad', setter: setUnidades },
        { list: 'lista_contenido', setter: setContenidos },
        { list: 'lista_tipo_clase', setter: setClases },
        { list: 'lista_semestre', setter: setSemestres },
    ]

    //Estados para cargar los datos del formulario
    const [asignaturaItems, setAsignaturaItems] = useState([]);
    const [carreraItems, setCarreraItems] = useState([]);
    const [planItems, setPlanItems] = useState([]);
    const [unidadItems, setUnidadItems] = useState([]);
    const [contenidoItems, setContenidoItems] = useState([])
    const [semestreItems, setSemestresItems] = useState([]);

    //Estados para almacenar los datos del formulario
    const [selectedFacultad, setSelectedFacultad] = useState('');
    const [selectedCarrera, setSelectedCarrera] = useState('');
    const [selectedPlan, setSelectedPlan] = useState('');
    const [selectedAsignatura, setSelectedAsignatura] = useState('');
    const [selectedClase, setSelectedClase] = useState('');

    //Variable para verificar si todos los campos estan llenos
    const selects = [selectedFacultad, selectedCarrera, selectedPlan, selectedAsignatura, selectedClase];

    //Estados para relacionar los pickers del formulario
    const [asignaturaPicker, setAsignaturaPicker] = useState('');
    const [carreraPicker, setCarreraPicker] = useState('');
    const [planPicker, setPlanPicker] = useState('');
    const [unidadPicker, setUnidadPicker] = useState('');
    const [contenidoPicker, setContenidoPicker] = useState('')

    //Estados para almacenar horarios y fecha
    const [date, setDate] = useState(new Date());
    const [mode, setMode] = useState('date');
    const [show, setShow] = useState(false);
    const [selectedDate, setSelectedDate] = useState('Complete la fecha!');
    const [selectedStartTime, setSelectedStartTime] = useState('Complete Hora de Inicio!');
    const [selectedEndTime, setSelectedEndTime] = useState('Complete Hora de Fin!');
    const [isStartTime, setIsStartTime] = useState(false);

    //Estados para determinar a donde se dirige el usuario
    const [check1, setCheck1] = useState(false)
    const [isDisabled, setIsDisabled] = useState(true)

    const submitForm = () => {
        axios.post(`${URL}/crear_cabecera`, {
            cod_tipo_clase: selectedClase,
            cod_asignatura: selectedAsignatura,
            cod_usuario: user.cod_usuario,
            fecha_clase: selectedDate,
            hora_entrada: selectedStartTime,
            hora_salida: selectedEndTime,
            fecha_vencimiento: semestreItems,
            evaluacion: check1 ? 1 : 0,
            estado: 1,
        })
    }

    //Funcion para obtener una lista especifica de la API
    const getAPIData = (response, list, setList) => {
        const res = JSON.parse(response.data[list])
        setList(res.map(field => field))
    }

    //Funcion para elegir fecha
    const onChange = (event, selectedDate) => {
        const currentDate = selectedDate || date;
        const fTimeDescription = isStartTime ? 'Hora de Inicio: ' : 'Hora de Fin: ';
        setShow(Platform.OS === 'ios');
        setDate(currentDate);

        let tempDate = new Date(currentDate);
        let fDate = 'Fecha de clase: ' + tempDate.getDate() + '/' + (tempDate.getMonth() + 1) + '/' + tempDate.getFullYear();
        let fTime = fTimeDescription + tempDate.getHours() + ':' + tempDate.getMinutes();

        setSelectedDate(fDate);

        if(mode != 'date') {
            if(isStartTime) {
                setSelectedStartTime(fTime);
            }
            else {
                setSelectedEndTime(fTime);
            }
        }
    };

    //Funcion para elegir hora o fecha
    const showMode = (currentMode) => {
        setShow(true);
        setMode(currentMode);
    };

    useEffect(() => {
        axios.get(`${URL}/listaFacultades_Carreras/${user.cod_usuario}`)
        .then((response) => {
            listsAndSetters.map(detail => getAPIData(response, detail.list, detail.setter))
            
        })
        .catch((error) => {
            console.log(error);
        });
    }, [])

    useEffect(() => {
        setCarreraItems(getItems(carreras, 'cod_facultad', carreraPicker));
    }, [carreraPicker])

    useEffect(() => {
        setPlanItems(getItems(planes, 'cod_carrera', planPicker));
    }, [planPicker])

    useEffect(() => {
        setAsignaturaItems(getItems(asignaturas, 'cod_plan_estudio', asignaturaPicker));
        
        semestres.forEach((semestre) => {
            asignaturas.map((asignatura) => {
                if(asignatura.pk == asignaturaPicker) {
                    if(asignatura.fields.cod_semestre == semestre.pk) {
                        console.log(semestre.pk)
                        setSelectedAsignatura(semestre.pk)
                    }
                }
            })
        })
    }, [asignaturaPicker])

    useEffect(() => {
        const items = [unidades, contenidos];
        const cod = ['cod_asignatura', 'cod_unidad_aprendizaje']
        setContenidoItems(getMultiItems(items, cod, unidadPicker))
    }, [unidadPicker])

    useEffect(() => {
        if(selectedDate != 'Complete la fecha!' && selectedStartTime != 'Complete Hora de Inicio!' && selectedEndTime != 'Complete Hora de Fin!') {
            if(selects.every(item => item == 0 || item != null)) {
                setIsDisabled(false);
            }
            else {
                setIsDisabled(true);
            }
        }
    }, [selects])
    //Carga individual de los pickers que no tienen relaciones con otros

    //Carga de facultades
    const FacultadItems = (facultades.map(facultad => ({
        label: facultad.fields.descripcion,
        value: facultad.pk,
        key: facultad.pk
    })));

    //Carga de clases
    const ClaseItems = (clases.map(clase => ({
        label: clase.fields.descripcion,
        value: clase.pk,
        key: clase.pk
    })));

    //Funcion para carga de pickers
    const getItems = (items, cod, itemPicker) => {
        let arr = []
        items.forEach(item => {
            if(item.fields[cod] == itemPicker) {
                let obj = {
                    label: item.fields.descripcion,
                    value: item.pk,
                    key: item.pk
                }
                arr.push(obj);

                return arr;
            }
        })
        return arr;
    }

    //Funcion para carga de picker multiple
    const getMultiItems = (items, cod, itemPicker) => {
        //contenido de la unidad
        const getSubItems = (subItemCod) => {
            let arrItems = [];
            items[1].forEach(subItem => {
                if(subItem.fields[cod[1]] == subItemCod) {
                    let obj1 = {
                        name: subItem.fields.descripcion,
                        id: subItem.pk,
                    }
                    arrItems.push(obj1);
                }
            })
            return arrItems;
        }

        //titulo de la unidad
        let arr = []
        items[0].forEach(item => {
            if(item.fields[cod[0]] == itemPicker) {
                let obj = {
                    name: item.fields.descripcion,
                    id: item.fields.descripcion,
                    children: getSubItems(item.pk)
                }
                arr.push(obj);
                return arr;
            }
        })
        return arr;
    }

    //Alerta para activar o desactivar modo evaluacion
    const alertEvaluacion = () => {
        const info = !check1 ? ['Activar Evaluación', '¿Desea que el tipo de clase sea "Evaluación"?'] : ['Desactivar Evaluación', '¿Desea desactivar el tipo de clase "Evaluación"?'];
        Alert.alert(info[0], info[1], [
            {
                text: 'Cancelar',
                style: 'cancel',
            },
            { text: 'Sí!', onPress: () => {
                setCheck1(!check1); 
                !check1 ? setSelectedClase(0) : setSelectedClase(null);
            }},
        ]);
    }

    //Alerta para guardar la cabecera
    const alertSubmit = () => {
        Alert.alert('Confirmar', '¿Desea guardar la cabecera del informe?', [
            {
                text: 'Cancelar',
                style: 'cancel',
            },
            { text: 'Sí!', onPress: () => {
                setIsDisabled(true);
            }},
        ]);
    }
    
    return(
        <ScrollView>
            <StyledText
                fontSize="large"
                fontWeight="bold"
                color="primary"
                align="center"
                style={{ marginTop: 10 }}>
                Informe de Clase
            </StyledText>
            <View style={styles.form}>
                <View style={{ flexDirection:'row', justifyContent:'center', alignItems:'center' }}>
                    <View>
                    <StyledText align="center" fontWeight="bold" color="primary">{selectedDate}</StyledText>
                        <StyledText align="center" fontWeight="bold" color="primary">{selectedStartTime}</StyledText>
                        <StyledText align="center" fontWeight="bold" color="primary">{selectedEndTime}</StyledText>
                    </View>
                    <View style={{ marginLeft: 8, justifyContent:'space-between', height: 120 }}>
                        <Button title='Fecha de Clase' onPress={() => showMode('date')}/>
                        <Button title='Hora de Entrada' onPress={() => { showMode('time'); setIsStartTime(true) }}/>
                        <Button title='Hora de Salida' onPress={() => { showMode('time'); setIsStartTime(false) }}/>
                    </View>
                </View>
                
                <PickerSelect 
                    title="Facultad"
                    items={ FacultadItems }
                    selectedValue={ selectedFacultad }
                    setPicker={ setCarreraPicker }
                    setSelected={ setSelectedFacultad }
                />

                <PickerSelect 
                    title="Carrera"
                    items={ carreraItems }
                    selectedValue={ selectedCarrera }
                    setPicker={ setPlanPicker }
                    setSelected={ setSelectedCarrera }
                />

                <PickerSelect 
                    title="Plan de Estudio"
                    items={ planItems }
                    selectedValue={ selectedPlan }
                    setPicker={ setAsignaturaPicker }
                    setSelected={ setSelectedPlan }
                />

                <PickerSelect 
                    title="Asignatura"
                    items={ asignaturaItems }
                    selectedValue={ selectedAsignatura }
                    setPicker={ setUnidadPicker }
                    setSelected={ setSelectedAsignatura }
                />

                <CheckBox
                    center
                    title="¿Usar evaluación como tipo de clase?"
                    checked={ check1 }
                    onPress={ () => alertEvaluacion() }
                />

                { !check1 ? <PickerSelect 
                    title="Tipo de Clase"
                    items={ ClaseItems }
                    selectedValue={ selectedClase }
                    setSelected={ setSelectedClase }
                /> : null }

                <Button 
                    title='Continuar'
                    onPress={ () => {
                        alertSubmit();
                    }}
                    disabled={ isDisabled }
                />

                { isDisabled ? 
                    <StyledText 
                        fontWeight="bold"
                        fontSize="body"
                        align="center"
                        color="red">
                            Todos los campos deben ser rellenados!
                    </StyledText> : null 
                }

                {/* <SectionedMultiSelect
                    items={ contenidoItems }
                    IconRenderer={ Icon }
                    uniqueKey="id"
                    subKey="children"
                    selectText="Seleccione los contenidos"
                    confirmText="Listo"
                    searchPlaceholderText="Buscar contenidos"
                    noItemsComponent={ () => <StyledText align="center" style={{marginTop:20}}>No hay contenidos</StyledText> }
                    noResultsComponent={ () => <StyledText align="center" style={{marginTop:20}}>No hay resultados</StyledText> }
                    selectedText=""
                    showDropDowns={ true }
                    readOnlyHeadings={ true }
                    onSelectedItemsChange={ setSelectedItems }
                    selectedItems={ selectedItems }
                /> */}

                {show && (
                    <DateTimePicker
                        testID="dateTimePicker"
                        value={ date }
                        mode={ mode }
                        is24Hour={ true }
                        display="default"
                        onChange={ onChange }
                    />)
                }
            
            </View>
        </ScrollView>
    )
}

const styles = StyleSheet.create({
    form: {
        marginHorizontal: 12,
        marginVertical: 12,
        flex: 1,
        height: '100%',
        gap: 12,
        backgroundColor: '#fff',
        paddingVertical: 12,
        paddingHorizontal: 12,
        marginBottom: 12,
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.23,
        shadowRadius: 2.62,
        elevation: 4,
        borderRadius: 12
    },
})

export default NewForm;