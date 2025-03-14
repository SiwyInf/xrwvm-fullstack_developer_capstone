import LoginPanel from "./components/Login/Login"
import Register from './components/Register/Register'; // jeśli komponent znajduje się w folderze components
import { Routes, Route } from "react-router-dom";
import Dealers from './components/Dealers/Dealers';
function App() {
  return (
    <Routes>
      <Route path="/register" element={<Register />} />
      <Route path="/login" element={<LoginPanel />} />
            <Route path="/dealers" element={<Dealers/>} />
    </Routes>
  );
}
export default App;
