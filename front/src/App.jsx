import {BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import Login from './pages/login';
import HomeUser from './pages/user/home';
import PropertiesUser from './pages/user/properties';
import ContractsUser from './pages/user/contracts';
import PaymentsUser from './pages/user/payments';
import PropertiesAdmin from './pages/admin/properties';
import ContractsAdmin from './pages/admin/contracts';
import PaymentsAdmin from './pages/admin/payments';
import HomeAdmin from './pages/admin/home';
import Register from './pages/register/register';

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login /> } />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        
        <Route path="/user/home" element={<HomeUser />} />
        <Route path="/user/properties" element={<PropertiesUser />} />
        <Route path="/user/contracts" element={<ContractsUser />} />
        <Route path="/user/payments" element={<PaymentsUser />} />
        
        <Route path="/admin/home" element={<HomeAdmin />} />
        <Route path="/admin/properties" element={<PropertiesAdmin />} />
        <Route path="/admin/contracts" element={<ContractsAdmin />} />
        <Route path="/admin/payments" element={<PaymentsAdmin />} />
      </Routes>
    </Router>
  );
}