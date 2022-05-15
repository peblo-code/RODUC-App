import * as yup from 'yup'

export const loginValidationSchema = yup.object().shape({
    email: yup
        .string()
        .email('Ingrese un email válido')
        .required('El email es requerido'),
    password: yup
        .string()
        .min(5, 'Muy corto!')
        .max(20, 'Muy largo!')
        .required('Contraseña es requerida'),
})