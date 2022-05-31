import Main from './src/components/Main.jsx';
import { NativeRouter } from 'react-router-native';
import { StatusBar } from 'expo-status-bar';
import { UserProvider } from './src/context/UserContext.js';

export default function App() {
  return (
    <UserProvider>
      <StatusBar style='light'/>
      <NativeRouter>
        <Main />
      </NativeRouter>
    </UserProvider>
  );
}
