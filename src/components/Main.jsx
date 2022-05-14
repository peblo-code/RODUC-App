import { View } from 'react-native';
import AppBar from './AppBar.jsx';
import { Route, Routes } from 'react-router-native';
import LoginInPage from '../pages/LogIn.jsx';

const Main = () => {
    return(
        <View style={{flex: 1}}>
            <AppBar />
            <Routes>
                <Route path='/signin' element={<LoginInPage />} />
            </Routes>
        </View>
    )
}

export default Main;