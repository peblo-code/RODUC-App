import { Platform } from 'react-native';

const theme = {
    appBar: {
        primary: '#24292e',
        textSecondary: '#999',
        textPrimary: '#fff'
    },
    colors: {
        textPrimary: '#24292e',
        textSecondary: '#586869',   
        primary: '#8366d6',
        secondary: '#586069',
        white: '#fefefe',
    },
    fontSizes: {
        body: 14,
        subheading: 16,
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