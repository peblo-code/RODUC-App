import { View, StyleSheet, Button } from 'react-native';
import StyledText from '../components/StyledText';
import useUserContext from '../hooks/useUserContext';

const CardContainer = ({ children }) => {
    return (
        <View style={ styles.cardContainer }>
            { children }
        </View>
    )
}

const InfoBar = ({ user }) => {
    const { nombre_usuario, nombres_del_usuario, apellidos_del_usuario, direccion_email } = user;
    const styles = StyleSheet.create({
        infoContainerRow: {
            justifyContent: 'space-between',
            alignItems: 'center',
            width: '100%',
            justifyContent: 'space-between',
            flexDirection: 'row',
        },
        infoContainerColumn: {
            justifyContent: 'space-between',
            alignItems: 'center',
            width: '100%',
            height: '100%',
            flexDirection: 'column'
        },
        infoBarRow: {
            justifyContent: 'space-between',
            alignItems: 'center',
            width: '50%',
        },
        infoBarColumn: {
            alignItems: 'center',
            width: '95%',
            justifyContent: 'center'
        },
        bar: {
            borderColor: "#3F48CC", 
            borderWidth: 0.5,
            width: '100%', 
            marginVertical: 3,
            shadowColor: "#000",
            shadowOffset: {
                width: 0,
                height: 2,
            },
            shadowOpacity: 0.23,
            shadowRadius: 2.62,
            elevation: 4,
        }
    })

    return (
        <View style={styles.infoContainerColumn}>
            <View style={styles.infoBarColumn}>
                <StyledText
                    fontSize="subheading"
                    color="speechBlue">
                    USUARIO
                </StyledText>

                <View style={styles.bar}/>
                
                <StyledText
                    fontSize="subheading"
                    fontWeight="bold">
                    { nombre_usuario }
                </StyledText>
            </View>

            <View style={styles.infoContainerRow}>
                <View style={styles.infoBarRow}>
                    <StyledText
                        fontSize="subheading"
                        color="lightBlue">
                        NOMBRES
                    </StyledText>



                    <StyledText 
                        fontSize="subheading"
                        fontWeight="bold">
                        { nombres_del_usuario }
                    </StyledText>
                </View>

                <View style={styles.infoBarRow}>
                    <StyledText
                        fontSize="subheading"
                        color="lightBlue">
                        APELLIDOS
                    </StyledText>

 

                    <StyledText 
                        fontSize="subheading"
                        fontWeight="bold">
                        { apellidos_del_usuario }
                    </StyledText>
                </View>
            </View>
            <View style={styles.infoBarColumn}>
                <StyledText
                    fontSize="subheading"
                    color="speechBlue">
                    EMAIL
                </StyledText>

                <View style={styles.bar}/>
                
                <StyledText
                    fontSize="subheading"
                    fontWeight="bold">
                    { direccion_email }
                </StyledText>
            </View>
        </View>
    )
}

export default function UserView() {
    const { user } = useUserContext();
    return(
        <View style={ styles.container }>

            <View style={styles.image}>
                <StyledText
                    fontWeight="bold"
                    fontSize="large"
                    color="white">
                    {user.nombres_del_usuario[0]}{user.apellidos_del_usuario[0]}
                </StyledText>
            </View>
            <CardContainer>
                <InfoBar user={user} />
            </CardContainer>
            <View style={{ flexDirection:'row', justifyContent: 'flex-end' }}>
                <Button
                    title="Cambiar Contraseña"
                    onPress={ () => {
                        console.log('Cambiar contraseña');
                    } }
                />
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 12,
    },
    cardContainer: {
        justifyContent: 'space-between',
        height: 200,
        backgroundColor: '#fff',
        paddingVertical: 12,
        paddingHorizontal: 2,
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
    image: {
        width: 100,
        height: 100,
        backgroundColor: '#0d3498',
        borderRadius: 100,
        borderColor: '#fff',
        borderWidth: 5,
        justifyContent: 'center',
        alignItems: 'center',
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.23,
        shadowRadius: 2.62,
        elevation: 4,
        marginLeft: 120,
        marginVertical: 10
    }
});