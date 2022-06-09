import { View, StyleSheet, Button } from 'react-native';
import useUserContext from '../hooks/useUserContext';
import StyledText from '../components/StyledText';
import theme from '../theme';
import CardMenu from '../components/CardMenu';

const extraerPrimerNombre = (nombres_del_usuario) => {
    const nombres = nombres_del_usuario.split(' ');
    return nombres[0];
}

const saludo = () => {
    const hora = new Date().getHours();
    if(hora >= 6 && hora < 12) {
        return 'Buenos días,';
    } else if(hora >= 12 && hora < 18) {
        return 'Buenas tardes,';
    } else {
        return 'Buenas noches,';
    }
}

const Home = ({navigation}) => {
    const { user } = useUserContext();
    const { nombres_del_usuario, apellidos_del_usuario } = user;
    return (
        <View style={styles.container}>
            <View
                style={styles.welcomeText}>
                <StyledText
                    fontSize="heading"
                    fontWeight="bold"
                    align="start">
                        {saludo()} {extraerPrimerNombre(nombres_del_usuario)} {extraerPrimerNombre(apellidos_del_usuario)}
                </StyledText>
                <StyledText
                    fontSize="heading"
                    align="start">
                        Seleccione una opción
                </StyledText>
                <CardMenu navigation={navigation}/>
            </View>
        </View>

    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
    },

    btnNewForm: {
        justifyContent: 'center',
        alignItems: 'center',
        paddingVertical: 10,
        backgroundColor: '#f2f2f2',
    },

    welcomeText: {
        paddingHorizontal: 12,
        paddingTop: 20,
        paddingBottom: 8,
    }

})

export default Home;