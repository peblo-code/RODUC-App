import { View, Button, Alert, ScrollView } from 'react-native';
import { useEffect, useState } from 'react';
import PickerSelect from './PickerSelect';
import SectionedMultiSelect from 'react-native-sectioned-multi-select';
import Icon from 'react-native-vector-icons/MaterialIcons';
import StyledText from './StyledText';
import useUserContext from '../hooks/useUserContext';
import axios from 'axios';

const styles = {
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
}

export default function DetailForm({navigation, route}) {
    const { URL, user } = useUserContext();
    const { detalleObj } = route.params;
    const { codCabecera, check1, contenidoItems, instrumentos, recursos, tiposEvaluacion, trabajos, metodologias } = detalleObj;
    //metodologia - recursos - trabajos
    const [instrumentosItems, setInstrumentosItems] = useState([]);
    const [tipoEvaluacionItems, setTipoEvaluacionItems] = useState([]);

    const [metodologiasItems, setMetodologiasItems] = useState([]);
    const [recursosItems, setRecursosItems] = useState([]);
    const [trabajosItems, setTrabajosItems] = useState([]);

    const [selectedInstrumento, setSelectedInstrumento] = useState([]);
    const [selectedTipoEvaluacion, setSelectedTipoEvaluacion] = useState([]);
    const [selectedContenidos, setSelectedContenidos] = useState([]);
    const [selectedMetodologias, setSelectedMetodologias] = useState([]);
    const [selectedRecursos, setSelectedRecursos] = useState([]);
    const [selectedTrabajos, setSelectedTrabajos] = useState([]);

    const getIndividual = ((items) => {
        const list = items.map(item => ({
            label: item.fields.descripcion,
            value: item.pk,
            key: item.pk
        }))
        return list
    });
    
    const cleanData = () => {
        setSelectedInstrumento([]);
        setSelectedTipoEvaluacion([]);
        setSelectedContenidos([]);
        setSelectedMetodologias([]);
        setSelectedRecursos([]);
        setSelectedTrabajos([]);
    }

    const submitForm = () => {
        if(check1) {
            axios.post(`${URL}/crear_evaluaciones`, {
                cod_cabecera_planilla: codCabecera,
                cod_tipo_eva: selectedTipoEvaluacion,
                cod_instrumento_evaluacion: selectedInstrumento,
                estado: 1,
                alta_usuario: user.nombre_usuario,
            })
            .then(res => {
                Alert.alert('Exito!', 'Informe de la Clase creada con exito!',[
                    {text: 'Cargar otro', onPress: () => cleanData()},
                    {text: 'OK', onPress: () => navigation.navigate('Inicio')},
                ])
            })
            .catch(err => {
                Alert.alert('Error!', 'No se pudo crear informe de la clase')
                console.log(err)
            })
        } else {
            selectedContenidos.map(item => {
                axios.post(`${URL}/cargar_contenidos`, {
                    cod_cabecera_planilla: codCabecera,
                    cod_contenido: item,
                    estado: 1,
                    alta_usuario: user.nombre_usuario,

                })
            })

            selectedRecursos.map(item => {
                axios.post(`${URL}/cargar_recursos`, {
                    cod_cabecera_planilla: codCabecera,
                    cod_recurso_auxiliar: item,
                    estado: 1,
                    alta_usuario: user.nombre_usuario,

                })
            })

            selectedTrabajos.map(item => {
                axios.post(`${URL}/cargar_trabajos`, {
                    cod_cabecera_planilla: codCabecera,
                    cod_trabajo_autonomo: item,
                    estado: 1,
                    alta_usuario: user.nombre_usuario,

                })
            })

            selectedMetodologias.map(item => {
                axios.post(`${URL}/cargar_metodologia`, {
                    cod_cabecera_planilla: codCabecera,
                    cod_metodologia_enseñanza: item,
                    estado: 1,
                    alta_usuario: user.nombre_usuario,

                })
            })
            Alert.alert('Exito!', 'Informe de la Clase creada con exito!',[
                {text: 'OK', onPress: () => navigation.navigate('Inicio')},
            ])
        }
    }

    //Alerta para guardar el detalle
    const alertSubmit = () => {
        Alert.alert('Confirmar', '¿Desea guardar el detalle del informe?', [
            {
                text: 'Cancelar',
                style: 'cancel',
            },
            { text: 'Sí!', onPress: () => {
                //setIsDisabled(true);
                submitForm();
            }},
        ]);
    }

    useEffect(() => {
        setInstrumentosItems(getIndividual(instrumentos));
        setTipoEvaluacionItems(getIndividual(tiposEvaluacion));
        setMetodologiasItems([{
            name: 'Metodologias',
            id: 'metodologias',
            children: getMulti(metodologias)
        }]);
        setRecursosItems([{
            name: 'Recursos',
            id: 'recursos',
            children: getMulti(recursos)
        }]);
        setTrabajosItems([{
            name: 'Trabajos',
            id: 'trabajos',
            children: getMulti(trabajos)
        }]);
    }, [])

    const getMulti = ((items) => {
        //titulo de la unidad
        let arr = []
        items.forEach(item => {
            let obj = {
                name: item.fields.descripcion,
                id: item.pk,
            }
            arr.push(obj);
            return arr;
        })
        return arr;
    });

    useEffect(() => {
        console.log(selectedMetodologias)
    }, [selectedMetodologias])

    return (
        <ScrollView>
            <View style={styles.form}>
                {check1 ? <>
                <PickerSelect 
                    title="Instrumento de Evaluación"
                    items={ instrumentosItems }
                    selectedValue={ selectedInstrumento }
                    setSelected={ setSelectedInstrumento }
                />

                <PickerSelect 
                    title="Tipo de Evaluación"
                    items={ tipoEvaluacionItems }
                    selectedValue={ selectedTipoEvaluacion }
                    setSelected={ setSelectedTipoEvaluacion }
                />
                </> : <>
                        <StyledText
                            fontSize="subheading"
                            fontWeight="bold"
                            color="secondary">
                            Contenidos
                        </StyledText>
                        <SectionedMultiSelect
                            items={ contenidoItems }
                            IconRenderer={ Icon }
                            uniqueKey="id"
                            subKey="children"
                            selectText="Seleccione los contenidos"
                            confirmText="Listo"
                            searchPlaceholderText="Buscar contenidos"
                            noItemsComponent={ () => <StyledText align="center" style={{marginTop:20}}>No hay contenidos</StyledText> }
                            noResultsComponent={ () => <StyledText align="center" style={{marginTop:20}}>No hay resultados</StyledText> }
                            selectedText="seleccionados"
                            showDropDowns={ true }
                            readOnlyHeadings={ true }
                            onSelectedItemsChange={ setSelectedContenidos }
                            selectedItems={ selectedContenidos }
                        />

                        <StyledText
                            fontSize="subheading"
                            fontWeight="bold"
                            color="secondary">
                            Metodologias
                        </StyledText>

                        <SectionedMultiSelect
                            items={ metodologiasItems }
                            IconRenderer={ Icon }
                            uniqueKey="id"
                            subKey="children"
                            selectText="Seleccione las metodologias"
                            confirmText="Listo"
                            searchPlaceholderText="Buscar metodologias"
                            noItemsComponent={ () => <StyledText align="center" style={{marginTop:20}}>No hay metodologias</StyledText> }
                            noResultsComponent={ () => <StyledText align="center" style={{marginTop:20}}>No hay resultados</StyledText> }
                            selectedText="seleccionados"
                            showDropDowns={ false }
                            readOnlyHeadings={ true }
                            onSelectedItemsChange={ setSelectedMetodologias }
                            selectedItems={ selectedMetodologias }
                        />

                        <StyledText
                            fontSize="subheading"
                            fontWeight="bold"
                            color="secondary">
                            Recursos
                        </StyledText>

                        <SectionedMultiSelect
                            items={ recursosItems }
                            IconRenderer={ Icon }
                            uniqueKey="id"
                            subKey="children"
                            selectText="Seleccione los recursos"
                            confirmText="Listo"
                            searchPlaceholderText="Buscar recursos"
                            noItemsComponent={ () => <StyledText align="center" style={{marginTop:20}}>No hay recursos</StyledText> }
                            noResultsComponent={ () => <StyledText align="center" style={{marginTop:20}}>No hay resultados</StyledText> }
                            selectedText="seleccionados"
                            showDropDowns={ false }
                            readOnlyHeadings={ true }
                            onSelectedItemsChange={ setSelectedRecursos }
                            selectedItems={ selectedRecursos }
                        />

                        <StyledText
                            fontSize="subheading"
                            fontWeight="bold"
                            color="secondary">
                            Trabajos
                        </StyledText>

                        <SectionedMultiSelect
                            items={ trabajosItems }
                            IconRenderer={ Icon }
                            uniqueKey="id"
                            subKey="children"
                            selectText="Seleccione los trabajos"
                            confirmText="Listo"
                            searchPlaceholderText="Buscar trabajos"
                            noItemsComponent={ () => <StyledText align="center" style={{marginTop:20}}>No hay trabajos</StyledText> }
                            noResultsComponent={ () => <StyledText align="center" style={{marginTop:20}}>No hay resultados</StyledText> }
                            selectedText="seleccionados"
                            showDropDowns={ false }
                            readOnlyHeadings={ true }
                            onSelectedItemsChange={ setSelectedTrabajos }
                            selectedItems={ selectedTrabajos }
                        />

                        
                </>}
                <Button
                    title='Confirmar'
                    style={{marginTop:20}}
                    onPress={alertSubmit}
                />
            </View>
        </ScrollView>
    );
}