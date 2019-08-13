# Introduction 
This document is created to support Sentia assessment. It briefly explains the step by step approach
on the tasks performed as part of the assessment.

# The Assessment

Using ARM templates and best practices, create the following:
1. An Azure Datalake Gen 2 storage account.
2. key vault with a secret
3. virtual network
4. web app that can access both the datalake storage and the key vault secret
5. load balancer that sits between the web app and the internet
6. Use tags to group the resources.

# Deploy Azure Resources using ARM Templates

1. **Deploy Azure Datalake Gen2:**

    Data Lake Storage Gen2 is the result of converging the capabilities of our two existing storage services, Azure Blob storage and Azure Data Lake Storage Gen1

    Refer the folder 'ArmTemplates\AdlsGen2' for ARM templates and it can be deployed using 'DeployAzResources.ps1' PowerShell script.
    The ARM template is fully parameterized so that it can be reused.

    Note: There is not Python SDK for Datalake Gen2 at this moment.

2. **Deploy Azure KeyVault:**

    Key Vault allows you to securely access sensitive information like Keys, Secrets, Certificates used within your applications.

    Refer the folder 'ArmTemplates\KeyVault' for ARM templates and it can be deployed using 'DeployAzResources.ps1' PowerShell script.
    The ARM template is fully parameterized so that it can be reused.

    While deploying KeyVault we need to provide configure the access policies so that the secrets can be accessed within the application easily.

    As part of this task, keyvault has been deployed and secrets have been created, which was later used in the Web App.

3. **Deploy Azure Vitual Network:**

    An Azure Virtual Network (VNet) is a representation of your own network in the cloud. It is a logical isolation of the Azure cloud dedicated to your subscription.

    Refer the folder 'ArmTemplates\VirtualNetwork' for ARM templates and it can be deployed using 'DeployAzResources.ps1' PowerShell script.
    The ARM template is fully parameterized so that it can be reused.

    This ARM template will also deploy a default subnet along with the VNet.

4. **Web App to access both Datalake & KeyVault:**

    A web application can be created in different ways. I have used Python flask package to create an API which can be hosted on Azure App Services (WebApp) or Virtual Machine.

    Refer the folder 'ArmTemplates\WebApp' for ARM templates and it can be deployed using 'DeployAzResources.ps1' PowerShell script.
    The ARM template is fully parameterized so that it can be reused.

    This template is used to create Azure Web App with following configurations:
    
        a) Environment: Linux
        b) Runtime stack: Python 3.6
        c) App Service Plan: PremiumV2

    The load balancing for Azure Web Apps is automatically enabled and managed by Azure. If we still want ensure the availability of application, it is recommended to use Application Gateway.

    Apart from Azure Web App, there is also ARM template for deploying the Virtual Machine with Load Balancing configurations. It will deploy a VM behind an existing external load balancer.

    The python flask application can be hosted on VM as well.

5. **Deploy Load Balancer:**

    Load balancing provides a higher level of availability by spreading incoming requests across multiple virtual machines.

    Refer the folder 'ArmTemplates\LoadBalancer' for ARM templates and it can be deployed using 'DeployAzResources.ps1' PowerShell script.
    The ARM template is fully parameterized so that it can be reused.

    Note: This ARM template is to deploy an external load balancer with a public ip address.

    After the deployment, I have configured the following with load balancer:
    
        a) To use VM at the backend pool so the load balancer acts as a mediator between the internet and VM.
        b) Configured the health probe with TCP protocol with uses port 80
        c) Created load balancer rule

6. **Tags for Resource:**

    All the resources have been deployed with tags 'sentia' so the resource can be grouped for budgeting purposes.

7. **Deploy Azure Resources:**

    Last but not least, a PowerShell script has been created to deploy the ARM templates. It is possible to deploy multiple ARM templates at the same time. 
    
    The script uses Service Principal for the deployment, which is considered as standard way of deployment.








