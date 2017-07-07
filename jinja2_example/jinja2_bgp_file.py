import jinja2

template_file = 'juniper_bgp.j2'
with open(template_file) as f:
    bgp_template = f.read()

my_vars = {
    'peer_as': '22',
    'neighbor1': '10.10.10.2',
    'neighbor2': '10.10.10.99',
    'neighbor3': '10.10.10.220',
}

template = jinja2.Template(bgp_template)
print template.render(my_vars)
