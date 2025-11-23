from fastapi import FastAPI
import src.controller as routes


app = FastAPI()

app.include_router(routes.HealthController)
app.include_router(routes.LoginController)
app.include_router(routes.CurrencyPairController)
