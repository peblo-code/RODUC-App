import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import StyledText from './StyledText';
import { FontAwesome } from '@expo/vector-icons';

const CardButton = ({ title, iconName, color, onPress }) => {
    return (
        <TouchableOpacity 
            style={styles.itemContainer}
            onPress={onPress}>
            <FontAwesome 
                name={iconName} 
                size={60} 
                color={color} 
            />
            <StyledText 
                fontSize="subheading"
                align="center"
                style={{marginTop: 10}}>
                {title}
            </StyledText>
        </TouchableOpacity>
    )
}

export default function CardMenu({navigation}) {
    return(
        <View style={styles.container}>
            <View style={styles.rowContainer}>
                <CardButton 
                    iconName="file-text-o"
                    color="#0d3498"
                    title="Nuevo Informe"
                    onPress={() => navigation.navigate('Nuevo Informe')}
                />
                <CardButton 
                    iconName="history"
                    color="#0d3498"
                    title="Historial"
                    onPress={() => navigation.navigate('Historial')}
                />
            </View>
            <View style={styles.rowContainer}>
                <CardButton 
                    iconName="user"
                    color="#0d3498"
                    title="Perfil"
                    onPress={() => navigation.navigate('Mi Perfil')}
                />
                <CardButton
                    iconName="info-circle"
                    color="#0d3498"
                    title="Acerda De"
                />
            </View>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        padding: 12,
        flexGrow: 1,
        justifyContent: 'center',
        height: '90%',
    },
    rowContainer: {
        width: '100%',
        height: '45%',
        marginBottom: 12,
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    itemContainer: {
        backgroundColor: '#f2f2f2',
        padding: 12,
        borderRadius: 4,
        width: '48%',
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.23,
        shadowRadius: 2.62,
        elevation: 4,
        justifyContent: 'center',
        alignItems: 'center',
    },
});