from app.main import get_btc_price


def test_get_btc_price():
    price = get_btc_price()
    assert isinstance(price, (int, float))
    assert price > 0