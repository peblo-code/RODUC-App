import { View, StyleSheet } from 'react-native';
import { useEffect, useState } from 'react'
import StyledText from './StyledText';
import PickerSelect from './PickerSelect';
import useUserContext from '../hooks/useUserContext.js';
import axios from 'axios';

const NewForm = ({ navigation }) => {
    const { user, URL } = useUserContext();
    const [facultades, setFacultades] = useState([]);
    const [carreras, setCarreras] = useState([]);
    const [planes, setPlanes] = useState([]);
    const [asignaturas, setAsignaturas] = useState([]);
    const [asignaturaItems, setAsignaturaItems] = useState([]);
    const [carreraItems, setCarreraItems] = useState([]);
    const [planItems, setPlanItems] = useState([]);
    const [asignaturaPicker, setAsignaturaPicker] = useState('');
    const [carreraPicker, setCarreraPicker] = useState('');
    const [planPicker, setPlanPicker] = useState('');

    useEffect(() => {
        axios.get(`${URL}/listaFacultades_Carreras/${user.cod_usuario}`)
        .then((response) => {
            const resFacu = JSON.parse(response.data.lista_facultades);
            const resCarreras = JSON.parse(response.data.lista_carreras);
            const resAsignaturas = JSON.parse(response.data.lista_asignaturas);
            const resPlanes = JSON.parse(response.data.lista_planes);
            setFacultades(resFacu.map(field => field));
            setCarreras(resCarreras.map(field => field));
            setPlanes(resPlanes.map(field => field));
            setAsignaturas(resAsignaturas.map(field => field));
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

    const FacultadItems = (facultades.map(facultad => ({
        label: facultad.fields.descripcion,
        value: facultad.pk,
        key: facultad.pk
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
    
    return(
        <View style={styles.form}>
            <StyledText
                fontSize="large"
                fontWeight="bold"
                color="primary">
                Nuevo Informe
            </StyledText>
            
            <PickerSelect 
                title="Facultad"
                items={FacultadItems}
                onValueChange={ setCarreraPicker }
            />

            <PickerSelect 
                title="Carrera"
                items={carreraItems}
                onValueChange={ setPlanPicker }
            />

            <PickerSelect 
                title="Plan de Estudio"
                items={planItems}
                onValueChange={ setAsignaturaPicker }
            />

            <PickerSelect 
                title="Asignatura"
                items={asignaturaItems}
            />
        </View>
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