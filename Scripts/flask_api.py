#import python libraries
from azure.common.credentials import ServicePrincipalCredentials
from azure.datalake.store import core, lib, multithread
from azure.keyvault import KeyVaultClient
from flask import Flask
import os

#define variables
tenantId = os.environ['TENANT_ID']
clientId = os.environ['CLIENT_ID']
clientKey = os.environ['CLIENT_KEY']
adlsAccountName = os.environ['ADLS']
adlsFolderName = os.environ['ADLS_FOLDER']
file_to_read = adlsFolderName+'/sentia.txt'

#Authentication
credentials = ServicePrincipalCredentials(
    client_id = clientId,
    secret = clientKey,
    tenant = tenantId
)
key_vault_client = KeyVaultClient(credentials)
key_vault_uri = "https://sentia.vault.azure.net/"

adlCreds = lib.auth(tenant_id = tenantId, client_id = clientId, client_secret = clientKey)
adlsFileSystemClient = core.AzureDLFileSystem(adlCreds, store_name=adlsAccountName)

#flask API
app = Flask(__name__)

@app.route('/')

def pythonapp():     

    with adlsFileSystemClient.open(file_to_read, 'rb') as f:
        adls_contents = f.read()

    SpnId = key_vault_client.get_secret(key_vault_uri, "ServicePrincipalId", "e70e1e7909d54d9a8b19b414a6dfcc03")
    SpnKey = key_vault_client.get_secret(key_vault_uri, "ServicePrincipalKey", "c2fee9f394454c1894df784fd1abb99b")

    return  'File contents(adls): {} <br/> <br/> Service Principal Id: {} <br/> <br/> Service Principal Key: {}'.format(adls_contents, SpnId.value, SpnKey.value)

if __name__ == "__main__":
    app.run(host='localhost',debug=True)