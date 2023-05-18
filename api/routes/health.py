from fastapi import APIRouter


def init_health_router():
    health_router = APIRouter()

    @health_router.get("/health")
    def health():
        """
        Endpoint to validate status of the resource
        :return dict: Info with health status
        """
        return {"status": "Healthy"}

    return health_router
