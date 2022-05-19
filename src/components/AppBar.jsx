import { StyleSheet, View, ScrollView, TouchableWithoutFeedback } from 'react-native'
import { useState } from 'react'
import StyledText from './StyledText.jsx'
import Constants from 'expo-constants'
import theme from '../theme.js'
import { Link, useLocation } from 'react-router-native'
import Ionicons from '@expo/vector-icons/Ionicons';
import CustomAlert from './CustomAlert.jsx'

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
    const [showLogout, setShowLogout] = useState(false)
    return (
        <View style={styles.container}>
            <CustomAlert isShowed={showLogout} title="Cerrar Sesión" message="Estas seguro/a de cerrar tu sesión?">
                <View style={{flexDirection:'row', justifyContent:'space-between'}}>
                    <StyledText color='red' onPress={() => setShowLogout(false)}>Cancelar</StyledText>
                    <AppBarTab to='/signin' onPress={() => setShowLogout(false)}>
                        Cerrar Sesión
                    </AppBarTab>
                </View>
            </CustomAlert>
            <ScrollView horizontal style={styles.scroll}>
                <AppBarTab to='/'>Inicio</AppBarTab>
            </ScrollView>
            <View style={styles.logout}>
                <StyledText fontWeight='bold' style={styles.text} onPress={() => setShowLogout(true)}>
                    Cerrar Sesión <Ionicons name="log-out" size={16} style={{marginLeft:10}}/> 
                </StyledText>
            </View>
        </View>
    )
}

export default AppBar