"""Defines our top level DI container.
Utilizes the Lagom library for dependency injection, see more at:

- https://lagom-di.readthedocs.io/en/latest/
- https://github.com/meadsteve/lagom
"""

import logging
import os

from dotenv import load_dotenv
from lagom import Container, dependency_definition

from azure_content_safety.protocols.i_content_safety_service import (
    IContentSafetyService,
)

load_dotenv(dotenv_path=".env")


container = Container()
"""The top level DI container for our application."""


# Register our dependencies ------------------------------------------------------------


@dependency_definition(container, singleton=True)
def logger() -> logging.Logger:
    logging.basicConfig(level=os.getenv("LOG_LEVEL", "ERROR"))
    logging.Formatter(fmt=" %(name)s :: %(levelname)-8s :: %(message)s")
    return logging.getLogger("azure_content_safety")


@dependency_definition(container, singleton=True)
def content_safety_service() -> IContentSafetyService:
    from azure_content_safety.services.content_safety_service import (
        ContentSafetyService,
    )

    return container[ContentSafetyService]
