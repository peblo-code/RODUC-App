import { FontAwesome } from '@expo/vector-icons';
import { TouchableOpacity } from 'react-native';

const TouchIcon = ({ name, size, color, onPress }) => (
    <TouchableOpacity onPress={onPress}>
        <FontAwesome name={name} size={size} color={color} />
    </TouchableOpacity>
);

export default TouchIcon;