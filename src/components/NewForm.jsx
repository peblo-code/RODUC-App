import { View, StyleSheet, Button, Text, Platform, ScrollView } from 'react-native';
import { useEffect, useState } from 'react'
import StyledText from './StyledText';
import PickerSelect from './PickerSelect';
import useUserContext from '../hooks/useUserContext.js';
import DateTimePicker from '@react-native-community/datetimepicker';
import axios from 'axios';
import Icon from 'react-native-vector-icons/MaterialIcons'
import SectionedMultiSelect from 'react-native-sectioned-multi-select';


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

    const [asignaturaPicker, setAsignaturaPicker] = useState('');
    const [carreraPicker, setCarreraPicker] = useState('');
    const [planPicker, setPlanPicker] = useState('');
    const [unidadPicker, setUnidadPicker] = useState('');
    const [contenidoPicker, setContenidoPicker] = useState('')

    const [date, setDate] = useState(new Date());
    const [mode, setMode] = useState('date');
    const [show, setShow] = useState(false);
    const [text, setText] = useState('Empty');
    const [selectedItems, setSelectedItems] = useState([]);

    const onChange = (event, selectedDate) => {
        const currentDate = selectedDate || date;
        setShow(Platform.OS === 'ios');
        setDate(currentDate);

        let tempDate = new Date(currentDate);
        let fDate = tempDate.getDate() + '/' + (tempDate.getMonth() + 1) + '/' + tempDate.getFullYear();
        let fTime = 'Hours: ' + tempDate.getHours() + ' Minutes: ' + tempDate.getMinutes();
        setText(fDate + '\n' + fTime);

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

/*     useEffect(() => {
        setUnidadItems(getItems(unidades, 'cod_asignatura', unidadPicker));
    }, [unidadPicker]) */

    useEffect(() => {
        const items = [unidades, contenidos];
        const cod = ['cod_asignatura', 'cod_unidad_aprendizaje']
        setContenidoItems(getMultiItems(items, cod, unidadPicker))
    }, [unidadPicker])

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
    
    return(
        <ScrollView>
            <View style={styles.form}>

                <StyledText
                    fontSize="large"
                    fontWeight="bold"
                    color="primary">
                    Nuevo Informe
                </StyledText>

                <Text>{text}</Text>
                <Button title='DatePicker' onPress={() => showMode('date')}/>
                <Button title='TimePicker' onPress={() => showMode('time')}/>
                
                <PickerSelect 
                    title="Facultad"
                    items={ FacultadItems }
                    onValueChange={ setCarreraPicker }
                />

                <PickerSelect 
                    title="Carrera"
                    items={ carreraItems }
                    onValueChange={ setPlanPicker }
                />

                <PickerSelect 
                    title="Plan de Estudio"
                    items={ planItems }
                    onValueChange={ setAsignaturaPicker }
                />

                <PickerSelect 
                    title="Asignatura"
                    items={ asignaturaItems }
                    onValueChange={ setUnidadPicker }
                />

                <PickerSelect 
                    title="Tipo de Clase"
                    items={ ClaseItems }
                />

                <SectionedMultiSelect
                    items={contenidoItems}
                    IconRenderer={Icon}
                    uniqueKey="id"
                    subKey="children"
                    selectText="Seleccione los contenidos"
                    showDropDowns={true}
                    readOnlyHeadings={true}
                    onSelectedItemsChange={setSelectedItems}
                    selectedItems={selectedItems}
                />

                {show && (
                    <DateTimePicker
                        testID="dateTimePicker"
                        value={date}
                        mode={mode}
                        is24Hour={true}
                        display="default"
                        onChange={onChange}
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
        gap: 12
    },
})

export default NewForm;