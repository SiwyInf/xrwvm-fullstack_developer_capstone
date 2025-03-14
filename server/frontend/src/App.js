import LoginPanel from "./components/Login/Login"
import Register from './components/Register/Register'; // jeśli komponent znajduje się w folderze components
import { Routes, Route } from "react-router-dom";
import Dealers from './components/Dealers/Dealers';
import Dealer from "./components/Dealers/Dealer"
import PostReview from "./components/Dealers/PostReview"
function App() {
  return (
    <Routes>
      <Route path="/register" element={<Register />} />
      <Route path="/login" element={<LoginPanel />} />
            <Route path="/dealers" element={<Dealers/>} />
            <Route path="/postreview/:id" element={<PostReview/>} />
            <Route path="/dealer/:id" element={<Dealer/>} />S
    </Routes>
  );
}
export default App;
