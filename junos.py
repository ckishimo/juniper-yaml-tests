
from jnpr.junos.factory import loadyaml

logical_system = 'pe-london'
# file imported from napalm: https://github.com/napalm-automation/napalm
input_file = 'junos_views.yml'
globals().update(loadyaml(input_file))

# ARP tests
arp_table_raw = junos_arp_table(path='arp.xml')
arp_table_raw.get()
arp_table_items = arp_table_raw.items()
print('* Printing all entries')
for item in arp_table_items:
	print item

arp_table_raw = junos_arp_table(path='arp.logical.xml')
arp_table_raw.get(logical_system=logical_system)
arp_table_items = arp_table_raw.items()
print('* Printing entries for logical_systems')
for item in arp_table_items:
	print item

