#!/usr/bin/python
# Copyright 2011 Google Inc. All Rights Reserved.
#
# AUTO-GENERATED BY parse-schema.py
#
# DO NOT EDIT!!
#
#pylint: disable-msg=C6202
#pylint: disable-msg=C6409
#pylint: disable-msg=C6310
# These should not actually be necessary (bugs in gpylint?):
#pylint: disable-msg=E1101
#pylint: disable-msg=W0231
#
"""Auto-generated from spec: urn:broadband-forum-org:tr-157-1-2."""

import core
from tr157_v1_1 import InternetGatewayDevice_v1_6
from tr181_v1_0 import Device_v1_5


class Device_v1_6(Device_v1_5):
  """Represents Device_v1_6."""

  def __init__(self, **defaults):
    Device_v1_5.__init__(self, defaults=defaults)
    self.Export(params=['SmartCardReaderNumberOfEntries',
                        'UserNumberOfEntries'],
                objects=['DeviceInfo',
                         'DownloadAvailability',
                         'ManagementServer',
                         'NSLookupDiagnostics',
                         'PeriodicStatistics',
                         'SelfTestDiagnostics',
                         'UPnP',
                         'USBHosts',
                         'UserInterface'])

  class DeviceInfo(Device_v1_5.DeviceInfo):
    """Represents Device_v1_6.DeviceInfo."""

    def __init__(self, **defaults):
      Device_v1_5.DeviceInfo.__init__(self, defaults=defaults)
      self.Export(params=['SupportedDataModelNumberOfEntries'],
                  objects=['ProcessStatus',
                           'TemperatureStatus'])

    class ProcessStatus(Device_v1_5.DeviceInfo.ProcessStatus):
      """Represents Device_v1_6.DeviceInfo.ProcessStatus."""

      def __init__(self, **defaults):
        Device_v1_5.DeviceInfo.ProcessStatus.__init__(self, defaults=defaults)
        self.Export(params=['ProcessNumberOfEntries'])

    class TemperatureStatus(Device_v1_5.DeviceInfo.TemperatureStatus):
      """Represents Device_v1_6.DeviceInfo.TemperatureStatus."""

      def __init__(self, **defaults):
        Device_v1_5.DeviceInfo.TemperatureStatus.__init__(self, defaults=defaults)
        self.Export(params=['TemperatureSensorNumberOfEntries'])

  class DownloadAvailability(Device_v1_5.DownloadAvailability):
    """Represents Device_v1_6.DownloadAvailability."""

    def __init__(self, **defaults):
      Device_v1_5.DownloadAvailability.__init__(self, defaults=defaults)
      self.Export(objects=['Announcement'])

    class Announcement(Device_v1_5.DownloadAvailability.Announcement):
      """Represents Device_v1_6.DownloadAvailability.Announcement."""

      def __init__(self, **defaults):
        Device_v1_5.DownloadAvailability.Announcement.__init__(self, defaults=defaults)
        self.Export(params=['GroupNumberOfEntries'])

  class ManagementServer(Device_v1_5.ManagementServer):
    """Represents Device_v1_6.ManagementServer."""

    def __init__(self, **defaults):
      Device_v1_5.ManagementServer.__init__(self, defaults=defaults)
      self.Export(objects=['AutonomousTransferCompletePolicy'])

    class AutonomousTransferCompletePolicy(Device_v1_5.ManagementServer.AutonomousTransferCompletePolicy):
      """Represents Device_v1_6.ManagementServer.AutonomousTransferCompletePolicy."""

      def __init__(self, **defaults):
        Device_v1_5.ManagementServer.AutonomousTransferCompletePolicy.__init__(self, defaults=defaults)
        self.Export(params=['ResultTypeFilter'])

  class NSLookupDiagnostics(Device_v1_5.NSLookupDiagnostics):
    """Represents Device_v1_6.NSLookupDiagnostics."""

    def __init__(self, **defaults):
      Device_v1_5.NSLookupDiagnostics.__init__(self, defaults=defaults)
      self.Export(params=['DiagnosticsState',
                          'ResultNumberOfEntries'],
                  lists=['Result'])

    class Result(Device_v1_5.NSLookupDiagnostics.Result):
      """Represents Device_v1_6.NSLookupDiagnostics.Result.{i}."""

      def __init__(self, **defaults):
        Device_v1_5.NSLookupDiagnostics.Result.__init__(self, defaults=defaults)
        self.Export(params=['Status'])

  class PeriodicStatistics(Device_v1_5.PeriodicStatistics):
    """Represents Device_v1_6.PeriodicStatistics."""

    def __init__(self, **defaults):
      Device_v1_5.PeriodicStatistics.__init__(self, defaults=defaults)
      self.Export(params=['SampleSetNumberOfEntries'],
                  lists=['SampleSet'])

    class SampleSet(Device_v1_5.PeriodicStatistics.SampleSet):
      """Represents Device_v1_6.PeriodicStatistics.SampleSet.{i}."""

      def __init__(self, **defaults):
        Device_v1_5.PeriodicStatistics.SampleSet.__init__(self, defaults=defaults)
        self.Export(params=['ParameterNumberOfEntries'])

  class SelfTestDiagnostics(Device_v1_5.SelfTestDiagnostics):
    """Represents Device_v1_6.SelfTestDiagnostics."""

    def __init__(self, **defaults):
      Device_v1_5.SelfTestDiagnostics.__init__(self, defaults=defaults)
      self.Export(params=['DiagnosticsState'])

  class UPnP(Device_v1_5.UPnP):
    """Represents Device_v1_6.UPnP."""

    def __init__(self, **defaults):
      Device_v1_5.UPnP.__init__(self, defaults=defaults)
      self.Export(objects=['Device',
                           'Discovery'])

    class Device(Device_v1_5.UPnP.Device):
      """Represents Device_v1_6.UPnP.Device."""

      def __init__(self, **defaults):
        Device_v1_5.UPnP.Device.__init__(self, defaults=defaults)
        self.Export(params=['UPnPDMBasicMgmt',
                            'UPnPDMConfigurationMgmt',
                            'UPnPDMSoftwareMgmt'],
                    objects=['Capabilities'])

      class Capabilities(Device_v1_5.UPnP.Device.Capabilities):
        """Represents Device_v1_6.UPnP.Device.Capabilities."""

        def __init__(self, **defaults):
          Device_v1_5.UPnP.Device.Capabilities.__init__(self, defaults=defaults)
          self.Export(params=['UPnPArchitecture',
                              'UPnPArchitectureMinorVer',
                              'UPnPDMBasicMgmt',
                              'UPnPDMConfigurationMgmt',
                              'UPnPDMSoftwareMgmt'])

    class Discovery(Device_v1_5.UPnP.Discovery):
      """Represents Device_v1_6.UPnP.Discovery."""

      def __init__(self, **defaults):
        Device_v1_5.UPnP.Discovery.__init__(self, defaults=defaults)
        self.Export(params=['DeviceNumberOfEntries',
                            'RootDeviceNumberOfEntries',
                            'ServiceNumberOfEntries'])

  class USBHosts(Device_v1_5.USBHosts):
    """Represents Device_v1_6.USBHosts."""

    def __init__(self, **defaults):
      Device_v1_5.USBHosts.__init__(self, defaults=defaults)
      self.Export(params=['HostNumberOfEntries'],
                  lists=['Host'])

    class Host(Device_v1_5.USBHosts.Host):
      """Represents Device_v1_6.USBHosts.Host.{i}."""

      def __init__(self, **defaults):
        Device_v1_5.USBHosts.Host.__init__(self, defaults=defaults)
        self.Export(params=['DeviceNumberOfEntries'],
                    lists=['Device'])

      class Device(Device_v1_5.USBHosts.Host.Device):
        """Represents Device_v1_6.USBHosts.Host.{i}.Device.{i}."""

        def __init__(self, **defaults):
          Device_v1_5.USBHosts.Host.Device.__init__(self, defaults=defaults)
          self.Export(params=['ConfigurationNumberOfEntries',
                              'Parent'],
                      lists=['Configuration'])

        class Configuration(Device_v1_5.USBHosts.Host.Device.Configuration):
          """Represents Device_v1_6.USBHosts.Host.{i}.Device.{i}.Configuration.{i}."""

          def __init__(self, **defaults):
            Device_v1_5.USBHosts.Host.Device.Configuration.__init__(self, defaults=defaults)
            self.Export(params=['InterfaceNumberOfEntries'])

  class UserInterface(Device_v1_5.UserInterface):
    """Represents Device_v1_6.UserInterface."""

    def __init__(self, **defaults):
      Device_v1_5.UserInterface.__init__(self, defaults=defaults)
      self.Export(objects=['RemoteAccess'])

    class RemoteAccess(Device_v1_5.UserInterface.RemoteAccess):
      """Represents Device_v1_6.UserInterface.RemoteAccess."""
      pass


