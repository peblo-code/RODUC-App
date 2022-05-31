import { View, StyleSheet, Button } from 'react-native';
import useUserContext from '../hooks/useUserContext';
import RepositoryList from '../components/RepositoryList';
import { useNavigate } from 'react-router-native';
import theme from '../theme';

const extraerPrimerNombre = (nombres_del_usuario) => {
    const nombres = nombres_del_usuario.split(' ');
    return nombres[0];
}


const Home = ({navigation}) => {
    return (
        <View style={styles.container}>
            <RepositoryList />
            <View style={styles.btnNewForm}>
                <Button 
                    color={theme.appBar.primary} 
                    title="Registrar nuevo formulario" 
                    onPress={() => navigation.navigate('Nuevo Formulario')}/>
            </View>
        </View>

    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
    },

    btnNewForm: {
        justifyContent: 'center',
        alignItems: 'center',
        paddingVertical: 10,
        backgroundColor: '#f2f2f2',
    }

})

export default Home;