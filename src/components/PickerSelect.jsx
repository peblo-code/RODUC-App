import RNPickerSelect, { defaultStyles } from 'react-native-picker-select';
import { StyleSheet, View } from 'react-native';  
import StyledText from './StyledText';
import theme from '../theme';
import { useState, useEffect } from 'react';

export default function PickerSelect({ title, items, selectedValue, setPicker, setSelected }) {

    const placeholder = {
        label: 'Seleccione una opción',
        value: null,
        color: '#9EA0A4',
    };

    const pickerSelectStyles = StyleSheet.create({
        inputIOS: {
          fontSize: 16,
          paddingVertical: 12,
          paddingHorizontal: 10,
          borderWidth: 1,
          borderColor: theme.colors.speechBlue,
          borderRadius: 4,
          color: 'black',
          paddingRight: 30, // to ensure the text is never behind the icon
        },
        inputAndroid: {
          fontSize: 16,
          paddingHorizontal: 10,
          paddingVertical: 8,
          borderWidth: 0.5,
          borderColor: theme.colors.primary,
          borderRadius: 8,
          color: 'black',
          paddingRight: 30, // to ensure the text is never behind the icon
        },
    });

    return(
        <View style={{marginBottom: 10}}>
            <StyledText
                fontSize="subheading"
                fontWeight="bold"
                color="secondary"
            >{ title }</StyledText>
            <RNPickerSelect
                placeholder={ placeholder }
                items={ items }
                style={ pickerSelectStyles }
                useNativeAndroidPickerStyle={ false }
                value={ selectedValue }
                onValueChange={ (value) => { 
                    setPicker ? setPicker(value) : console.log(value)
                    setSelected ? setSelected(value) : console.log(value)
                }}
            />
        </View> 
    )
}