# Plantilla para Informes de prácticas en LaTeX

En este repositorio se puede encontrar una plantilla hecha en LaTeX pensada para informes de prácticas científicas o de ingeniería de extensión relativamente breve (entre 10 y 30 páginas).

La plantilla se ha desarrollado en un ordenador con macOS, por lo que es probable que no todas las instrucciones que aparecen aquí sean válidas en todos los sistemas operativos.

**Plantilla de ejemplo:** [main.pdf](main.pdf)

**Contenidos:**

- [Plantilla para Informes de prácticas en LaTeX](#plantilla-para-informes-de-prácticas-en-latex)
  - [Modo de uso](#modo-de-uso)
  - [Integración con Visual Studio Code](#integración-con-visual-studio-code)
  - [Compresión del archivo PDF](#compresión-del-archivo-PDF)

## Modo de uso

La plantilla está pensada para compilarse desde un contenedor de Docker con la imagen `7rocky/latex` (disponible en [Docker Hub](https://hub.docker.com/repository/docker/7rocky/latex)), por lo que es necesario tener [Docker](https://docs.docker.com/get-docker/) instalado.

No es necesario instalar LaTeX en el ordenador de trabajo, ya que se puede compilar el código en un contenedor Docker mediante el siguiente comando desde el directorio `template` (donde está el archivo `main.tex`):

```bash
git clone https://github.com/7Rocky/plantilla-informe-LaTeX

cd plantilla-informe-LaTeX/template

docker run --rm -v $(pwd)/..:/project -it 7rocky/latex
```

Cuando termine de compilar, se puede abrir el archivo PDF generado mediante cualquier visor de PDF. En macOS se puede indicar desde la consola, modificando el comando anterior:

```bash
docker run --rm -v $(pwd)/..:/project -it 7rocky/latex && open main.pdf
```

La imagen de este contenedor es bastante pesada (4.2 GB), pero Docker permite usar el contenedor cuando se necesite y después borrarlo y recuperar espacio:

```bash
docker rmi 7rocky/latex
```

**Nota:** Es importante que la ruta absoluta del directorio de trabajo no tenga espacios. De lo contrario, el montaje del volumen de Docker mediante `-v $(pwd)/..:/project` no funcionará.

## Integración con Visual Studio Code

Se recomienda utilizar Visual Studio Code y configurar el siguiente _keybinding_ teniendo la Terminal integrada abierta en el directorio `template`:

```json
{
  "key": "cmd+t",
  "command": "workbench.action.terminal.sendSequence",
  "args": {
    "text": "docker run --rm -v $(pwd)/..:/project -it 7rocky/latex; open main.pdf\u000D"
  }
}
```

Con esto, cada vez que se pulse la combinación de teclas `cmd + T`, se compilará el documento LaTeX y se abrirá el archivo PDF resultante si no hay errores en el código.

## Compresión del archivo PDF

Si el archivo generado con LaTeX es muy grande, se puede comprimir el PDF utilizando GhostScript.

La imagen de Docker `7rocky/latex` ya tiene instalado GhostScript. Para comprimir el archivo `main.pdf` habrá que ejecutar:

```bash
docker run --rm -v $(pwd)/..:/project -it 7rocky/latex sh compress.sh
```

El archivo comprimido se llama `main-compressed.pdf`.
