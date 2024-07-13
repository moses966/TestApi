from ape import project, networks

def get_greeting():
    contract_address = "0x897107AcE23bDcFF9D556DAef791Ae71Dfb6bA94" # Dev: Replace with your depoymen contract address
    testnets = {
        "ethereum": ["sepolia"]
    }

    for ecosystem_name, networks_list in testnets.items():
        ecosystem = networks.ecosystems[ecosystem_name]

        for network_name in networks_list:
            # Start making connections.
            network = ecosystem.get_network(network_name)

            with network.use_provider("alchemy") as provider:
                print(f"Connected to {provider.network_choice}")
                
                # Load the deployed contract
                contract = project.Greeting.at(contract_address)
                text = contract.greet()
                return text

    return None
