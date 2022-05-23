import { View, StyleSheet } from 'react-native';
import { useEffect, useState } from 'react'
import StyledText from './StyledText';
import RNPickerSelect from 'react-native-picker-select';
import useUserContext from '../hooks/useUserContext.js';
import axios from 'axios';

const URL = 'http://26.247.235.244:8000/restapi'; //url del servidor

const NewForm = () => {
    const { user } = useUserContext();
    const [facultades, setFacultades] = useState([]);
    const [carreras, setCarreras] = useState([]);
    const [carreraItems, setCarreraItems] = useState([]);
    const [carreraPicker, setCarreraPicker] = useState('');
    const { URL } = useUserContext();


    useEffect(() => {
        axios.get(`${URL}/listaFacultades_Carreras/${user.cod_usuario}`)
        .then((response) => {
            const resFacu = JSON.parse(response.data.lista_facultades);
            const resCarreras = JSON.parse(response.data.lista_carreras);
            setFacultades(resFacu.map(field => field));
            setCarreras(resCarreras.map(field => field));
            //getCarreras(response);
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
        if(carreraPicker == undefined) {
            return [{key: '', label: 'Seleccione una carrera', value: ''}];
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

    useEffect(() => {
        setCarreraItems(getCarreraItems(carreras));
    }, [carreraPicker])
    
    const placeholder = {
        label: 'Seleccione una facultad',
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
            <RNPickerSelect
                placeholder={{
                    label: 'Seleccione una facultad',
                    value: null,
                    color: '#9EA0A4',
                }}
                onValueChange={(value) => setCarreraPicker(value)}
                items={FacultadItems}
            /> 

            <RNPickerSelect
                placeholder={{
                    label: 'Seleccione una carrera',
                    value: null,
                    color: '#9EA0A4',
                }}
                onValueChange={(value) => console.log("Id de carrera:" + value)}
                items={carreraItems}
            /> 
        </View>
    )
}

const styles = StyleSheet.create({
    form: {
        marginHorizontal: 12,
        marginVertical: 12,
        alignItems: 'center',
        flex: 1
    },
})

export default NewForm;