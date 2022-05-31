import Main from './src/components/Main.jsx';
import { StatusBar } from 'expo-status-bar';
import { UserProvider } from './src/context/UserContext.js';

export default function App() {
  return (
    <UserProvider>
      <StatusBar style='light'/>
        <Main />
    </UserProvider>
  );
}
