import { StyleSheet, View, Button } from 'react-native';
import { Formik, useField } from 'formik';
import StyledTextInput from '../components/StyledTextInput.jsx';
import StyledText from '../components/StyledText.jsx';

const initialValues = {
    email: '',
    password: ''
}

const styles = StyleSheet.create({
    error: {
        color: 'red',
        fontSize: 12,
        marginBottom: 20,
        marginTop: -5
    },
    form: {
        margin: 12
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