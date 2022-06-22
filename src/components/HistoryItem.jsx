import { View, StyleSheet, TouchableOpacity } from 'react-native';
import StyledText from './StyledText.jsx';
import HistoryStats from './HistoryStats.jsx';
import theme from '../theme.js';

const HistoryItemHeader = ({ carrera, asignatura, curso, plan, tipo_clase }) => (
    <View style={{ flexDirection: 'row', paddingBottom: 2 }}>
        <View style={{ flex: 1 }}>
            <StyledText fontWeight='bold' align="center">{carrera}</StyledText>
            <StyledText color='secondary' align="center">{asignatura}</StyledText>
            <View style={{flexDirection:'row', justifyContent:'space-between'}}>
                <StyledText style={styles.tipo_clase}>{tipo_clase}</StyledText>
                <StyledText style={styles.curso}>{curso}</StyledText>
                <StyledText style={styles.plan}>{plan}</StyledText>
            </View>
        </View>
    </View>
)

const HistoryItem = (props, navigation) => (
        <View key={props.id} style={styles.container}>
            <HistoryItemHeader {...props} />
            <HistoryStats {...props} />
        </View>
)


const styles = StyleSheet.create({
    container: {
        padding: 20,
        paddingVertical: 5
    },
    tipo_clase: {
        padding: 4,
        color: theme.colors.white,
        backgroundColor: theme.colors.primary,
        alignSelf: 'center',
        borderRadius: 4,
        marginVertical: 4,
        overflow: 'hidden',
    },
    curso: {
        padding: 4,
        color: theme.colors.white,
        backgroundColor: theme.colors.secondary,
        alignSelf: 'center',
        borderRadius: 4,
        marginVertical: 4,
        overflow: 'hidden',
    },
    plan: {
        padding: 4,
        color: theme.colors.white,
        backgroundColor: theme.colors.lightBlue,
        alignSelf: 'center',
        borderRadius: 4,
        marginVertical: 4,
        overflow: 'hidden',
    },

    image: {
        width: 48,
        height: 48,
        borderRadius: 4,
    }
})

export default HistoryItem;