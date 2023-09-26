import os

# Execute terraform state list command and capture the output
state_list_output = os.popen("terraform state list").read()

# Split the output by newlines to get a list of resource addresses
resource_addresses = state_list_output.split('\n')

# Loop through the resource addresses and execute terraform state show <address> for each resource
for address in resource_addresses:
    if address != "":
        state_show_output = os.popen(f"terraform state show {address}").read()
        print(f"Resource: {address}")
        print(state_show_output)
        print("------------------------------------------------------------")