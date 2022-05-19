import * as yup from 'yup'

export const loginValidationSchema = yup.object().shape({
    username: yup
        .string()
        .required('El nombre de usuario es requerido'),
    password: yup
        .string()
        .min(5, 'Muy corto!')
        .max(20, 'Muy largo!')
        .required('Contraseña es requerida'),
})