import { StyleSheet, View, Button, Image, Alert, ActivityIndicator } from 'react-native';
import { Formik, useField } from 'formik';
import StyledTextInput from '../components/StyledTextInput.jsx';
import StyledText from '../components/StyledText.jsx';
import { loginValidationSchema } from '../validationSchemas/login.js';
import useUserContext from '../hooks/useUserContext.js';
import { useEffect, useState } from 'react';
import ModalStyled from '../components/ModalStyled.jsx';

const initialValues = { //valores iniciales
    username: '',
    password: ''
}

const logoSimple = require('../../assets/logo-simple.png'); //importar imagen

const styles = StyleSheet.create({ //estilos
    error: {
        marginBottom: 20,
        marginTop: -5
    },
    form: {
        marginHorizontal: 12,
        justifyContent: 'center',
        height: '100%',
    },
    loginLogo: {
        alignSelf: 'center',
        marginBottom: 50,
        width: 100,
        height: 100,
        resizeMode: 'contain',
        backgroundColor: '#004494',
        borderRadius: 5,
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 6,
        },
        shadowOpacity: 0.37,
        shadowRadius: 7.49,
        elevation: 12,
    },
    image: {
        height: 100,
        width: 100,
        resizeMode: 'contain',
        marginBottom: 10
    }
});

const FormikInputValue = ({ name, ...props }) => { //funcion para obtener el valor del input
    const [field, meta, helpers] = useField(name) //obtener el valor del input
    return (
        <>
            <StyledTextInput
                error={meta.error}
                value={field.value}
                onChangeText={value => helpers.setValue(value)}
                {...props}
            />
            {meta.error &&
                <StyledText
                    color="red"
                    fontSize="minimal"
                    style={styles.error}>
                    {meta.error}
                </StyledText>
            }
        </>
    )
}

export default function LoginInPage() {
    const { Auth, closeSession, error, setError } = useUserContext(); //obtener el contexto
    const [isLoading, setIsLoading] = useState(false); //estado del loading

    useEffect(() => { //funcion para cerrar sesion
        closeSession();
    }, []);

    useEffect(() => { //funcion para mostrar error
        if(error != '') {
            Alert.alert(
                'Ups!',
                error,
                [
                    { text: 'OK', onPress: () => setIsLoading(false) },
                ],
                { cancelable: false },
            );
        }
        setError(false);
    }, [error]);

    return <Formik validationSchema={loginValidationSchema} initialValues={initialValues} onSubmit=
        {values => {
            Auth(values);
            setIsLoading(true);
        }}>
        {({ handleChange, handleSubmit, values }) => {
            return (
                <View style={styles.form}>
                    <ModalStyled isVisible={isLoading}>
                        <StyledText
                            align='center'
                            color='primary'
                            fontSize='subheading'>Iniciando Sesión</StyledText>
                        <ActivityIndicator style={{ marginTop: 10 }} size="large" color="#004494" />
                    </ModalStyled>
                    <View style={styles.loginLogo}>
                        <Image style={styles.image} source={logoSimple} />
                        <StyledText
                            align='center'
                            color='blue'
                            fontWeight='bold'
                            fontSize='heading'>RODUC</StyledText>
                    </View>
                    <FormikInputValue
                        name="username"
                        placeholder="Usuario"
                    />
                    <FormikInputValue
                        name="password"
                        placeholder="Contraseña"
                        secureTextEntry
                    />
                    <Button
                        onPress={handleSubmit}
                        title="Iniciar Sesión"
                    />
                    <StyledText
                        style={{
                            marginTop: 30
                        }}
                        align='center'
                        color='black'
                        fontSize='subheading'>Ingeniería Informática 2022</StyledText>
                </View>
            )
        }}
    </Formik>
}