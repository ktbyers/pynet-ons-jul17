#!/usr/bin/env python
from __future__ import print_function
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import jinja2
from getpass import getpass
from pprint import pprint

USER = "pyclass"
PASSWORD = getpass()

def render_template(template_file, template_vars):
    """Render the specified template using the given vars."""
    template = jinja2.Template(template_file)
    return template.render(template_vars)


if __name__ == "__main__":

    template_file = 'juniper_bgp.j2'

    with open(template_file) as f:
        bgp_template = f.read()

    rtr1 = {
        'device_name' : 'juniper1.twb-tech.com',
        'local_as' : 10,
        'neighbor_ip' : '10.100.1.2',
        'neighbor_as' : 20,
    }

    rtr2 = {
        'device_name' : 'juniper2.twb-tech.com',
        'local_as' : 20,
        'neighbor_ip' : '10.100.1.1',
        'neighbor_as' : 10,
    }

    configs = {}
    for bgp_vars in [rtr1, rtr2]:
        device_name = bgp_vars['device_name']
        config_section = render_template(bgp_template, bgp_vars)
        configs[device_name] = config_section

    for host, load_config in configs.items():
        a_device = Device(host=host, user=USER, password=PASSWORD)
        a_device.open()
        a_device.timeout = 90
        cfg = Config(a_device)
        print("\n")
        print("-" * 70)
        print("Working on device: {}".format(host))
        print("Configuring BGP")
        cfg.load(load_config, format="text", merge=True)
        print("Current config differences: ")
        print(cfg.diff())
        if cfg.diff():
            print("Performing commit")
            cfg.commit()
        print()
