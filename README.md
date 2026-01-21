# Managed Identity Key Vault Client 🔐



## Requirements

**Python Version:**
```
Python 3.12+
```

**Azure SDK Packages:**
```
azure-identity==1.25.1
azure-keyvault-secrets==4.10.0
```

## Architecture
```
VM (vm-hub) --[Managed Identity]--> Key Vault (mkyenkeyvault)
```


## Project Structure
```
azure-managed-identity-keyvault-lab/
├── assets/
│   ├── AcessControl.JPG
│   ├── identity.png
│   ├── mysecretkey.JPG
│   ├── role.png
│   └── role_assignment.png
├── lab_identity.py
└── README.md
```

## Step 1 Configuration Steps

### - Enable System-Assigned Managed Identity on VM
- Azure Portal → Virtual Machines → Select VM (vm-hub) → Identity → System assigned → Toggle Status to "On" → Save

![Enable Managed Identity](assets/identity.png)

### - Create Key Vault and Secret
- Azure Portal → Create Resource → Key Vault → Create

Key Vault created → Go to Secrets → Generate/Import → Name: `mysecretkey` → Value: `Eeee19901999***` → Create

![Create Secret](assets/mysecretkey.JPG)

### -  Open Access Control (IAM)
- Key Vault (mkyenkeyvault) → Access control (IAM) → Add → Add role assignment

![Access Control](assets/AcessControl.JPG)

### - Select Key Vault Secrets User Role
- Role tab → Search "Key Vault Secrets User" → Select → Next

![Select Role](assets/role.png)

### - Assign VM Managed Identity to Role
- Members tab → Assign access to: "Managed identity" → Select members → Choose VM (vm-hub) → Select → Review + assign

![Assign Role](assets/role_assigment.png)








## Architecture
```
VM (vm-hub) --[Managed Identity]--> Key Vault (mkyenkeyvault)
```

## Step 2: Install Python venv
```bash
sudo apt install python3.12-venv -y
```
```
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  python3-pip-whl python3-setuptools-whl python3.12-venv
0 upgraded, 3 newly installed, 0 to remove and 3 not upgraded.
Need to get 2429 kB of archives.
After this operation, 2777 kB of additional disk space will be used.
```

## Step 3: Create Virtual Environment
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```
(venv) kemal@vm-hub:~$
```

## Step 4: Install Azure SDK
```bash
pip install azure-identity azure-keyvault-secrets
```
```
Collecting azure-identity
  Downloading azure_identity-1.25.1-py3-none-any.whl (191 kB)
Collecting azure-keyvault-secrets
  Downloading azure_keyvault_secrets-4.10.0-py3-none-any.whl (125 kB)
Collecting azure-core>=1.31.0
  Downloading azure_core-1.38.0-py3-none-any.whl (217 kB)
Collecting cryptography>=2.5
  Downloading cryptography-46.0.3-cp311-abi3-manylinux_2_34_x86_64.whl (4.5 MB)
Collecting msal>=1.30.0
  Downloading msal-1.34.0-py3-none-any.whl (116 kB)
Collecting msal-extensions>=1.2.0
  Downloading msal_extensions-1.3.1-py3-none-any.whl (20 kB)

Successfully installed PyJWT-2.10.1 azure-core-1.38.0 azure-identity-1.25.1 
azure-keyvault-secrets-4.10.0 certifi-2026.1.4 cffi-2.0.0 charset_normalizer-3.4.4 
cryptography-46.0.3 idna-3.11 isodate-0.7.2 msal-1.34.0 msal-extensions-1.3.1 
pycparser-2.23 requests-2.32.5 typing-extensions-4.15.0 urllib3-2.6.3
```

## Step 5: Create Python Script
```bash
cat < lab_identity.py
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
import sys

VAULT_URL = "https://mkyenkeyvault.vault.azure.net/"

def main():
    try:
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=VAULT_URL, credential=credential)

        print(f"\n[Status] Connecting to: {VAULT_URL}")

        retrieved_secret = client.get_secret("mysecretkey")

        print("\n" + "="*45)
        print(f"SUCCESS! Secret retrieved from Azure.")
        print(f"Secret Name : mysecretkey")
        print(f"Secret Value: {retrieved_secret.value}")
        print("="*45 + "\n")

    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred:")
        print(f"{str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
EOF
```

## Step 6: Run Script
```bash
python3 lab_identity.py
```


```

[Status] Connecting to: https://mkyenkeyvault.vault.azure.net/

=============================================
SUCCESS! Secret retrieved from Azure.
Secret Name : mysecretkey
Secret Value: AA***REDACTED***
=============================================
```

## License
MIT License

