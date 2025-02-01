# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatPostedToChatPageStories(BaseObject):
    """
    Returns the list of stories that posted by the given chat to its chat page. If from_story_id == 0, then pinned stories are returned first. Then, stories are returned in reverse chronological order (i.e., in order of decreasing story_id). For optimal performance, the number of returned stories is chosen by TDLib

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param from_story_id: Identifier of the story starting from which stories must be returned; use 0 to get results from pinned and the newest story
    :type from_story_id: :class:`Int32`
    :param limit: The maximum number of stories to be returned. For optimal performance, the number of returned stories is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getChatPostedToChatPageStories"] = Field(
        "getChatPostedToChatPageStories", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    from_story_id: Int32
    limit: Int32
