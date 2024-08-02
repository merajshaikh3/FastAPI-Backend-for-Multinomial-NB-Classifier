from sklearn.pipeline import Pipeline
import os
import joblib
from typing import Optional
from .schemas import PredictionInput, PredictionOutput

class NewsgroupsModel:
    model: Optional[Pipeline] = None
    targets: Optional[list[str]] = None

    def load_model(self) -> None:
        """Loads the model"""
        model_file = os.path.join(os.path.dirname(__file__), "newsgroups_model.joblib")
        loaded_model: tuple[Pipeline, list[str]] = joblib.load(model_file)
        model, targets = loaded_model
        self.model = model
        self.targets = targets


    def predict(self, input: PredictionInput) -> PredictionOutput:
        """Runs a prediction"""
        if not self.model or not self.targets:
            raise RuntimeError("Model is not loaded")
        prediction = predict(self.model, input.text)
        category = self.targets[prediction]
        return PredictionOutput(category=category)
    

memory = joblib.Memory(location="app/cache.joblib")

@memory.cache(ignore=["model"])
def predict(model: Pipeline, text: str) -> int:
    prediction = model.predict([text])
    return prediction[0]

# x = NewsgroupsModel()
# x.load_model()
# p = x.model.predict(["computer cpu memory ram"])
# print(x.targets[p[0]])
