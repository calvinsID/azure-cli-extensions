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

from .resource import Resource


class WebApplicationFirewallPolicy(Resource):
    """Defines web application firewall policy.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param policy_settings: Describes settings for the policy.
    :type policy_settings: ~azure.mgmt.frontdoor.models.PolicySettings
    :param custom_rules: Describes custom rules inside the policy.
    :type custom_rules: ~azure.mgmt.frontdoor.models.CustomRuleList
    :param managed_rules: Describes managed rules inside the policy.
    :type managed_rules: ~azure.mgmt.frontdoor.models.ManagedRuleSetList
    :ivar frontend_endpoint_links: Describes Frontend Endpoints associated
     with this Web Application Firewall policy.
    :vartype frontend_endpoint_links:
     list[~azure.mgmt.frontdoor.models.FrontendEndpointLink]
    :ivar provisioning_state: Provisioning state of the policy.
    :vartype provisioning_state: str
    :ivar resource_state: Resource status of the policy. Possible values
     include: 'Creating', 'Enabling', 'Enabled', 'Disabling', 'Disabled',
     'Deleting'
    :vartype resource_state: str or
     ~azure.mgmt.frontdoor.models.PolicyResourceState
    :param etag: Gets a unique read-only string that changes whenever the
     resource is updated.
    :type etag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'frontend_endpoint_links': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'resource_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'policy_settings': {'key': 'properties.policySettings', 'type': 'PolicySettings'},
        'custom_rules': {'key': 'properties.customRules', 'type': 'CustomRuleList'},
        'managed_rules': {'key': 'properties.managedRules', 'type': 'ManagedRuleSetList'},
        'frontend_endpoint_links': {'key': 'properties.frontendEndpointLinks', 'type': '[FrontendEndpointLink]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'resource_state': {'key': 'properties.resourceState', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(WebApplicationFirewallPolicy, self).__init__(**kwargs)
        self.policy_settings = kwargs.get('policy_settings', None)
        self.custom_rules = kwargs.get('custom_rules', None)
        self.managed_rules = kwargs.get('managed_rules', None)
        self.frontend_endpoint_links = None
        self.provisioning_state = None
        self.resource_state = None
        self.etag = kwargs.get('etag', None)