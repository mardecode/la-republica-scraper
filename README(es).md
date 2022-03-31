# 📰 La república scraper

Este repositorio descarga las noticias diarias del periódico Colombiano **La República** https://www.larepublica.co/

Los pasos que se realizan son:

- 🔗 Los links de cada noticia son obtenidos
- 📰 Se accede a cada noticia
- 🧾 El título, resumen y cuerpo de la noticia son extraidos
- 📂 Cada noticia es almacenada en un archivo `título_de_la_noticia`.txt


## Requisitos
- python
  - requests
  - lxml

Puedes instalarlos así:

```
pip3 install requests
pip3 install lxml
```

## Ejecución
```
python3 scraper.py
```

Cada vez que se ejecute el archivo `scraper.py`, se descargará las noticias del día actual creando un folder donde el programa guardará la información. **Cada folder es nombrado don la fecha en la que fue ejecutado**. Todos los archivos son almacenados en la carpeta princial 📂 `data` si esta carpeta no existe, el programa la creará.  


> Por favor considera que este repositorio podría dejar de funcionar ya que La República está constantemente cambiando su estructura HTML. Si esto pasa, no dudes en dejar un issue. 