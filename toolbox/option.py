
import sys
import argparse
import logging

class appendTypeQuantity(argparse.Action):
    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        if nargs == 2:
            super(appendTypeQuantity, self).__init__(option_strings, dest, nargs=nargs, **kwargs)
        else:
            logging.error("Option %s must have 2 arguments in its definition" % option_strings)
    def __call__(self, parser, namespace, values, option_string=None):
        try:
            quantity = abs(int(values[1]))
        except ValueError:
            logging.warning("Quantity Input value is Not A Number (NaN): '" + values[1] + "'. Using None instead, and apply rules (see man page)")
            values[1] = None
        else:
            values[1] = quantity if quantity <= 100 else None

        current_dest_value = getattr(namespace, self.dest)
        if type(current_dest_value) is list:
            current_dest_value.append(values)
            setattr(namespace, self.dest, current_dest_value)
        else:
            logging.debug(values)
            setattr(namespace, self.dest, [values])
