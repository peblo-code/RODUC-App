import { View, Text, StyleSheet } from 'react-native';
import { useEffect, useState } from 'react'
import StyledText from './StyledText';
import RNPickerSelect from 'react-native-picker-select';
import axios from 'axios';

const URL = 'http://26.247.235.244:8000/restapi'; //url del servidor

const NewForm = () => {

    const [facultades, setFacultades] = useState([]);

    useEffect(() => {
        axios.get(`${URL}/lista_facultades`)
        .then((response) => {
            setFacultades(response.data);
        })
        .catch((error) => {
            console.log(error);
        });
    }, [])

    const FacultadItems = (facultades.map(facultad => ({
        label: facultad.descripcion,
        value: facultad.cod_facultad,
        key: facultad.cod_facultad
    })));
    
    return(
        <View style={styles.form}>
            <StyledText 
                fontSize="large"
                fontWeight="bold"
                color="primary">
                Nuevo Informe
            </StyledText>
            <RNPickerSelect
            onValueChange={(value) => console.log(value)}
            items={FacultadItems}
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