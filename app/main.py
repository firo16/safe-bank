from fastapi import FastAPI

from app.config import settings


app = FastAPI(title="SafeBank API",
              description='edukacyjny symulator bankowosci',
              version='0.1.0',)

@app.get("/health")
def health_chcek():
    return {'status': 'ok',
            'application': settings.app_name,
            'enviroment': settings.enviroment,}

