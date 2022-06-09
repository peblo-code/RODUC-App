import { View } from 'react-native';
import StyledText from './StyledText.jsx';

const parseThousands = value => {
    return value >= 1000
    ? `${Math.round(value / 1000)}k`
    : String(value)
}

const HistoryStats = (props) => {
    return(
        <View style={{flexDirection: 'row', justifyContent: 'space-around'}}>
            <View>
                <StyledText align='center' fontWeight='bold'>{parseThousands(props.fecha)}</StyledText>
                <StyledText align='center'>Fecha de Clase</StyledText>
            </View>
            <View>
                <StyledText align='center' fontWeight='bold'>{parseThousands(props.horaInicio)}</StyledText>
                <StyledText align='center'>Hora de Inicio</StyledText>
            </View>
            <View>
                <StyledText align='center' fontWeight='bold'>{parseThousands(props.horaFin)}</StyledText>
                <StyledText align='center'>Hora de Fin</StyledText>
            </View>
        </View>
    )
}

export default HistoryStats;