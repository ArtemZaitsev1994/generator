import ipaddress
import random

import argparse


if __name__ == '__main__':
	# We are use parser to get an arguments from terminal.
    parser = argparse.ArgumentParser(description='Generate random IP4 or IP6 addresses.')
    parser.add_argument(
        "protocol", type=str, choices=['ipv4', 'ipv6'],
        help="Required version of protocol."
    )
    parser.add_argument("prefix_from", type=int, help="Prefix from.")
    parser.add_argument("prefix_to", type=int, help="Prefix to.")

    args = parser.parse_args()

    prefix_from, prefix_to, protocol = args.prefix_from, args.prefix_to, args.protocol

    if prefix_from > prefix_to:
        parser.error("'prefix_from' must be equal or less than 'prefix_from'")

    # Available range of prefix for protocol versions.
    min_prefix, max_prefix = (0, 32) if protocol == 'ipv4' else (0, 128)

    if prefix_from < min_prefix or prefix_from > max_prefix:
        parser.error(
            "'prefix_from' for type '{}' must be in range {} - {}".format(protocol, min_prefix, max_prefix)
        )
    if prefix_to < min_prefix or prefix_to > max_prefix:
        parser.error(
            "'prefix_to' for type '{}' must be in range {} - {}".format(protocol, min_prefix, max_prefix)
        )

    while True:
        if protocol == 'ipv4':
        	# We generate an integer with 32 random bits and create address from them.
            address = '{}/{}'.format(
                str(ipaddress.IPv4Address(random.getrandbits(32))),
                random.randint(prefix_from, prefix_to)
            )
        else:
        	# We generate an integer with 128 random bits and create address from them.
            # When we call str(), it returned short version of the IPv6 address
            address = '{}::/{}'.format(
            	# We don't needs to compress the string from "0000:0000:0000:0000:0000:0abc:0007:0def" format
            	# to "::abc:7:def" because it's implemented in module.
                str(ipaddress.IPv6Address(random.getrandbits(128))),
                random.randint(prefix_from, prefix_to)
            )
            
        print(address)
