import asyncio
import sys

from azure_content_safety.hosting import container
from azure_content_safety.protocols.i_content_safety_service import (
    IContentSafetyService,
)

svc = container[IContentSafetyService]


async def main(text: str):
    results = await svc.analyze_text(text)
    print("Content Safety Analysis Results:")
    for result in results:
        print(result)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <text>")
        sys.exit(1)

    asyncio.run(main(sys.argv[1]))
