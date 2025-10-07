import { useState, useEffect } from "react";

export default function Ingles() {
  const [apuntes, setApuntes] = useState([]);
  const [titulo, setTitulo] = useState("");
  const [contenido, setContenido] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000/apuntes")
      .then(res => res.json())
      .then(data => setApuntes(data))
      .catch(err => console.error(err));
  }, []);

  const handleRegistrar = async (e) => {
    e.preventDefault();
    if (!titulo || !contenido) return;

    try {
      const res = await fetch("http://localhost:5000/apuntes", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ titulo, contenido }),
      });
      await res.json();
      setApuntes([...apuntes, { titulo, contenido }]);
      setTitulo("");
      setContenido("");
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{
      minHeight: "100vh",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      padding: "50px",
      fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
      color: "#333"
    }}>
      {/* Título */}
      <h1 style={{
  marginBottom: "10px",
  fontSize: "3rem",
  textAlign: "center",
  background: "linear-gradient(90deg, #00CED1, #1E90FF)",
  WebkitBackgroundClip: "text",
  WebkitTextFillColor: "transparent",
  fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
  letterSpacing: "1px"
}}>
   Apuntes UBA
</h1>


      <p style={{ marginBottom: "30px", fontSize: "1.2rem", color: "#666" }}>Registra tu apunte</p>

      {/* Formulario */}
      <form onSubmit={handleRegistrar} style={{
        display: "flex",
        flexDirection: "column",
        gap: "15px",
        width: "100%",
        maxWidth: "500px",
        marginBottom: "40px"
      }}>
        <input
          type="text"
          placeholder="Título"
          value={titulo}
          onChange={(e) => setTitulo(e.target.value)}
          style={{
            padding: "14px",
            fontSize: "16px",
            borderRadius: "8px",
            border: "1px solid #ccc",
            outline: "none",
            boxShadow: "0 2px 5px rgba(129, 40, 40, 0.1)",
            transition: "0.3s"
          }}
          onFocus={e => e.currentTarget.style.borderColor = "#00CED1"}
          onBlur={e => e.currentTarget.style.borderColor = "#ccc"}
        />
        <input
          type="text"
          placeholder="Contenido"
          value={contenido}
          onChange={(e) => setContenido(e.target.value)}
          style={{
            padding: "14px",
            fontSize: "16px",
            borderRadius: "8px",
            border: "1px solid #ccc",
            outline: "none",
            boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
            transition: "0.3s"
          }}
          onFocus={e => e.currentTarget.style.borderColor = "#00CED1"}
          onBlur={e => e.currentTarget.style.borderColor = "#ccc"}
        />
        <button
          type="submit"
          style={{
            padding: "14px",
            fontSize: "16px",
            borderRadius: "8px",
            border: "none",
            fontWeight: "bold",
            backgroundColor: "#00CED1",
            color: "#fff",
            cursor: "pointer",
            transition: "all 0.3s",
            boxShadow: "0 4px 6px rgba(0,0,0,0.15)"
          }}
          onMouseOver={e => {
            e.currentTarget.style.backgroundColor = "#00b7c7";
            e.currentTarget.style.transform = "translateY(-2px)";
          }}
          onMouseOut={e => {
            e.currentTarget.style.backgroundColor = "#00CED1";
            e.currentTarget.style.transform = "translateY(0)";
          }}
        >
          Registrar
        </button>
      </form>

      {/* Lista de apuntes */}
      <ul style={{ listStyle: "none", padding: 0, width: "100%", maxWidth: "500px" }}>
        {apuntes.map((a, i) => (
          <li key={i} style={{
            backgroundColor: "#fff",
            borderRadius: "10px",
            padding: "18px",
            marginBottom: "15px",
            textAlign: "left",
            color: "#333",
            boxShadow: "0 4px 10px rgba(0,0,0,0.1)",
            transition: "all 0.3s"
          }}
          onMouseOver={e => e.currentTarget.style.boxShadow = "0 8px 16px rgba(0,0,0,0.2)"}
          onMouseOut={e => e.currentTarget.style.boxShadow = "0 4px 10px rgba(0,0,0,0.1)"}
          >
            <h3 style={{ margin: "0 0 6px 0" }}>{a.titulo}</h3>
            <p style={{ margin: 0 }}>{a.contenido}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
