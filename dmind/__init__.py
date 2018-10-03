from .mind import MindMagics

__version__ = '0.0.6'


def load_ipython_extension(ipython):
    ipython.register_magics(MindMagics)
