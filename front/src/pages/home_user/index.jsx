import React, { useEffect, useState } from "react";
import axios from "axios";

const HomeUser = () => {
  const [usuarios, setUsuarios] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("token");

    axios.get("http://localhost:8000/api/usuarios", {
      headers: { Authorization: `Bearer ${token}` }
    })
    .then(response => {
      console.log("Dados da API:", response.data); 
      setUsuarios(response.data);
      setLoading(false);
    })
    .catch(error => {
      console.error("Erro ao buscar usuários:", error);
      setLoading(false);
    });
  }, []);

  if (loading) {
    return <p>Carregando usuários...</p>;
  }

  return (
    <div style={{ padding: "20px" }}>
      <h2>Lista de Usuários</h2>

      <table border="1" cellPadding="10" cellSpacing="0">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          {usuarios.map((usuario) => (
            <tr key={usuario.id}>
              <td>{usuario.id}</td>
              <td>{usuario.nome}</td>
              <td>{usuario.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default HomeUser;