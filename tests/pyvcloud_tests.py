from nose.tools import with_setup
from testconfig import config
import pkg_resources

def test_0001():
    """Check version"""
    assert '18.0.2' == pkg_resources.require("pyvcloud")[0].version
