from fastapi import APIRouter

from src.models.preprocess_schema import (
    TextRequest,
    TextResponse
)

from src.services.preprocessing_service import preprocess_text

from src.utils.logger import logger


router = APIRouter()


@router.post(
    "/preprocess",
    response_model=TextResponse,
    tags=["Preprocessing"],
    summary="Clean Arabic and English text",
    description="Preprocesses Arabic and English text using normalization and cleaning techniques."
)
async def preprocess(req: TextRequest):

    try:

        logger.info("Preprocessing request received")

        cleaned = preprocess_text(req.text)

        logger.info("Preprocessing completed successfully")

        return {
            "cleaned_text": cleaned
        }

    except Exception:

        logger.exception("Preprocessing failed")

        return {
            "error": "Preprocessing failed"
        }