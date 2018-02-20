from unittest import TestCase
import os
from fc_yaml import config_reader


class TestRead_inventory(TestCase):
    def test_read_inventory(self):
        file = os.path.join('inventory.yml');
        hosts = config_reader.read_inventory(file)
        self.assertIsNotNone(hosts, 'yml file read')

        for data in hosts:
            # host has a dictionary
            host_attributes = data['host']
            if host_attributes['name'] == 'alpha':
                print("first node found")
            if host_attributes['ip'] == '192.168.1.110':
                self.assertEqual('omega', host_attributes['name'], 'ip: 192.168.1.110 belongs to omega')
                print('last node found')
                print('  node name is {} with ip {}'.format(host_attributes['name'], host_attributes['ip']))
