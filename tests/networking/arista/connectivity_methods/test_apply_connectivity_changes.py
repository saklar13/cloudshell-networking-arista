from unittest import TestCase

from mock import MagicMock, patch

from cloudshell.networking.arista.runners.arista_connectivity_runner import AristaConnectivityRunner


class TestAristaConnectivityOperations(TestCase):
    def setUp(self):
        self.handler = AristaConnectivityRunner(MagicMock(), MagicMock())

    @patch("cloudshell.networking.arista.runners.arista_connectivity_runner."
           "AristaConnectivityRunner.remove_vlan_flow")
    def test_remove_vlan_triggered(self, rem_vlan_mock):
        rem_vlan_exec_flow_mock = MagicMock(return_value="")
        rem_vlan_mock.execute_flow = rem_vlan_exec_flow_mock
        request = self._get_request().replace("vlan_config_type", "removeVlan")
        self.handler.apply_connectivity_changes(request)
        rem_vlan_exec_flow_mock.assert_called_once()

    @patch("cloudshell.networking.arista.runners.arista_connectivity_runner."
           "AristaConnectivityRunner.add_vlan_flow")
    def test_add_vlan_triggered(self, add_vlan_mock):
            add_vlan_exec_flow_mock = MagicMock(return_value="")
            add_vlan_mock.execute_flow = add_vlan_exec_flow_mock
            request = self._get_request().replace("vlan_config_type", "setVlan")
            self.handler.apply_connectivity_changes(request)
            add_vlan_exec_flow_mock.assert_called_once()

    @staticmethod
    def _get_request():
        return """{
        "driverRequest" : {
            "actions" : [{
                    "connectionId" : "0b0f37df-0f70-4a8a-bd7b-fd21e5fbc23d",
                    "connectionParams" : {
                        "vlanId" : "435",
                        "mode" : "Access",
                        "vlanServiceAttributes" : [{
                                "attributeName" : "QnQ",
                                "attributeValue" : "False",
                                "type" : "vlanServiceAttribute"
                            }, {
                                "attributeName" : "CTag",
                                "attributeValue" : "",
                                "type" : "vlanServiceAttribute"
                            }, {
                                "attributeName" : "Isolation Level",
                                "attributeValue" : "Shared",
                                "type" : "vlanServiceAttribute"
                            }, {
                                "attributeName" : "Access Mode",
                                "attributeValue" : "Access",
                                "type" : "vlanServiceAttribute"
                            }, {
                                "attributeName" : "VLAN ID",
                                "attributeValue" : "435",
                                "type" : "vlanServiceAttribute"
                            }, {
                                "attributeName" : "Pool Name",
                                "attributeValue" : "",
                                "type" : "vlanServiceAttribute"
                            }, {
                                "attributeName" : "Virtual Network",
                                "attributeValue" : "435",
                                "type" : "vlanServiceAttribute"
                            }
                        ],
                        "type" : "setVlanParameter"
                    },
                    "connectorAttributes" : [],
                    "actionId" : "0b0f37df-0f70-4a8a-bd7b-fd21e5fbc23d_5dded658-3389-466a-a479-4b97a3c17ebd",
                    "actionTarget" : {
                        "fullName" : "sw9003-vpp-10-3.cisco.com/port-channel2",
                        "fullAddress" : "10.89.143.226/PC2",
                        "type" : "actionTarget"
                    },
                    "customActionAttributes" : [],
                    "type" : "vlan_config_type"
                }
            ]
        }
        }"""
