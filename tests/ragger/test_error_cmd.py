import pytest

from ragger import ApplicationError

from boilerplate_client.exception import *


@pytest.mark.xfail(raises=ApplicationError)
def test_bad_cla(client):
    client.exchange(cla=0xa0,  # 0xa0 instead of 0xe0
                        ins=0x03)

@pytest.mark.xfail(raises=ApplicationError)
def test_bad_ins(client):
    client.exchange(cla=0xe0, ins=0xff)  # bad INS

@pytest.mark.xfail(raises=ApplicationError)
def test_wrong_p1p2(client):
    client.exchange(cla=0xe0,
                    ins=0x03,
                    p1=0x01)  # 0x01 instead of 0x00

@pytest.mark.xfail(raises=ApplicationError)
def test_wrong_data_length(client):
    # APDUs must be at least 5 bytes: CLA, INS, P1, P2, Lc.
    client.exchange_raw(b"E000")