class InternetGatewayDevice_v1_7(InternetGatewayDevice_v1_6):
  """Represents InternetGatewayDevice_v1_7."""

  def __init__(self, **defaults):
    InternetGatewayDevice_v1_6.__init__(self, defaults=defaults)
    self.Export(params=['SmartCardReaderNumberOfEntries',
                        'UserNumberOfEntries'],
                objects=['DeviceInfo',
                         'DownloadAvailability',
                         'ManagementServer',
                         'NSLookupDiagnostics',
                         'PeriodicStatistics',
                         'SelfTestDiagnostics',
                         'UPnP',
                         'USBHosts',
                         'UserInterface'])

  class DeviceInfo(InternetGatewayDevice_v1_6.DeviceInfo):
    """Represents InternetGatewayDevice_v1_7.DeviceInfo."""

    def __init__(self, **defaults):
      InternetGatewayDevice_v1_6.DeviceInfo.__init__(self, defaults=defaults)
      self.Export(params=['SupportedDataModelNumberOfEntries'],
                  objects=['ProcessStatus',
                           'TemperatureStatus'])

    class ProcessStatus(InternetGatewayDevice_v1_6.DeviceInfo.ProcessStatus):
      """Represents InternetGatewayDevice_v1_7.DeviceInfo.ProcessStatus."""

      def __init__(self, **defaults):
        InternetGatewayDevice_v1_6.DeviceInfo.ProcessStatus.__init__(self, defaults=defaults)
        self.Export(params=['ProcessNumberOfEntries'])

    class TemperatureStatus(InternetGatewayDevice_v1_6.DeviceInfo.TemperatureStatus):
      """Represents InternetGatewayDevice_v1_7.DeviceInfo.TemperatureStatus."""

      def __init__(self, **defaults):
        InternetGatewayDevice_v1_6.DeviceInfo.TemperatureStatus.__init__(self, defaults=defaults)
        self.Export(params=['TemperatureSensorNumberOfEntries'])

  class DownloadAvailability(InternetGatewayDevice_v1_6.DownloadAvailability):
    """Represents InternetGatewayDevice_v1_7.DownloadAvailability."""

    def __init__(self, **defaults):
      InternetGatewayDevice_v1_6.DownloadAvailability.__init__(self, defaults=defaults)
      self.Export(objects=['Announcement'])

    class Announcement(InternetGatewayDevice_v1_6.DownloadAvailability.Announcement):
      """Represents InternetGatewayDevice_v1_7.DownloadAvailability.Announcement."""

      def __init__(self, **defaults):
        InternetGatewayDevice_v1_6.DownloadAvailability.Announcement.__init__(self, defaults=defaults)
        self.Export(params=['GroupNumberOfEntries'])

  class ManagementServer(InternetGatewayDevice_v1_6.ManagementServer):
    """Represents InternetGatewayDevice_v1_7.ManagementServer."""

    def __init__(self, **defaults):
      InternetGatewayDevice_v1_6.ManagementServer.__init__(self, defaults=defaults)
      self.Export(objects=['AutonomousTransferCompletePolicy'])

    class AutonomousTransferCompletePolicy(InternetGatewayDevice_v1_6.ManagementServer.AutonomousTransferCompletePolicy):
      """Represents InternetGatewayDevice_v1_7.ManagementServer.AutonomousTransferCompletePolicy."""

      def __init__(self, **defaults):
        InternetGatewayDevice_v1_6.ManagementServer.AutonomousTransferCompletePolicy.__init__(self, defaults=defaults)
        self.Export(params=['ResultTypeFilter'])

  class NSLookupDiagnostics(InternetGatewayDevice_v1_6.NSLookupDiagnostics):
    """Represents InternetGatewayDevice_v1_7.NSLookupDiagnostics."""

    def __init__(self, **defaults):
      InternetGatewayDevice_v1_6.NSLookupDiagnostics.__init__(self, defaults=defaults)
      self.Export(params=['DiagnosticsState',
                          'ResultNumberOfEntries'],
                  lists=['Result'])

    class Result(InternetGatewayDevice_v1_6.NSLookupDiagnostics.Result):
      """Represents InternetGatewayDevice_v1_7.NSLookupDiagnostics.Result.{i}."""

      def __init__(self, **defaults):
        InternetGatewayDevice_v1_6.NSLookupDiagnostics.Result.__init__(self, defaults=defaults)
        self.Export(params=['Status'])

  class PeriodicStatistics(InternetGatewayDevice_v1_6.PeriodicStatistics):
    """Represents InternetGatewayDevice_v1_7.PeriodicStatistics."""

    def __init__(self, **defaults):
      InternetGatewayDevice_v1_6.PeriodicStatistics.__init__(self, defaults=defaults)
      self.Export(params=['SampleSetNumberOfEntries'],
                  lists=['SampleSet'])

    class SampleSet(InternetGatewayDevice_v1_6.PeriodicStatistics.SampleSet):
      """Represents InternetGatewayDevice_v1_7.PeriodicStatistics.SampleSet.{i}."""

      def __init__(self, **defaults):
        InternetGatewayDevice_v1_6.PeriodicStatistics.SampleSet.__init__(self, defaults=defaults)
        self.Export(params=['ParameterNumberOfEntries'])

  class SelfTestDiagnostics(InternetGatewayDevice_v1_6.SelfTestDiagnostics):
    """Represents InternetGatewayDevice_v1_7.SelfTestDiagnostics."""

    def __init__(self, **defaults):
      InternetGatewayDevice_v1_6.SelfTestDiagnostics.__init__(self, defaults=defaults)
      self.Export(params=['DiagnosticsState'])

  class UPnP(InternetGatewayDevice_v1_6.UPnP):
    """Represents InternetGatewayDevice_v1_7.UPnP."""

    def __init__(self, **defaults):
      InternetGatewayDevice_v1_6.UPnP.__init__(self, defaults=defaults)
      self.Export(objects=['Device',
                           'Discovery'])

    class Device(InternetGatewayDevice_v1_6.UPnP.Device):
      """Represents InternetGatewayDevice_v1_7.UPnP.Device."""

      def __init__(self, **defaults):
        InternetGatewayDevice_v1_6.UPnP.Device.__init__(self, defaults=defaults)
        self.Export(params=['UPnPDMBasicMgmt',
                            'UPnPDMConfigurationMgmt',
                            'UPnPDMSoftwareMgmt'],
                    objects=['Capabilities'])

      class Capabilities(InternetGatewayDevice_v1_6.UPnP.Device.Capabilities):
        """Represents InternetGatewayDevice_v1_7.UPnP.Device.Capabilities."""

        def __init__(self, **defaults):
          InternetGatewayDevice_v1_6.UPnP.Device.Capabilities.__init__(self, defaults=defaults)
          self.Export(params=['UPnPArchitecture',
                              'UPnPArchitectureMinorVer',
                              'UPnPDMBasicMgmt',
                              'UPnPDMConfigurationMgmt',
                              'UPnPDMSoftwareMgmt'])

    class Discovery(InternetGatewayDevice_v1_6.UPnP.Discovery):
      """Represents InternetGatewayDevice_v1_7.UPnP.Discovery."""

      def __init__(self, **defaults):
        InternetGatewayDevice_v1_6.UPnP.Discovery.__init__(self, defaults=defaults)
        self.Export(params=['DeviceNumberOfEntries',
                            'RootDeviceNumberOfEntries',
                            'ServiceNumberOfEntries'])

  class USBHosts(InternetGatewayDevice_v1_6.USBHosts):
    """Represents InternetGatewayDevice_v1_7.USBHosts."""

    def __init__(self, **defaults):
      InternetGatewayDevice_v1_6.USBHosts.__init__(self, defaults=defaults)
      self.Export(params=['HostNumberOfEntries'],
                  lists=['Host'])

    class Host(InternetGatewayDevice_v1_6.USBHosts.Host):
      """Represents InternetGatewayDevice_v1_7.USBHosts.Host.{i}."""

      def __init__(self, **defaults):
        InternetGatewayDevice_v1_6.USBHosts.Host.__init__(self, defaults=defaults)
        self.Export(params=['DeviceNumberOfEntries'],
                    lists=['Device'])

      class Device(InternetGatewayDevice_v1_6.USBHosts.Host.Device):
        """Represents InternetGatewayDevice_v1_7.USBHosts.Host.{i}.Device.{i}."""

        def __init__(self, **defaults):
          InternetGatewayDevice_v1_6.USBHosts.Host.Device.__init__(self, defaults=defaults)
          self.Export(params=['ConfigurationNumberOfEntries',
                              'Parent'],
                      lists=['Configuration'])

        class Configuration(InternetGatewayDevice_v1_6.USBHosts.Host.Device.Configuration):
          """Represents InternetGatewayDevice_v1_7.USBHosts.Host.{i}.Device.{i}.Configuration.{i}."""

          def __init__(self, **defaults):
            InternetGatewayDevice_v1_6.USBHosts.Host.Device.Configuration.__init__(self, defaults=defaults)
            self.Export(params=['InterfaceNumberOfEntries'])

  class UserInterface(InternetGatewayDevice_v1_6.UserInterface):
    """Represents InternetGatewayDevice_v1_7.UserInterface."""

    def __init__(self, **defaults):
      InternetGatewayDevice_v1_6.UserInterface.__init__(self, defaults=defaults)
      self.Export(objects=['RemoteAccess'])

    class RemoteAccess(InternetGatewayDevice_v1_6.UserInterface.RemoteAccess):
      """Represents InternetGatewayDevice_v1_7.UserInterface.RemoteAccess."""
      pass


if __name__ == '__main__':
  print core.DumpSchema(Device_v1_6)
  print core.DumpSchema(InternetGatewayDevice_v1_7)