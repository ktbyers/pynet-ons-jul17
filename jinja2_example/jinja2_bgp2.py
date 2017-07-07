import jinja2

bgp_template = """
router bgp 10
  neighbor {{ peer_ip }} remote-as 10
    address-family ipv4 unicast 
{% if peer2 %}
  neighbor {{ peer_ip2 }} remote-as 10
    address-family ipv4 unicast 
{% endif %}

"""

my_vars = {
    'peer_ip': '10.10.10.2',
    'peer2': True,
    'peer_ip2': '10.10.12.2',
}

t = jinja2.Template(bgp_template)
print t.render(my_vars)
