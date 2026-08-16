from sqlalchemy import inspect

from app.db.database import engine
from app.db.models import (
    ClinicalEntity,
    Code,
    Document,
    Encounter,
    Patient,
    Prediction,
    Review,
    User,
)


MODELS = [
    User,
    Patient,
    Encounter,
    Document,
    ClinicalEntity,
    Code,
    Prediction,
    Review,
]


def test_model_relationships():
    print("Checking SQLAlchemy models...\n")

    for model in MODELS:
        mapper = inspect(model)

        print(f"{model.__name__} ({model.__tablename__})")

        for relationship in mapper.relationships:
            print(
                f"  └── {relationship.key}"
                f" → {relationship.mapper.class_.__name__}"
            )

        print()


if __name__ == "__main__":
    test_model_relationships()