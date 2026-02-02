> Cambio a Dólar (USD → CRC)

Aplicación web sencilla que muestra el **tipo de cambio de Dólar (USD) a Colón Costarricense (CRC)** en tiempo real, utilizando **Flask** como backend y **HTML/CSS/JS** como frontend.

El backend consume una API pública de tipo de cambio y expone un endpoint propio para el frontend.

>  Tecnologías usadas

- **Python 3**
- **Flask**
- **Flask-CORS**
- **Requests**
- **python-dotenv**
- **HTML / CSS / JavaScript**

## 📁 Estructura del proyecto

Cambio_a_dolar/
├─ static/
│ └─ assets/
│ └─ dolar.svg
├─ servidor_flask.py
├─ conversor.html
├─ requirements.txt
├─ .gitignore
├─ .env.example
└─ README.md

## ⚙️ Instalación y ejecución local

1️⃣ Clona el repositorio
```bash
git clone https://github.com/TU_USUARIO/TU_REPO.git
cd Cambio_a_dolar

2️⃣ Crea y activa el entorno virtual
Windows

python -m venv venv
venv\Scripts\activate

3️⃣ Instala las dependencias
pip install -r requirements.txt

4️⃣ Configura las variables de entorno
Crea un archivo .env en la raíz del proyecto basado en .env.example:

EXCHANGE_API_URL=https://open.er-api.com/v6/latest/USD

5️⃣ Ejecuta la aplicación
python servidor_flask.py

La aplicación estará disponible en:
http://127.0.0.1:5000


>Endpoints disponibles

GET /

Devuelve la página principal (conversor.html).

GET /api/exchange-rate

Devuelve el tipo de cambio USD → CRC en formato JSON.

Ejemplo de respuesta:

{
  "success": true,
  "rate": 530.25,
  "base": "USD",
  "target": "CRC"
}

🔐 Seguridad

No se incluyen claves ni secretos en el repositorio.

Las variables sensibles se manejan mediante variables de entorno (.env).

El entorno virtual (venv) y archivos temporales están ignorados con .gitignore.

📌 Notas

Este proyecto está pensado con fines educativos y demostrativos.

La API de tipo de cambio utilizada es pública.

Ideal como base para proyectos Flask más grandes o separación frontend/backend.

👤 Autor

Yordin Herrera
Proyecto académico / práctico con Flask y APIs REST.

📄 Licencia
Este proyecto es de uso libre para fines educativos.