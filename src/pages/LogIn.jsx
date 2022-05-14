import { StyleSheet, View, Button, Image } from 'react-native';
import { Formik, useField } from 'formik';
import StyledTextInput from '../components/StyledTextInput.jsx';
import StyledText from '../components/StyledText.jsx';

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

const validate = values => {
    const errors = {}

    if (!values.email) {
        errors.email = 'Email is Required'
    } else if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i.test(values.email)) {
        errors.email = 'Invalid email address'
    }

    console.log(errors)

    return errors;
}

export default function LoginInPage() {
    return <Formik validate={validate} initialValues={initialValues} onSubmit=
        {values => console.log(values)}>
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
                        placeholder="Password"
                        secureTextEntry
                    />
                    <Button
                        onPress={handleSubmit}
                        title="Log In"
                    />
                </View>
            )
        }}
    </Formik>
}