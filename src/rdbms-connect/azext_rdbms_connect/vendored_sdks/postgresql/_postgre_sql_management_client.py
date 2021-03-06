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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import PostgreSQLManagementClientConfiguration
from .operations import ServersOperations
from .operations import ReplicasOperations
from .operations import FirewallRulesOperations
from .operations import VirtualNetworkRulesOperations
from .operations import DatabasesOperations
from .operations import ConfigurationsOperations
from .operations import LogFilesOperations
from .operations import ServerAdministratorsOperations
from .operations import LocationBasedPerformanceTierOperations
from .operations import CheckNameAvailabilityOperations
from .operations import Operations
from .operations import ServerSecurityAlertPoliciesOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkResourcesOperations
from .operations import ServerKeysOperations
from . import models


class PostgreSQLManagementClient(SDKClient):
    """The Microsoft Azure management API provides create, read, update, and delete functionality for Azure PostgreSQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model.

    :ivar config: Configuration for client.
    :vartype config: PostgreSQLManagementClientConfiguration

    :ivar servers: Servers operations
    :vartype servers: azure.mgmt.rdbms.postgresql.operations.ServersOperations
    :ivar replicas: Replicas operations
    :vartype replicas: azure.mgmt.rdbms.postgresql.operations.ReplicasOperations
    :ivar firewall_rules: FirewallRules operations
    :vartype firewall_rules: azure.mgmt.rdbms.postgresql.operations.FirewallRulesOperations
    :ivar virtual_network_rules: VirtualNetworkRules operations
    :vartype virtual_network_rules: azure.mgmt.rdbms.postgresql.operations.VirtualNetworkRulesOperations
    :ivar databases: Databases operations
    :vartype databases: azure.mgmt.rdbms.postgresql.operations.DatabasesOperations
    :ivar configurations: Configurations operations
    :vartype configurations: azure.mgmt.rdbms.postgresql.operations.ConfigurationsOperations
    :ivar log_files: LogFiles operations
    :vartype log_files: azure.mgmt.rdbms.postgresql.operations.LogFilesOperations
    :ivar server_administrators: ServerAdministrators operations
    :vartype server_administrators: azure.mgmt.rdbms.postgresql.operations.ServerAdministratorsOperations
    :ivar location_based_performance_tier: LocationBasedPerformanceTier operations
    :vartype location_based_performance_tier: azure.mgmt.rdbms.postgresql.operations.LocationBasedPerformanceTierOperations
    :ivar check_name_availability: CheckNameAvailability operations
    :vartype check_name_availability: azure.mgmt.rdbms.postgresql.operations.CheckNameAvailabilityOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.rdbms.postgresql.operations.Operations
    :ivar server_security_alert_policies: ServerSecurityAlertPolicies operations
    :vartype server_security_alert_policies: azure.mgmt.rdbms.postgresql.operations.ServerSecurityAlertPoliciesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnections operations
    :vartype private_endpoint_connections: azure.mgmt.rdbms.postgresql.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResources operations
    :vartype private_link_resources: azure.mgmt.rdbms.postgresql.operations.PrivateLinkResourcesOperations
    :ivar server_keys: ServerKeys operations
    :vartype server_keys: azure.mgmt.rdbms.postgresql.operations.ServerKeysOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = PostgreSQLManagementClientConfiguration(credentials, subscription_id, base_url)
        super(PostgreSQLManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.servers = ServersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.replicas = ReplicasOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.firewall_rules = FirewallRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.virtual_network_rules = VirtualNetworkRulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.databases = DatabasesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.configurations = ConfigurationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.log_files = LogFilesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.server_administrators = ServerAdministratorsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.location_based_performance_tier = LocationBasedPerformanceTierOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.check_name_availability = CheckNameAvailabilityOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.server_security_alert_policies = ServerSecurityAlertPoliciesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.server_keys = ServerKeysOperations(
            self._client, self.config, self._serialize, self._deserialize)
