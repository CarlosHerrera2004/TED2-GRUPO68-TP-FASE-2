# Experiencia WebAR - Muestra de Micro-Racismos
## TED 2 - GRUPO 68

Experiencia interactiva de Realidad Aumentada sobre navegador móvil (**Image Tracking WebAR**) desarrollada con **MindAR** y **Three.js**, sin necesidad de instalar aplicaciones nativas.

---

## 🎨 Pantalla de Inicio y Diseño Visual

- **Fondo Institucional**: Ilustración orgánica en tonos lavanda y violeta (`assets/images/fondo.png`).
- **Botón Superior ("Volver al inicio")**: Botón rectangular en color temático institucional (`#9999CC` / CMYK `C:48.97 M:42.72 Y:0 K:0`) que enlaza directamente al sitio principal del proyecto en Wix: [https://mgalibnz.wixstudio.com/ted-2-grupo68](https://mgalibnz.wixstudio.com/ted-2-grupo68).
- **Título**: EXPERIENCIA DE REALIDAD AUMENTADA.
- **Subtítulo**: Muestra de Micro-Racismos.
- **Botón de Acción**: Botón rectangular "INICIAR EXPERIENCIA".
- **Indicador de Tracking Superior**: Indicador discreto que comunica exclusivamente el estado del reconocimiento físico:
  - 🟡 *Buscando imagen...*
  - 🟢 *Imagen detectada*
- **Finalización de la Experiencia**: Al concluir la animación de las 3 frases, el botón inferior se actualiza automáticamente a **"VOLVER HACIA ATRÁS"** para que el usuario pueda regresar a la pantalla inicial en cualquier momento.

---

## 🎬 Flujo de la Experiencia en 2 Partes

1. **Parte 1 (Puerta 3D)**:
   - Al reconocer el desplegable físico (`targets.mind`), emerge el modelo `puerta-3d.glb` centrado verticalmente.
   - Se reproducen sus animaciones de apertura y textos (~5.1s).
   - Realiza una transición suave de desvanecimiento (*Fade Out* de 0.8s).
2. **Parte 2 (Frases y Palabras 3D)**:
   - Aparece secuencialmente cada modelo de texto: `palabras1.glb`, `palabras2.glb` y `palabras3.glb`.
   - Escala calibrada (`TEXT_SCALE = 0.04`) para legibilidad óptima en celulares.
   - Entre cada frase hay una pausa de lectura ("un toquesin") y transiciones de *Fade In* y *Fade Out*.
   - Iluminación frontal y propiedad emisiva optimizada para garantizar colores vivos (rojo y azul) sobre cualquier iluminación ambiental.

---

## 💡 Cómo resaltar textos en 3D (Rebordes / Outlines)

Para que los textos resalten al máximo sobre la cámara del celular existen dos caminos complementarios:

### 1. Optimización en Código (Ya implementada en Three.js)
- **Emissive Boost**: Se inyecta un 25% de componente emisivo a los materiales de los textos y se añade una luz frontal directa (`frontLight`), evitando que las letras queden oscuras o apagadas frente a la cámara.

### 2. Reborde tipo Cómic / Toon Outline (En Blender antes de exportar)
Si querés que las letras tengan un contorno negro nítido 3D:
1. En **Blender**, seleccioná la malla del texto.
2. Agregá un modificador **Solidify**.
3. En las opciones del modificador:
   - **Mode**: Simple
   - **Thickness**: un valor negativo pequeño (ej. `-0.015 m`)
   - **Normals**: marcá la casilla **Flip Normals**.
   - **Materials**: poné **Material Offset = 1**.
4. En la pestaña de Materiales del objeto, agregá un segundo slot de material con color Negro puro (`#000000`) y Roughness en 1.0.
5. Exportá el `.glb`. El contorno se calculará automáticamente en tiempo real sin perder rendimiento.

---

## 📁 Estructura del Proyecto

```text
TED2-GRUPO68-TP-FASE-2/
├── index.html                  # Estructura HTML con pantalla de inicio y visor AR
├── README.md                   # Documentación técnica y guía de despliegue
├── iniciar.bat                 # Script de prueba local en Windows
├── server.py                   # Servidor HTTP local con desactivación de caché
│
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions para despliegue automático en GitHub Pages
│
├── css/
│   └── style.css               # Diseño visual responsivo, botones rectangulares y fondo
│
├── js/
│   └── app.js                  # Lógica de Three.js, MindAR, secuencia en 2 fases y tracking
│
├── targets/
│   ├── targets.mind            # Archivo binario compilado del desplegable (horizontal)
│   └── target.mind             # Alias sincronizado para compatibilidad
│
└── assets/
    ├── images/
    │   └── fondo.png           # Fondo ilustrado de la pantalla de bienvenida
    └── models/
        ├── puerta-3d.glb       # Parte 1: Puerta 3D animada
        ├── palabras1.glb       # Parte 2: Frase 1 animada
        ├── palabras2.glb       # Parte 2: Frase 2 animada
        └── palabras3.glb       # Parte 2: Frase 3 animada
```

---

## 🌐 Despliegue en GitHub Pages (HTTPS Automático)

El proyecto incluye el workflow oficial de **GitHub Actions** (`.github/workflows/deploy.yml`) para publicar la WebAR de forma 100% estática y con HTTPS activo (obligatorio para la cámara del celular).

### Pasos para activar GitHub Pages en el repositorio:
1. Entrá a tu repositorio en GitHub: [https://github.com/CarlosHerrera2004/TED2-GRUPO68-TP-FASE-2](https://github.com/CarlosHerrera2004/TED2-GRUPO68-TP-FASE-2).
2. Hacé clic en la pestaña **Settings** (Configuración) arriba a la derecha.
3. En el menú lateral izquierdo, seleccioná **Pages**.
4. En la sección **Build and deployment**:
   - **Opción A (Recomendada con GitHub Actions)**: En *Source*, seleccioná **GitHub Actions**. El archivo `.github/workflows/deploy.yml` compilará y publicará el sitio automáticamente en cada push.
   - **Opción B (Directa de rama)**: En *Source*, seleccioná **Deploy from a branch**, elegí la rama `main` y la carpeta `/(root)`.
5. En pocos segundos, GitHub generará tu enlace público:
   ```text
   https://carlosherrera2004.github.io/TED2-GRUPO68-TP-FASE-2/
   ```
   ¡Ya podés abrir ese enlace desde cualquier celular con Chrome o Safari para escanear el desplegable físico!

---

## 💻 Pruebas Locales (Windows)

1. Hacé doble clic en `iniciar.bat`.
2. Presioná `Y` para iniciar el servidor local en `http://localhost:8000`.
3. Para pruebas móviles en la misma red local mediante un túnel HTTPS rápido:
   ```bash
   npx cloudflared tunnel --url http://localhost:8000
   ```
