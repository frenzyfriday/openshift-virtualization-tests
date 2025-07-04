from typing import Final

from libs.vm.spec import Interface, NetBinding, Network

UDN_L2BRIDGE_BINDING_PLUGIN_NAME: Final[str] = "l2bridge"
UDN_PASST_BINDING_PLUGIN_NAME: Final[str] = "passt"


def udn_primary_network(name: str) -> tuple[Interface, Network]:
    return Interface(name=name, binding=NetBinding(name=UDN_L2BRIDGE_BINDING_PLUGIN_NAME)), Network(name=name, pod={})


def udn_primary_network_passt(name: str) -> tuple[Interface, Network]:
    return Interface(name=name, binding=NetBinding(name=UDN_L2BRIDGE_BINDING_PLUGIN_NAME)), Network(name=name, pod={})
