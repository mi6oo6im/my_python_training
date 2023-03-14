class HDMIConnectivity:
    def connect_to_device_via_hdmi_cable(self, device):
        pass


class RCAConnectivity:
    def connect_to_device_via_rca_cable(self, device):
        pass


class EthernetConnectivity:
    def connect_to_device_via_ethernet_cable(self, device):
        pass


class PowerOutlet:
    def connect_device_to_power_outlet(self):
        pass


class Television(RCAConnectivity, HDMIConnectivity, PowerOutlet):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)


class DVDPlayer(HDMIConnectivity, PowerOutlet):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)


class GameConsole(HDMIConnectivity, EthernetConnectivity, PowerOutlet):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)


class Router(EthernetConnectivity, PowerOutlet):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)
