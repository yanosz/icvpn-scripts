import mkbgp
from unittest.mock import Mock
from unittest.mock import create_autospec
from optparse import OptionParser


def test_optionparser_supports_interface():
    # Mock fuer den Optionparser
    mock = Mock()
    mock.parse_args = create_autospec(OptionParser().parse_args, return_value=[1,2])
    mock.add_option = create_autospec(OptionParser().add_option, return_value='')
    create_config_mock = create_autospec(mkbgp.create_config)
    
    # Debugging-Anweisung - arbeitet der Mock?
    print(mock.parse_args())
    
    # Mocks verdrahten
    mkbgp.create_config = create_config_mock
    mkbgp.OptionParser = mock

    # Main ausfuehren - Auskommentieren fuerht zu Fehler
    #mkbgp.main()
    mock.add_option.assert_called_once_with("-I", "--interface", dest="interface",
                      help="""Interface used for link local addresses.
                              Default: icvpn""", metavar="INTERFACE",
                      default="icvpn")


if __name__ == "__main__":
    test_optionparser_supports_interface()  