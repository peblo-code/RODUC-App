import RNPickerSelect, { defaultStyles } from 'react-native-picker-select';
import { StyleSheet, Platform, Text } from 'react-native';  

export default function PickerSelect({ title, items, onValueChange }) {

    const isAndroid = Platform.OS === 'android';

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
          borderColor: 'red',
          borderRadius: 4,
          color: 'black',
          paddingRight: 30, // to ensure the text is never behind the icon
        },
        inputAndroid: {
          fontSize: 16,
          paddingHorizontal: 10,
          paddingVertical: 8,
          borderWidth: 0.5,
          borderColor: 'purple',
          borderRadius: 8,
          color: 'black',
          paddingRight: 30, // to ensure the text is never behind the icon
        },
    });

    return(
        <>
            <Text>{ title }</Text>
            <RNPickerSelect
                placeholder={ placeholder }
                items={ items }
                style={ pickerSelectStyles }
                useNativeAndroidPickerStyle={ isAndroid }
                onValueChange={ (value) => onValueChange ? onValueChange(value) : console.log(value) }
            />
        </> 
    )
    
}