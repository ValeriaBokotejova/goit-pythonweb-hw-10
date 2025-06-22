import time

from fastapi import HTTPException, Request
from starlette.status import HTTP_429_TOO_MANY_REQUESTS

request_times: dict[str, float] = {}

RATE_LIMIT_SECONDS = 5  # Time interval between allowed requests


async def rate_limiter(request: Request) -> None:
    """Limit access to endpoint per IP address."""
    ip: str = request.client.host
    current_time: float = time.time()

    if ip in request_times:
        elapsed = current_time - request_times[ip]
        if elapsed < RATE_LIMIT_SECONDS:
            raise HTTPException(
                status_code=HTTP_429_TOO_MANY_REQUESTS,
                detail=f"Too many requests. Please wait {int(RATE_LIMIT_SECONDS - elapsed)} seconds.",
            )

    request_times[ip] = current_time
