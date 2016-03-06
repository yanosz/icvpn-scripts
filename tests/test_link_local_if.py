from . import mkbgp

def test_bird_formatter_shows_interface_for_link_local():
    bfmd = mkbgp.BirdFormatter()
    bfmd.add_data("4711", "Das Test-AS", "template", "fe80::42", "eth42")
    assert 'fe80::42%eth42 as 4711' in bfmd.finalize()

def test_bird_formatter_shows_interface_for_non_link_local():
    bfmd = mkbgp.BirdFormatter()
    bfmd.add_data("4711", "Das Test-AS", "template", "2001::42", "eth42")
    assert '2001::42 as 4711' in bfmd.finalize()


def test_quagga_formatter_shows_interface_for_link_local():
    qfmd = mkbgp.QuaggaFormatter()
    qfmd.add_data("4711", "Das Test-AS", "template", "fe80::42", "eth42")
    assert 'fe80::42%eth42 as 4711' in qfmd.finalize()

def test_quagga_formatter_shows_interface_for_non_link_local():
    qfmd = mkbgp.QuaggaFormatter()
    qfmd.add_data("4711", "Das Test-AS", "template", "2001::42", "eth42")
    assert '2001::42 as 4711' in qfmd.finalize()