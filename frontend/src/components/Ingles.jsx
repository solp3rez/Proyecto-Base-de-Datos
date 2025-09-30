import React, { useState, useEffect } from "react";
import { getIngles, postIngles } from "./api"; // Ajusta la ruta según donde esté api.js



function Ingles() {
  const [ingles, setIngles] = useState([]);

  useEffect(() => {
    getIngles().then(res => setIngles(res.data)).catch(err => console.error(err));
  }, []);

  const agregarApunte = () => {
    postIngles({ Apuntes: "Gramática", Profesor: "Juan" })
      .then(() => getIngles().then(res => setIngles(res.data)))
      .catch(err => console.error(err));
  };

  return (
    <div>
      <h1>Apuntes de Inglés</h1>
      <ul>
        {ingles.map(a => (
          <li key={a.Ingles_id}>
            {a.Apuntes} - {a.Profesor}
          </li>
        ))}
      </ul>
      <button onClick={agregarApunte}>Agregar Apunte</button>
    </div>
  );
}

export default Ingles;