import { Platform } from 'react-native';

const theme = {
    appBar: {
        primary: '#0d3498',
        textSecondary: '#999',
        textPrimary: '#fff',
        logOut: '#092979'
    },
    colors: {
        textPrimary: '#24292e',
        textSecondary: '#586869',   
        primary: '#8366d6',
        secondary: '#586069',
        white: '#fefefe',
        red: '#ff0000',
        blue: '#0000FF',
        speechBlue: '#3F48CC',
        lightBlue: '#027d9c'
    },
    fontSizes: {
        minimal: 12,
        body: 14,
        subheading: 16,
        heading: 20,
        large: 28,
    },
    fonts: {
        main: Platform.select({
            ios: 'Arial',
            android: 'Roboto',
            default: 'System'
        }),
    },
    fontWeights: {
       normal: '400',
       bold: '700'
    }
}

export default theme