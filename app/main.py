from fastapi import FastAPI


app = FastAPI(
    title="Clinical Coding AI",
    description=(
        "Healthcare clinical coding intelligence platform "
        "for ICD-10-CM and CPT code prediction."
    ),
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
async def health_check():
    """
    Basic application health check.
    """
    return {
        "status": "healthy",
        "service": "clinical-coding-ai",
        "version": "0.1.0",
    }