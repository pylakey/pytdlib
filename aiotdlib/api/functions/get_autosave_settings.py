# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetAutosaveSettings(BaseObject):
    """
    Returns autosave settings for the current user
    """

    ID: typing.Literal["getAutosaveSettings"] = Field("getAutosaveSettings", validation_alias="@type", alias="@type")
