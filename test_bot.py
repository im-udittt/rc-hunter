import unittest
from unittest.mock import AsyncMock, MagicMock
from bot import find

class TestBot(unittest.IsolatedAsyncioTestCase):
    async def test_find(self):
        ctx = MagicMock()
        ctx.send = AsyncMock()
        ctx.send_file = AsyncMock()

        rc_number = "MH01AX1234"
        await find(ctx, rc_number)

        # Check that the response was sent
        ctx.send.assert_called_once()
        
        # Check that the file was sent
        ctx.send_file.assert_called_once()
