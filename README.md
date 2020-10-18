# Plantilla para Informes de prácticas en LaTeX

En este repositorio se puede encontrar una plantilla hecha en LaTeX pensada para informes de prácticas científicas o de ingeniería de extensión relativamente breve (entre 10 y 30 páginas).

La plantilla se ha desarrollado en un ordenador con macOS, por lo que es probable que no todas las instrucciones que aparecen aquí sean válidas en todos los sistemas operativos.

**Plantilla de ejemplo:** [main.pdf](main.pdf)

**Contenidos:**

- [Plantilla para Informes de prácticas en LaTeX](#plantilla-para-informes-de-prácticas-en-latex)
  - [Uso con LaTeX y Pygments instalados](#h2-iduso-con-latex-y-pygments-instalados-131uso-con-latex-y-pygments-instaladosh2)
  - [Uso con Docker instalado](#h2-iduso-con-docker-instalado-108uso-con-docker-instaladoh2)
  - [Instalación de LaTeX](#h2-idinstalación-de-latex-169instalación-de-latexh2)
    - [MacTeX](#mactex)
    - [TeX Live](#tex-live)
  - [Instalación de Pygments](#h2-idinstalación-de-pygments-187instalación-de-pygmentsh2)

## Uso con LaTeX y Pygments instalados

Si se tiene LaTeX y Pygments instalados, se puede clonar el repositorio o descargar un archivo comprimido. Desde ahí, se puede acceder a la carpeta del proyecto y ejecutar el comando:

```bash
pdflatex -shell-escape -interaction=nonstopmode -halt-on-error main
```

Si se quiere abrir el archivo PDF generado, se puede usar cualquier visor de PDF. En macOS, se puede abrir desde la consola, modificando el comando anterior:

```bash
pdflatex -shell-escape -interaction=nonstopmode -halt-on-error main && open main.pdf
```

Se recomienda utilizar Visual Studio Code y configurar el siguiente _keybinding_:

```json
{
  "key": "cmd+t",
  "command": "workbench.action.terminal.sendSequence",
  "args": {
    "text": "pdflatex -shell-escape -interaction=nonstopmode -halt-on-error main; open main.pdf\u000D"
  }
}
```

Con esto, cada vez que se pulse la combinación de teclas `cmd + T`, se compilará el documento LaTeX y se abrirá el archivo PDF resultante si no hay errores en el código.

## Uso con Docker instalado

Si se dispone de [Docker](https://docs.docker.com/get-docker/) instalado, no es necesario instalar LaTeX, ya que se puede compilar el código en un contenedor Docker mediante el siguiente comando desde el directorio principal (donde esté el archivo `main.tex`):

```bash
docker run -v $(pwd):/project -it 7rocky/latex
```

Cuando termine de compilar, se puede abrir el archivo PDF generado mediante cualquier visor de PDF. En macOS se puede indicar desde la consola, modificando el comando anterior:

```bash
docker run -v $(pwd):/project -it 7rocky/latex && open main.pdf
```

Este contenedor es bastante pesado, ocupa 4.2 GB, pero el usar Docker permite usar el contenedor cuando se necesite y después borrarlo y recuperar espacio.

Desde Visual Studio Code, el _keybinding_ se puede cambiar entonces por:

```json
{
  "key": "cmd+t",
  "command": "workbench.action.terminal.sendSequence",
  "args": {
    "text": "docker run -v $(pwd):/project -it 7rocky/latex; open main.pdf\u000D"
  }
}
```

Además, evita que se tenga que instalar LaTeX y sus dependencias en el equipo local.

## Instalación de LaTeX

### MacTeX

[MacTeX](https://tug.org/mactex/) es una versión de TeX Live para macOS (es probable que la versión 2020 dé algunos fallos. Este proyecto está realizado en la versión 2019). Desde la página web se puede descargar un instalador de MacTeX que instalará los programas para usar LaTeX y otras aplicaciones.

Se puede instalar también con Homebrew:

```bash
brew cask install mactex
```

Este paquete MacTeX trae programas como TeX Shop, LaTeXiT o BibDesk, pero no son necesarios. Si se prefiere no instalarlos existe otro paquete de Homebrew:

```bash
brew cask install mactex-no-gui
```

### TeX Live

En Linux (Ubuntu) se puede instalar LaTeX mediante:

```bash
sudo apt install texlive-full
```

Existen otros paquetes de `texlive` en el repositorio de `apt`. Si se tienen conocimientos sobre las funcionalidades que se necesitan para compilar el documento, se pueden elegir los paquetes induvidualmente en lugar del paquete `texlive-full`, que es bastante pesado.

No obstante, es recomendable instalar `texlive-full` para evitar problemas.

## Instalación de Pygments

Tambien es necesario tener el paquete [Pygments](https://pygments.org) instalado para que funcione el resaltado de código fuente.

Se puede instalar mediante Python y `pip`:

```bash
pip install Pygments
```

También se puede instalar en Linux (Ubuntu) con:

```bash
sudo apt install python3-pygments
```

O en macOS con Homebrew:

```bash
brew install pygments
```
