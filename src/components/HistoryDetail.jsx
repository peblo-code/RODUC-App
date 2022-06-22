import { StyleSheet } from 'react-native';
import NewForm from './NewForm';

function HistoryDetail({ navigation, route }) {
    const { editObj } = route.params;
    return (
        <NewForm navigation={ navigation } editObj={ editObj } />
    );
}

export default HistoryDetail;