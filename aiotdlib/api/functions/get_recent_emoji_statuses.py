# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetRecentEmojiStatuses(BaseObject):
    """
    Returns recent emoji statuses
    """

    ID: typing.Literal["getRecentEmojiStatuses"] = Field(
        "getRecentEmojiStatuses", validation_alias="@type", alias="@type"
    )
