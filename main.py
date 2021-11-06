# import uvicorn
from fastapi import FastAPI
app = FastAPI()


@app.get('/')
def index():
    return {'message': 'index page'}

# uvicorn.run(app=app, host='127.0.0.1', port=5000, reload=True)
#
# main
# # Created by Sergey Yaksanov at 07.10.2021
# Copyright © 2020 Yakser. All rights reserved.
