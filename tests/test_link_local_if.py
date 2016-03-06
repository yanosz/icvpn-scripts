from . import mkbgp
from unittest.mock import Mock
from unittest.mock import create_autospec
from optparse import OptionParser
import filereader
import unittest


# Test: -I for interface is present in the option-parser and passed to 
def test_optionparser_supports_interface():
    mock = Mock()
    options_mock = Mock()  
    options_mock.exclude = [1,2]
    options_mock.fmt = 'bird'
    options_mock.interface = "eth42"
    mock.parse_args = create_autospec(OptionParser().parse_args, return_value=[options_mock,Mock()])
    mock.add_option = create_autospec(OptionParser().add_option, return_value='')
    create_config_mock = create_autospec(mkbgp.create_config)

    
    # Mocks verdrahten
    mkbgp.create_config = create_config_mock
    mkbgp.OptionParser = lambda: mock

   
    # Main ausfuehren - Auskommentieren fuerht zu Fehler
    mkbgp.main()
    mock.add_option.assert_called_with("-I", "--interface", dest="interface",
                      help="""Interface used for link local addresses. Default: icvpn""", metavar="INTERFACE",
                      default="icvpn")

    # Interface is the eigth argument
    assert create_config_mock.call_args[0][8] == options_mock.interface

# Test: Interface is passed to the formatter
def test_formatter_knows_interface():
    # Mock Method for reading files
    get_communities_data_backup = mkbgp.get_communities_data
    mkbgp.get_communities_data = create_autospec(mkbgp.get_communities_data, return_value=('test_community',{}))
    mkbgp.create_config("srcdir", "exclude", "prefix", "defaulttemplate", "templates", "family",
                  "fmtclass", "timeout","eth42")


if __name__ == "__main__":
    test_optionparser_supports_interface()  