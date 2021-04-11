from datetime import datetime


async def formatTime(time: datetime) -> str:
    return time.strftime("%B %-d, %Y")
