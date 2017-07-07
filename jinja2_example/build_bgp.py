from __future__ import print_function
import jinja2
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass

USER = "pyclass"
PASSWD = getpass()

my_vars = {
    'juniper1':
            {
                'management_ip': 'juniper1.twb-tech.com',
                'ge_ip': '10.10.10.1',
                'ge_netmask': '24',
                'local_as': '101',
                'peer_as': '102',
                'peer_ip': '10.10.10.2',
            },
    'juniper2':
            {
                'management_ip': 'juniper2.twb-tech.com',
                'ge_ip': '10.10.10.2',
                'ge_netmask': '24',
                'local_as': '102',
                'peer_as': '101',
                'peer_ip': '10.10.10.1',
            },
}


template_file = 'build_bgp.j2'
with open(template_file) as f:
    bgp_template = f.read()

for router_id, router_vars in my_vars.items():
    template = jinja2.Template(bgp_template)
    rtr_cfg = template.render(router_vars)
    print()
    print('-' * 60)
    print("This is router: {}".format(router_id))
    print(rtr_cfg)
    print()

    # Connecting to device
    host = router_vars['management_ip']
    a_device = Device(host=host, user=USER, password=PASSWD)
    a_device.open()
    a_device.timeout = 90
    cfg = Config(a_device)
    cfg.load(rtr_cfg, format="text", merge=False)
    diff = cfg.diff()
    print(diff)
    status = raw_input("Do you want to continue: ")
    if diff:
        print("Commit changes")
        cfg.commit()
    else:
        print("No changes")

