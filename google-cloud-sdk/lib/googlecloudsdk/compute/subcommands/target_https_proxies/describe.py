# Copyright 2014 Google Inc. All Rights Reserved.
"""Command for describing target HTTPS proxies."""
from googlecloudsdk.compute.lib import base_classes


class Describe(base_classes.GlobalDescriber):
  """Display detailed information about a target HTTPS proxy."""

  @staticmethod
  def Args(parser):
    cli = Describe.GetCLIGenerator()
    base_classes.GlobalDescriber.Args(
        parser, 'compute.targetHttpsProxies', cli,
        'compute.target-https-proxies')
    base_classes.AddFieldsFlag(parser, 'targetHttpsProxies')

  @property
  def service(self):
    return self.compute.targetHttpsProxies

  @property
  def resource_type(self):
    return 'targetHttpsProxies'


Describe.detailed_help = {
    'brief': 'Display detailed information about a target HTTPS proxy',
    'DESCRIPTION': """\
        *{command}* displays all data associated with a target HTTPS proxy
        in a project.
        """,
}
