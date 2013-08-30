"""
This is the module for the remove command.
"""

__helpstr__ = """Usage: nodevers remove <version> [options]

  Summary:
      Uninstalls the specified Node version

  Options:
      -h/--help         Print this text

"""

import shutil
import sys
import getopt
import nodevers.shared as shared
import nodevers.use as use
import nodevers.version as version

def remove(ver):
    """
    Uninstalls the specified version.
    """
    if ver == version.current_version():
        use.link_to("system")
    shutil.rmtree(shared.get_version_dir(ver))

def parse(args):
    """
    Parse the arguments and call the correct functions
    based on them.
    """
    if len(args) == 0:
        shared.help_func(__helpstr__)
    else:
        try:
            optlist, arglist = getopt.getopt(args, "h", ["help"])
        except getopt.error:
            err = sys.exc_info()[1]
            sys.stderr.write("Error: %s.\n" % str(err))
            sys.exit(-1)
        for option, value in optlist:
            if option in ("-h", "--help"):
                shared.help_func(__helpstr__)
        if shared.version_exists(args[0]):
            remove(args[0])
        else:
            sys.stdout.write("There is no such version installed.\n")
