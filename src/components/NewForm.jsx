import { View, StyleSheet, Platform, Text } from 'react-native';
import { useEffect, useState } from 'react'
import StyledText from './StyledText';
import RNPickerSelect, { defaultStyles } from 'react-native-picker-select';
import useUserContext from '../hooks/useUserContext.js';
import axios from 'axios';

const NewForm = () => {
    const { user } = useUserContext();
    const [facultades, setFacultades] = useState([]);
    const [carreras, setCarreras] = useState([]);
    const [asignaturas, setAsignaturas] = useState([]);
    const [asignaturaItems, setAsignaturaItems] = useState([]);
    const [carreraItems, setCarreraItems] = useState([]);
    const [asignaturaPicker, setAsignaturaPicker] = useState('');
    const [carreraPicker, setCarreraPicker] = useState('');
    const { URL } = useUserContext();

    useEffect(() => {
        axios.get(`${URL}/listaFacultades_Carreras/${user.cod_usuario}`)
        .then((response) => {
            const resFacu = JSON.parse(response.data.lista_facultades);
            const resCarreras = JSON.parse(response.data.lista_carreras);
            const resAsignaturas = JSON.parse(response.data.lista_asignaturas);
            setFacultades(resFacu.map(field => field));
            setCarreras(resCarreras.map(field => field));
            setAsignaturas(resAsignaturas.map(field => field));
        })
        .catch((error) => {
            console.log(error);
        });
    }, [])

    const FacultadItems = (facultades.map(facultad => ({
        label: facultad.fields.descripcion,
        value: facultad.pk,
        key: facultad.pk
    })));

    const getCarreraItems = (carreras) => {
        setCarreraItems([])
        if(carreraPicker == undefined) {
            return [{key: '', label: 'Seleccione una facultad', value: ''}];
        }

        let arr = []
        carreras.forEach(carrera => {
            if(carrera.fields.cod_facultad == carreraPicker) {
                let obj = {
                    label: carrera.fields.descripcion,
                    value: carrera.pk,
                    key: carrera.pk
                }
                arr.push(obj);

                return arr;
            }
        })

        return arr;
    }

    const getAsignaturaItems = (asignaturas) => {
        if(asignaturaPicker == undefined) {
            return [{key: '', label: 'Seleccione una carrera', value: ''}];
        }

        let arr = []
        asignaturas.forEach(asignatura => {
            if(asignatura.fields.cod_carrera == asignaturaPicker) {
                let obj = {
                    label: asignatura.fields.descripcion,
                    value: asignatura.pk,
                    key: asignatura.pk
                }
                arr.push(obj);

                return arr;
            }
        })

        return arr;
    }

    useEffect(() => {
        setCarreraItems(getCarreraItems(carreras));
    }, [carreraPicker])

    useEffect(() => {
        setAsignaturaItems(getAsignaturaItems(asignaturas));
    }, [asignaturaPicker])
    
    const placeholder = {
        label: 'Seleccione una opción',
        value: null,
        color: '#9EA0A4',
    };
    
    return(
        <View style={styles.form}>
            <StyledText
                fontSize="large"
                fontWeight="bold"
                color="primary">
                Nuevo Informe
            </StyledText>
            
            <Text>Facultad</Text>
            <RNPickerSelect
                placeholder={placeholder}
                items={FacultadItems}
                style={pickerSelectStyles}
                useNativeAndroidPickerStyle={true}
                onValueChange={(value) => setCarreraPicker(value)}
            /> 

            <Text>Carrera</Text>
            <RNPickerSelect
                placeholder={placeholder}
                items={carreraItems}
                style={pickerSelectStyles}
                useNativeAndroidPickerStyle={true}
                onValueChange={(value) => { setAsignaturaPicker(value) }}
            />

            <Text>Asignatura</Text>
            <RNPickerSelect
                placeholder={placeholder}
                items={asignaturaItems}
                style={pickerSelectStyles}
                useNativeAndroidPickerStyle={true}
                onValueChange={(value) => console.log(value)}
            />
        </View>
    )
}

const styles = StyleSheet.create({
    form: {
        marginHorizontal: 12,
        marginVertical: 12,
        //alignItems: 'center',
        flex: 1,
        height: '100%',
        gap: 12
    },
})

const pickerSelectStyles = StyleSheet.create({
    inputIOS: {
      fontSize: 16,
      paddingVertical: 12,
      paddingHorizontal: 10,
      borderWidth: 1,
      borderColor: 'red',
      borderRadius: 4,
      color: 'black',
      paddingRight: 30, // to ensure the text is never behind the icon
    },
    inputAndroid: {
      fontSize: 16,
      paddingHorizontal: 10,
      paddingVertical: 8,
      borderWidth: 0.5,
      borderColor: 'purple',
      borderRadius: 8,
      color: 'black',
      paddingRight: 30, // to ensure the text is never behind the icon
    },
  });
  

export default NewForm;