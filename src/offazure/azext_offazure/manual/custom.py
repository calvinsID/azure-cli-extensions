# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines


def offazure_hyperv_cluster_list(cmd,
                                 client,
                                 resource_group_name,
                                 site_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.get_all_clusters_in_site(subscription_id=subscription_id,
                                           resource_group_name=resource_group_name,
                                           site_name=site_name,
                                           filter=None)


def offazure_hyperv_cluster_show(cmd,
                                 client,
                                 resource_group_name,
                                 site_name,
                                 cluster_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.get_cluster(subscription_id=subscription_id,
                              resource_group_name=resource_group_name,
                              site_name=site_name,
                              cluster_name=cluster_name)


def offazure_hyperv_host_list(cmd,
                              client,
                              resource_group_name,
                              site_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.get_all_hosts_in_site(subscription_id=subscription_id,
                                        resource_group_name=resource_group_name,
                                        site_name=site_name,
                                        filter=None)


def offazure_hyperv_host_show(cmd,
                              client,
                              resource_group_name,
                              site_name,
                              host_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.get_host(subscription_id=subscription_id,
                           resource_group_name=resource_group_name,
                           site_name=site_name,
                           host_name=host_name)


def offazure_hyperv_machine_list(cmd,
                                 client,
                                 resource_group_name,
                                 site_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.get_all_machines_in_site(subscription_id=subscription_id,
                                           resource_group_name=resource_group_name,
                                           site_name=site_name,
                                           filter=None,
                                           top=None,
                                           continuation_token_parameter=None,
                                           total_record_count=None)


def offazure_hyperv_machine_show(cmd,
                                 client,
                                 resource_group_name,
                                 site_name,
                                 machine_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.get_machine(subscription_id=subscription_id,
                              resource_group_name=resource_group_name,
                              site_name=site_name,
                              machine_name=machine_name)


def offazure_hyperv_run_as_account_list(cmd,
                                        client,
                                        resource_group_name,
                                        site_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.get_all_run_as_accounts_in_site(subscription_id=subscription_id,
                                                  resource_group_name=resource_group_name,
                                                  site_name=site_name)


def offazure_hyperv_run_as_account_show(cmd,
                                        client,
                                        resource_group_name,
                                        site_name,
                                        account_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.get_run_as_account(subscription_id=subscription_id,
                                     resource_group_name=resource_group_name,
                                     site_name=site_name,
                                     account_name=account_name)


def offazure_hyperv_site_show(cmd,
                              client,
                              resource_group_name,
                              site_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.get_site(subscription_id=subscription_id,
                           resource_group_name=resource_group_name,
                           site_name=site_name)


def offazure_hyperv_site_create(cmd,
                                client,
                                resource_group_name,
                                site_name,
                                tags=None,
                                location=None,
                                identity=None,
                                agent=None,
                                solution_id=None,
                                appliance_name=None):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    body = {}
    body['name'] = None
    body['tags'] = tags
    body['e_tag'] = None
    body['location'] = location
    body['properties'] = {}
    body['properties']['service_principal_identity_details'] = identity
    body['properties']['agent_details'] = agent
    body['properties']['discovery_solution_id'] = solution_id
    body['properties']['appliance_name'] = appliance_name
    return client.put_site(subscription_id=subscription_id,
                           resource_group_name=resource_group_name,
                           site_name=site_name,
                           body=body)


def offazure_hyperv_site_delete(cmd,
                                client,
                                resource_group_name,
                                site_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.delete_site(subscription_id=subscription_id,
                              resource_group_name=resource_group_name,
                              site_name=site_name)


def offazure_vmware_machine_list(cmd,
                                 client,
                                 resource_group_name,
                                 site_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.get_all_machines_in_site(subscription_id=subscription_id,
                                           resource_group_name=resource_group_name,
                                           site_name=site_name,
                                           filter=None,
                                           top=None,
                                           continuation_token_parameter=None,
                                           total_record_count=None)


def offazure_vmware_machine_show(cmd,
                                 client,
                                 resource_group_name,
                                 site_name,
                                 machine_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.get_machine(subscription_id=subscription_id,
                              resource_group_name=resource_group_name,
                              site_name=site_name,
                              machine_name=machine_name)


def offazure_vmware_run_as_account_list(cmd,
                                        client,
                                        resource_group_name,
                                        site_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.get_all_run_as_accounts_in_site(subscription_id=subscription_id,
                                                  resource_group_name=resource_group_name,
                                                  site_name=site_name)


def offazure_vmware_run_as_account_show(cmd,
                                        client,
                                        resource_group_name,
                                        site_name,
                                        account_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.get_run_as_account(subscription_id=subscription_id,
                                     resource_group_name=resource_group_name,
                                     site_name=site_name,
                                     account_name=account_name)


def offazure_vmware_site_show(cmd,
                              client,
                              resource_group_name,
                              site_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.get_site(subscription_id=subscription_id,
                           resource_group_name=resource_group_name,
                           site_name=site_name)


def offazure_vmware_site_create(cmd,
                                client,
                                resource_group_name,
                                site_name,
                                tags=None,
                                location=None,
                                identity=None,
                                agent=None,
                                solution_id=None,
                                appliance_name=None):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    body = {}
    body['name'] = None
    body['tags'] = tags
    body['e_tag'] = None
    body['location'] = location
    body['properties'] = {}
    body['properties']['service_principal_identity_details'] = identity
    body['properties']['agent_details'] = agent
    body['properties']['discovery_solution_id'] = solution_id
    body['properties']['appliance_name'] = appliance_name
    return client.put_site(subscription_id=subscription_id,
                           resource_group_name=resource_group_name,
                           site_name=site_name,
                           body=body)


def offazure_vmware_site_delete(cmd,
                                client,
                                resource_group_name,
                                site_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.delete_site(subscription_id=subscription_id,
                              resource_group_name=resource_group_name,
                              site_name=site_name)


def offazure_vmware_vcenter_list(cmd,
                                 client,
                                 resource_group_name,
                                 site_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.get_all_v_centers_in_site(subscription_id=subscription_id,
                                            resource_group_name=resource_group_name,
                                            site_name=site_name,
                                            filter=None)


def offazure_vmware_vcenter_show(cmd,
                                 client,
                                 resource_group_name,
                                 site_name,
                                 vcenter_name):
    from azure.cli.core.commands.client_factory import get_subscription_id

    subscription_id = get_subscription_id(cmd.cli_ctx)

    return client.get_v_center(subscription_id=subscription_id,
                               resource_group_name=resource_group_name,
                               site_name=site_name,
                               vcenter_name=vcenter_name)
