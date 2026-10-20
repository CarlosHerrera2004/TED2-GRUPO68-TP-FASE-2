# Experiencia WebAR - Muestra de Micro-Racismos
## TED 2 - GRUPO 68

Experiencia interactiva de Realidad Aumentada sobre navegador móvil (**Image Tracking WebAR**) desarrollada con **MindAR** y **Three.js**, sin necesidad de instalar aplicaciones nativas.

---

## 🎨 Pantalla de Inicio y Guía de Escaneo

- **Fondo Institucional**: Ilustración orgánica en tonos lavanda y violeta (`assets/images/fondo.png`).
- **Botón Superior ("Volver al inicio")**: Botón rectangular en color temático institucional (`#9999CC` / CMYK `C:48.97 M:42.72 Y:0 K:0`) que enlaza al sitio principal del proyecto: [https://mgalibnz.wixstudio.com/ted-2-grupo68](https://mgalibnz.wixstudio.com/ted-2-grupo68).
- **Título**: EXPERIENCIA DE REALIDAD AUMENTADA.
- **Subtítulo**: Muestra de Micro-Racismos.
- **Apartado de Escaneo Visual**:
  - Muestra miniaturas de los dos **grupos de caras** que se encuentran en el desplegable.
  - Aclaración para el usuario: **Se escanean los grupos de caras completos**, no rostros individuales.
- **Botón Rectangular**: "INICIAR EXPERIENCIA".
- **Indicador de Tracking Superior**:
  - 🟡 *Buscando imagen...*
  - 🟢 *Imagen detectada*
- **Finalización de la Experiencia**: Al concluir la animación de las 3 frases, el botón inferior se actualiza automáticamente a **"VOLVER HACIA ATRÁS"** para regresar a la pantalla inicial.

---

## 🎯 Cómo Funcionan los 2 Targets para la Misma Experiencia

La aplicación soporta **múltiples targets en un único archivo binario `.mind`** apuntando exactamente a la **misma experiencia interactiva** sin duplicar código ni modelos:

1. **Compilación conjunta**: Ambos grupos de caras se compilan en un único `targets.mind`:
   - `Target 0`: Grupo 1 de caras (`assets/images/target-grupo1.png`).
   - `Target 1`: Grupo 2 de caras (`assets/images/target-grupo2.png`).
2. **Experiencia compartida (`experienceGroup`)**: En Three.js, todos los modelos 3D (`puerta-3d` y las 3 frases de `palabras`) pertenecen a un único grupo contenedor.
3. **Anclaje dinámico**:
   - Si la cámara enfoca el **Grupo 1**, la experiencia se ancla automáticamente sobre el Grupo 1.
   - Si la cámara enfoca el **Grupo 2**, la experiencia se ancla automáticamente sobre el Grupo 2.
   - La secuencia interactiva se reproduce fluidamente sin importar cuál de los dos grupos se escanee primero.

### 🛠️ Cómo compilar los 2 Targets en `targets.mind`:

Tenés 2 formas sencillas:

#### Opción A (Local con la herramienta incluida):
1. Iniciá el servidor con `iniciar.bat` (o `python server.py`).
2. En tu navegador abrí:
   ```text
   http://localhost:8000/compilar.html
   ```
3. Hacé clic en **"COMPILAR ARCHIVO TARGETS.MIND"**.
4. La herramienta procesa ambas imágenes en tu navegador y actualiza automáticamente los archivos en la carpeta `targets/` (además de descargar una copia).

#### Opción B (Compilador oficial online de MindAR):
1. Entrá a: [https://hiukim.github.io/mind-ar-js-doc/tools/compile](https://hiukim.github.io/mind-ar-js-doc/tools/compile).
2. Arrastrá `target-grupo1.png` y luego `target-grupo2.png` a la ventana.
3. Hacé clic en **"Compile"**.
4. Descargá el archivo resultante como `targets.mind` y guardalo en `targets/targets.mind`.

---

## 🎬 Flujo de la Experiencia en 2 Partes

1. **Parte 1 (Puerta 3D)**:
   - Al reconocer cualquiera de los dos grupos de caras del desplegable, emerge el modelo `puerta-3d.glb` centrado verticalmente.
   - Se reproducen sus animaciones de apertura y textos (~5.1s).
   - Realiza una transición suave de desvanecimiento (*Fade Out* de 0.8s).
2. **Parte 2 (Frases y Palabras 3D)**:
   - Aparece secuencialmente cada modelo de texto: `palabras1.glb`, `palabras2.glb` y `palabras3.glb`.
   - Escala calibrada (`TEXT_SCALE = 0.04`) para legibilidad óptima en celulares.
   - Entre cada frase hay una pausa de lectura ("un toquesin") y transiciones de *Fade In* y *Fade Out*.
   - Iluminación frontal y componente emisivo calibrados para garantizar colores vivos (rojo y azul) sobre cualquier superficie física.

---

## 📁 Estructura del Proyecto

```text
TED2-GRUPO68-TP-FASE-2/
├── index.html                  # Pantalla de inicio con guía visual de targets y visor AR
├── compilar.html               # Herramienta local para compilar los 2 targets en targets.mind
├── README.md                   # Documentación técnica y guía de uso
├── iniciar.bat                 # Script de prueba local en Windows
├── server.py                   # Servidor HTTP local con endpoint para guardar targets
│
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions para despliegue automático en GitHub Pages
│
├── css/
│   └── style.css               # Estilos responsivos, botones rectangulares y grilla de targets
│
├── js/
│   └── app.js                  # Lógica Three.js, soporte multi-target y anclaje dinámico
│
├── targets/
│   ├── targets.mind            # Archivo binario compilado (reconocimiento de imagen)
│   └── target.mind             # Alias sincronizado para compatibilidad
│
└── assets/
    ├── images/
    │   ├── fondo.png           # Fondo ilustrado de la pantalla de bienvenida
    │   ├── target-grupo1.png   # Imagen del Grupo 1 de caras
    │   └── target-grupo2.png   # Imagen del Grupo 2 de caras
    └── models/
        ├── puerta-3d.glb       # Parte 1: Puerta 3D animada
        ├── palabras1.glb       # Parte 2: Frase 1 animada
        ├── palabras2.glb       # Parte 2: Frase 2 animada
        └── palabras3.glb       # Parte 2: Frase 3 animada
```

---

## 🌐 Despliegue en GitHub Pages (HTTPS Automático)

El proyecto incluye el workflow oficial de **GitHub Actions** (`.github/workflows/deploy.yml`) para publicar la WebAR de forma 100% estática y con HTTPS activo.

Enlace público del proyecto:
👉 **`https://carlosherrera2004.github.io/TED2-GRUPO68-TP-FASE-2/`**
