import { View, StyleSheet, Image } from 'react-native';
import StyledText from '../components/StyledText';

const CardContainer = ({ children }) => {
    return (
        <View style={ styles.cardContainer }>
            { children }
        </View>
    )
}

const logoRoduc = require('../../assets/roduc_ico.png'); //importar imagen
const logoUCI = require('../../assets/uci_logo.png'); //importar imagen

export default function UserView() {
    return(
        <View style={ styles.container }>
            <View style={ styles.imageContainer }>
                <Image style={styles.image} source={logoRoduc} />
                <Image style={styles.image} source={logoUCI} />
            </View>
            <CardContainer>
                <StyledText
                    fontWeight="bold"
                    color="primary"
                    fontSize="large"
                    align="center"
                    style={{ marginBottom: 20 }}>
                    RODUC
                </StyledText>
                <StyledText
                    color="secondary"
                    fontSize="subheading"
                    align="center"
                    style={{ marginBottom: 20 }}
                >
                    Es una aplicación móvil destinada al registro de actividades del docente. 
                    La misma fue desarrollada por alumnos de cuarto año de Ingeniería Informática.
                </StyledText>
                <StyledText
                    color="speechBlue"
                    fontSize="subheading"
                    align="center"
                    fontWeight="bold"
                >
                    Informática de la Universidad Católica - Campus Itapúa.
                    2022
                </StyledText>
            </CardContainer>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 12,
        justifyContent: 'center',
    },
    cardContainer: {
        backgroundColor: '#fff',
        paddingVertical: 12,
        paddingHorizontal: 8,
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
    imageContainer: {
        flexDirection: 'row',
        justifyContent: 'space-around',
    },
    image: {
        width: 100,
        height: 100,
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.23,
        shadowRadius: 2.62,
        elevation: 4,
        marginVertical: 10
    }
});