"""
Purumigram Library
A custom Pyrogram-based wrapper designed for UBot stability and smooth execution.
"""

import asyncio
import logging
from pyrogram import Client, filters
from pyrogram.types import Message

# Internal logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Purumigram")

class PurumigramClient(Client):
    """
    Main Purumigram client optimized for MTProto connection handling 
    and built-in UBot command decorators.
    """
    def __init__(
        self, 
        name="purumigram_session", 
        api_id=None, 
        api_hash=None, 
        session_string=None,
        in_memory=True
    ):
        super().__init__(
            name=name,
            api_id=api_id,
            api_hash=api_hash,
            session_string=session_string if session_string else None,
            in_memory=in_memory
        )
        logger.info("⚡ Purumigram Core successfully initialized.")

    def command(self, commands, prefixes="."):
        """
        A clean custom decorator to filter commands specifically for your own account (filters.me).
        """
        return filters.command(commands, prefixes=prefixes) & filters.me

    async def send_log(self, chat_id: int, text: str):
        """
        Internal helper function to send formatted system logs.
        """
        try:
            return await self.send_message(chat_id, f"<b>[Purumigram Log]</b>\n{text}")
        except Exception as e:
            logger.error(f"Failed to send log: {e}")
            return None
