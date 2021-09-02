# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatList


class GetChats(BaseObject):
    """
    Returns an ordered list of chats from the beginning of a chat list. For informational purposes only. Use loadChats instead to maintain chat lists
    
    Params:
        chat_list (:class:`ChatList`)
            The chat list in which to return chats
        
        limit (:class:`int`)
            The maximum number of chats to be returned
        
    """

    ID: str = Field("getChats", alias="@type")
    chat_list: ChatList
    limit: int

    @staticmethod
    def read(q: dict) -> GetChats:
        return GetChats.construct(**q)
