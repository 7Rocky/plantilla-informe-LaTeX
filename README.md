# Plantilla para Informes de prácticas en LaTeX

En este repositorio se puede encontrar una plantilla hecha en LaTeX pensada para informes de prácticas científicas o de ingeniería de extensión relativamente breve (entre 10 y 20 páginas).

La plantilla se ha desarrollado en un ordenador con macOS, por lo que es probable que no todas las instrucciones que aparecen aquí sean válidas en todos los sistemas operativos.

En primer lugar, es necesario tener LaTeX instalado. Para macOS, se recomienda instalar MacTeX (es probable que la versión 2020 dé algunos fallos. Este proyecto está realizado en la versión 2019).

Una vez instalado, se puede clonar el repositorio o descargar un archivo comprimido. Desde ahí, se puede acceder a la carpeta del proyecto y ejecutar el comando:

```bash
pdflatex -shell-escape -interaction=nonstopmode -halt-on-error main
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


