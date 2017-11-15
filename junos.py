

from jnpr.junos.factory import loadyaml
import json

logical_system = 'pe-london'
# file imported from napalm: https://github.com/napalm-automation/napalm
input_file = 'junos_views.yml'
globals().update(loadyaml(input_file))

# ===================================================
# ARP tests
# ===================================================
arp_table_raw = junos_arp_table(path='arp.xml')
arp_table_raw.get()
arp_table_items = arp_table_raw.items()
print('* Printing all entries')
for item in arp_table_items:
	print item

# Outputs are identical, no logical-system tags in the xml file...
arp_table_raw = junos_arp_table(path='arp.logical.xml')
arp_table_raw.get(logical_system=logical_system)
arp_table_items = arp_table_raw.items()
print('* Printing entries for logical_systems')
for item in arp_table_items:
	print item

# ===================================================
# BGP configuration
# ===================================================
# Global logical-system configuration
bgp_config = junos_bgp_logical_systems_config_table(path='pe-london.xml')
print(bgp_config)

# Nothing bgp_config.get(logical_system=logical_system)
# bgp_config.get(logical_system)

kk = bgp_config.get()
print(kk)

lres = bgp_config.items()
for item in lres:
	if item[0] == 'pe-london':
		print(item[0])
		for subitem in item[1]:
			print("\t%s" % str(subitem))
		break

# Group logical-system configuration
bgp_config = junos_bgp_logical_systems_config_group_table(path='pe-london.xml')
bgp_config.get(logical_system=logical_system)
lres = bgp_config.items()
for item in lres:
	if item[0] == 'pe-london':
		print(item[0])
		for subitem in item[1]:
			print("\t%s" % str(subitem))
		break
