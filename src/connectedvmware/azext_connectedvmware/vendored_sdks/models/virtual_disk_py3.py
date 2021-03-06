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


class VirtualDisk(Model):
    """Virtual disk model.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param name: Gets or sets the name of the virtual disk.
    :type name: str
    :ivar label: Gets or sets the label of the virtual disk in vCenter.
    :vartype label: str
    :ivar disk_object_id: Gets or sets the disk object id.
    :vartype disk_object_id: str
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

    _validation = {
        'label': {'readonly': True},
        'disk_object_id': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'label': {'key': 'label', 'type': 'str'},
        'disk_object_id': {'key': 'diskObjectId', 'type': 'str'},
        'disk_size_gb': {'key': 'diskSizeGB', 'type': 'int'},
        'device_key': {'key': 'deviceKey', 'type': 'int'},
        'disk_mode': {'key': 'diskMode', 'type': 'str'},
        'controller_key': {'key': 'controllerKey', 'type': 'int'},
        'unit_number': {'key': 'unitNumber', 'type': 'int'},
    }

    def __init__(self, *, name: str=None, disk_size_gb: int=None, device_key: int=None, disk_mode=None, controller_key: int=None, unit_number: int=None, **kwargs) -> None:
        super(VirtualDisk, self).__init__(**kwargs)
        self.name = name
        self.label = None
        self.disk_object_id = None
        self.disk_size_gb = disk_size_gb
        self.device_key = device_key
        self.disk_mode = disk_mode
        self.controller_key = controller_key
        self.unit_number = unit_number
