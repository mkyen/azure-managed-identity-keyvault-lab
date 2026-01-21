
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
