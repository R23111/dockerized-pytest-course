from scripts.chp2.video2.mapmaker_start import Point


def test_make_one_point():
    p1 = Point("SBC", 123, 321)
    assert p1.get_lat_long() == (123, 321)
