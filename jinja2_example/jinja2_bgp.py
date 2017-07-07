import jinja2

bgp_cisco_template = """
router bgp 10
  neighbor {{ peer_ip }} remote-as {{ remote_as }}
    address-family ipv4 unicast 

"""

bgp_juniper_template = """
protocols {
    bgp {
        group EBGP {
            type external;
            peer-as {{ remote_as }};
            neighbor {{ peer_ip }};
        }
    }
}
"""

bgp_template = bgp_juniper_template

my_vars = {
    'remote_as': '100',
    'peer_ip': '10.10.10.2',
}

template = jinja2.Template(bgp_template)
print template.render(my_vars)
