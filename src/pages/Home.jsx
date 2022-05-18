import { View, StyleSheet } from 'react-native';
import useUserContext from '../hooks/useUserContext';
import StyledText from '../components/StyledText';

const extraerPrimerNombre = (nombres_del_usuario) => {
    const nombres = nombres_del_usuario.split(' ');
    return nombres[0];
}

const Home = () => {
    const { user } = useUserContext();

    return (
        <View style={styles.container}>
            <View style={styles.card}>
                <StyledText 
                fontWeight="bold"
                color="white"
                align="center"
                fontSize="subheading">
                    Bienvenido {extraerPrimerNombre(user.nombres_del_usuario)} {extraerPrimerNombre(user.apellidos_del_usuario)}!
                </StyledText>
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#F5FCFF',
    },
    card: {
        backgroundColor: '#0d3498',
        height: 50,
        padding: 10,
        margin: 10,
        borderRadius: 10,
        borderWidth: 1,
        shadowColor: '#0d3498',
        shadowOffset: {
            width: 0,
            height: 2,
        
        },
        justifyContent: 'center',
        alignItems: 'center',
    },
})

export default Home;