import { StyleSheet, View, ScrollView, TouchableWithoutFeedback } from 'react-native'
import StyledText from './StyledText.jsx'
import Constants from 'expo-constants'
import theme from '../theme.js'
import { Link, useLocation } from 'react-router-native'
import Ionicons from '@expo/vector-icons/Ionicons';

const styles = StyleSheet.create({
    container: {
        backgroundColor: theme.appBar.primary,
        flexDirection: 'row',
        paddingTop: Constants.statusBarHeight + 10,
    },
    scroll: {
        paddingBottom: 15,
    },
    text: {
        color: theme.appBar.textSecondary,
        paddingHorizontal: 10,
    },
    active: {
        color: theme.appBar.textPrimary,
    },
    logout: {
        paddingBottom: 15,
        flexDirection:'row',
        alignContent:'flex-end',
    }
})

const AppBarTab = ({ children, to }) => {
    const { pathname } = useLocation()
    const active = pathname === to

    const textStyles = [
        styles.text,
        active && styles.active
    ]
    return(
        <Link to={to} component={TouchableWithoutFeedback}>
            <StyledText fontWeight='bold' style={textStyles}>
                {children}
            </StyledText>
        </Link>
    )
}

const AppBar = () => {    
    return (
        <View style={styles.container}>
            <ScrollView horizontal style={styles.scroll}>
                <AppBarTab to='/'>Inicio</AppBarTab>
            </ScrollView>
            <View style={styles.logout}>
                <AppBarTab to='/signin'>
                    Cerrar Sesión <Ionicons name="log-out" size={16} style={{marginLeft:10}}/> 
                </AppBarTab>
            </View>
        </View>
    )
}

export default AppBar