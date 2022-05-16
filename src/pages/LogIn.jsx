import { StyleSheet, View, Button, Image } from 'react-native';
import { Formik, useField } from 'formik';
import StyledTextInput from '../components/StyledTextInput.jsx';
import StyledText from '../components/StyledText.jsx';
import { loginValidationSchema } from '../validationSchemas/login.js';
import axios from 'axios';

const initialValues = {
    email: '',
    password: ''
}

const logoSimple = require('../../assets/logo-simple.png');

const styles = StyleSheet.create({
    error: {
        color: 'red',
        fontSize: 12,
        marginBottom: 20,
        marginTop: -5
    },
    form: {
        marginHorizontal: 12,
        justifyContent: 'center',
        height: '80%',
    },
    loginLogo: {
        alignSelf: 'center',
        marginBottom: 20,
        width: 100,
        height: 100,
        resizeMode: 'contain',
        backgroundColor: '#004494',
        borderRadius: 5
    },
    image: {
        height: 100,
        width: 100,
        resizeMode: 'contain',
    }
});

const FormikInputValue = ({ name, ...props }) => {
    const [field, meta, helpers] = useField(name)
    return (
        <>
            <StyledTextInput
                error={meta.error}
                value={field.value}
                onChangeText={value => helpers.setValue(value)}
                {...props}
            />
            {meta.error && 
                <StyledText style={styles.error}>
                    {meta.error}
                </StyledText>
            }
        </>
    )
}

const authLogin = ({ email, password }) => {
    axios.get(`http://26.247.235.244:8000/restapi/lista_usuarios/${email}`)
    .then(response => {
        if(response.data.nombre_usuario.length > 0) {
            response.data.nombre_usuario === email && response.data.contraseña === password ?
                console.log('Login correcto') : console.log('Login incorrecto')
        }
    })
    .catch(error => {
        console.log(error);
    });
}

export default function LoginInPage() {
    return <Formik validationSchema={loginValidationSchema} initialValues={initialValues} onSubmit=
        {values => authLogin(values)}>
        {({ handleChange, handleSubmit, values }) => {
            return (
                <View style={styles.form}>
                    <View style={styles.loginLogo}>
                        <Image style={styles.image} source={ logoSimple }/>
                    </View>
                    <FormikInputValue
                        name="email"
                        placeholder="E-mail"
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
                </View>
            )
        }}
    </Formik>
}