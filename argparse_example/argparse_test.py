#!/usr/bin/env python
import argparse

def main():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description="Some description of what this tool does")

    # Add required argument named vlan_id
    parser.add_argument("vlan_id", help="VLAN number", action="store", type=int)
    parser.add_argument("--name", help="Specify VLAN name", action="store", 
                        dest="vlan_name", type=str)
    parser.add_argument("--remove", help="Remove the given VLAN ID", action="store_true")

    cli_args = parser.parse_args()
    vlan_id = cli_args.vlan_id
    remove = cli_args.remove
    vlan_name = cli_args.vlan_name

    print
    print cli_args
    print "vlan_id: {}".format(vlan_id)
    print "vlan_name: {}".format(vlan_name)
    print "remove: {}".format(remove)
    print

if __name__ == "__main__":
    main()

