import { View, StyleSheet } from 'react-native';
import { useEffect, useState } from 'react'
import StyledText from './StyledText';
import Select2 from "react-select2-native";
import useUserContext from '../hooks/useUserContext.js';
import axios from 'axios';

const NewForm = () => {
    const { user } = useUserContext();
    const [facultades, setFacultades] = useState([]);
    const [carreras, setCarreras] = useState([]);
    const [carreraItems, setCarreraItems] = useState([]);
    const [carreraPicker, setCarreraPicker] = useState('');
    const [facultadPicker, setFacultadPicker] = useState('');
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
        id: facultad.pk,
        name: facultad.fields.descripcion,
    })));


    const getCarreraItems = (carreras) => {
        if (carreraPicker == undefined) {
            return [{ key: '', label: 'Seleccione una carrera', value: '' }];
        }

        let arr = []
        carreras.forEach(carrera => {
            if (carrera.fields.cod_facultad == facultadPicker) {
                let obj = {
                    id: carrera.pk,
                    name: carrera.fields.descripcion,
                }
                arr.push(obj);

                return arr;
            }
        })

        return arr;
    }

    useEffect(() => {
        setCarreraItems(getCarreraItems(carreras));
    }, [facultadPicker])


    return (
        <View style={styles.form}>
            <StyledText
                fontSize="large"
                fontWeight="bold"
                color="primary">
                Nuevo Informe
            </StyledText>

            <Select2
                isSelectSingle
                style={{ borderRadius: 5 }}
                colorTheme="blue"
                popupTitle="Select item"
                title='Seleccione una Facultad'
                data={FacultadItems}
                onSelect={(data) => {
                    console.log(data[0]);
                    setFacultadPicker(data[0]);
                }}
                onRemoveItem={(data) => {
                    setFacultadPicker(data[0]);
                }}
            />

            <Select2
                isSelectSingle
                style={{ borderRadius: 5 }}
                colorTheme="blue"
                popupTitle="Select item"
                title='Seleccione una Carrera'
                data={carreraItems}
                onSelect={(data) => {
                    console.log(data[0]);
                    setCarreraPicker({data})
                }}
                onRemoveItem={(data) => {
                    removeEventListener()
                    setFacultadPicker({data});
                }}
            />


        </View>
    )
}

const styles = StyleSheet.create({
    form: {
        marginHorizontal: 12,
        marginVertical: 12,
        alignItems: 'center',
        flex: 1,
        height: '100%',
        gap: 12
    },
})

const pickerSelectStyles = StyleSheet.create({
    inputAndroid: {
      fontSize: 16,
      paddingHorizontal: 10,
      paddingVertical: 8,
      borderWidth: 0.5,
      borderColor: 'purple',
      borderRadius: 8,
      color: 'red',
      paddingRight: 30, // to ensure the text is never behind the icon
    },
  });
  

export default NewForm;