# Carros Deportivos - Página de Inicio

Este es el archivo HTML principal (`index.html`) de un sitio web dedicado a los **autos deportivos**. La página sirve como portal de bienvenida e introduce al usuario a la temática, marcas destacadas, novedades, y un formulario de suscripción.

---

## Contenido del sitio

La página está dividida en varias secciones:

- **Encabezado y Navegación:** Con enlaces a otras páginas del sitio como `modelos.html`, `contacto.html` y `caracteristicas.html`.
- **Acerca de Nosotros:** Breve descripción sobre la comunidad amante de los autos deportivos.
- **Marcas Destacadas:** Lista de fabricantes emblemáticos como Lamborghini, Ferrari, McLaren, entre otros.
- **Novedades:** Noticias recientes sobre lanzamientos y colaboraciones de marcas importantes.
- **Formulario de Suscripción:** Permite al usuario dejar su correo para recibir novedades.
- **Características del Sitio:** Razones para elegir esta comunidad.
- **Pie de página:** Derechos de autor.

---

## Archivos relacionados

- `index.html`: Página principal del sitio (este archivo).
- `estilos.css`: Archivo de estilos enlazado para dar formato y diseño visual (debe estar en la misma carpeta).
- Otras páginas vinculadas:  
  - `modelos.html`  
  - `contacto.html`  
  - `caracteristicas.html`

# Modelos Deportivos - Carros Deportivos

Esta página (`modelos.html`) forma parte del sitio **Carros Deportivos** y presenta una galería visual de modelos icónicos de autos deportivos de alto rendimiento.

---

## ¿Qué contiene esta página?

- Una **galería de autos deportivos** con imágenes y nombres.
- Cada modelo está dentro de un `<article>`, mostrando su **imagen** y su **nombre**.
- Las imágenes están alojadas en la carpeta `./Imagenes/`.

---

## Modelos incluidos

A continuación, los modelos de autos presentados:

1. **Ferrari SF90 Stradale**
2. **Lamborghini Huracán EVO**
3. **Porsche 911 Turbo S**
4. **Bugatti Chiron Super Sport**
5. **McLaren 720S**
6. **Audi R8 V10 Performance**
7. **Koenigsegg Agera**
8. **Corvette**
9. **Aston Martin Vantage**
10. **GTR-R35**
11. **Koenigsegg Jesko**
12. **Pagani Huayra**

---

## Archivos relacionados

- `modelos.html`: Esta página.
- `estilos.css`: Archivo de estilos enlazado para aplicar diseño visual.
- Carpeta `Imagenes/`: Contiene las imágenes de los autos.


# Características de Modelos - Carros Deportivos

Este archivo (`caracteristicas.html`) es parte del sitio **Carros Deportivos** y presenta una tabla comparativa detallada con las especificaciones técnicas de 12 autos deportivos de alto rendimiento.

---

## ¿Qué incluye esta página?

Cada modelo deportivo está representado por:

- Un `<article>` individual
- Un `<h3>` con el nombre del vehículo
- Una tabla `<table>` con especificaciones clave:
  - Motor
  - Potencia
  - Velocidad máxima
  - Aceleración 0-100 km/h
  - Tipo de tracción

---

## Modelos detallados

Esta página presenta especificaciones de los siguientes modelos:

1. **Ferrari SF90 Stradale**
2. **Lamborghini Huracán EVO**
3. **Porsche 911 Turbo S**
4. **Bugatti Chiron Super Sport**
5. **McLaren 720S**
6. **Audi R8 V10 Performance**
7. **Koenigsegg Agera**
8. **Corvette (C8 Z06)**
9. **Aston Martin Vantage**
10. **Nissan GT-R R35**
11. **Koenigsegg Jesko**
12. **Pagani Huayra**

---

## Archivos relacionados

- `caracteristicas.html`: Esta página.
- `estilos.css`: Archivo CSS para aplicar diseño visual.
- Imágenes no están presentes en esta página, pero se pueden añadir fácilmente por cada modelo si se desea.

