import { View, StyleSheet, Button, Platform, ScrollView, Alert } from 'react-native';
import { useEffect, useState } from 'react'
import StyledText from './StyledText';
import PickerSelect from './PickerSelect';
import useUserContext from '../hooks/useUserContext.js';
import DateTimePicker from '@react-native-community/datetimepicker';
import axios from 'axios';
import Icon from 'react-native-vector-icons/MaterialIcons'
import SectionedMultiSelect from 'react-native-sectioned-multi-select';
import { CheckBox } from '@rneui/themed';


const NewForm = ({ navigation }) => {
    const { user, URL } = useUserContext();
    const [facultades, setFacultades] = useState([]);
    const [carreras, setCarreras] = useState([]);
    const [clases, setClases] = useState([]);
    const [planes, setPlanes] = useState([]);
    const [asignaturas, setAsignaturas] = useState([]);
    const [unidades, setUnidades] = useState([]);
    const [contenidos, setContenidos] = useState([])

    const [asignaturaItems, setAsignaturaItems] = useState([]);
    const [carreraItems, setCarreraItems] = useState([]);
    const [planItems, setPlanItems] = useState([]);
    const [unidadItems, setUnidadItems] = useState([]);
    const [contenidoItems, setContenidoItems] = useState([])

    const [selectedFacultad, setSelectedFacultad] = useState('');
    const [selectedCarrera, setSelectedCarrera] = useState('');
    const [selectedPlan, setSelectedPlan] = useState('');
    const [selectedAsignatura, setSelectedAsignatura] = useState('');
    const [selectedClase, setSelectedClase] = useState('');
    const selects = [selectedFacultad, selectedCarrera, selectedPlan, selectedAsignatura, selectedClase];

    const [asignaturaPicker, setAsignaturaPicker] = useState('');
    const [carreraPicker, setCarreraPicker] = useState('');
    const [planPicker, setPlanPicker] = useState('');
    const [unidadPicker, setUnidadPicker] = useState('');
    const [contenidoPicker, setContenidoPicker] = useState('')

    const [date, setDate] = useState(new Date());
    const [mode, setMode] = useState('date');
    const [show, setShow] = useState(false);
    const [selectedDate, setSelectedDate] = useState('Seleccionar Fecha');
    const [selectedStartTime, setSelectedStartTime] = useState('Seleccionar Hora Inicio');
    const [selectedEndTime, setSelectedEndTime] = useState('Seleccionar Hora Fin');
    const [isStartTime, setIsStartTime] = useState(false);
    const [check1, setCheck1] = useState(false)
    const [isDisabled, setIsDisabled] = useState(true)

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

        console.log(fDate + ' (' + fTime + ')');
    };

    const showMode = (currentMode) => {
        setShow(true);
        setMode(currentMode);
    };

    useEffect(() => {
        axios.get(`${URL}/listaFacultades_Carreras/${user.cod_usuario}`)
        .then((response) => {
            const resFacu = JSON.parse(response.data.lista_facultades);
            const resCarreras = JSON.parse(response.data.lista_carreras);
            const resAsignaturas = JSON.parse(response.data.lista_asignaturas);
            const resPlanes = JSON.parse(response.data.lista_planes);
            const resUnidades = JSON.parse(response.data.lista_unidad);
            const resContenido = JSON.parse(response.data.lista_contenido)
            const resClases = JSON.parse(response.data.lista_tipo_clase);
            setFacultades(resFacu.map(field => field));
            setCarreras(resCarreras.map(field => field));
            setPlanes(resPlanes.map(field => field));
            setAsignaturas(resAsignaturas.map(field => field));
            setUnidades(resUnidades.map(field => field));
            setContenidos(resContenido.map(field => field));
            setClases(resClases.map(field => field));
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
    }, [asignaturaPicker])

    useEffect(() => {
        const items = [unidades, contenidos];
        const cod = ['cod_asignatura', 'cod_unidad_aprendizaje']
        setContenidoItems(getMultiItems(items, cod, unidadPicker))
    }, [unidadPicker])

    useEffect(() => {
        if(selectedDate != 'Seleccionar Fecha' && selectedStartTime != 'Seleccionar Hora Inicio' && selectedEndTime != 'Seleccionar Hora Fin') {
            if(selects.every(item => item == 0 || item != null)) {
                setIsDisabled(false);
            }
            else {
                setIsDisabled(true);
            }
        }
    }, [selects])

    const FacultadItems = (facultades.map(facultad => ({
        label: facultad.fields.descripcion,
        value: facultad.pk,
        key: facultad.pk
    })));

    const ClaseItems = (clases.map(clase => ({
        label: clase.fields.descripcion,
        value: clase.pk,
        key: clase.pk
    })));

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
                    <StyledText align="center" fontWeight="bold">{selectedDate}</StyledText>
                        <StyledText align="center" fontWeight="bold">{selectedStartTime}</StyledText>
                        <StyledText align="center" fontWeight="bold">{selectedEndTime}</StyledText>
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
                    disabled={ isDisabled }/>

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