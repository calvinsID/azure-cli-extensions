# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=unused-import,ungrouped-imports,import-outside-toplevel,super-with-arguments
from azure.cli.core import AzCommandsLoader
from azure.cli.command_modules.appservice.commands import ex_handler_factory
from knack.arguments import CLIArgumentType
from azure.cli.core.commands.parameters import (resource_group_name_type, get_resource_name_completion_list)
import azext_webapp._help


class WebappExtCommandLoader(AzCommandsLoader):
    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azure.cli.core.profiles import ResourceType
        webapp_custom = CliCommandType(
            operations_tmpl='azext_webapp.custom#{}')
        super(WebappExtCommandLoader, self).__init__(cli_ctx=cli_ctx,
                                                     custom_command_type=webapp_custom,
                                                     resource_type=ResourceType.MGMT_CONTAINERREGISTRY)

    def load_command_table(self, _):
        with self.command_group('webapp') as g:
            g.custom_command('container up', 'create_deploy_container_app', exception_handler=ex_handler_factory())
            g.custom_command('remote-connection create', 'create_tunnel')
            g.custom_command('deploy', 'perform_onedeploy')

        with self.command_group('webapp scan') as g:
            g.custom_command('start', 'start_scan')
            g.custom_command('show-result', 'get_scan_result')
            g.custom_command('track', 'track_scan')
            g.custom_command('list-result', 'get_all_scan_result')
            g.custom_command('stop', 'stop_scan')

        with self.command_group('webapp deployment github-actions') as g:
            g.custom_command('add', 'add_github_actions')

        return self.command_table

    def load_arguments(self, _):
        # pylint: disable=line-too-long
        # PARAMETER REGISTRATION
        webapp_name_arg_type = CLIArgumentType(configured_default='web', options_list=['--name', '-n'], metavar='NAME',
                                               completer=get_resource_name_completion_list('Microsoft.Web/sites'), id_part='name',
                                               help="name of the webapp. You can configure the default using 'az configure --defaults web=<name>'")

        with self.argument_context('webapp container up') as c:
            c.argument('name', arg_type=webapp_name_arg_type)
            c.argument('source_location', options_list=['--source-location', '-s'],
                       help='the path to the web app source directory')
            c.argument('docker_custom_image_name', options_list=['--docker-custom-image-name', '-i'],
                       help='the container image name and optionally the tag name (currently public DockerHub images only)')
            c.argument('dryrun', help="show summary of the create and deploy operation instead of executing it", default=False, action='store_true')
            c.argument('registry_rg', help="the resource group of the Azure Container Registry")
            c.argument('registry_name', help="the name of the Azure Container Registry")
            c.argument('slot', help="Name of the deployment slot to use")
        with self.argument_context('webapp remote-connection create') as c:
            c.argument('port', options_list=['--port', '-p'],
                       help='Port for the remote connection. Default: Random available port', type=int)
            c.argument('name', options_list=['--name', '-n'], help='Name of the webapp to connect to')
            c.argument('slot', help="Name of the deployment slot to use")
        with self.argument_context('webapp scan') as c:
            c.argument('name', options_list=['--name', '-n'], help='Name of the webapp to connect to')
            c.argument('scan_id', options_list=['--scan-id'], help='Unique scan id')
            c.argument('timeout', options_list=['--timeout'], help='Timeout for operation in milliseconds')
            c.argument('slot', help="Name of the deployment slot to use")

        with self.argument_context('webapp deploy') as c:
            c.argument('name', options_list=['--name'], help='Name of the webapp to connect to')
            c.argument('src_path', options_list=['--src-path'], help='Path of the file to be deployed. Example: /mnt/apps/myapp.war')
            c.argument('src_url', options_list=['--src-url'], help='url to download the package from. Example: http://mysite.com/files/myapp.war?key=123')
            c.argument('target_path', options_list=['--target-path'], help='Target path relative to wwwroot to which the file will be deployed to.')
            c.argument('artifact_type', options_list=['--type'], help='Type of deployment requested')
            c.argument('is_async', options_list=['--async'], help='Asynchronous deployment', choices=['true', 'false'])
            c.argument('restart', options_list=['--restart'], help='restart or not. default behavior is to restart.', choices=['true', 'false'])
            c.argument('clean', options_list=['--clean'], help='clean or not. default is target-type specific.', choices=['true', 'false'])
            c.argument('ignore_stack', options_list=['--ignore-stack'], help='should override the default stack check', choices=['true', 'false'])
            c.argument('timeout', options_list=['--timeout'], help='Timeout for operation in milliseconds')
            c.argument('slot', help="Name of the deployment slot to use")

        with self.argument_context('webapp deployment github-actions')as c:
            c.argument('name', arg_type=webapp_name_arg_type)
            c.argument('resource_group', arg_type=resource_group_name_type)
            c.argument('repo', help='The GitHub repository to which the workflow file will be added. In the format: <owner>/<repository-name>')
            c.argument('runtime', options_list=['--runtime', '-r'], help='Canonicalized web runtime in the format of Framework|Version, e.g. "PHP|5.6". Use "az webapp list-runtimes" for available list.')
            c.argument('token', help='A Personal Access Token with write access to the specified repository. For more information: https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line')
            c.argument('slot', options_list=['--slot', '-s'], help='The name of the slot. Default to the production slot if not specified.')
            c.argument('branch', options_list=['--branch', '-b'], help='The branch to which the workflow file will be added. Defaults to "master" if not specified.')
            c.argument('force', options_list=['--force', '-f'], help='When true, the command will overwrite any workflow file with a conflicting name.')


COMMAND_LOADER_CLS = WebappExtCommandLoader
