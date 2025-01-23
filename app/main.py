# импортируем библиотеку для работы со случайными числами
import random

# импортируем класс для создания экземпляра FastAPI-приложения
from fastapi import FastAPI

# создаём экземпляр FastAPI-приложения
app = FastAPI()

# обрабатываем запросы к корню приложения
@app.get("/")
def read_root():
    return {"Hello": "World"}

# обрабатываем запросы к специальному пути для получения предсказания модели
# временно имитируем предсказание со случайной генерацией score
@app.get("/api/churn/{user_id}")
def get_prediction_for_item(user_id: str):
    return {"user_id": user_id, "score": random.random()}

# обработка GET-запросов к URL /service-status
@app.get("/service-status")
def health_check():
    return {"status": "ok"}

# обрабатываем GET-запросы по пути /api/credit/{client_id},
# чтобы узнать, выдать кредит или нет на основании кредитного score клиента
@app.get("/api/credit/{client_id}")
def is_credit_approved(client_id: int):
    score = random.uniform(0, 1)  # генерируем случайный score от 0 до 1
    if score > 0.8:
        return {"approved": 1}
    else:
        return {"approved": 0}