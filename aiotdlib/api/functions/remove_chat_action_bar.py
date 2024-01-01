# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class RemoveChatActionBar(BaseObject):
    """
    Removes a chat action bar without any other action

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["removeChatActionBar"] = Field("removeChatActionBar", validation_alias="@type", alias="@type")
    chat_id: Int53
