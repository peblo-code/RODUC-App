import { Text, FlatList } from 'react-native';
import repositories from '../data/repositories.js';
import RepositoryItem from './RepositoryItem';

const RepositoryList = () => {
    return(
        <FlatList 
            data={repositories}
            ItemSeparatorComponent={() => <Text> </Text>}
            renderItem={({ item: repo }) => (
                <RepositoryItem {...repo} />
            )}
        >
        </FlatList>
    )
}

export default RepositoryList;