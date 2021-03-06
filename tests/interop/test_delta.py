import unittest
import pytest
import trio_asyncio
import asyncio
from tests import aiotest

DT = trio_asyncio.loop.DeltaTime

class TestDeltaTime(aiotest.TestCase):
    def test_do(self):
        a = DT(10)
        assert a.delta == 10
        b = a + 5
        assert b.delta == 15
        a += 2
        assert a.delta == 12

        a -= 3
        assert a.delta == 9
        b = DT(3)
        assert a-b == 6
        assert (b-1).delta == 2
