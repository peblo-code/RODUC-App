import { View, StyleSheet } from 'react-native';
import StyledText from './StyledText.jsx';
import RepositoryStats from './RepositoryStats.jsx';
import theme from '../theme.js';

const RepositoryItemHeader = ({ carrera, asignatura, curso, plan }) => (
    <View style={{ flexDirection: 'row', paddingBottom: 2 }}>
        <View style={{ flex: 1 }}>
            <StyledText fontWeight='bold' align="center">{carrera}</StyledText>
            <StyledText color='secondary' align="center">{asignatura}</StyledText>
            <View style={{flexDirection:'row', justifyContent:'center'}}>
                <StyledText style={styles.curso}>{curso}</StyledText>
                <StyledText style={styles.plan}>{plan}</StyledText>
            </View>
        </View>
    </View>
)

const RepositoryItem = (props) => (
    <View key={props.id} style={styles.container}>
        <RepositoryItemHeader {...props} />
        <RepositoryStats {...props} />
    </View>
)


const styles = StyleSheet.create({
    container: {
        padding: 20,
        paddingVertical: 5
    },
    curso: {
        padding: 4,
        color: theme.colors.white,
        backgroundColor: theme.colors.primary,
        alignSelf: 'flex-start',
        borderRadius: 4,
        marginVertical: 4,
        overflow: 'hidden',
        marginRight: 15
    },
    plan: {
        padding: 4,
        color: theme.colors.white,
        backgroundColor: theme.colors.secondary,
        alignSelf: 'flex-start',
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

export default RepositoryItem;