# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class VirtualDiskUpdate(Model):
    """Defines the virtual disk update.

    :param name: Gets or sets the name of the virtual disk.
    :type name: str
    :param disk_size_gb: Gets or sets the disk total size.
    :type disk_size_gb: int
    :param device_key: Gets or sets the device key value.
    :type device_key: int
    :param disk_mode: Gets or sets the disk mode. Possible values include:
     'persistent', 'independent_persistent', 'independent_nonpersistent'
    :type disk_mode: str or
     ~azure.mgmt.vmware.v2020_10_01_preview.models.DiskMode
    :param controller_key: Gets or sets the controller id.
    :type controller_key: int
    :param unit_number: Gets or sets the unit number of the disk on the
     controller.
    :type unit_number: int
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'disk_size_gb': {'key': 'diskSizeGB', 'type': 'int'},
        'device_key': {'key': 'deviceKey', 'type': 'int'},
        'disk_mode': {'key': 'diskMode', 'type': 'str'},
        'controller_key': {'key': 'controllerKey', 'type': 'int'},
        'unit_number': {'key': 'unitNumber', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(VirtualDiskUpdate, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.disk_size_gb = kwargs.get('disk_size_gb', None)
        self.device_key = kwargs.get('device_key', None)
        self.disk_mode = kwargs.get('disk_mode', None)
        self.controller_key = kwargs.get('controller_key', None)
        self.unit_number = kwargs.get('unit_number', None)
