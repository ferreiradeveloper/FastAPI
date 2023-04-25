from fastapi import FastAPI #1 importar la lib

app = FastAPI() #2 instancia

@app.get("/")  #4 llamada a ruta root
async def root():  #3 funcion root async
    return "!Hola FastApi!"

@app.get("/url")  #4 llamada a ruta root
async def url():  #3 funcion root async
    return {"url_curso": "https://mouredev.com/python"}


'''
    levantar el server uvicor
    uvicorn main:app --reload
    CTRL+C para pararlo
    documentacion Swagger URL/docs
    documentacion Redocly URL/rdoc
'''








