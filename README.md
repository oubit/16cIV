# Instrucciones

## Consideraciones RTD + Sphinx
Todo, empezando por el índice, debe estar dentro de la carpeta `docs`.
Los `title` y estructura de carpetas, debe estar definida en un fichero aparte.

## Dependencias
https://docs.readthedocs.io/en/stable/guides/specifying-dependencies.html

## Varias cuentas de GitHub
Artículos:
- https://medium.com/@pinglinh/how-to-have-2-github-accounts-on-one-machine-windows-69b5b4c5b14e
- https://docs.github.com/en/free-pro-team@latest/developers/overview/managing-deploy-keys#deploy-keys

El punto clave final es el comando:
```
git remote set-url origin git@github.com:oubit/16cIV.git
```

Esto hará que realmente use el fichero RSA generado.
Preguntará si es un destino de confianza, generando en la carpeta `~/.ssh` el fichero:
- known_hosts

## Themes

https://sphinx-themes.org

Parece que solo pueden usarse los built-in
https://stackoverflow.com/questions/45878953/use-custom-theme-on-readthedocs

## Editar restructuredText en VSCode

Hay varios plugins, pero muchos prerequisitos.

https://docs.restructuredtext.net/articles/prerequisites.html#install-python-for-most-features

## Para correrlo en local

https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html

## A instalar

https://sphinx-hoverxref.readthedocs.io/en/latest/
copybutton