import Main from './src/components/Main.jsx';
import { NativeRouter } from 'react-router-native';
import { StatusBar } from 'expo-status-bar';

export default function App() {
  return (
    <>
      <StatusBar style='light-content'/>
      <NativeRouter>
        <Main />
      </NativeRouter>
    </>
  );
}
