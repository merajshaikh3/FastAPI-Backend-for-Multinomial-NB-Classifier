from fastapi import FastAPI, Depends, status
from .predict import NewsgroupsModel, memory
from contextlib import asynccontextmanager
from .schemas import PredictionInput, PredictionOutput

newsgroups_model = NewsgroupsModel()

@asynccontextmanager
async def lifespan(app: FastAPI):
    newsgroups_model.load_model()
    yield

app = FastAPI(lifespan=lifespan)

@app.post("/prediction")
def prediction(output: PredictionOutput = Depends(newsgroups_model.predict)) -> PredictionOutput:
    return output

@app.delete("/cache", status_code=status.HTTP_204_NO_CONTENT)
def delete_cache():
    memory.clear()


