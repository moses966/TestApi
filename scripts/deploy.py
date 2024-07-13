from ape import accounts, project

deployer = accounts.load('meta_wallet') # Replace this with your account alias. Run 'ape accounts list' to see the alias you set

def main():
    contract = deployer.deploy(project.Greeting)
    print(f"Contract deployed at: {contract.address}")
