# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    MessageSender,
)


class GetStarWithdrawalUrl(BaseObject):
    """
    Returns URL for Telegram star withdrawal

    :param owner_id: Identifier of the owner of the Telegram stars; can be identifier of an owned bot, or identifier of a channel chat with supergroupFullInfo.can_get_revenue_statistics == true
    :type owner_id: :class:`MessageSender`
    :param star_count: The number of Telegram stars to withdraw. Must be at least getOption("star_withdrawal_count_min")
    :type star_count: :class:`Int53`
    :param password: The 2-step verification password of the current user
    :type password: :class:`String`
    """

    ID: typing.Literal["getStarWithdrawalUrl"] = Field("getStarWithdrawalUrl", validation_alias="@type", alias="@type")
    owner_id: MessageSender
    star_count: Int53
    password: String