---

## Tecnologías utilizadas

- HTML5
- CSS3 (vía archivo externo)
- Tablas HTML con etiquetas semánticas (`<table>`, `<thead>`, `<tr>`, `<th>`, `<td>`)
- Diseño responsive (meta viewport incluido)

---

## Notas importantes

- Las especificaciones están organizadas en tablas para facilitar la comparación técnica.
- Algunas cifras están sujetas a variación según versiones específicas de los modelos (por ejemplo, **Koenigsegg Agera RS** vs estándar).
- Las unidades están en **km/h** y **hp**, adecuadas para el mercado hispanohablante.


# Página de Contacto - Carros Deportivos

Este archivo (`contacto.html`) forma parte del sitio **Carros Deportivos** y permite a los usuarios **enviar consultas, sugerencias o comentarios** mediante un formulario de contacto.

---

## ¿Qué incluye esta página?

- Un encabezado con navegación global hacia las otras secciones del sitio.
- Una sección principal con un **formulario de contacto** estructurado con los siguientes campos:
  - **Nombre** (`<input type="text">`)
  - **Correo electrónico** (`<input type="email">`)
  - **Mensaje** (`<textarea>`)
- Un botón para enviar el formulario.
- Un pie de página con derechos de autor.

---

## Archivos relacionados

- `contacto.html`: Esta página.
- `estilos.css`: Archivo de estilos donde se define el diseño visual (colores, espaciado, etc.).

---

## Funcionalidad

- El formulario usa `method="post"` y `action="#"`, lo que significa que **actualmente no está conectado a un backend** (no envía la información a ningún servidor).
- Todos los campos están marcados como `required`, lo cual **evita el envío sin completar el formulario**.


# Hoja de Estilos - Carros Deportivos (`estilos.css`)

Este archivo define todos los **estilos visuales** para el sitio web **Carros Deportivos**, incluyendo paleta de colores, tipografías, diseño de secciones, tablas, formularios y elementos interactivos.

---

## Estilos Generales

- **Reset universal**: Elimina márgenes, paddings y aplica `box-sizing: border-box` para control de layout.
- **Tipografía**: Fuente `Segoe UI`, moderna y legible.
- **Color de texto**: Predomina el blanco para contraste sobre fondos oscuros.

---

## Fondos y Temas

- `.fondo-inicio`, `.fondo-contacto`, etc.: Fondos con gradientes lineales para cada página.
- Uso de `linear-gradient()` para dar sensación de profundidad.

---

## Encabezado y Navegación

- **`<header>`** con fondo oscuro degradado y título con sombra.
- **`<nav>`** con enlaces estilizados:
  - Colores vibrantes (naranja, rojo, amarillo).
  - Efectos `hover` con `transform: scale()` y cambio de gradiente.
  - Diseño responsivo con `flex`.

---

## Secciones Principales

### `presentacion`
- Centrada, con fondo oscuro translúcido.
- Títulos grandes y coloridos.
- Botón con gradiente verde-azul.

### `caracteristicas`
- Lista de ventajas en tarjetas con bordes redondeados y sombreado.
- Fondo semitransparente para diferenciar visualmente.

---

## Galería de Modelos (`.galeria`)

- Diseño de **grid responsivo** con `auto-fit` y `minmax`.
- Tarjetas para cada vehículo:
  - Imagen con `object-fit: cover`.
  - Título sobre fondo translúcido.
  - Transiciones al hacer `hover`.

---

## Formulario de Contacto (`.formulario-contacto`)

- Fondo en gradiente azul celeste.
- Campos con bordes redondeados, efectos de `focus`.
- Botón con gradiente y efecto `hover`.

---

## Tablas de Especificaciones

- Tablas estilizadas con colores sutiles sobre fondo oscuro.
- Títulos (`caption`) destacados.
- Efecto "zebra striping" suave para mejorar la legibilidad.
- Responsive y con `border-collapse`.






