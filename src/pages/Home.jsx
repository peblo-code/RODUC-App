import { View, StyleSheet, Button } from 'react-native';
import useUserContext from '../hooks/useUserContext';
import RepositoryList from '../components/RepositoryList';
import StyledText from '../components/StyledText';
import theme from '../theme';
import CardMenu from '../components/CardMenu';

const extraerPrimerNombre = (nombres_del_usuario) => {
    const nombres = nombres_del_usuario.split(' ');
    return nombres[0];
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
                        Bienvenido {extraerPrimerNombre(nombres_del_usuario)} {extraerPrimerNombre(apellidos_del_usuario)}
                </StyledText>
                <StyledText
                    fontSize="heading"
                    align="start">
                        Seleccione una opción
                </StyledText>
                <CardMenu navigation={navigation}/>
            </View>
            {/* <View style={styles.btnNewForm}>
                <Button 
                    color={theme.appBar.primary} 
                    title="Registrar nuevo formulario" 
                    onPress={() => navigation.navigate('Nuevo Formulario')}/>
            </View> */}
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