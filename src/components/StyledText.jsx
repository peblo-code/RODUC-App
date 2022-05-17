import { Text, StyleSheet } from 'react-native';
import theme from '../theme.js';

const styles = StyleSheet.create({
    text: {
        color: theme.colors.textPrimary,
        fontSize: theme.fontSizes.body,
        fontFamily: theme.fonts.main,
        fontWeight: theme.fontWeights.normal,
    },
    colorPrimary: {
        color: theme.colors.primary,
    },
    colorSecondary: {
        color: theme.colors.secondary,
    },
    colorWhite: {
        color: theme.colors.white,
    },
    colorRed: {
        color: theme.colors.red,
    },
    bold: {
        fontWeight: theme.fontWeights.bold,
    },
    minimal: {
        fontSize: theme.fontSizes.minimal,
    },
    subheading: {
        fontSize: theme.fontSizes.subheading,
    },
    large: {
        fontSize: theme.fontSizes.large,
    },
    textAlignCenter: {
        textAlign: 'center',
    },
    
})

export default function StyledText ({children, align, color, fontSize, fontWeight, 
    style, ...restOfProps}) {
    const textStyles = [
        styles.text,
        align === 'center' && styles.textAlignCenter,
        color === 'primary' && styles.colorPrimary,
        color === 'secondary' && styles.colorSecondary,
        color === 'white' && styles.colorWhite,
        color === 'red' && styles.colorRed,
        fontSize && 'minimal' && styles.minimal,
        fontSize === 'subheading' && styles.subheading,
        fontSize === 'large' && styles.large,
        fontWeight === 'bold' && styles.bold,
        style
    ]

    return (
       <Text style={textStyles} {...restOfProps}>
           {children}
       </Text> 
    )
}