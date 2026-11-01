---
{"title": "Deploying and managing RHEL on Microsoft Azure", "guide": "deploying_and_managing_rhel_on_microsoft_azure", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/deploying_and_managing_rhel_on_microsoft_azure/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

Streamline your workflow with the new MCP server for Red Hat product documentation.Connect your AI tools and LLMs directly to live Red Hat product documentation. [Connect now](https://docs.redhat.com/en/documentation/mcp_server_for_red_hat_documentation/current%20).

# Deploying and managing RHEL on Microsoft Azure {#deploying-and-managing-rhel-on-microsoft-azure .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Obtaining RHEL system images and creating RHEL instances on Azure {#obtaining-rhel-system-images-and-creating-rhel-instances-on-azure .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140065998123664)

**Abstract**

To use Red Hat Enterprise Linux (RHEL) on Microsoft Azure, you can create and deploy RHEL system images.

This also involves:

-   Registering, deploying, and provisioning RHEL images on Azure

-   Managing networking configurations for RHEL Azure virtual machine (VM)

-   Configuring platform security and trusted execution technologies

-   Managing Red Hat High Availability (HA) clusters for RHEL instances

------------------------------------------------------------------------

## [Providing feedback on Red Hat documentation](#providing-feedback-on-red-hat-documentation) {#providing-feedback-on-red-hat-documentation .title}

We are committed to providing high-quality documentation and value your feedback. To help us improve, you can submit suggestions or report errors through the Red Hat Jira tracking system.

**Procedure**

1.  Log in to the [Jira](https://redhat.atlassian.net/jira/software/c/projects/RHELDOCS/issues/) website.

    If you do not have an account, select the option to create one.

2.  Click **Create** in the top navigation bar.

3.  Enter a descriptive title in the **Summary** field.

4.  Enter your suggestion for improvement in the **Description** field. Include links to the relevant parts of the documentation.

5.  Click **Create** at the bottom of the window.

## [Chapter 1. Introducing RHEL on public cloud platforms](#introducing-rhel-on-public-cloud-platforms) {#chapter-1.-introducing-rhel-on-public-cloud-platforms .title}

Public cloud platforms provide computing resources as a service. Instead of maintaining on-premises hardware, you can run IT workloads as public cloud instances. This includes Red Hat Enterprise Linux (RHEL) systems.

### [1.1. Benefits of using RHEL in a public cloud](#benefits-of-using-rhel-in-a-public-cloud) {#benefits-of-using-rhel-in-a-public-cloud .title}

Running Red Hat Enterprise Linux (RHEL) on public cloud platforms provides flexible resource allocation, cost efficiency, and software-controlled configurations to optimize your infrastructure without managing physical hardware.

RHEL as a cloud instance located on a public cloud platform has the following benefits over RHEL on-premises physical systems or virtual machines (VMs):

Flexible and fine-grained allocation of resources

:   A RHEL instance runs as a VM on a cloud platform. The cloud platform is a cluster of remote servers maintained by the cloud service provider. Therefore, on the software level, allocating hardware resources to the instance is easily customizable, such as a specific type of CPU or storage.

    In contrast to local RHEL systems, your resource options are not restricted by the limitations of physical hardware. Instead, you can select from a wide range of features and configurations that the cloud provider makes available.

Space and cost efficiency

:   You do not need to own any on-premises servers to host cloud workloads. This avoids the space, power, and maintenance requirements associated with physical hardware.

    Instead, you pay the cloud provider directly for using a cloud instance. The cost is based on allocation of hardware and usage time. Therefore, you can optimize your costs based on the requirements.

Software-controlled configurations

:   You can save the entire configuration of a cloud instance as data. Also, you can control it with software through the cloud platform. Therefore, create, remove, clone, or migrate the instance. You also operate a cloud instance remotely in a cloud provider console, and it connects to remote storage by default.

    In addition, you can back up the current state of a cloud instance as a snapshot at any time. Afterwards, you can load the snapshot to restore the instance to the saved state.

Separation from the host and software compatibility

:   Similarly to a local VM, the RHEL guest operating system on a cloud instance runs on a Kernel-based Virtual Machine (KVM). KVM is a loadable kernel module that transforms the local RHEL kernel into a `TYPE-1 hypervisor`{.literal}. KVM is separate from the host operating system. It is also separate from the client system, which you can connect to the instance.

    Therefore, you can install any operating system on the cloud instance. This means that on a RHEL public cloud instance, you can run RHEL-specific applications that might not be usable on your local operating system. In addition, even if the operating system of the instance becomes unstable or compromised, it does not affect your client system.

**Additional resources**

-   [What is public cloud?](https://www.redhat.com/en/topics/cloud-computing/what-is-public-cloud)
-   [What is a hyperscaler?](https://www.redhat.com/en/topics/cloud/what-is-a-hyperscaler)
-   [Types of cloud computing](https://www.redhat.com/en/topics/cloud-computing/public-cloud-vs-private-cloud-and-hybrid-cloud)

### [1.2. Public cloud use cases for RHEL](#public-cloud-use-cases-for-rhel) {#public-cloud-use-cases-for-rhel .title}

Deploying applications on a public cloud depends on the use case. Consider the advantages for your Red Hat Enterprise Linux (RHEL) deployments when evaluating if it is beneficial to migrate your deployments to the public cloud.

Beneficial use cases

:   -   Public cloud instances effectively scale your computing power on and off based on-demand. This is known as *scaling up* and *scaling down*. You can use RHEL on public cloud in the following scenarios:

        -   Clusters with peak workloads and low general performance requirements benefit from flexible scaling. Scaling up and down based on your demands can be highly efficient in terms of resource costs.
        -   Quickly configuring or expanding your clusters. This avoids high upfront costs of configuring local servers.

    -   Changes in your local environment do not affect cloud instances. Therefore, you can use them for backup and disaster recovery.

Potentially problematic use cases

:   -   You are running an existing environment that you cannot adjust. Customizing a cloud instance to fit existing deployment needs might not be economically efficient. Your current host platform might be more cost-effective.
    -   You are operating with a hard limit on your budget. Local data centers typically provide less flexibility than public clouds. However, they offer more control over maximum resource costs.

**Additional resources**

-   [Should I migrate my application to the cloud? Here's how to decide.](https://www.redhat.com/en/blog/should-i-migrate-my-application-cloud-heres-how-decide)
-   [Obtaining RHEL for public cloud deployments](#obtaining-rhel-for-public-cloud-deployments "1.4. Obtaining RHEL for public cloud deployments")

### [1.3. Frequent concerns when migrating to a public cloud](#frequent-concerns-when-migrating-to-a-public-cloud) {#frequent-concerns-when-migrating-to-a-public-cloud .title}

Moving your RHEL workloads from a local environment to a public cloud platform might raise concerns about the changes involved. The following are the most commonly asked questions:

Will my RHEL work differently as a cloud instance than as a local virtual machine?

:   In most respects, RHEL instances on a public cloud platform work the same as RHEL virtual machines on a local host, such as an on-premises server. Notable exceptions include:

    -   Instead of private orchestration interfaces, public cloud instances use provider-specific console interfaces for managing your cloud resources.
    -   Certain features, such as nested virtualization, might not work correctly. If a specific feature is critical for your deployment, check the feature's compatibility in advance with your chosen public cloud provider.

Will my data stay safe in a public cloud as opposed to a local server?

:   The data in your RHEL cloud instances remains in your ownership. Your public cloud provider does not have access to it. Major cloud providers support data encryption in transit. This improves data security when migrating your virtual machines to the public cloud. Security of RHEL public cloud instances can be summarized as follows:

    -   Your public cloud provider is responsible for the security of the cloud hypervisor
    -   Red Hat provides the security features of the RHEL guest operating systems in your instances
    -   You manage the specific security settings and practices in your cloud infrastructure

What effect does my geographic region have on the functionality of RHEL public cloud instances?
:   You can use RHEL instances on a public cloud platform regardless of your geographical location. Therefore, you can run your instances in the same region as your on-premises server. However, hosting your instances in a physically distant region might lead to high latency and reduced performance. In addition, depending on the public cloud provider, certain regions might offer additional features or be more cost-efficient. Before creating your RHEL instances, review the properties of the hosting regions available for your chosen cloud provider.

### [1.4. Obtaining RHEL for public cloud deployments](#obtaining-rhel-for-public-cloud-deployments) {#obtaining-rhel-for-public-cloud-deployments .title}

To deploy Red Hat Enterprise Linux (RHEL) in a public cloud environment, you must select a certified cloud service provider (CCSP) and create a RHEL cloud instance.

-   Based on your requirements and the current offerings in the market, select the optimal CCSP for your use case to run RHEL instances are Amazon Web Services (AWS), Google Cloud, and Microsoft Azure.

    Note

    This document specifically addresses the process of deploying RHEL on Azure.

-   Create a RHEL cloud instance on your cloud platform.

-   Use Red Hat Update Infrastructure (RHUI) to keep your RHEL deployment up-to-date.

**Additional resources**

-   [RHUI documentation](https://docs.redhat.com/en/documentation/red_hat_update_infrastructure)
-   [Red Hat Open Hybrid Cloud](https://www.redhat.com/en/products/open-hybrid-cloud)
-   [Red Hat Ecosystem Catalog](https://catalog.redhat.com/)
-   [Methods for creating RHEL cloud instances](#methods-for-creating-rhel-cloud-instances "1.5. Methods for creating RHEL cloud instances")

### [1.5. Methods for creating RHEL cloud instances](#methods-for-creating-rhel-cloud-instances) {#methods-for-creating-rhel-cloud-instances .title}

You can create a Red Hat Enterprise Linux (RHEL) system image and import it to the cloud platform.

To build the system image, you can use either RHEL image builder or purchase the image from the cloud service provider marketplace. You can then deploy the RHEL image as a cloud instance.

To deploy a RHEL instance on a public cloud platform, you can use either of the following methods:

Create a RHEL system image and import it to the cloud platform

:   -   To create the system image, you can use the [RHEL image builder](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/installing-rhel-image-builder) or build the image manually.
    -   \"This method uses your existing RHEL subscription (bring your own subscription (BYOS).
    -   You pre-pay a yearly subscription, and you can use your Red Hat customer discount.
    -   Red Hat provides customer service.
    -   For creating many images effectively, you can use the `cloud-init`{.literal} utility.

Purchase a RHEL instance directly from the cloud provider marketplace

:   -   You post-pay an hourly rate for using the service. This method is also referred to as pay as you go (PAYG).
    -   The cloud service provider provides customer service.

**Additional resources**

-   [What is a golden image?](https://www.redhat.com/en/topics/linux/what-is-a-golden-image)

## [Chapter 2. Preparing and uploading VHD images to Microsoft Azure](#preparing-and-uploading-vhd-images-to-microsoft-azure) {#chapter-2.-preparing-and-uploading-vhd-images-to-microsoft-azure .title}

You can create custom images and update them, either manually or automatically, on the Microsoft Azure cloud by using RHEL image builder.

### [2.1. Preparing to upload Microsoft Azure VHD images manually](#preparing-to-manually-upload-microsoft-azure-vhd-images) {#preparing-to-upload-microsoft-azure-vhd-images-manually .title}

To create a virtual hard drive (VHD) image that you can manually upload to the `Microsoft Azure`{.literal} cloud, you can use RHEL image builder.

**Prerequisites**

-   You must have a Microsoft Azure resource group and storage account.
-   You have Python installed. The `AZ CLI`{.literal} tool depends on Python.

**Procedure**

1.  Import the Microsoft repository key:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo rpm --import https://packages.microsoft.com/keys/microsoft-2025.asc
    ```

2.  Create a `packages-microsoft-com-prod`{.literal} repository:

    ``` {.language-plaintext tabindex="-1"}
    [azure-cli]
    name=Azure CLI
    baseurl=https://packages.microsoft.com/yumrepos/packages.microsoft.com/rhel/10/prod/
    enabled=1
    gpgcheck=1
    gpgkey=https://packages.microsoft.com/keys/microsoft.asc
    ```

3.  Install Microsoft Azure CLI. The downloaded version of the Microsoft Azure CLI package can vary depending on the currently available version.

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dnf install azure-cli
    ```

4.  Run Microsoft Azure CLI:

    ``` {.language-plaintext tabindex="-1"}
    $ az login
    ```

    The command line shows the following message: `Note, we have launched a browser for you to login. For old experience with device code, use az login --use-device-code`{.literal}. Then, the command line opens the [Login](https://microsoft.com/devicelogin) from where you can log in.

    Note

    If you are running a remote (SSH) session, the login page link does not open in the browser. In this case, you can copy the link to a browser and log in to authenticate your remote session. To sign in, use a web browser to open the [Login](https://microsoft.com/devicelogin) page and enter the device code to authenticate.

5.  List the keys for the storage account in Microsoft Azure and make note of the value `key1`{.literal} from the output of the previous command.

    ``` {.language-plaintext tabindex="-1"}
    $ az storage account keys list --resource-group <resource_group_name> --account-name <account_name>
    ```

    Replace *`resource-group-name`{.literal}* with the name of your Microsoft Azure resource group and *`storage-account-name`{.literal}* with the name of your Microsoft Azure storage account.

    a.  To list the available resources using the following command:

        ``` {.language-plaintext tabindex="-1"}
        $ az resource list
        ```

6.  Create a storage container:

    ``` {.language-plaintext tabindex="-1"}
    $ az storage container create --account-name <storage_account_name> \
    --account-key <key1_value> --name <storage_account_name>
    ```

    Replace *`storage-account-name`{.literal}* with the name of the storage account.

**Additional resources**

-   [Microsoft Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?view=azure-cli-latest&pivots=dnf)

### [2.2. Manually uploading VHD images to Microsoft Azure cloud](#manually-uploading-vhd-images-to-microsoft-azure-cloud) {#manually-uploading-vhd-images-to-microsoft-azure-cloud .title}

Create your customized virtual hard drive (VHD) image, and manually upload it to the Microsoft Azure cloud. When you create a `.vhd`{.literal} image by using the CLI, RHEL image builder writes temporary files to the `/var`{.literal} subdirectory.

Note

The partition and filesystem configurations in your blueprint determine `.vhd`{.literal} image size. Insufficient storage might cause a "No space left on device" error. Ensure `/var`{.literal} has at least 15 to 20 GB of free space.

**Prerequisites**

-   Your system must be configured for uploading Microsoft Azure VHD images.
-   You have an Azure access key storage account.

**Procedure**

1.  Create a `azure.toml`{.literal} blueprint, and add the following information to it:

    ``` {.language-plaintext tabindex="-1"}
    provider = "azure"

    [settings]
    storageAccount = "<your-storage-account-name>"
    storageAccessKey = "<storage-access-key-you-copied-in-the-Azure-portal>"
    container = "<your-storage-container-name>"
    ```

2.  Build the image, passing the following arguments:

    ``` {.language-plaintext tabindex="-1"}
    $ image-builder build <your-blueprint> vhd <your-image-key> azure.toml
    ```

    Replace *\<your-image-key\>* with the name of the image that you want.

3.  Push the image to Microsoft Azure and create an instance from it:

    ``` {.language-plaintext tabindex="-1"}
    $ az storage blob upload --account-name <account-name> --container-name <container-name> --file <image-disk>.vhd --name image-disk.vhd --type page
    ```

4.  After the upload to the Microsoft Azure Blob storage completes, create a Microsoft Azure image from it. The images that you create with RHEL image builder generate hybrid images that support `V1 = BIOS`{.literal} and `V2 = UEFI`{.literal}. Use `--hyper-v-generation`{.literal} to specify instance type. `V1`{.literal} is the default.

    ``` {.language-plaintext tabindex="-1"}
    $ az image create --resource-group resource_group_name --name image-disk.vhd --os-type linux --location location \
    --source https://$account_name.blob.core.windows.net/container_name/image-disk.vhd
    - Running
    ```

**Verification**

1.  Create an instance either with the Microsoft Azure portal, or a command similar to the following:

    ``` {.language-plaintext tabindex="-1"}
    $ az vm create --resource-group resource_group_name --location location --name vm_name --image image-disk.vhd(--admin-username azure-user --generate-ssh-keys*
    - Running
    ```

2.  Use your private key by using SSH to access the resulting instance. Log in as `azure-user`{.literal}.

**Additional resources**

-   [Composing an image for the `.vhd`{.literal} format fails (Red Hat Knowledgebase)](https://access.redhat.com/solutions/6955577)

### [2.3. Creating and automatically uploading VHD images to Microsoft Azure cloud](#creating-and-automatically-uploading-vhd-images-to-microsoft-azure-cloud) {#creating-and-automatically-uploading-vhd-images-to-microsoft-azure-cloud .title}

By using RHEL image builder, you can create `.vhd`{.literal} images, which are automatically uploaded to an Azure Blob Storage in the Microsoft Azure Cloud service provider.

**Prerequisites**

-   You have root access to the system.
-   You have access to the RHEL image builder interface of the RHEL web console.
-   You created a blueprint. See [Creating a RHEL image builder blueprint in the web console interface](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/creating-system-images-with-gui#creating-a-blueprint-in-the-web-console-interface).
-   You have a [Microsoft Storage Account](https://portal.azure.com/#create/Microsoft.StorageAccount) created.
-   You have a writable [Blob Storage](https://portal.azure.com/#blade/HubsExtension/BrowseResource/resourceType/Microsoft.Storage%2FStorageAccounts) prepared.

**Procedure**

1.  In the RHEL image builder dashboard, select your blueprint, click the **Images** tab, and click **Create Image** to create your customized `.vhd`{.literal} image.
2.  Select `Microsoft Azure (.vhd)`{.literal} from the **Type** drop-down, check **Upload to Azure**, enter the **Image Size**, and click **Next**.
3.  Enter your **Storage account** name and your **Storage access key** then, click **Next**.
4.  Review the configuration and click **Create**. The RHEL image builder and upload processes start.
5.  In the [Microsoft Azure portal](https://portal.azure.com) navigate to **Storage accounts** \> **Containers** and verify if your `.vhd`{.literal} is present.

**Verification**

1.  In the Azure portal search bar, type **Images** and click **+Create**. Configure the following details:

    -   Select your resource group and enter an image name.
    -   Set **OS type** to Linux and VM generation to **Gen 2**.
    -   Under **Storage Blob**, browse to select your VHD file.
    -   Choose an **Account Type**, for example, Standard SSD.

2.  Click **Review + Create**, and then **Create**. Wait for the image creation to complete.

3.  Click **Go to resource**, then click **Create VM**. Enter a VM name, configure the **Size** and **Administrator account** sections, then click **Review + Create** and **Create**.

4.  After the deployment finishes, retrieve the public IP address and connect by using SSH.

    \$ **ssh *\<username\>*@*\<public-IP-address\>***

**Additional resources**

-   [Microsoft Azure Storage Documentation](https://docs.microsoft.com/en-us/azure/storage/)
-   [Create an Azure storage account](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?toc=%2Fazure%2Fstorage%2Fblobs%2Ftoc.json&tabs=azure-portal)

## [Chapter 3. Deploying a RHEL image as a compute instance on Azure](#deploying-a-rhel-image-as-a-compute-instance-on-azure) {#chapter-3.-deploying-a-rhel-image-as-a-compute-instance-on-azure .title}

You can deploy a Red Hat Enterprise Linux (RHEL) image as an Azure Compute virtual machine (VM) by converting the image to an Azure-compatible format and then deploying it. Use the RHEL image builder or manually create a virtual hard drive (VHD) to customize and deploy your RHEL image to Azure.

### [3.1. Available RHEL image types for public cloud](#available-rhel-image-types-for-public-cloud) {#available-rhel-image-types-for-public-cloud .title}

To deploy your Red Hat Enterprise Linux (RHEL) virtual machine (VM) on a certified cloud service provider (CCSP), you can use several options. The following table lists the available image types, subscriptions, considerations, and sample scenarios for the image types.

To deploy customized ISO images, you can use RHEL image builder. With RHEL image builder, you can create, upload, and deploy these custom images specific to your chosen CCSP.

+----------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Image types                                        | Subscriptions                                  | Considerations                                                                                                                                                                                                                                                                                       | Sample scenario                                                                                                                     |
+:===================================================+:===============================================+:=====================================================================================================================================================================================================================================================================================================+:====================================================================================================================================+
| Deploy a Red Hat gold image                        | Use your existing Red Hat subscriptions        | The subscriptions include the Red Hat product cost and support for Cloud Access images, while you pay the CCSP for all other instance costs.                                                                                                                                                         | Select a Red Hat gold image on the CCSP according to requirement.                                                                   |
+----------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Deploy a custom image that you move to the CCSP    | Use your existing Red Hat subscriptions        | The subscriptions includes the Red Hat product cost and support for custom RHEL image, while you pay the CCSP for all other instance costs.                                                                                                                                                          | Upload your custom image and attach your subscriptions                                                                              |
+----------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Deploy an existing RHEL based custom machine image | The custom machine images include a RHEL image | You pay the CCSP on an hourly basis based on a *pay-as-you-go* model. For this model, on-demand images are available on the CCSP marketplace. The CCSP provides support for these images, while Red Hat handles updates. The CCSP provides updates through the Red Hat Update Infrastructure (RHUI). | Select a RHEL image when you launch an instance on the CCSP cloud management console, or choose an image from the CCSP marketplace. |
+----------------------------------------------------+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+

: Table 3.1. Image options

Show more

**Additional resources**

-   [Composing a Customized RHEL System Image](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/installing-rhel-image-builder)
-   [Red Hat Ecosystem Catalog](https://catalog.redhat.com/)
-   [Red Hat Cloud Access Reference Guide](https://www.redhat.com/en/technologies/cloud-computing/cloud-access)
-   [Red Hat Cloud Access program overview](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_rhel_system_registration/con-red-hat-cloud-access-program-overview)
-   [Required list of system packages](#required-system-packages "3.2. Required system packages")
-   [Azure Marketplace](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/redhat.rhel-20190605?tab=PlansAndPrice)
-   [Billing options in the Azure Marketplace](https://learn.microsoft.com/en-us/azure/marketplace/marketplace-commercial-transaction-capabilities-and-considerations)
-   [Red Hat Enterprise Linux Bring-Your-Own-Subscription gold images in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/workloads/redhat/byos)

### [3.2. Required system packages](#required-system-packages) {#required-system-packages .title}

To create and configure a base image of RHEL, your host system must have the following packages installed.

+---------------+-----------------------------------------------+--------------------------------------------------------------------------------------+
| Package       | Repository                                    | Description                                                                          |
+:==============+:==============================================+:=====================================================================================+
| libvirt       | `rhel-10-for-x86_64-appstream-rpms`{.literal} | Open source API, daemon, and management tool for managing platform virtualization    |
+---------------+-----------------------------------------------+--------------------------------------------------------------------------------------+
| virt-install  | `rhel-10-for-x86_64-appstream-rpms`{.literal} | A command-line utility for building VMs                                              |
+---------------+-----------------------------------------------+--------------------------------------------------------------------------------------+
| libguestfs    | `rhel-10-for-x86_64-appstream-rpms`{.literal} | A library for accessing and modifying VM file systems                                |
+---------------+-----------------------------------------------+--------------------------------------------------------------------------------------+
| guestfs-tools | `rhel-10-for-x86_64-appstream-rpms`{.literal} | System administration tools for VMs; includes the `virt-customize`{.literal} utility |
+---------------+-----------------------------------------------+--------------------------------------------------------------------------------------+

: Table 3.2. System packages

Show more

After confirming installation of the mentioned system packages, follow the deployment steps in [deploying a RHEL instance by using a custom base image](#deploying-a-rhel-instance-by-using-a-custom-base-image "3.3. Deploying a RHEL instance by using a custom base image")

**Additional resources**

-   [Tools and interfaces for virtualization management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/basic-concepts-of-virtualization-in-rhel#tools-and-interfaces-for-virtualization-management)
-   [Creating virtual machines by using the command line](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/creating-virtual-machines#creating-virtual-machines-by-using-the-command-line-interface)
-   [Creating a virtual machine template by using virt-sysprep](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/cloning-virtual-machines#creating-a-virtual-machine-template-by-using-virt-sysprep)
-   [libguestfs documentation](https://www.libguestfs.org/)

### [3.3. Deploying a RHEL instance by using a custom base image](#deploying-a-rhel-instance-by-using-a-custom-base-image) {#deploying-a-rhel-instance-by-using-a-custom-base-image .title}

To manually configure a virtual machine (VM) on cloud platforms, create a base (starter) image, modify configuration settings, and add the packages to the VM. This VM is customizable, flexible, and lightweight. After uploading the image, you can change settings for these specific applications.

**Prerequisites**

-   You have access to the command line interface (CLI) or the web console for creating and configuring VM. If you do not have access to the CLI or the web console, you can use the Red Hat Cloud Access portal to create and configure VM.
-   You have prepared a Hyper-V cloud image of RHEL.
-   You have enabled the required settings either during the initial VM creation or provisioning a VM image to the Azure cloud.
-   You have checked the [required list of system packages](#required-system-packages "3.2. Required system packages").
-   Secure Shell (SSH) - Enable SSH to give remote access to your VM.
-   Dynamic Host Configuration Protocol (DHCP) - Configure the primary virtual adapter to use DHCP.
-   Swap space - Do not create a dedicated `swap`{.literal} file or partition during installation. Avoid creating the `swap`{.literal} partition on the operating system disk or storage disk. Configure the `cloud-init`{.literal} utility to automatically create a `swap`{.literal} partition on an ephemeral disk of the VM. Ephemeral disks provide local VM storage. Resource disks provide mounted storage. Both storage types store data temporarily.
-   Network Interface Card (NIC) - Choose virtio for the primary virtual network adapter.
-   Encryption - For custom images, use Network Bound Disk Encryption (NBDE) for full disk encryption on Azure.
-   You have enabled virtualization on the host machine.
-   For web console, ensure the following options:
-   You have not checked the **Immediately Start VM** option.
-   You have already changed the **Memory** size to your preferred settings.
-   You have changed the **Model** option under **Virtual Network Interface Settings** to **virtio** and **vCPUs** to the capacity settings for the VM.

**Procedure**

1.  Configure the Red Hat Enterprise Linux (RHEL) VM. See the Additional resources section for details:

    a.  To install from CLI, ensure that you set the default memory, network interfaces, and CPUs according to your requirement for the VM.
    b.  You can also install RHEL from the web console.

2.  When the installation starts:

    a.  Create a `root`{.literal} password.
    b.  Create an administrative user account.

3.  After the installation completes, reboot the VM and log in to the `root`{.literal} account.

4.  After logging in as `root`{.literal}, you can configure the image.

5.  Register the VM and enable the RHEL repository:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager register
    ```

6.  Install the `cloud-init`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install cloud-init
    ```

7.  Enable and start the `cloud-init`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now cloud-init.service
    ```

8.  Reboot the VM to apply the changes.

**Next steps**

-   Install [the Azure CLI](#installing-the-azure-cli "3.4. Installing the Azure CLI") to access Azure resources and services.

**Verification**

-   Verify that the VM is running:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status cloud-init
    ```

**Additional resources**

-   [Prepare a Red Hat-based virtual machine from Hyper-V Manager](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/redhat-create-upload-vhd#prepare-a-red-hat-based-virtual-machine-from-hyper-v-manager)
-   [Prepare an AMD64 or Intel 64 system to host virtual machines](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/preparing-rhel-to-host-virtual-machines#preparing-an-amd64-or-intel64-system-to-host-virtual-machines)
-   [Creating virtual machines by using the command line](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/creating-virtual-machines#creating-virtual-machines-by-using-the-command-line-interface)
-   [Creating virtual machines by using the web console](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/creating-virtual-machines#creating-virtual-machines-by-using-the-web-console)

### [3.4. Installing the Azure CLI](#installing-the-azure-cli) {#installing-the-azure-cli .title}

To connect to Azure Cloud and manage Azure resources directly from the command line of your host system, you can use the Azure command-line interface (CLI).

**Prerequisites**

-   You have created a [Red Hat account](https://www.redhat.com/wapps/ugc/register.html).
-   You have completed [the deployment of a RHEL image on Azure](#deploying-a-rhel-instance-by-using-a-custom-base-image "3.3. Deploying a RHEL instance by using a custom base image").
-   You have an account with [Microsoft Azure](https://azure.microsoft.com/en-us/free/).
-   You have installed Python 3.x.

**Procedure**

1.  Import the Microsoft repository key:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc
    ```

2.  Create a local Azure CLI repository entry:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo sh -c 'echo -e "[azure-cli]\nname=Azure CLI\nbaseurl=https://packages.microsoft.com/yumrepos/azure-cli\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/azure-cli.repo'
    ```

3.  Update the `dnf`{.literal} package index:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dnf update
    ```

4.  Install the Azure CLI:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dnf install -y azure-cli
    ```

5.  Run the Azure CLI:

    ``` {.language-plaintext tabindex="-1"}
    $ az login
    ```

**Verification**

-   Verify that the Azure CLI is installed and running:

    ``` {.language-plaintext tabindex="-1"}
    $ az --version
    ```

**Next steps**

-   Install [the Hyper-V device drivers](#installing-hyper-v-device-drivers "3.5. Installing Hyper-V device drivers") to efficiently run VM on Azure.

**Additional resources**

-   [Install the Azure CLI on Linux](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=dnf)
-   [Azure CLI command reference](https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest)

### [3.5. Installing Hyper-V device drivers](#installing-hyper-v-device-drivers) {#installing-hyper-v-device-drivers .title}

Before provisioning a virtual machine (VM) image as an Azure VM, you must install Hyper-V device drivers. Microsoft provides these network and storage device drivers in their Linux Integration Services (LIS) for Hyper-V package.

**Prerequisites**

-   You have created a [Red Hat account](https://www.redhat.com/wapps/ugc/register.html).
-   You have a [Microsoft Azure account](https://azure.microsoft.com/en-us/Free).
-   You have installed [the Azure CLI](#installing-the-azure-cli "3.4. Installing the Azure CLI").

**Procedure**

1.  Verify if the system has Hyper-V device drivers:

    ``` {.language-plaintext tabindex="-1"}
    # lsinitrd | grep hv
    ```

    ``` {.language-plaintext tabindex="-1"}
    drwxr-xr-x   2 root     root            0 Aug 12 14:21 usr/lib/modules/3.10.0-932.el10.x86_64/kernel/drivers/*hv*
    -rw-r--r--   1 root     root        31272 Aug 11 08:45 usr/lib/modules/3.10.0-932.el10.x86_64/kernel/drivers/hv/*hv_vmbus.ko.xz*
    -rw-r--r--   1 root     root        25132 Aug 11 08:46 usr/lib/modules/3.10.0-932.el10.x86_64/kernel/drivers/net/hyperv/*hv_netvsc.ko.xz*
    -rw-r--r--   1 root     root         9796 Aug 11 08:45 usr/lib/modules/3.10.0-932.el10.x86_64/kernel/drivers/scsi/*hv_storvsc.ko.xz*
    ```

    In case, all the drivers are not installed or even the `hv_vmbus`{.literal} driver is listed, complete the remaining steps.

2.  Create the `hv.conf`{.literal} file in the `/etc/dracut.conf.d`{.literal} directory and add the following driver parameters:

    ``` {.language-plaintext tabindex="-1"}
    # vi hv.conf
    ```

    ``` {.language-plaintext tabindex="-1"}
    add_drivers+=" hv_vmbus "
    add_drivers+=" hv_netvsc "
    add_drivers+=" hv_storvsc "
    add_drivers+=" nvme "
    ```

    Ensure that you have added spaces after and before the double quotes `add_drivers+=" hv_vmbus "`{.literal} to load unique drivers, in case other Hyper-V drivers already exist in the environment.

3.  Regenerate the `initramfs`{.literal} image:

    ``` {.language-plaintext tabindex="-1"}
    # dracut -f -v --regenerate-all
    ```

**Verification**

1.  Reboot the machine.

2.  Verify installation of drivers:

    ``` {.language-plaintext tabindex="-1"}
    # lsinitrd | grep hv
    ```

**Next steps**

-   Prepare your VM for [deployment on Azure cloud](#preparing-a-virtual-machine-for-azure-deployment "3.7. Preparing a virtual machine for Azure deployment").

**Additional resources**

-   [Bring your own image to Azure](https://learn.microsoft.com/en-us/partner-center/marketplace-offers/azure-vm-use-own-image#bring-your-image-into-azuree)
-   [Microsoft Hyper-V Network Virtualization (NetVSC) driver](https://docs.kernel.org/networking/device_drivers/ethernet/microsoft/netvsc.html)

### [3.6. Configuring swap space with cloud-init on Azure](#configuring-swap-space-with-cloud-init-on-azure) {#configuring-swap-space-with-cloud-init-on-azure .title}

To use swap space for a Red Hat Enterprise Linux (RHEL) virtual machine (VM) on Microsoft Azure, create a swap partition on an ephemeral disk. Only use the ephemeral disk for creating the swap partition, not the operating system disk or data disk.

**Prerequisites**

-   Both the ephemeral and resource disks offer only temporary data storage: deleting, moving, stopping, or experiencing a VM failure will result in the loss of data stored on these disks.

-   You have understood that you should not use the ephemeral disk for persistent data. All contents, including the swap partition, are deleted when the VM is stopped or moved.

-   You have understood the difference between ephemeral and resource disks:

    -   The ephemeral disk is local storage attached directly to the VM.
    -   The resource disk is mounted storage on the VM itself.

-   You have created a [Red Hat account](https://www.redhat.com/wapps/ugc/register.html).

-   You have a [Microsoft Azure account](https://azure.microsoft.com/en-us/Free).

-   You have installed the `cloud-init`{.literal} utility on the VM.

-   You have disabled the swap configuration in the Windows Azure Linux Agent (WALA) by setting the parameters in the `/etc/waagent.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    ResourceDisk.Format=n
    ResourceDisk.EnableSwap=n
    ResourceDisk.SwapSizeMB=0
    ```

-   You have an ephemeral disk available on the VM.

**Procedure**

1.  Log in to the VM.

2.  Create and edit the `/etc/cloud/cloud.cfg.d/00-azure-swap.cfg`{.literal} configuration file and add the following `cloud-init`{.literal} configuration to the file:

    ``` {.language-plaintext tabindex="-1"}
    # vi /etc/cloud/cloud.cfg.d/00-azure-swap.cfg
    ```

    ``` {.language-yaml tabindex="-1"}
    #cloud-config
    disk_setup:
      ephemeral0:
        table_type: gpt
        layout: [66, [33,82]]
        overwrite: true
    fs_setup:
      - device: ephemeral0.1
        filesystem: ext4
      - device: ephemeral0.2
        filesystem: swap
    mounts:
      - ["ephemeral0.1", "/mnt"]
      - ["ephemeral0.2", "none", "swap", "sw,nofail,x-systemd.requires=cloud-init.service", "0", "0"]
    ```

    This configuration:

    -   Partitions the ephemeral disk (`ephemeral0`{.literal}) with a GPT partition table.

    -   Creates two partitions: 66% for a file system (mounted at `/mnt`{.literal}) and 33% for `swap`{.literal} space.

    -   Formats the first partition as `ext4`{.literal} and the second partition as `swap`{.literal}.

    -   Configures automatic mounting of both partitions at boot time.

        Note

        The partition layout `[66, [33,82]]`{.literal} allocates 66% of the disk to the first partition and 33% to the second partition. The `82`{.literal} in the second partition specification indicates a Linux swap partition type. You can adjust these percentages based on your requirements.

3.  Verify the configuration file for any errors:

    ``` {.language-plaintext tabindex="-1"}
    # cloud-init devel schema --config-file /etc/cloud/cloud.cfg.d/00-azure-swap.cfg
    ```

    If the configuration is valid, the command returns no errors.

**Verification**

-   After rebooting the VM, check that the swap partition is configured and active by verifying the active swap space, swap usage, and the swap partition entry in the `/etc/fstab`{.literal} file.

    -   Check active swap space:

        ``` {.language-plaintext tabindex="-1"}
        $ swapon -s
        ```

        The output should show the swap partition from `ephemeral0.2`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        Filename  Type  Size  Used  Priority
        /dev/ephemeral0.2  partition  8388604  0  2
        ```

    -   Check swap usage:

        ``` {.language-plaintext tabindex="-1"}
        $ free -h
        ```

        The output should show swap space in the `Swap`{.literal} row:

        ``` {.language-plaintext tabindex="-1"}
              total  used  free  shared  buffered/cache  available
        Mem: 7.8Gi  1.2Gi  5.8Gi  16MiB  800MiB  6.3Gi
        Swap: 8.0Gi  0B  8.0Gi
        ```

    -   Verify the swap partition is present in the `/etc/fstab`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        $ grep swap /etc/fstab
        ```

        The output should include an entry for the swap partition, for example:

        ``` {.language-plaintext tabindex="-1"}
        /dev/ephemeral0.2  none  swap  sw,nofail,x-systemd.requires=cloud-init.service  0  0
        ```

**Additional resources**

-   [Configure swap file with cloud-init on Azure Linux VMs](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/cloudinit-configure-swapfile)
-   [Create and configure a swap file on a Linux VM in Azure](https://learn.microsoft.com/en-us/troubleshoot/azure/virtual-machines/linux/create-swap-file-linux-vm)
-   [Disk setup for cloud-init](https://docs.cloud-init.io/en/latest/reference/examples.html#disk-setup)

### [3.7. Preparing a virtual machine for Azure deployment](#preparing-a-virtual-machine-for-azure-deployment) {#preparing-a-virtual-machine-for-azure-deployment .title}

To ensure a virtual machine (VM) has compatibility and can operate in the Azure environment, perform configuration changes before deploying a custom base image in Azure.

**Prerequisites**

-   You have created a [Red Hat account](https://www.redhat.com/wapps/ugc/register.html).
-   You have a [Microsoft Azure account](https://azure.microsoft.com/en-us/Free).
-   You have installed [the Hyper-V device drivers](#installing-hyper-v-device-drivers "3.5. Installing Hyper-V device drivers").

**Procedure**

1.  Log in and register the VM to enable the Red Hat Enterprise Linux (RHEL) repository:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager register
    ```

2.  Install the `cloud-init`{.literal} and `hyperv-daemons`{.literal} packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install cloud-init hyperv-daemons -y
    ```

3.  Create the `cloud-init`{.literal} configuration files and edit them to offer integration with Azure services:

    a.  To enable logging to the Hyper-V Data Exchange Service, also known as Key Value Pair (KVP), edit the `/etc/cloud/cloud.cfg.d/10-azure-kvp.cfg`{.literal} file and append the following lines:

        ``` {.language-plaintext tabindex="-1"}
        reporting:
            logging:
                type: log
            telemetry:
                type: hyperv
        ```

    b.  To add the Azure datasource, edit the `/etc/cloud/cloud.cfg.d/91-azure_datasource.cfg`{.literal} file and append the following lines:

        ``` {.language-plaintext tabindex="-1"}
        datasource_list: [ Azure ]
        datasource:
            Azure:
                apply_network_config: False
        ```

    c.  To configure swap space on the ephemeral disk, create the `/etc/cloud/cloud.cfg.d/00-azure-swap.cfg`{.literal} configuration file and add the following lines to that file.

        Important

        The ephemeral disk is temporary storage. Therefore, data stored on it, including swap space, is lost when the VM is deallocated or moved. Use the ephemeral disk only for temporary data such as swap space.

        ``` {.language-plaintext tabindex="-1"}
        #cloud-config
        disk_setup:
          ephemeral0:
            table_type: gpt
            layout: [66, [33,82]]
            overwrite: true
        fs_setup:
          - device: ephemeral0.1
            filesystem: ext4
          - device: ephemeral0.2
            filesystem: swap
        mounts:
          - ["ephemeral0.1", "/mnt"]
          - ["ephemeral0.2", "none", "swap", "sw,nofail,x-systemd.requires=cloud-init.service", "0", "0"]
        ```

4.  To block automatic loading of specific kernel modules, edit the `/etc/modprobe.d/blocklist.conf`{.literal} file and append the following lines:

    ``` {.language-plaintext tabindex="-1"}
    blacklist nouveau
    blacklist lbm-nouveau
    blacklist floppy
    blacklist amdgpu
    blacklist skx_edac
    blacklist intel_cstate
    ```

5.  Modify `udev`{.literal} network device rules:

    a.  If present, remove the following persistent network device rules:

        ``` {.language-plaintext tabindex="-1"}
        # rm -f /etc/udev/rules.d/70-persistent-net.rules
        ```

        ``` {.language-plaintext tabindex="-1"}
        # rm -f /etc/udev/rules.d/75-persistent-net-generator.rules
        ```

        ``` {.language-plaintext tabindex="-1"}
        # rm -f /etc/udev/rules.d/80-net-name-slot-rules
        ```

    b.  To ensure working of accelerated networking on Azure, edit the `/etc/udev/rules.d/68-azure-sriov-nm-unmanaged.rules`{.literal} new network device rule and append:

        ``` {.language-plaintext tabindex="-1"}
        SUBSYSTEM=="net", DRIVERS=="hv_pci", ACTION=="add", ENV{NM_UNMANAGED}="1"
        ```

6.  Set the `sshd`{.literal} service to start automatically:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now sshd
    ```

7.  Modify kernel boot parameters:

    a.  Update the `GRUB_TIMEOUT`{.literal} parameter value in the `/etc/default/grub`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        GRUB_TIMEOUT=10
        ```

    b.  Remove the following option from the end of the `GRUB_CMDLINE_LINUX`{.literal} line, if present:

        ``` {.language-plaintext tabindex="-1"}
        rhgb quiet
        ```

    c.  Update the `/etc/default/grub`{.literal} file with the following configuration details:

        ``` {.language-plaintext tabindex="-1"}
        GRUB_CMDLINE_LINUX="loglevel=3 crashkernel=auto console=tty1 console=ttyS0 earlyprintk=ttyS0 rootdelay=300"
        GRUB_TIMEOUT_STYLE=countdown
        GRUB_TERMINAL="serial console"
        GRUB_SERIAL_COMMAND="serial --speed=115200 --unit=0 --word=8 --parity=no --stop=1"
        ```

        Note

        By adding the `elevator=none`{.literal} option to the end of the `GRUB_CMDLINE_LINUX`{.literal} line. This instructs the I/O scheduler to process I/O requests in the order of execution, without optimizing disk performance.

        With `elevator=none`{.literal} on:

        -   Hard disk drive (HDD): Performance and throughput decreases, therefore not suitable for running workloads.
        -   Solid state drive (SSD): High performance and low latency, therefore suitable for running workloads.

    d.  Regenerate the `grub.cfg`{.literal} file:

        -   On a BIOS-based machine:

            ``` {.language-plaintext tabindex="-1"}
            # grub2-mkconfig -o /boot/grub2/grub.cfg --update-bls-cmdline
            ```

        -   On a UEFI-based machine:

            ``` {.language-plaintext tabindex="-1"}
            # grub2-mkconfig -o /boot/grub2/grub.cfg --update-bls-cmdline
            ```

            Note

            The path to rebuild `grub.cfg`{.literal} is same for both BIOS and UEFI based machines. Original `grub.cfg`{.literal} is present at BIOS path only. The UEFI path has a stub file that must not be modified or recreated using `grub2-mkconfig`{.literal} command.

            If your system uses a non-default location for `grub.cfg`{.literal}, change the command.

8.  Configure the Windows Azure Linux Agent (`WALinuxAgent`{.literal}):

    a.  Install and enable the `WALinuxAgent`{.literal} package:

        ``` {.language-plaintext tabindex="-1"}
        # dnf install WALinuxAgent -y
        ```

        ``` {.language-plaintext tabindex="-1"}
        # systemctl enable waagent
        ```

    b.  To disable swap configuration in `WALinuxAgent`{.literal} (required when using cloud-init to manage swap), edit the following lines in the `/etc/waagent.conf`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        Provisioning.DeleteRootPassword=y
        ResourceDisk.Format=n
        ResourceDisk.EnableSwap=n
        ResourceDisk.SwapSizeMB=0
        ```

        Note

        By disabling swap in `WALinuxAgent`{.literal}, you enable `cloud-init`{.literal} to manage the swap configuration on the ephemeral disk.

**Verification**

-   Verify that the VM is registered to Red Hat Subscription Manager and can access RHEL repositories:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager status
    ```

    The output shows `Overall Status: Current`{.literal}.

-   Verify that the required packages are installed:

    ``` {.language-plaintext tabindex="-1"}
    # rpm -q cloud-init hyperv-daemons WALinuxAgent
    ```

    The command lists a version for each package and does not report that a package is not installed.

-   Verify the `cloud-init`{.literal} configuration files:

    -   Validate `/etc/cloud/cloud.cfg.d/10-azure-kvp.cfg`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # cloud-init devel schema --config-file /etc/cloud/cloud.cfg.d/10-azure-kvp.cfg
        ```

    -   Validate `/etc/cloud/cloud.cfg.d/91-azure-datasource.cfg`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # cloud-init devel schema --config-file /etc/cloud/cloud.cfg.d/91-azure_datasource.cfg
        ```

    -   Validate `/etc/cloud/cloud.cfg.d/00-azure-swap.cfg`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        # cloud-init devel schema --config-file /etc/cloud/cloud.cfg.d/00-azure-swap.cfg
        ```

        If a configuration file is valid, the command returns no errors.

-   Verify that persistent `udev`{.literal} network rules are removed and the SR-IOV rule is present:

    ``` {.language-plaintext tabindex="-1"}
    # test ! -f /etc/udev/rules.d/70-persistent-net.rules && test ! -f /etc/udev/rules.d/75-persistent-net-generator.rules && test ! -f /etc/udev/rules.d/80-net-name-slot.rules && grep -q 'hv_pci' /etc/udev/rules.d/68-azure-sriov-nm-unmanaged.rules
    ```

    The command returns no output when the checks succeed.

-   Verify that the `sshd`{.literal} and `waagent`{.literal} services are enabled to start at boot:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl is-enabled sshd waagent
    ```

    The command returns `enabled`{.literal} for each service.

-   Verify the kernel boot parameters in `/etc/default/grub`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # grep '^GRUB_CMDLINE_LINUX=' /etc/default/grub
    ```

    The output includes `console=ttyS0`{.literal} and does not include `rhgb`{.literal} or `quiet`{.literal}.

-   Verify that swap configuration is disabled in `/etc/waagent.conf`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # grep -E '^ResourceDisk\.(Format|EnableSwap)=n$' /etc/waagent.conf
    ```

    The command returns:

    ``` {.language-plaintext tabindex="-1"}
    ResourceDisk.Format=n
    ResourceDisk.EnableSwap=n
    ```

**Next steps**

-   Unregister the VM from Red Hat Subscription Manager:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager unregister
    ```

-   Clean up the existing provisioning details:

    ``` {.language-plaintext tabindex="-1"}
    # waagent -force -deprovision
    ```

    Note

    This command generates warnings as Azure automatically handles the VM provisioning.

-   Clear the shell history and shut down the VM:

    ``` {.language-plaintext tabindex="-1"}
    # export HISTSIZE=0
    # poweroff
    ```

-   To upload the RHEL image to Azure cloud, [convert it to Azure disk image format](#converting-a-rhel-image-to-azure-disk-image "3.8. Converting a RHEL image to Azure disk image").

**Additional resources**

-   [Prepare a Windows VHD or VHDX to upload to Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/prepare-for-upload-vhd-image)
-   [Prepare a Linux VHD or VHDX to upload to Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/redhat-create-upload-vhd?tabs=rhel89hv#tabpanel_1_rhel89hv)

### [3.8. Converting a RHEL image to Azure disk image](#converting-a-rhel-image-to-azure-disk-image) {#converting-a-rhel-image-to-azure-disk-image .title}

You can convert a Red Hat Enterprise Linux (RHEL) image from `qcow2`{.literal} to a fixed Azure disk image virtual hard drive (`.vhd`{.literal}) format. Ensure the image file starts at a position that is a multiple of 1 MB before conversion.

**Prerequisites**

-   You have created a [Red Hat account](https://www.redhat.com/wapps/ugc/register.html).
-   You have a [Microsoft Azure account](https://azure.microsoft.com/en-us/Free).
-   You have completed the steps of [preparing VM for Azure deployment](#preparing-a-virtual-machine-for-azure-deployment "3.7. Preparing a virtual machine for Azure deployment").
-   You are using `qemu-img`{.literal} version 2.12.0.

**Procedure**

1.  Convert the image from `qcow2`{.literal} to `raw`{.literal} format.

    ``` {.language-plaintext tabindex="-1"}
    $ qemu-img convert -f qcow2 -O raw <example_image_name>.qcow2 <output_image_name>.raw
    ```

2.  Edit the `align.sh`{.literal} shell script:

    ``` {.language-plaintext tabindex="-1"}
    $ vi align.sh
    ```

    ``` {.language-bash tabindex="-1"}
    #!/bin/bash
    MB=$((1024 * 1024))
    size=$(qemu-img info -f raw --output json "$1" | gawk 'match($0, /"virtual-size": ([0-9]+),/, val) {print val[1]}')
    rounded_size=$((($size/$MB + 1) * $MB))
    if [ $(($size % $MB)) -eq  0 ]
    then
     echo "Your image is already aligned. You do not need to resize."
     exit 1
    fi
    echo "rounded size = $rounded_size"
    export rounded_size
    ```

3.  Run the script:

    ``` {.language-plaintext tabindex="-1"}
    $ sh align.sh <example_image_name>.raw
    ```

4.  If the message displays as *Your image is already aligned. You do not need to resize.*:

    a.  Convert the file to a fixed `VHD`{.literal} format:

        ``` {.language-plaintext tabindex="-1"}
        $ qemu-img convert -f raw -o subformat=fixed,force_size -O vpc <example_image_name>.raw <output_image_name>.vhd
        ```

        Once converted, the `VHD`{.literal} file is ready to upload to Azure.

5.  If a value displays mean the `raw`{.literal} image is not aligned:

    a.  Resize the `raw`{.literal} file by using the rounded value as displayed in the earlier output:

        ``` {.language-plaintext tabindex="-1"}
        $ qemu-img resize -f raw <example_image_name>.raw +1G
        ```

    b.  Convert the `raw`{.literal} image file to a `VHD`{.literal} format.

        ``` {.language-plaintext tabindex="-1"}
        $ qemu-img convert -f raw -o subformat=fixed,force_size -O vpc <example_image_name>.raw <output_image_name>.vhd
        ```

        Once converted, the `VHD`{.literal} file is ready to upload to Azure.

**Verification**

-   Verify that the `VHD`{.literal} file is ready to upload to Azure:

    ``` {.language-plaintext tabindex="-1"}
    $ qemu-img info <example_image_name>.vhd
    ```

    The output shows the `VHD`{.literal} file is ready to upload to Azure.

**Next steps**

-   You can now [configure Azure resources for your RHEL image](#configuring-the-azure-resources-for-a-rhel-image "3.9. Configuring the Azure resources for a RHEL image").

**Additional resources**

-   [Upload a VHD to Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/upload-vhd)

### [3.9. Configuring the Azure resources for a RHEL image](#configuring-the-azure-resources-for-a-rhel-image) {#configuring-the-azure-resources-for-a-rhel-image .title}

Before uploading the virtual hard drive (VHD) image file and creating the Azure image, configure Azure resources such as compute, network, and storage.

**Prerequisites**

-   You have created a [Red Hat account](https://www.redhat.com/wapps/ugc/register.html).
-   You have a [Microsoft Azure account](https://azure.microsoft.com/en-us/Free).
-   You have installed the Azure CLI. For details, see [Installing the Azure CLI](#installing-the-azure-cli "3.4. Installing the Azure CLI").
-   You have completed the process of [conversion of a RHEL image to Azure disk image](#converting-a-rhel-image-to-azure-disk-image "3.8. Converting a RHEL image to Azure disk image").

**Procedure**

1.  Authenticate your host with Azure credentials and log in:

    ``` {.language-plaintext tabindex="-1"}
    $ az login
    ```

    To login from a browser, open the Azure sign-in page from the Azure CLI. For details, see [sign in with a browser](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli-interactively?view=azure-cli-latest#sign-in-with-a-browser).

2.  Create a resource group in an Azure region:

    ``` {.language-plaintext tabindex="-1"}
    $ az group create --name <example_resource_group> \
    --location <example_azure_region>
    ```

    Example:

    ``` {.language-plaintext tabindex="-1"}
    [clouduser@localhost]$ az group create --name azrhelclirsgrp \
    --location southcentralus
    ```

    ``` {.language-plaintext tabindex="-1"}
    {
      "id": "/subscriptions//resourceGroups/azrhelclirsgrp",
      "location": "southcentralus",
      "managedBy": null,
      "name": "azrhelclirsgrp",
      "properties": {
        "provisioningState": "Succeeded"
      },
      "tags": null
    }
    ```

3.  Create a storage account with a valid stock keeping units (SKU) types:

    ``` {.language-plaintext tabindex="-1"}
    $ az storage account create -l <example_azure_region> \
    --name <example_storage_account_name> \
    --resource-group <example_resource_group> \
    --sku <example_sku_type>
    ```

    Example:

    ``` {.language-plaintext tabindex="-1"}
    $ az storage account create -l southcentralus \
    --name azrhelclistact \
    --resource-group azrhelclirsgrp \
    --sku Standard_LRS
    ```

    ``` {.language-plaintext tabindex="-1"}
    {
      "accessTier": null,
      "creationTime": "2017-04-05T19:10:29.855470+00:00",
      "customDomain": null,
      "encryption": null,
      "id": "/subscriptions//resourceGroups/azrhelclirsgrp/providers/Microsoft.Storage/storageAccounts/azrhelclistact",
      "kind": "StorageV2",
      "lastGeoFailoverTime": null,
      "location": "southcentralus",
      "name": "azrhelclistact",
      "primaryEndpoints": {
        "blob": "https://azrhelclistact.blob.core.windows.net/",
        "file": "https://azrhelclistact.file.core.windows.net/",
        "queue": "https://azrhelclistact.queue.core.windows.net/",
        "table": "https://azrhelclistact.table.core.windows.net/"
    },
    "primaryLocation": "southcentralus",
    "provisioningState": "Succeeded",
    "resourceGroup": "azrhelclirsgrp",
    "secondaryEndpoints": null,
    "secondaryLocation": null,
    "sku": {
      "name": "Standard_LRS",
      "tier": "Standard"
    },
    "statusOfPrimary": "available",
    "statusOfSecondary": null,
    "tags": {},
      "type": "Microsoft.Storage/storageAccounts"
    }
    ```

4.  Display the storage account details:

    ``` {.language-plaintext tabindex="-1"}
    $ az storage account show-connection-string \
    -n <example_storage_account_name> \
    --resource-group <example_resource_group>
    ```

    Example:

    ``` {.language-plaintext tabindex="-1"}
    $ az storage account show-connection-string \
    -n azrhelclistact \
    --resource-group azrhelclirsgrp
    ```

    ``` {.language-plaintext tabindex="-1"}
    {
      "connectionString": "DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=azrhelclistact;AccountKey=NreGk...=="
    }
    ```

5.  Set the environment variable by exporting the existing connection string to connect system to the storage account:

    ``` {.language-plaintext tabindex="-1"}
    $ export AZURE_STORAGE_CONNECTION_STRING="<storage_connection_string>"
    ```

    Example:

    ``` {.language-plaintext tabindex="-1"}
    $ export AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;EndpointSuffix=core.windows.net;AccountName=azrhelclistact;AccountKey=NreGk...=="
    ```

6.  Create a storage container:

    ``` {.language-plaintext tabindex="-1"}
    $ az storage container create -n <example_container_name>
    ```

    Example:

    ``` {.language-plaintext tabindex="-1"}
    $ az storage container create -n azrhelclistcont
    ```

    ``` {.language-plaintext tabindex="-1"}
    {
      "created": true
    }
    ```

7.  Create a virtual network:

    ``` {.language-plaintext tabindex="-1"}
    $ az network vnet create -g <example_resource_group> \
    --name <example_vnet_name> \
    --subnet-name <example_subnet_name>
    ```

    Example:

    ``` {.language-plaintext tabindex="-1"}
    $ az network vnet create --resource-group azrhelclirsgrp \
    --name azrhelclivnet1 \
    --subnet-name azrhelclisubnet1
    ```

    ``` {.language-plaintext tabindex="-1"}
    {
      "newVNet": {
        "addressSpace": {
          "addressPrefixes": [
          "10.0.0.0/16"
          ]
      },
      "dhcpOptions": {
        "dnsServers": []
      },
      "etag": "W/\"\"",
      "id": "/subscriptions//resourceGroups/azrhelclirsgrp/providers/Microsoft.Network/virtualNetworks/azrhelclivnet1",
      "location": "southcentralus",
      "name": "azrhelclivnet1",
      "provisioningState": "Succeeded",
      "resourceGroup": "azrhelclirsgrp",
      "resourceGuid": "0f25efee-e2a6-4abe-a4e9-817061ee1e79",
      "subnets": [
        {
          "addressPrefix": "10.0.0.0/24",
          "etag": "W/\"\"",
          "id": "/subscriptions//resourceGroups/azrhelclirsgrp/providers/Microsoft.Network/virtualNetworks/azrhelclivnet1/subnets/azrhelclisubnet1",
          "ipConfigurations": null,
          "name": "azrhelclisubnet1",
          "networkSecurityGroup": null,
          "provisioningState": "Succeeded",
          "resourceGroup": "azrhelclirsgrp",
          "resourceNavigationLinks": null,
          "routeTable": null
        }
      ],
      "tags": {},
      "type": "Microsoft.Network/virtualNetworks",
      "virtualNetworkPeerings": null
      }
    }
    ```

**Verification**

-   Verify that the virtual network is created:

    ``` {.language-plaintext tabindex="-1"}
    $ az network vnet list --output table
    ```

    ``` {.language-plaintext tabindex="-1"}
    Name              ResourceGroup    Location    AddressPrefix
    ----------------  ---------------  ----------  -------------
    azrhelclivnet1   azrhelclirsgrp  southcentralus  10.0.0.0/16
    ```

**Next steps**

-   You now [upload the custom Azure disk image to Azure Blob storage](#uploading-a-vhd-image-to-azure-blob-storage "3.10. Uploading a VHD image to Azure Blob storage").

**Additional resources**

-   [Azure Managed Disks Overview](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/managed-disks-overview)
-   [SKU Types](https://learn.microsoft.com/en-us/rest/api/storagerp/srp_sku_types)

### [3.10. Uploading a VHD image to Azure Blob storage](#uploading-a-vhd-image-to-azure-blob-storage) {#uploading-a-vhd-image-to-azure-blob-storage .title}

To create a custom Azure VM image, use Microsoft Azure Blob storage to upload and store your converted Red Hat Enterprise Linux (RHEL) virtual hard drive (VHD) image file.

**Prerequisites**

-   You have created a [Red Hat account](https://www.redhat.com/wapps/ugc/register.html).

-   You have a [Microsoft Azure account](https://azure.microsoft.com/en-us/Free).

-   You have already [configured Azure resources](#configuring-the-azure-resources-for-a-rhel-image "3.9. Configuring the Azure resources for a RHEL image").

    Warning

    The exported storage connection string is active only for your current session. After reboot, re-export the connection string before running storage commands to obtain and export a connection string. See [configuring the Azure resources for a RHEL image](#configuring-the-azure-resources-for-a-rhel-image "3.9. Configuring the Azure resources for a RHEL image").

**Procedure**

1.  Upload the VHD file to the storage container:

    ``` {.language-plaintext tabindex="-1"}
    $ az storage blob upload \
    --account-name <storage_account_name> \
    --container-name <container_name> \
    --type page \
    --file <path_to_vhd> \
    --name <image_name>.vhd
    ```

    Example:

    ``` {.language-plaintext tabindex="-1"}
    $ az storage blob upload \
    --account-name azrhelclistact \
    --container-name azrhelclistcont \
    --type page \
    --file ~/Downloads/rhel-image-10.vhd \
    --name rhel-10-image.vhd
    ```

    ``` {.language-plaintext tabindex="-1"}
    Percent complete: 100.0%
    ```

2.  List the storage containers:

    -   To display in the tabular format, enter:

        ``` {.language-plaintext tabindex="-1"}
        $ az storage container list --output table
        ```

    -   To display in the YAML format, enter:

        ``` {.language-plaintext tabindex="-1"}
        $ az storage container list --output yaml
        ```

3.  Use the URL for the uploaded VHD file from the 1st step:

    ``` {.language-plaintext tabindex="-1"}
    $ az storage blob url \
    -c <container_name> \
    -n <image_name>.vhd \
    <url_of_vhd_file>
    ```

    Example:

    ``` {.language-plaintext tabindex="-1"}
    $ az storage blob url \
    -c azrhelclistcont \
    -n rhel-image-10.vhd 'https://azrhelclistact.blob.core.windows.net/azrhelclistcont/rhel-image-10.vhd'
    ```

4.  Create the Azure custom image:

    ``` {.language-plaintext tabindex="-1"}
    $ az image create -n <image_name> \
    -g <resource_group> \
    -l <azure_region> \
    --source <URL> \
    --os-type linux
    ```

    Note

    By default, Azure creates the VM with a Generation 1 hypervisor. If you want to use a Generation 2 VM, which provides UEFI-based boot architecture, add the `--hyper-v-generation V2`{.literal} option to the command.

    Example:

    ``` {.language-plaintext tabindex="-1"}
    $ az image create -n rhel10 \
    -g azrhelclirsgrp2 \
    -l southcentralus \
    --source https://azrhelclistact.blob.core.windows.net/azrhelclistcont/rhel-image-10.vhd \
    --os-type linux
    ```

**Verification**

-   Verify that the Azure custom image is created:

    ``` {.language-plaintext tabindex="-1"}
    $ az image list --output table
    ```

    ``` {.language-plaintext tabindex="-1"}
    Name              ResourceGroup    Location    StorageProfile
    ----------------  ---------------  ----------  ------------------
    rhel10            azrhelclirsgrp2  southcentralus
    ```

**Next steps**

-   You can [launch and connect to an Azure VM](#launching-and-connecting-to-a-rhel-vm-in-azure "3.11. Launching and connecting to a RHEL VM in Azure").

**Troubleshooting**

-   If you see the error message `Only blobs formatted as VHDs can be imported`{.literal}, the image is not aligned to the nearest 1 MB boundary before being converted to VHD format. For details, see [Converting a RHEL image to Azure disk image](#converting-a-rhel-image-to-azure-disk-image "3.8. Converting a RHEL image to Azure disk image").

**Additional resources**

-   [Support for generation 2 VMs on Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/generation-2)

### [3.11. Launching and connecting to a RHEL VM in Azure](#launching-and-connecting-to-a-rhel-vm-in-azure) {#launching-and-connecting-to-a-rhel-vm-in-azure .title}

You can create a managed disk Azure virtual machine (VM) from your uploaded RHEL image and connect to it by using SSH. A managed disk VM uses Azure-managed storage, which simplifies disk management and provides better reliability.

**Prerequisites**

-   You have created a [Red Hat account](https://www.redhat.com/wapps/ugc/register.html).
-   You have a [Microsoft Azure account](https://azure.microsoft.com/en-us/Free).
-   You have completed the [uploading of Azure VHD image to Azure Blob storage](#uploading-a-vhd-image-to-azure-blob-storage "3.10. Uploading a VHD image to Azure Blob storage").

**Procedure**

1.  Create the VM:

    ``` {.language-plaintext tabindex="-1"}
    $ az vm create \
    --resource-group <resource_group> \
    --location <azure_region> \
    --name <vm_name> \
    --vnet-name <vnet_name> \
    --subnet <subnet_name> \
    --size Standard_A2 \
    --os-disk-name <simple_name> \
    --admin-username <administrator_name> \
    --generate-ssh-keys \
    --image <path_to_image>
    ```

    Example:

    ``` {.language-plaintext tabindex="-1"}
    $ az vm create \
    --resource-group azrhelclirsgrp2 \
    --location southcentralus \
    --name rhel-azure-vm-1 \
    --vnet-name azrhelclivnet1 \
    --subnet azrhelclisubnet1 \
    --size Standard_A2 \
    --os-disk-name vm-1-osdisk \
    --admin-username clouduser \
    --generate-ssh-keys \
    --image rhel10
    ```

    ``` {.language-plaintext tabindex="-1"}
    {
      "fqdns": "",
      "id": "/subscriptions//resourceGroups/azrhelclirsgrp/providers/Microsoft.Compute/virtualMachines/rhel-azure-vm-1",
      "location": "southcentralus",
      "macAddress": "",
      "powerState": "VM running",
      "privateIpAddress": "10.0.0.4",
      "publicIpAddress": "__<public_ip_address>__",
      "resourceGroup": "azrhelclirsgrp2"
    }
    ```

    -   `--generate-ssh-keys`{.literal} option creates a private and public key pair files in the `~/.ssh`{.literal} directory.

    -   The public key is added to the `authorized_keys`{.literal} file on the VM for the user specified by the `--admin-username`{.literal} option.

        For details, see [Types of SSH authentication methods](#types-of-ssh-authentication-methods "3.12. Types of SSH authentication methods"). Note the `publicIpAddress`{.literal}, which is required for logging in to the VM in the following step.

2.  Start an SSH session and log in to the Azure VM:

    ``` {.language-plaintext tabindex="-1"}
    [clouduser@localhost]$ ssh -i /home/clouduser/.ssh/id_rsa clouduser@<public_ip_address>
    ```

    ``` {.language-plaintext tabindex="-1"}
    The authenticity of host '__<public_ip_address>__' can't be established.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added '__<public_ip_address>__' (ECDSA) to the list of known hosts.
    ```

**Verification**

-   If you successfully connected to the VM, you see a user prompt.
-   Use the Microsoft Azure portal to check the audit logs, assigned resources properties, and manage virtual machines. For details, see [Tutorial: Create and manage Linux VMs with the Azure portal](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/tutorial-manage-vm).
-   You can also use the Azure CLI if you are managing many VMs. For details, enter `az --help`{.literal} in the CLI or see [Azure CLI command reference](https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest).

**Additional resources**

-   [Tutorial: Create and manage Linux VMs with the Azure portal](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/tutorial-manage-vm)
-   [Azure CLI command reference](https://learn.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest)

### [3.12. Types of SSH authentication methods](#types-of-ssh-authentication-methods) {#types-of-ssh-authentication-methods .title}

You can connect to an Azure virtual machine (VM) by using various SSH authentication methods, including password authentication or an existing public key file.

Example 1
:   Provision a new Azure VM with a password without generating a public key file.

``` {.language-plaintext tabindex="-1"}
$ az vm create \
    -g <resource_group> -l <azure_region> -n <vm_name> \
    -vnet-name <vnet_name> -subnet <subnet_name> -size Standard_A2 \
    -os-disk-name <simple_name> -authentication-type password \
    -admin-username <administrator_name> -admin-password <ssh_password> -image <path_to_image>
```

``` {.language-plaintext tabindex="-1"}
$ ssh <admin_username>@<public_ip_address>
```

Example 2
:   Provision a new Azure VM with an existing public key file.

``` {.language-plaintext tabindex="-1"}
$ az vm create \
    -g <resource_group> -l <azure_region> -n <vm_name> \
    -vnet-name <vnet_name> -subnet <subnet_name> -size Standard_A2 \
    -os-disk-name <simple_name> -admin-username <administrator_name> \
    -ssh-key-value <path_to_existing_ssh_key> -image <path_to_image>
```

``` {.language-plaintext tabindex="-1"}
$ ssh -i <path_to_existing_ssh_key> <admin_username>@<public_ip_address>
```

**Additional resources**

-   [Create SSH keys for Linux VMs in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/create-ssh-keys-detailed)

### [3.13. Attaching Red Hat subscriptions](#attaching-red-hat-subscriptions) {#attaching-red-hat-subscriptions .title}

To register and attach your Red Hat subscription to a RHEL instance, you can use the `subscription-manager`{.literal} command.

**Prerequisites**

-   You have an active [Red Hat account](https://www.redhat.com/wapps/ugc/register.html).

**Procedure**

1.  Register your system:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager register
    ```

2.  Attach your subscriptions:

    -   You can use an activation key to attach subscriptions. For details, see [creating Red Hat Customer Portal Activation Keys](https://access.redhat.com/articles/1378093).
    -   Otherwise, you can manually attach a subscription by using the subscription Pool ID [attaching a host-based subscription by using Pool ID to hypervisors](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_rhel_system_registration/con-adv-reg-rhel-config-vm-sub#proc_attaching-a-host-based-subscription-to-hypervisors).

3.  Optional: To collect various system metrics about the instance in the [Red Hat Hybrid Cloud Console](https://console.redhat.com), you can register the instance with [Red Hat Lightspeed](https://www.redhat.com/en/lightspeed).

    ``` {.language-plaintext tabindex="-1"}
    # insights-client register --display-name <display_name_value>
    ```

**Verification**

-   Verify that the system is registered and attached to the correct subscriptions:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager list --consumed
    ```

**Additional resources**

-   [Creating Red Hat Customer Portal Activation Keys](https://access.redhat.com/articles/1378093)
-   [Client Configuration Guide for Red Hat Lightspeed](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html/client_configuration_guide_for_red_hat_lightspeed/index)
-   [Red Hat Cloud Access Reference Guide](https://www.redhat.com/en/technologies/cloud-computing/cloud-access)

### [3.14. Configuring automatic registration on Azure gold images](#setting-up-automatic-registration-on-azure-gold-images) {#configuring-automatic-registration-on-azure-gold-images .title}

You can deploy Red Hat Enterprise Linux (RHEL) virtual machines (VMs) more efficiently on Microsoft Azure by using gold images of RHEL. This ensures that the VMs are automatically registered to the Red Hat Subscription Manager (RHSM).

**Prerequisites**

-   You have created a [Red Hat account](https://www.redhat.com/wapps/ugc/register.html).

-   You have a [Microsoft Azure account](https://azure.microsoft.com/en-us/Free).

-   You have downloaded the latest RHEL gold image for Azure. For details, see Additional resources.

    Note

    At a time, you can only attach an Azure account to a single Red Hat account. Therefore, ensure no other users require access to the Azure account before attaching it to your Red Hat account.

**Procedure**

-   Upload the gold image to Azure. For details, see [Launching and connecting to a RHEL VM in Azure](#launching-and-connecting-to-a-rhel-vm-in-azure "3.11. Launching and connecting to a RHEL VM in Azure").

    If your RHSM settings are correct, the VM will be automatically subscribed to RHSM.

**Verification**

-   In a RHEL VM created by using the earlier instructions, verify that RHSM connects to the system. On a successfully registered system, the `subscription-manager identity`{.literal} command displays the UUID of the system. For example:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager identity
    ```

    ``` {.language-plaintext tabindex="-1"}
    system identity: fdc46662-c536-43fb-a18a-bbcb283102b7
    name: 192.168.122.222
    org name: 6340056
    org ID: 6340056
    ```

**Additional resources**

-   [Red Hat gold images in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/workloads/redhat/byos)
-   [Overview of RHEL images in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/workloads/redhat/redhat-images)
-   [Configuring cloud integration for Red Hat services](https://docs.redhat.com/en/documentation/red_hat_hybrid_cloud_console/1-latest/html/configuring_cloud_integrations_for_red_hat_services/index)
-   [Use gold images on Azure](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_rhel_system_registration/con-red-hat-cloud-access-program-overview)

### [3.15. Configuring kdump for Microsoft Azure virtual machines](#configuring-kdump-for-microsoft-azure-instances) {#configuring-kdump-for-microsoft-azure-virtual-machines .title}

To generate crash dump (`vmcore`{.literal}) files when a kernel crash occurs, configure the `kdump`{.literal} service on Azure virtual machine (VM). Adjust the `kdump`{.literal} reserved memory and the `vmcore`{.literal} target as needed for your VM size and Red Hat Enterprise Linux (RHEL) version to ensure reliable crash diagnostics.

**Prerequisites**

-   You have created a [Red Hat account](https://www.redhat.com/wapps/ugc/register.html).

-   You have a [Microsoft Azure account](https://azure.microsoft.com/en-us/Free).

-   You are using a VM from Microsoft Azure environment that supports `kdump`{.literal}:

    -   Standard_DS2_v2
    -   Standard NV16as v4
    -   Standard M416-208s v2
    -   Standard M416ms v2

-   You have the administrative privileges.

-   Your system meets the requirements for `kdump`{.literal} configurations and targets.

**Procedure**

1.  Install `kdump`{.literal} and other necessary packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install kexec-tools kdump-utils makedumpfile
    ```

2.  Verify that the default location for crash dump files is set in the `kdump`{.literal} configuration file and that the `/var/crash`{.literal} file is available:

    ``` {.language-plaintext tabindex="-1"}
    # grep -v "#" /etc/kdump.conf
    ```

    ``` {.language-plaintext tabindex="-1"}
    path /var/crash
    core_collector makedumpfile -l --message-level 7 -d 31
    ```

3.  Based on the RHEL VM size and version, check if you need a `vmcore`{.literal} target with more free space, such as `/mnt/crash`{.literal}:

    +--------------------+----------------------------------+---------------------------------------+---------------------------------------------+-------------------------------------------+
    | RHEL Version       | Standard DS1 v2 (1 vCPU, 3.5GiB) | Standard NV16as v4 (16 vCPUs, 56 GiB) | Standard M416-208s v2 (208 vCPUs, 5700 GiB) | Standard M416ms v2 (416 vCPUs, 11400 GiB) |
    +:===================+:=================================+:======================================+:============================================+:==========================================+
    | RHEL 9.4 - RHEL 10 | Default                          | Default                               | Target                                      | Target                                    |
    +--------------------+----------------------------------+---------------------------------------+---------------------------------------------+-------------------------------------------+

    : Table 3.3. Virtual machine sizes that have been tested with GEN2 VM on Azure

    Show more

    -   **Default** indicates that `kdump`{.literal} works as expected with the default memory and the default `kdump`{.literal} target. The default `kdump`{.literal} target is the `/var/crash`{.literal} file.
    -   **Target** indicates that `kdump`{.literal} works as expected with the default memory. However, you might need to assign a target with more free space.

4.  To assign a target with free space, such as `/mnt/crash`{.literal}, edit the `/etc/kdump.conf`{.literal} file and replace the default path:

    ``` {.language-plaintext tabindex="-1"}
    $ sed s/"path /var/crash"/"path /mnt/crash"
    ```

    The option path `/mnt/crash`{.literal} represents the path to the file system where `kdump`{.literal} saves the crash dump file.

    For details, such as writing the crash dump file to a different partition, directly to a device or storing it to a remote machine, see [Configuring the kdump target](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/configuring-kdump-on-the-command-line#configuring-the-kdump-target).

5.  If required, increase the crash kernel size by adding a boot parameter to ensure `kdump`{.literal} can capture the `vmcore`{.literal}:

    For example, for a Standard M416-208s v2 VM, the sufficient size is 512 MB, so the boot parameter would be `crashkernel=512M`{.literal}.

    a.  Open the GRUB configuration file and add `crashkernel=512M`{.literal} to the boot parameter line:

        ``` {.language-plaintext tabindex="-1"}
        # vi /etc/default/grub
        ```

        ``` {.language-plaintext tabindex="-1"}
        GRUB_CMDLINE_LINUX="console=tty1 console=ttyS0 earlyprintk=ttyS0 rootdelay=300 crashkernel=512M"
        ```

    b.  Update the GRUB configuration file:

        ``` {.language-plaintext tabindex="-1"}
        # grub2-mkconfig -o /boot/grub2/grub.cfg --update-bls-cmdline
        ```

6.  Reboot the VM to allocate separate kernel crash memory to the VM.

**Verification**

-   Ensure that `kdump`{.literal} is active and running.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status kdump
    ```

    ``` {.language-plaintext tabindex="-1"}
    ● kdump.service - Crash recovery kernel arming
       Loaded: loaded (/usr/lib/systemd/system/kdump.service; enabled; vendor prese>
       Active: active (exited) since Fri 2024-02-09 10:50:18 CET; 1h 20min ago
      Process: 1252 ExecStart=/usr/bin/kdumpctl start (code=exited, status=0/SUCCES>
     Main PID: 1252 (code=exited, status=0/SUCCESS)
        Tasks: 0 (limit: 16975)
       Memory: 512B
       CGroup: /system.slice/kdump.service
    ```

**Additional resources**

-   [Installing kdump](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/installing-kdump)
-   [How to troubleshoot kernel crashes, hangs, or reboots with kdump on Red Hat Enterprise Linux (Red Hat Knowledgebase)](https://access.redhat.com/solutions/6038#dumptargets)
-   [Memory requirements for kdump](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/supported-kdump-configurations-and-targets#memory-requirements-for-kdump)
-   [Supported kdump configurations and targets](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/managing_monitoring_and_updating_the_kernel/supported-kdump-configurations-and-targets)

## [Chapter 4. Configuring a Red Hat High Availability cluster on Microsoft Azure](#configuring-a-red-hat-high-availability-cluster-on-microsoft-azure) {#chapter-4.-configuring-a-red-hat-high-availability-cluster-on-microsoft-azure .title}

To group nodes on Azure and redistribute workloads if a node fails, configure a high availability (HA) cluster on Azure with Red Hat Enterprise Linux (RHEL) image based virtual hard drive (VHD) instances. The process for HA clusters setup on Azure is comparable to traditional, non-cloud HA configuration.

### [4.1. Benefits of using high-availability clusters on public cloud platforms](#benefits-of-using-high-availability-clusters-on-public-cloud-platforms) {#benefits-of-using-high-availability-clusters-on-public-cloud-platforms .title}

A high-availability (HA) cluster uses multiple computers (*nodes*) to run workloads with redundancy. If a node fails, the Pacemaker resource manager automatically shifts workloads to healthy nodes, minimizing downtime and keeping services available without manual intervention.

You can also run HA clusters on public cloud platforms. In this case, you would use virtual machine (VM) instances in the cloud as the individual cluster nodes. By using HA clusters on a public cloud platform has the following benefits:

-   *Improved availability*: In case of a VM failure, the workload is quickly redistributed to other nodes, so running services are not disrupted.
-   *Scalability*: You can start additional nodes when demand is high and stop them when demand is low.
-   *Cost-effectiveness*: With the pay-as-you-go pricing, you pay only for nodes that are running.
-   *Simplified management*: Some public cloud platforms offer management interfaces to make configuring HA clusters easier.

To enable HA on your RHEL systems, Red Hat offers a HA Add-On. You can configure a RHEL cluster with Red Hat HA Add-On to manage HA clusters with groups of RHEL servers. Red Hat HA Add-On gives access to integrated and streamlined tools. With cluster resource manager, fencing agents, and resource agents, you can configure the cluster for automation. The Red Hat HA Add-On offers the following components for automation:

-   `Pacemaker`{.literal}, a cluster resource manager that offers both a command line utility (`pcs`{.literal}) and a GUI (`pcsd`{.literal}) to support many nodes.
-   `Corosync`{.literal} and `Kronosnet`{.literal} to create and manage HA clusters.
-   Resource agents to configure and manage custom applications.
-   Fencing agents to use cluster on platforms such as bare-metal servers and virtual machines.

The Red Hat HA Add-On handles critical tasks:

-   Node failures.
-   Load balancing.
-   Node health checks for fault tolerance and system reliability.

Before you begin, make sure to complete following steps:

-   You have created a Red Hat account.
-   You have signed up and configured a Cloud service provider account.
-   Red Hat Enterprise Linux 10 Server: `rhel-10-server-rpms/10/x86_64`{.literal}
-   Red Hat Enterprise Linux 10 Server (High Availability): `rhel-10-server-ha-rpms/10/x86_64`{.literal}
-   Your project should have a service account that belongs to a VM instance and not an individual user.
-   You can use the default service account instead of creating a separate service account.

If you or your project administrator create a custom service account, configure the service account for the following roles:

-   Cloud Trace Agent
-   Compute Admin
-   Compute Network Admin
-   Cloud Datastore User
-   Logging Admin
-   Monitoring Editor
-   Monitoring Metric Writer
-   Service Account Administrator
-   Storage Admin

**Additional resources**

-   [High Availability Add-On overview](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_high_availability_clusters/overview-of-high-availability)

### [4.2. Installing the High Availability packages and agents for Azure](#installing-the-high-availability-packages-and-agents-for-azure) {#installing-the-high-availability-packages-and-agents-for-azure .title}

To create a fault-tolerant, highly available Red Hat Enterprise Linux (RHEL) system on Azure, install the High Availability packages and agents on each node. These provide features such as automatic failover capabilities, resource management, service continuity, and Azure-specific integration.

**Prerequisites**

-   You have created [a Red Hat account](https://www.redhat.com/wapps/ugc/register.html)
-   You have [signed up and configured an Azure account](https://azure.microsoft.com/en-in/free).
-   You have completed [deployment of RHEL image as an Azure compute instance](#deploying-a-rhel-image-as-a-compute-instance-on-azure "Chapter 3. Deploying a RHEL image as a compute instance on Azure").

**Procedure**

1.  To get the public IP address for an Azure VM, open the VM properties in the Azure Portal or enter:

    ``` {.language-plaintext tabindex="-1"}
    $ az vm list -g <resource_group> -d --output table
    ```

    Example:

    ``` {.language-plaintext tabindex="-1"}
    $ az vm list -g azrhelclirsgrp -d --output table
    ```

    ``` {.language-plaintext tabindex="-1"}
    Name    ResourceGroup  PowerState  PublicIps   Location
    ------  ------------- ---------  -------------  -------------
    node01 azrhelclirsgrp VM running 192.98.152.251 southcentralus
    ```

2.  Register the VM with Red Hat:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo -i
    # subscription-manager register
    ```

3.  Disable all repositories:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --disable=*
    ```

4.  Enable the RHEL Server HA repositories:

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --enable=rhel-10-for-x86_64-highavailability-rpms
    ```

5.  Update all packages:

    ``` {.language-plaintext tabindex="-1"}
    # dnf update -y
    ```

6.  Install the Red Hat HA Add-On packages, along with the Azure fencing agent:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pcs pacemaker fence-agents-azure-arm
    ```

7.  The `pcs`{.literal} and `pacemaker`{.literal} installation created the `hacluster`{.literal} user in the last step. Now, create a password for the `hacluster`{.literal} and use it for all cluster nodes:

    ``` {.language-plaintext tabindex="-1"}
    # passwd hacluster
    ```

8.  Add the `high availability`{.literal} service to the RHEL Firewall if your system has `firewalld.service`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=high-availability
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

9.  Start the `pcs`{.literal} service and enable it to start on boot.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl start pcsd.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable pcsd.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    Created symlink from /etc/systemd/system/multi-user.target.wants/pcsd.service to /usr/lib/systemd/system/pcsd.service.
    ```

**Verification**

-   Ensure the `pcs`{.literal} service is running.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status pcsd.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    Active: active (running) since Fri 2018-02-23 11:00:58 EST; 1min 23s ago
    ...
    ```

**Additional resources**

-   [Support Policies for RHEL High Availability Clusters - Microsoft Azure Virtual Machines as Cluster Members](https://access.redhat.com/articles/3131341)
-   [Failover Clustering Overview](https://learn.microsoft.com/en-us/windows-server/failover-clustering/failover-clustering-overview)

### [4.3. Creating an Azure AD application](#creating-an-azure-active-directory-application) {#creating-an-azure-ad-application .title}

To authorize and automate access for high availability (HA) operations for all nodes in the cluster, create an Azure Active Directory (AD) application.

**Prerequisites**

-   You have created [a Red Hat account](https://www.redhat.com/wapps/ugc/register.html).
-   You have [signed up and configured an Azure account](https://azure.microsoft.com/en-in/free).
-   The [Azure Command Line Interface (CLI)](#installing-the-azure-cli "3.4. Installing the Azure CLI") is installed on your system.
-   You are an administrator or owner for the Microsoft Azure subscription to create an Azure AD application.

**Procedure**

1.  From any node in the HA cluster, log in to your Azure account:

    ``` {.language-plaintext tabindex="-1"}
    $ az login
    ```

2.  Create a `json`{.literal} configuration file for a custom role for the Azure fence agent. Use the following configuration, but replace *\<subscription_id\>* with your subscription IDs:

    ``` {.language-plaintext tabindex="-1"}
    {
      "Name": "Linux Fence Agent Role",
      "description": "Allows to power-off and start virtual machines",
      "assignableScopes": [
        "/subscriptions/<subscription_id>"
      ],
      "permissions": [
        {
          "actions": [
            "Microsoft.Compute/*/read",
            "Microsoft.Compute/virtualMachines/powerOff/action",
            "Microsoft.Compute/virtualMachines/start/action"
          ],
          "notActions": [],
          "dataActions": [],
          "notDataActions": []
        }
      ]
    }
    ```

3.  Define the custom role for the Azure fence agent. Use the `json`{.literal} file created in the earlier step:

    ``` {.language-plaintext tabindex="-1"}
    $ az role definition create --role-definition <azure_fence_role.json>
    ```

    ``` {.language-plaintext tabindex="-1"}
    {
      "assignableScopes": [
        "/subscriptions/__<my_subscription_id>__"
      ],
      "description": "Allows to power-off and start virtual machines",
      "id": "/subscriptions/__<my_subscription_id>__/providers/Microsoft.Authorization/roleDefinitions/__<role_id>__",
      "name": "__<role_id>__",
      "permissions": [
        {
          "actions": [
            "Microsoft.Compute/*/read",
            "Microsoft.Compute/virtualMachines/powerOff/action",
            "Microsoft.Compute/virtualMachines/start/action"
          ],
          "dataActions": [],
          "notActions": [],
          "notDataActions": []
        }
      ],
      "roleName": "Linux Fence Agent Role",
      "roleType": "CustomRole",
      "type": "Microsoft.Authorization/roleDefinitions"
    }
    ```

4.  In the Azure web console interface, select **Virtual Machine** → click **Identity** in the left-side menu. Select **On** → click **Save** → click **Yes** to confirm. Click **Azure role assignments** → **Add role assignment**.

5.  Select the **Scope** required for the role and the required **Resource Group**.

6.  Optional: Change the **Subscription** if necessary.

7.  Select the **Linux Fence Agent Role** role and click **Save**

**Verification**

-   Display nodes visible in Azure AD:

    ``` {.language-plaintext tabindex="-1"}
    # fence_azure_arm --msi -o list
    ```

    ``` {.language-plaintext tabindex="-1"}
    node1,
    node2,
    ...
    ```

    If this command outputs all nodes on your cluster, you have successfully configured the AD application.

**Additional resources**

-   [View the access a user has to Azure resources](https://learn.microsoft.com/en-us/azure/role-based-access-control/check-access)
-   [Set up Pacemaker on Red Hat Enterprise Linux in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/workloads/sap/high-availability-guide-rhel-pacemaker#1-create-a-custom-role-for-the-fence-agent)
-   [Assign Azure roles by using Azure CLI](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-cli)

### [4.4. Creating a high availability cluster](#creating-a-high-availability-cluster) {#creating-a-high-availability-cluster .title}

You can create a Red Hat High Availability Add-On cluster. This example uses nodes `z1.example.com`{.literal} and `z2.example.com`{.literal}.

**Prerequisites**

-   You have created [a Red Hat account](https://www.redhat.com/wapps/ugc/register.html).

    Note

    To display the parameters of a `pcs`{.literal} command and a description of those parameters, use the `-h`{.literal} option of the `pcs`{.literal} command.

**Procedure**

1.  Authenticate the `pcs`{.literal} user `hacluster`{.literal} for each node in the cluster on the node from which you will be running `pcs`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs host auth z1.example.com z2.example.com
    ```

    ``` {.language-plaintext tabindex="-1"}
    Username: hacluster
    Password:
    z1.example.com: Authorized
    z2.example.com: Authorized
    ```

    This command authenticates user `hacluster`{.literal} on `z1.example.com`{.literal} for both of the nodes in a two-node cluster that will consist of `z1.example.com`{.literal} and `z2.example.com`{.literal}.

2.  Run the following command from the `z1.example.com`{.literal} node to create the two-node cluster `my_cluster`{.literal} that consists of nodes `z1.example.com`{.literal} and `z2.example.com`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs cluster setup my_cluster --start z1.example.com z2.example.com
    ```

    This will propagate the cluster configuration files to both nodes in the cluster. This command includes the `--start`{.literal} option, which will start the cluster services on both nodes in the cluster.

3.  Enable the cluster services to run on each node in the cluster when the node boots:

    Note

    For your particular environment, you can skip this step by keeping the cluster services disabled. If enabled and a node goes down, any issues with your cluster or your resources are resolved before the node rejoins the cluster. If you keep the cluster services disabled, manually start the services when you reboot a node by running the `pcs cluster start`{.literal} command on that node.

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs cluster enable --all
    ```

**Verification**

-   Display the status of the cluster you created:

    ``` {.language-plaintext tabindex="-1"}
    [root@z1 ~]# pcs cluster status
    ```

    ``` {.language-plaintext tabindex="-1"}
    Cluster Status:
     Stack: corosync
     Current DC: z2.example.com (version 2.0.0-10.el8-b67d8d0de9) - partition with quorum
     Last updated: Thu Oct 11 16:11:18 2018
     Last change: Thu Oct 11 16:11:00 2018 by hacluster via crmd on z2.example.com
     2 Nodes configured
     0 Resources configured
    ...
    ```

    There could be a slight delay before the cluster is up and running when you start the cluster services with the `--start`{.literal} option of the `pcs cluster setup`{.literal} command. Ensure that the cluster is up and running before performing any subsequent actions.

**Additional resources**

-   [How to set up a Pacemaker cluster for high availability Linux](https://www.redhat.com/en/blog/rhel-pacemaker-cluster)

### [4.5. Configuring fencing in a Red Hat High Availability cluster](#configuring-fencing) {#configuring-fencing-in-a-red-hat-high-availability-cluster .title}

When a node becomes unresponsive, the cluster must isolate it to prevent data corruption. Configure fencing since the node cannot be contacted directly. An external fence device cuts off the node's access to shared resources or performs a hard reboot.

Without a fence device, you do not know if the disconnected node has released its resources. This could prevent services from running on other nodes. Conversely, the system might wrongly assume resources are released, leading to data corruption. As a consequence, data integrity cannot be guaranteed and the cluster configuration will be unsupported.

When fencing is in progress, no other cluster operation is allowed to run. Normal operation of the cluster cannot resume until fencing has completed or the cluster node rejoins the cluster after the cluster node has been rebooted.

#### [4.5.1. Displaying available fence agents and their options](#displaying-fence-agents) {#displaying-available-fence-agents-and-their-options .title}

You can view available fencing agents and the available options for specific fencing agents.

Note

Your system's hardware determines the type of fencing device to use for your cluster. For information about supported platforms and architectures and the different fencing devices, see the Red Hat Knowledgebase article [Cluster Platforms and Architectures](https://access.redhat.com/articles/2912891#platforms) section of the article [Support Policies for RHEL High Availability Clusters](https://access.redhat.com/articles/2912891).

Run the following command to list all available fencing agents. When you specify a filter, this command displays only the fencing agents that match the filter.

``` {.language-plaintext tabindex="-1"}
# pcs stonith list [filter]
```

Run the following command to display the options for the specified fencing agent.

``` {.language-plaintext tabindex="-1"}
# pcs stonith describe [stonith_agent]
```

For example, the following command displays the options for the fence agent for APC over telnet/SSH.

``` {.language-plaintext tabindex="-1"}
# pcs stonith describe fence_apc
```

``` {.language-plaintext tabindex="-1"}
Stonith options for: fence_apc
  ipaddr (required): IP Address or Hostname
  login (required): Login Name
  passwd: Login password or passphrase
  passwd_script: Script to retrieve password
  cmd_prompt: Force command prompt
  secure: SSH connection
  port (required): Physical plug number or name of virtual machine
  identity_file: Identity file for ssh
  switch: Physical switch number on device
  inet4_only: Forces agent to use IPv4 addresses only
  inet6_only: Forces agent to use IPv6 addresses only
  ipport: TCP port to use for connection with device
  action (required): Fencing Action
  verbose: Verbose mode
  debug: Write debug information to given file
  version: Display version information and exit
  help: Display help and exit
  separator: Separator for CSV created by operation list
  power_timeout: Test X seconds for status change after ON/OFF
  shell_timeout: Wait X seconds for cmd prompt after issuing command
  login_timeout: Wait X seconds for cmd prompt after login
  power_wait: Wait X seconds after issuing ON/OFF
  delay: Wait X seconds before fencing is started
  retry_on: Count of attempts to retry power on
```

Warning

For fence agents that provide a `method`{.literal} option, with the exception of the `fence_sbd`{.literal} agent a value of `cycle`{.literal} is unsupported and should not be specified, as it may cause data corruption. Even for `fence_sbd`{.literal}, however. you should not specify a method and instead use the default value.

#### [4.5.2. Creating a fence device](#creating-fence-devices) {#creating-a-fence-device .title}

Create a fence device by using the `pcs stonith create`{.literal} command. To view all available creation options, use the `pcs stonith -h`{.literal} command.

**Procedure**

-   Create a fence device:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith create stonith_id stonith_device_type [stonith_device_options] [op operation_action operation_options]
    ```

-   The following command creates a single fencing device for a single node:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith create MyStonith fence_virt pcmk_host_list=f1 op monitor interval=30s
    ```

    Some fence devices can fence only a single node, while other devices can fence multiple nodes. The parameters you specify when you create a fencing device depend on what your fencing device supports and requires.

-   Some fence devices can automatically decide which nodes they can fence.

-   You can use the `pcmk_host_list`{.literal} parameter when creating a fencing device to specify all of the machines that are controlled by that fencing device.

-   Some fence devices require a mapping of host names to the specifications that the fence device understands. You can map host names with the `pcmk_host_map`{.literal} parameter when creating a fencing device.

**Additional resources**

-   [General properties of fencing devices](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_high_availability_clusters/configuring-fencing#general-fence-device-properties)
-   [Testing a fence device](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_high_availability_clusters/configuring-fencing#testing-fence-devices)

#### [4.5.3. General properties of fencing devices](#general-fence-device-properties) {#general-properties-of-fencing-devices .title}

Configure fencing behavior using device-specific options and cluster-wide properties. Device options define agent settings, such as IP addresses, and metadata like delays. Cluster properties manage global logic, including timeouts and the `stonith-enabled`{.literal} parameter.

Any cluster node can fence any other cluster node with any fence device, regardless of whether the fence resource is started or stopped. Whether the resource is started controls only the recurring monitor for the device, not whether it can be used, with the following exceptions:

-   You can disable a fencing device by running the `pcs stonith disable `{.literal .command}*`stonith_id`{.literal .command}* command. This will prevent any node from using that device.
-   To prevent a specific node from using a fencing device, you can configure location constraints for the fencing resource with the `pcs constraint location …​ avoids`{.literal} command.
-   Configuring `stonith-enabled=false`{.literal} will disable fencing altogether. Note, however, that Red Hat does not support clusters when fencing is disabled, as it is not suitable for a production environment.

The following table describes the general properties you can set for fencing devices.

+-----------------------------+--------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                       | Type   | Default                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
+:============================+:=======+:=====================================================================================================+:=======================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `pcmk_host_map`{.literal}   | string |                                                                                                      | A mapping of host names to port numbers for devices that do not support host names. For example: `node1:1;node2:2,3`{.literal} tells the cluster to use port 1 for node1 and ports 2 and 3 for node2. The `pcmk_host_map`{.literal} property supports special characters inside `pcmk_host_map`{.literal} values using a backslash in front of the value. For example, you can specify `pcmk_host_map="node3:plug\ 1"`{.literal} to include a space in the host alias. |
+-----------------------------+--------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_host_list`{.literal}  | string |                                                                                                      | A list of machines controlled by this device (Optional unless `pcmk_host_check=static-list`{.literal}).                                                                                                                                                                                                                                                                                                                                                                |
+-----------------------------+--------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_host_check`{.literal} | string | -   `static-list`{.literal} if either `pcmk_host_list`{.literal} or `pcmk_host_map`{.literal} is set | How to determine which machines are controlled by the device. Allowed values: `dynamic-list`{.literal} (query the device), `static-list`{.literal} (check the `pcmk_host_list`{.literal} attribute), none (assume every device can fence every machine)                                                                                                                                                                                                                |
|                             |        | -   Otherwise, `dynamic-list`{.literal} if the fence device supports the `list`{.literal} action     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                             |        | -   Otherwise, `status`{.literal} if the fence device supports the `status`{.literal} action         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|                             |        | -   Otherwise, `none`{.literal}.                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+-----------------------------+--------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 4.1. General Properties of Fencing Devices

Show more

The following table summarizes additional properties you can set for fencing devices. Note that these properties are for advanced use only.

+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Field                            | Type    | Default | Description                                                                                                                                                                                                                                                                                                                                                                                                                          |
+:=================================+:========+:========+:=====================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `pcmk_host_argument`{.literal}   | string  | port    | An alternate parameter to supply instead of port. Some devices do not support the standard port parameter or may provide additional ones. Use this to specify an alternate, device-specific parameter that should indicate the machine to be fenced. A value of `none`{.literal} can be used to tell the cluster not to supply any additional parameters.                                                                            |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_reboot_action`{.literal}   | string  | reboot  | An alternate command to run instead of `reboot`{.literal}. Some devices do not support the standard commands or may provide additional ones. Use this to specify an alternate, device-specific, command that implements the reboot action.                                                                                                                                                                                           |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_reboot_timeout`{.literal}  | time    | 60s     | Specify an alternate timeout to use for reboot actions instead of `stonith-timeout`{.literal}. Some devices need much more/less time to complete than normal. Use this to specify an alternate, device-specific, timeout for reboot actions.                                                                                                                                                                                         |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_reboot_retries`{.literal}  | integer | 2       | The maximum number of times to retry the `reboot`{.literal} command within the timeout period. Some devices do not support multiple connections. Operations may fail if the device is busy with another task so Pacemaker will automatically retry the operation, if there is time remaining. Use this option to alter the number of times Pacemaker retries reboot actions before giving up.                                        |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_off_action`{.literal}      | string  | off     | An alternate command to run instead of `off`{.literal}. Some devices do not support the standard commands or may provide additional ones. Use this to specify an alternate, device-specific, command that implements the off action.                                                                                                                                                                                                 |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_off_timeout`{.literal}     | time    | 60s     | Specify an alternate timeout to use for off actions instead of `stonith-timeout`{.literal}. Some devices need much more or much less time to complete than normal. Use this to specify an alternate, device-specific, timeout for off actions.                                                                                                                                                                                       |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_off_retries`{.literal}     | integer | 2       | The maximum number of times to retry the off command within the timeout period. Some devices do not support multiple connections. Operations may fail if the device is busy with another task so Pacemaker will automatically retry the operation, if there is time remaining. Use this option to alter the number of times Pacemaker retries off actions before giving up.                                                          |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_list_action`{.literal}     | string  | list    | An alternate command to run instead of `list`{.literal}. Some devices do not support the standard commands or may provide additional ones. Use this to specify an alternate, device-specific, command that implements the list action.                                                                                                                                                                                               |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_list_timeout`{.literal}    | time    | 60s     | Specify an alternate timeout to use for list actions. Some devices need much more or much less time to complete than normal. Use this to specify an alternate, device-specific, timeout for list actions.                                                                                                                                                                                                                            |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_list_retries`{.literal}    | integer | 2       | The maximum number of times to retry the `list`{.literal} command within the timeout period. Some devices do not support multiple connections. Operations may fail if the device is busy with another task so Pacemaker will automatically retry the operation, if there is time remaining. Use this option to alter the number of times Pacemaker retries list actions before giving up.                                            |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_monitor_action`{.literal}  | string  | monitor | An alternate command to run instead of `monitor`{.literal}. Some devices do not support the standard commands or may provide additional ones. Use this to specify an alternate, device-specific, command that implements the monitor action.                                                                                                                                                                                         |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_monitor_timeout`{.literal} | time    | 60s     | Specify an alternate timeout to use for monitor actions instead of `stonith-timeout`{.literal}. Some devices need much more or much less time to complete than normal. Use this to specify an alternate, device-specific, timeout for monitor actions.                                                                                                                                                                               |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_monitor_retries`{.literal} | integer | 2       | The maximum number of times to retry the `monitor`{.literal} command within the timeout period. Some devices do not support multiple connections. Operations may fail if the device is busy with another task so Pacemaker will automatically retry the operation, if there is time remaining. Use this option to alter the number of times Pacemaker retries monitor actions before giving up.                                      |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_status_action`{.literal}   | string  | status  | An alternate command to run instead of `status`{.literal}. Some devices do not support the standard commands or may provide additional ones. Use this to specify an alternate, device-specific, command that implements the status action.                                                                                                                                                                                           |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_status_timeout`{.literal}  | time    | 60s     | Specify an alternate timeout to use for status actions instead of `stonith-timeout`{.literal}. Some devices need much more or much less time to complete than normal. Use this to specify an alternate, device-specific, timeout for status actions.                                                                                                                                                                                 |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_status_retries`{.literal}  | integer | 2       | The maximum number of times to retry the status command within the timeout period. Some devices do not support multiple connections. Operations may fail if the device is busy with another task so Pacemaker will automatically retry the operation, if there is time remaining. Use this option to alter the number of times Pacemaker retries status actions before giving up.                                                    |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_delay_base`{.literal}      | string  | 0s      | Enables a base delay for fencing actions and specifies a base delay value. You can specify different values for different nodes with the `pcmk_delay_base`{.literal} parameter. For general information about fencing delay parameters and their interactions, see [Fencing delays](#fence-delays "4.5.4. Fencing delays").                                                                                                          |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_delay_max`{.literal}       | time    | 0s      | Enables a random delay for fencing actions and specifies the maximum delay, which is the maximum value of the combined base delay and random delay. For example, if the base delay is 3 and `pcmk_delay_max`{.literal} is 10, the random delay will be between 3 and 10. For general information about fencing delay parameters and their interactions, see [Fencing delays](#fence-delays "4.5.4. Fencing delays").                 |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_action_limit`{.literal}    | integer | 1       | The maximum number of actions that can be performed in parallel on this device. The cluster property `concurrent-fencing=true`{.literal} needs to be configured first (this is the default value). A value of -1 is unlimited.                                                                                                                                                                                                       |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_on_action`{.literal}       | string  | on      | For advanced use only: An alternate command to run instead of `on`{.literal}. Some devices do not support the standard commands or may provide additional ones. Use this to specify an alternate, device-specific, command that implements the `on`{.literal} action.                                                                                                                                                                |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_on_timeout`{.literal}      | time    | 60s     | For advanced use only: Specify an alternate timeout to use for `on`{.literal} actions instead of `stonith-timeout`{.literal}. Some devices need much more or much less time to complete than normal. Use this to specify an alternate, device-specific, timeout for `on`{.literal} actions.                                                                                                                                          |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_on_retries`{.literal}      | integer | 2       | For advanced use only: The maximum number of times to retry the `on`{.literal} command within the timeout period. Some devices do not support multiple connections. Operations may `fail`{.literal} if the device is busy with another task so Pacemaker will automatically retry the operation, if there is time remaining. Use this option to alter the number of times Pacemaker retries `on`{.literal} actions before giving up. |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 4.2. Advanced Properties of Fencing Devices

Show more

In addition to the properties you can set for individual fence devices, there are also cluster properties you can set that determine fencing behavior, as described in the following table.

+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option                               | Default           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                      |
+:=====================================+:==================+:=================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `stonith-enabled`{.literal}          | true              | Indicates that failed nodes and nodes with resources that cannot be stopped should be fenced. Protecting your data requires that you set this `true`{.literal}.                                                                                                                                                                                                                                                                                  |
|                                      |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                      |                   | If `true`{.literal}, or unset, the cluster will refuse to start resources unless one or more STONITH resources have been configured also.                                                                                                                                                                                                                                                                                                        |
|                                      |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                      |                   | Red Hat only supports clusters with this value set to `true`{.literal}.                                                                                                                                                                                                                                                                                                                                                                          |
+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `stonith-action`{.literal}           | reboot            | Action to send to fencing device. Allowed values: `reboot`{.literal}, `off`{.literal}. The value `poweroff`{.literal} is also allowed, but is only used for legacy devices.                                                                                                                                                                                                                                                                      |
+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `stonith-timeout`{.literal}          | 60s               | How long to wait for a STONITH action to complete.                                                                                                                                                                                                                                                                                                                                                                                               |
+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `stonith-max-attempts`{.literal}     | 10                | How many times fencing can fail for a target before the cluster will no longer immediately re-attempt it.                                                                                                                                                                                                                                                                                                                                        |
+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `stonith-watchdog-timeout`{.literal} |                   | The maximum time to wait until a node can be assumed to have been killed by the hardware watchdog. It is recommended that this value be set to twice the value of the hardware watchdog timeout. This option is needed only if watchdog-only SBD configuration is used for fencing.                                                                                                                                                              |
+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `concurrent-fencing`{.literal}       | true              | Allow fencing operations to be performed in parallel.                                                                                                                                                                                                                                                                                                                                                                                            |
+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `fence-reaction`{.literal}           | stop              | Determines how a cluster node should react if notified of its own fencing. A cluster node may receive notification of its own fencing if fencing is misconfigured, or if fabric fencing is in use that does not cut cluster communication. Allowed values are `stop`{.literal} to attempt to immediately stop Pacemaker and stay stopped, or `panic`{.literal} to attempt to immediately reboot the local node, falling back to stop on failure. |
|                                      |                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|                                      |                   | Although the default value for this property is `stop`{.literal}, the safest choice for this value is `panic`{.literal}, which attempts to immediately reboot the local node. If you prefer the stop behavior, as is most likely to be the case in conjunction with fabric fencing, it is recommended that you set this explicitly.                                                                                                              |
+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `priority-fencing-delay`{.literal}   | 0 (disabled)      | Sets a fencing delay that allows you to configure a two-node cluster so that in a split-brain situation the node with the fewest or least important resources running is the node that gets fenced. For general information about fencing delay parameters and their interactions, see [Fencing delays](#fence-delays "4.5.4. Fencing delays").                                                                                                  |
+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 4.3. Cluster Properties that Determine Fencing Behavior

Show more

For information about setting cluster properties, see [Setting Cluster properties](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_high_availability_clusters/index#setting-cluster-properties).

#### [4.5.4. Fencing delays](#fence-delays) {#fencing-delays .title}

In two-node clusters, simultaneous communication loss can cause nodes to fence each other, shutting down the entire cluster. Configure a fencing delay to prevent this race condition. Delays are unnecessary in larger clusters, where quorum determines fencing authority.

You can set different types of fencing delays, depending on your system requirements.

-   **static fencing delays**

    A static fencing delay is a fixed, predetermined delay. Setting a static delay on one node makes that node more likely to be fenced because it increases the chances that the other node will initiate fencing first after detecting lost communication. In an active/passive cluster, setting a delay on a passive node makes it more likely that the passive node will be fenced when communication breaks down. You configure a static delay by using the `pcmk_delay_base`{.literal} instance attribute. To configure different delays, set this attribute on a separate fence device for each node. If you use a single fence device for all nodes, you can set this attribute to a host map, for example, `node1:0s;node2:5s`{.literal}.

-   **dynamic fencing delays**

    A dynamic fencing delay is random. It can vary and is determined at the time fencing is needed. You configure a random delay and specify a maximum value for the combined base delay and random delay with the `pcmk_delay_max`{.literal} instance attribute. When the fencing delay for each node is random, which node is fenced is also random. You might find this feature useful if your cluster is configured with a single fence device for all nodes in an active/active design.

-   **priority fencing delays**

    A priority fencing delay is based on active resource priorities. If all resources have the same priority, the node with the fewest resources running is the node that gets fenced. In most cases, you use only one delay-related parameter, but it is possible to combine them. Combining delay-related parameters adds the priority values for the resources together to create a total delay. You configure a priority fencing delay with the `priority-fencing-delay`{.literal} cluster property. You may find this feature useful in an active/active cluster design because it can make the node running the fewest resources more likely to be fenced when communication between the nodes is lost.

**The `pcmk_delay_base`{.literal} instance attribute**

The ‎`pcmk_delay_base`{.literal} instance attribute specifies a base delay value for fencing.

When you set the `pcmk_delay_max`{.literal} instance attribute in addition to the `pcmk_delay_base`{.literal} instance attribute, the overall delay combines a random delay value with this static delay, keeping the sum below the maximum delay. When you set `pcmk_delay_base`{.literal} but do not set `pcmk_delay_max`{.literal}, there is no random component to the delay, and the delay is the value of ‎`pcmk_delay_base`{.literal}.

You can specify different values for different nodes with the `pcmk_delay_base`{.literal} instance attribute. This allows a single fence device to be used in a two-node cluster, with a different delay for each node. You do not need to configure two separate devices to use separate delays. To specify different values for different nodes, you map the host names to the delay value for that node using a similar syntax to `pcmk_host_map`{.literal}. For example, `node1:0;node2:10s`{.literal} would use no delay when fencing `node1`{.literal} and a 10-second delay when fencing `node2`{.literal}.

The `pcmk_delay_max`{.literal} instance attribute

:   Use the ‎`pcmk_delay_base`{.literal} instance attribute to specify a base delay for fencing actions and the maximum delay, which is the maximum value of the combined base delay and random delay. For example, if the base delay is 3 and `pcmk_delay_max`{.literal} is 10, the random delay will be between 3 and 10.

    When you set the `pcmk_delay_base`{.literal} instance attribute in addition to the `pcmk_delay_max`{.literal} instance attribute, the overall delay is derived from a random delay value added to this static delay so that the sum is kept below the maximum delay. When you set `pcmk_delay_max`{.literal} but do not set `pcmk_delay_base`{.literal} there is no static component to the delay.

**The `priority-fencing-delay`{.literal} cluster property**

Setting the `priority-fencing-delay`{.literal} cluster property allows you to configure a two-node cluster so that in a split-brain situation the node with the fewest or least important resources running is the node that gets fenced.

The `priority-fencing-delay`{.literal} property can be set to a time duration. The default value for this property is 0 (disabled). If this property is set to a non-zero value, and the priority meta-attribute is configured for at least one resource, then in a split-brain situation the node with the highest combined priority of all resources running on it will be more likely to remain operational. For example, if you set `pcs resource defaults update priority=1`{.literal} and `pcs property set priority-fencing-delay=15s`{.literal} and no other priorities are set, then the node running the most resources will be more likely to remain operational because the other node will wait 15 seconds before initiating fencing. If a particular resource is more important than the rest, you can give it a higher priority.

The node running the promoted role of a promotable clone gets an extra 1 point if a priority has been configured for that clone.

**Interaction of fencing delays**

Setting more than one type of fencing delay yields the following results:

-   Any delay set with the `priority-fencing-delay`{.literal} property is added to any delay from the `pcmk_delay_base`{.literal} and `pcmk_delay_max`{.literal} instance attributes. This behavior allows some delay when both nodes have equal priority, or both nodes need to be fenced for some reason other than node loss, as when `on-fail=fencing`{.literal} is set for a resource monitor operation. When setting these delays in combination, set the `priority-fencing-delay`{.literal} property to a value that is significantly greater than the maximum delay from `pcmk_delay_base`{.literal} and `pcmk_delay_max`{.literal} to be sure the prioritized node is preferred. Setting this property to twice this value is always safe.
-   Only fencing scheduled by Pacemaker itself observes fencing delays. Fencing scheduled by external code such as `dlm_controld`{.literal} and fencing implemented by the `pcs stonith fence`{.literal} command do not provide the necessary information to the fence device.
-   Some individual fence agents implement a delay parameter, with a name determined by the agent. This delay is independent of delays configured with a ‎`pcmk_delay_*`{.literal} instance attribute. If both of these delays are configured, they are added together and would generally not be used in conjunction.

#### [4.5.5. Testing a fence device](#testing-fence-devices) {#testing-a-fence-device .title}

To prevent data corruption and successfully recover a cluster from node failures, validate the fence device. For a complete testing strategy, verify network connectivity, run the fence agent script, trigger the fence action through the cluster manager, and simulate a physical node failure.

**Prerequisites**

-   You have configured fencing so that a Pacemaker cluster node or Pacemaker remote node results in a hard kill, not a graceful shutdown.
-   You have disabled ACPI soft-off in the `/etc/systemd/logind.conf`{.literal} file so that any power-button-pressed signal is ignored in case of a graceful shutdown.

**Procedure**

1.  Use SSH, Telnet, HTTP, or whatever remote protocol is used to connect to the device to manually log in and test the fence device or see what output is given. For example, if you will be configuring fencing for an IPMI-enabled device,then try to log in remotely with `ipmitool`{.literal}. Take note of the options used when logging in manually because those options might be needed when using the fencing agent.

    If you are unable to log in to the fence device, verify that the device is pingable, there is nothing such as a firewall configuration that is preventing access to the fence device, remote access is enabled on the fencing device, and the credentials are correct.

2.  Run the fence agent manually, using the fence agent script. This does not require that the cluster services are running, so you can perform this step before the device is configured in the cluster. This can ensure that the fence device is responding properly before proceeding.

    Note

    These examples use the `fence_ipmilan`{.literal} fence agent script for an iLO device. The actual fence agent you will use and the command that calls that agent will depend on your server hardware. You should consult the man page for the fence agent you are using to determine which options to specify. You will usually need to know the login and password for the fence device and other information related to the fence device.

    The following example shows the format you would use to run the `fence_ipmilan`{.literal} fence agent script with `-o status`{.literal} parameter to check the status of the fence device interface on another node without actually fencing it. This allows you to test the device and get it working before attempting to reboot the node. When running this command, you specify the name and password of an iLO user that has power on and off permissions for the iLO device.

    ``` {.language-plaintext tabindex="-1"}
    # fence_ipmilan -a ipaddress -l username -p password -o status
    ```

    The following example shows the format you would use to run the `fence_ipmilan`{.literal} fence agent script with the `-o reboot`{.literal} parameter. Running this command on one node reboots the node managed by this iLO device.

    ``` {.language-plaintext tabindex="-1"}
    # fence_ipmilan -a ipaddress -l username -p password -o reboot
    ```

    If the fence agent failed to properly do a status, off, on, or reboot action, you should check the hardware, the configuration of the fence device, and the syntax of your commands. In addition, you can run the fence agent script with the debug output enabled. The debug output is useful for some fencing agents to see where in the sequence of events the fencing agent script is failing when logging into the fence device.

    ``` {.language-plaintext tabindex="-1"}
    # fence_ipmilan -a ipaddress -l username -p password -o status -D /tmp/$(hostname)-fence_agent.debug
    ```

    When diagnosing a failure that has occurred, you should ensure that the options you specified when manually logging in to the fence device are identical to what you passed on to the fence agent with the fence agent script.

    For fence agents that support an encrypted connection, you may see an error due to certificate validation failing, requiring that you trust the host or that you use the fence agent's `ssl-insecure`{.literal} parameter. Similarly, if SSL/TLS is disabled on the target device, you may need to account for this when setting the SSL parameters for the fence agent.

    Note

    If the fence agent that is being tested is a `fence_drac`{.literal}, `fence_ilo`{.literal}, or some other fencing agent for a systems management device that continues to fail, then fall back to trying `fence_ipmilan`{.literal}. Most systems management cards support IPMI remote login and the only supported fencing agent is `fence_ipmilan`{.literal}.

3.  Once the fence device has been configured in the cluster with the same options that worked manually and the cluster has been started, test fencing with the `pcs stonith fence`{.literal} command from any node (or even multiple times from different nodes), as in the following example. The `pcs stonith fence`{.literal} command reads the cluster configuration from the CIB and calls the fence agent as configured to start the fence action. This verifies that the cluster configuration is correct.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith fence node_name
    ```

    If the `pcs stonith fence`{.literal} command works properly, that means the fencing configuration for the cluster should work when a fence event occurs. If the command fails, it means that cluster management cannot invoke the fence device through the configuration it has retrieved. Check for the following issues and update your cluster configuration as needed.

    -   Check your fence configuration. For example, if you have used a host map you should ensure that the system can find the node using the host name you have provided.

    -   Check whether the password and user name for the device include any special characters that could be misinterpreted by the bash shell. Making sure that you enter passwords and user names surrounded by quotation marks could address this issue.

    -   Check whether you can connect to the device using the exact IP address or host name you specified in the `pcs stonith`{.literal} command. For example, if you give the host name in the stonith command but test by using the IP address, that is not a valid test.

    -   If the protocol that your fence device uses is accessible to you, use that protocol to try to connect to the device. For example many agents use ssh or telnet. You should try to connect to the device with the credentials you provided when configuring the device, to see if you get a valid prompt and can log in to the device.

        If you determine that all your parameters are appropriate but you still have trouble connecting to your fence device, you can check the logging on the fence device itself, if the device provides that, which will show if the user has connected and what command the user issued. You can also search through the `/var/log/messages`{.literal} file for instances of stonith and error, which could give some idea of what is transpiring, but some agents can provide additional information.

4.  Once the fence device tests are working and the cluster is up and running, test an actual failure. To do this, take an action in the cluster that should initiate a token loss.

    -   Take down a network. How you take a network depends on your specific configuration. In many cases, you can physically pull the network or power cables out of the host. For information about simulating a network failure, see the Red Hat Knowledgebase solution [What is the proper way to simulate a network failure on a RHEL Cluster?](https://access.redhat.com/solutions/79523/).

        Note

        Disabling the network interface on the local host rather than physically disconnecting the network or power cables is not recommended as a test of fencing because it does not accurately simulate a typical real-world failure.

    -   Block corosync traffic both inbound and outbound using the local firewall.

        The following example blocks corosync, assuming the default corosync port is used, `firewalld`{.literal} is used as the local firewall, and the network interface used by corosync is in the default firewall zone:

        ``` {.language-plaintext tabindex="-1"}
        # firewall-cmd --direct --add-rule ipv4 filter OUTPUT 2 -p udp --dport=5405 -j DROP
        # firewall-cmd --add-rich-rule='rule family="ipv4" port port="5405" protocol="udp" drop'
        ```

    -   Simulate a crash and panic your machine with `sysrq-trigger`{.literal}. Note, however, that triggering a kernel panic can cause data loss; it is recommended that you disable your cluster resources first.

        ``` {.language-plaintext tabindex="-1"}
        # echo c > /proc/sysrq-trigger
        ```

**Additional resources**

-   [Disabling ACPI soft-off in the logind.conf file](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_managing_high_availability_clusters/index#disabling_acpi_soft_off_in_the_logind_conf_file)

#### [4.5.6. Configuring fencing levels](#configuring-fencing-levels) {#configuring-fencing-levels .title}

Pacemaker supports fencing nodes with multiple devices through a feature called fencing topologies. To implement topologies, create the individual devices as you normally would and then define one or more fencing levels in the fencing topology section in the configuration.

Pacemaker processes fencing levels as follows:

-   Each level is attempted in ascending numeric order, starting at 1.
-   If a device fails, processing terminates for the current level. No further devices in that level are exercised and the next level is attempted instead.
-   If all devices are successfully fenced, then that level has succeeded and no other levels are tried.
-   The operation is finished when a level has passed (success), or all levels have been attempted (failed).

Use the following command to add a fencing level to a node. The devices are given as a comma-separated list of `stonith`{.literal} ids, which are attempted for the node at that level.

``` {.language-plaintext tabindex="-1"}
# pcs stonith level add level node devices
```

The following example configures fence levels so that if the device `my_ilo`{.literal} fails and is unable to fence the node, then Pacemaker attempts to use the device `my_apc`{.literal}.

**Prerequisites**

-   You have configured an ilo fence device called `my_ilo`{.literal} for node `rh7-2`{.literal}.
-   You have configured an apc fence device called `my_apc`{.literal} for node `rh7-2`{.literal}.

**Procedure**

1.  Add a fencing level of 1 for fence device `my_ilo`{.literal} on node `rh7-2`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level add 1 rh7-2 my_ilo
    ```

2.  Add a fencing level of 2 for fence device `my_apc`{.literal} on node `rh7-2`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level add 2 rh7-2 my_apc
    ```

3.  List the currently configured fencing levels.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level
    ```

    ``` {.language-plaintext tabindex="-1"}
     Node: rh7-2
      Level 1 - my_ilo
      Level 2 - my_apc
    ```

**Additional resources**

-   [Configuring node-specific values using node attributes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/configuring_and_managing_high_availability_clusters/index#node-attributes)

#### [4.5.7. Removing a fence level](#removing-a-fence-level) {#removing-a-fence-level .title}

You can remove the fence level for the specified node and device. If no nodes or devices are specified then the fence level you specify is removed from all nodes.

**Procedure**

-   Remove the fence level for the specified node and device:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level remove level [node_id] [stonith_id] ... [stonith_id]
    ```

#### [4.5.8. Clearing fence levels](#clearing-fence-levels) {#clearing-fence-levels .title}

You can clear the fence levels on the specified node or stonith id. If you do not specify a node or stonith id, all fence levels are cleared.

**Procedure**

-   Clear the fence levels on the specified node or stonith id:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level clear [node]|stonith_id(s)]
    ```

-   If you specify more than one stonith id, they must be separated by a comma and no spaces, as in the following example.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level clear dev_a,dev_b
    ```

#### [4.5.9. Verifying nodes and devices in fence levels](#verifying-nodes-and-devices-in-fence-levels_general-fence) {#verifying-nodes-and-devices-in-fence-levels .title}

You can verify that all fence devices and nodes specified in fence levels exist.

**Procedure**

-   Use the following command to verify that all fence devices and nodes specified in fence levels exist:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level verify
    ```

#### [4.5.10. Specifying nodes in fencing topology](#specifying-nodes-in-fencing-topology) {#specifying-nodes-in-fencing-topology .title}

You can specify nodes in fencing topology by a regular expression applied on a node name and by a node attribute and its value.

**Procedure**

-   The following commands configure nodes `node1`{.literal}, `node2`{.literal}, and `node3`{.literal} to use fence devices `apc1`{.literal} and `apc2`{.literal}, and nodes `node4`{.literal}, `node5`{.literal}, and `node6`{.literal} to use fence devices `apc3`{.literal} and `apc4`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level add 1 "regexp%node[1-3]" apc1,apc2
    # pcs stonith level add 1 "regexp%node[4-6]" apc3,apc4
    ```

-   The following commands yield the same results by using node attribute matching:

    ``` {.language-plaintext tabindex="-1"}
    # pcs node attribute node1 rack=1
    # pcs node attribute node2 rack=1
    # pcs node attribute node3 rack=1
    # pcs node attribute node4 rack=2
    # pcs node attribute node5 rack=2
    # pcs node attribute node6 rack=2
    # pcs stonith level add 1 attrib%rack=1 apc1,apc2
    # pcs stonith level add 1 attrib%rack=2 apc3,apc4
    ```

#### [4.5.11. Configuring fencing for redundant power supplies](#configuring-fencing-for-redundant-power) {#configuring-fencing-for-redundant-power-supplies .title}

When configuring fencing for redundant power supplies, the cluster must ensure that when attempting to reboot a host, both power supplies are turned off before either power supply is turned back on.

If the node never completely loses power, the node may not release its resources. This opens up the possibility of nodes accessing these resources simultaneously and corrupting them.

You need to define each device only once and to specify that both are required to fence the node.

**Procedure**

1.  Create the first fence device.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith create apc1 fence_apc_snmp ipaddr=apc1.example.com login=user passwd='7a4D#1j!pz864' pcmk_host_map="node1.example.com:1;node2.example.com:2"
    ```

2.  Create the second fence device.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith create apc2 fence_apc_snmp ipaddr=apc2.example.com login=user passwd='7a4D#1j!pz864' pcmk_host_map="node1.example.com:1;node2.example.com:2"
    ```

3.  Specify that both devices are required to fence the node.

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level add 1 node1.example.com apc1,apc2
    # pcs stonith level add 1 node2.example.com apc1,apc2
    ```

#### [4.5.12. Administering fence devices](#administering-fence-devices) {#administering-fence-devices .title}

The `pcs`{.literal} command-line interface provides a variety of commands you can use to administer your fence devices after you have configured them.

##### [4.5.12.1. Displaying configured fence devices](#displaying_configured_fence_devices) {#displaying-configured-fence-devices .title}

The following command shows all currently configured fence devices. If a *stonith_id* is specified, the command shows the options for that configured fencing device only. If the `--full`{.literal} option is specified, all configured fencing options are displayed.

``` {.language-plaintext tabindex="-1"}
# pcs stonith config [stonith_id] [--full]
```

##### [4.5.12.2. Exporting fence devices as pcs commands](#exporting_fence_devices_as_pcs_commands) {#exporting-fence-devices-as-pcs-commands .title}

You can display the `pcs`{.literal} commands that can be used to re-create configured fence devices on a different system using the `--output-format=cmd`{.literal} option of the `pcs stonith config`{.literal} command.

The following commands create a `fence_apc_snmp`{.literal} fence device and display the `pcs`{.literal} command you can use to re-create the device.

``` {.language-plaintext tabindex="-1"}
# pcs stonith create myapc fence_apc_snmp ip="zapc.example.com" pcmk_host_map="z1.example.com:1;z2.example.com:2" username="apc" password="apc"
# pcs stonith config --output-format=cmd
```

``` {.language-plaintext tabindex="-1"}
Warning: Only 'text' output format is supported for stonith levels
pcs stonith create --no-default-ops --force -- myapc fence_apc_snmp \
  ip=zapc.example.com password=apc 'pcmk_host_map=z1.example.com:1;z2.example.com:2' username=apc \
  op \
    monitor interval=60s id=myapc-monitor-interval-60s
```

##### [4.5.12.3. Exporting fence level configuration](#exporting_fence_level_configuration) {#exporting-fence-level-configuration .title}

The `pcs stonith config`{.literal} and the `pcs stonith level config`{.literal} commands support the `--output-format=`{.literal} option to export the fencing level configuration in JSON format and as `pcs`{.literal} commands.

-   Specifying `--output-format=cmd`{.literal} displays the `pcs`{.literal} commands created from the current cluster configuration that configure fencing levels. You can use these commands to re-create configured fencing levels on a different system.
-   Specifying `--output-format=json`{.literal} displays the fencing level configuration in JSON format, which is suitable for machine parsing.

##### [4.5.12.4. Modifying and deleting fence devices](#modifying_and_deleting_fence_devices) {#modifying-and-deleting-fence-devices .title}

Modify or add options to a currently configured fencing device with the following command.

``` {.language-plaintext tabindex="-1"}
# pcs stonith update stonith_id [stonith_device_options]
```

Updating a SCSI fencing device with the `pcs stonith update`{.literal} command causes a restart of all resources running on the same node where the fencing resource was running. You can use either version of the following command to update SCSI devices without causing a restart of other cluster resources. SCSI fencing devices can be configured as multipath devices.

``` {.language-plaintext tabindex="-1"}
# pcs stonith update-scsi-devices stonith_id set device-path1 device-path2
# pcs stonith update-scsi-devices stonith_id add device-path1 remove device-path2
```

Use the following command to remove a fencing device from the current configuration.

``` {.language-plaintext tabindex="-1"}
# pcs stonith delete stonith_id
```

##### [4.5.12.5. Manually fencing a cluster node](#manually_fencing_a_cluster_node) {#manually-fencing-a-cluster-node .title}

You can fence a node manually with the following command. If you specify the `--off`{.literal} option this will use the `off`{.literal} API call to stonith which will turn the node off instead of rebooting it.

``` {.language-plaintext tabindex="-1"}
# pcs stonith fence node [--off]
```

In a situation where no fence device is able to fence a node even if it is no longer active, the cluster may not be able to recover the resources on the node. If this occurs, after manually ensuring that the node is powered down you can enter the following command to confirm to the cluster that the node is powered down and free its resources for recovery.

Warning

If the node you specify is not actually off, but running the cluster software or services normally controlled by the cluster, data corruption and cluster failure occurs.

``` {.language-plaintext tabindex="-1"}
# pcs stonith confirm node
```

##### [4.5.12.6. Disabling a fence device](#disabling_a_fence_device) {#disabling-a-fence-device .title}

To disable a fencing device, run the `pcs stonith disable`{.literal} command.

The following command disables the fence device `myapc`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs stonith disable myapc
```

##### [4.5.12.7. Preventing a node from using a fencing device](#preventing_a_node_from_using_a_fencing_device) {#preventing-a-node-from-using-a-fencing-device .title}

To prevent a specific node from using a fencing device, you can configure location constraints for the fencing resource.

The following example prevents fence device `node1-ipmi`{.literal} from running on `node1`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs constraint location node1-ipmi avoids node1
```

#### [4.5.13. Additional resources](#configuring-fencing_4513-additional-resources) {#additional-resources .title}

-   [Fencing in a Red Hat High Availability Cluster (Red Hat Knowledgebase)](https://access.redhat.com/solutions/15575)

### [4.6. Configuring ACPI for use with integrated fence devices](#configuring-acpi-for-use-with-integrated-fence-devices) {#configuring-acpi-for-use-with-integrated-fence-devices .title}

If your cluster uses integrated fence devices, you must configure ACPI (Advanced Configuration and Power Interface) to ensure immediate and complete fencing.

If a cluster node is configured to be fenced by an integrated fence device, disable ACPI Soft-Off for that node. Disabling ACPI Soft-Off allows an integrated fence device to turn off a node immediately and completely rather than attempting a clean shutdown (for example, `shutdown -h now`{.literal}). Otherwise, if ACPI Soft-Off is enabled, an integrated fence device can take four or more seconds to turn off a node (see the note that follows). In addition, if ACPI Soft-Off is enabled and a node panics or freezes during shutdown, an integrated fence device may not be able to turn off the node. Under those circumstances, fencing is delayed or unsuccessful. Consequently, when a node is fenced with an integrated fence device and ACPI Soft-Off is enabled, a cluster recovers slowly or requires administrative intervention to recover.

Note

The amount of time required to fence a node depends on the integrated fence device used. Some integrated fence devices perform the equivalent of pressing and holding the power button; therefore, the fence device turns off the node in four to five seconds. Other integrated fence devices perform the equivalent of pressing the power button momentarily, relying on the operating system to turn off the node; therefore, the fence device turns off the node in a time span much longer than four to five seconds.

-   The preferred way to disable ACPI Soft-Off is to change the BIOS setting to \"instant-off\" or an equivalent setting that turns off the node without delay.

Disabling ACPI Soft-Off with the BIOS may not be possible with some systems. If disabling ACPI Soft-Off with the BIOS is not satisfactory for your cluster, you can disable ACPI Soft-Off with one of the following alternate methods:

-   Setting `HandlePowerKey=ignore`{.literal} in the `/etc/systemd/logind.conf`{.literal} file and verifying that the node turns off immediately when fenced. This is the first alternate method of disabling ACPI Soft-Off.

-   Appending `acpi=off`{.literal} to the kernel boot command line. This is the second alternate method of disabling ACPI Soft-Off, if the preferred or the first alternate method is not available.

    Important

    This method completely disables ACPI; some computers do not boot correctly if ACPI is completely disabled. Use this method *only* if the other methods are not effective for your cluster.

#### [4.6.1. Disabling ACPI Soft-Off with the BIOS](#disabling-acpi-soft-off-with-the-bios) {#disabling-acpi-soft-off-with-the-bios .title}

You can disable ACPI Soft-Off by configuring the BIOS of each cluster node.

Note

The procedure for disabling ACPI Soft-Off with the BIOS may differ among server systems. You should verify this procedure with your hardware documentation.

**Procedure**

1.  Reboot the node and start the `BIOS CMOS Setup Utility`{.literal} program.

2.  Navigate to the Power menu (or equivalent power management menu).

3.  At the Power menu, set the `Soft-Off by PWR-BTTN`{.literal} function (or equivalent) to `Instant-Off`{.literal} (or the equivalent setting that turns off the node by means of the power button without delay). The `BIOS CMOS Setup Utiliy`{.literal} in the following example shows a Power menu with `ACPI Function`{.literal} set to `Enabled`{.literal} and `Soft-Off by PWR-BTTN`{.literal} set to `Instant-Off`{.literal}.

    Note

    The equivalents to `ACPI Function`{.literal}, `Soft-Off by PWR-BTTN`{.literal}, and `Instant-Off`{.literal} may vary among computers. However, the objective of this procedure is to configure the BIOS so that the computer is turned off by means of the power button without delay.

4.  Exit the `BIOS CMOS Setup Utility`{.literal} program, saving the BIOS configuration.

5.  Verify that the node turns off immediately when fenced. For information about testing a fence device, see [Testing a fence device](#testing-fence-devices "4.5.5. Testing a fence device").

**Example 4.1. BIOS CMOS Setup Utility**

``` {.language-plaintext tabindex="-1"}
`Soft-Off by PWR-BTTN` set to
`Instant-Off`
```

``` {.language-plaintext tabindex="-1"}
+---------------------------------------------|-------------------+
|    ACPI Function             [Enabled]      |    Item Help      |
|    ACPI Suspend Type         [S1(POS)]      |-------------------|
|  x Run VGABIOS if S3 Resume   Auto          |   Menu Level   *  |
|    Suspend Mode              [Disabled]     |                   |
|    HDD Power Down            [Disabled]     |                   |
|    Soft-Off by PWR-BTTN      [Instant-Off   |                   |
|    CPU THRM-Throttling       [50.0%]        |                   |
|    Wake-Up by PCI card       [Enabled]      |                   |
|    Power On by Ring          [Enabled]      |                   |
|    Wake Up On LAN            [Enabled]      |                   |
|  x USB KB Wake-Up From S3     Disabled      |                   |
|    Resume by Alarm           [Disabled]     |                   |
|  x  Date(of Month) Alarm       0            |                   |
|  x  Time(hh:mm:ss) Alarm       0 :  0 :     |                   |
|    POWER ON Function         [BUTTON ONLY   |                   |
|  x KB Power ON Password       Enter         |                   |
|  x Hot Key Power ON           Ctrl-F1       |                   |
|                                             |                   |
|                                             |                   |
+---------------------------------------------|-------------------+
```

This example shows `ACPI Function`{.literal} set to `Enabled`{.literal}, and `Soft-Off by PWR-BTTN`{.literal} set to `Instant-Off`{.literal}.

#### [4.6.2. Disabling ACPI Soft-Off in the logind.conf file](#disabling-acpi-soft-off-in-the-logind-conf-file) {#disabling-acpi-soft-off-in-the-logind.conf-file .title}

You can disable power-key handing in the `/etc/systemd/logind.conf`{.literal} file.

**Procedure**

1.  Define the following configuration in the `/etc/systemd/logind.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    HandlePowerKey=ignore
    ```

2.  Restart the `systemd-logind`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl restart systemd-logind.service
    ```

**Verification**

1.  Verify that the node turns off immediately when fenced. For information about testing a fence device, see [Testing a fence device](#testing-fence-devices "4.5.5. Testing a fence device").

#### [4.6.3. Disabling ACPI completely in the GRUB 2 file](#disabling-acpi-completely-in-the-grub-2-file) {#disabling-acpi-completely-in-the-grub-2-file .title}

Disable ACPI Soft-Off by appending `acpi=off`{.literal} to the GRUB menu entry for a kernel.

Important

Completely disabling ACPI can prevent some systems from booting correctly. Use this method only if other fence configuration methods are ineffective for the cluster.

**Procedure**

1.  Update the `grub.cfg`{.literal} file on each cluster node by using the `grubby`{.literal} tool with the `--args`{.literal} and `--update-kernel`{.literal} options:

    ``` {.language-plaintext tabindex="-1"}
    # grubby --args=acpi=off --update-kernel=ALL
    ```

2.  Reboot the node.

**Verification**

1.  Verify that the node turns off immediately when fenced. For details, see [Testing a fence device](#testing-fence-devices "4.5.5. Testing a fence device").

### [4.7. Creating an Azure internal load balancer](#creating-an-azure-internal-load-balancer) {#creating-an-azure-internal-load-balancer .title}

To ensure that cluster nodes that do not respond to health probe requests are removed, you can create an Azure internal load balancer. Configure the load balancer with settings customized for high availability (HA) clusters.

**Prerequisites**

-   You have created [a Red Hat account](https://www.redhat.com/wapps/ugc/register.html).
-   You have [signed up and configured an Azure account](https://azure.microsoft.com/en-in/free).
-   The [Azure Command Line Interface (CLI)](#installing-the-azure-cli "3.4. Installing the Azure CLI") is installed on your system.
-   You have created the Azure resources for your HA cluster, including a virtual network, subnet, and availability set that contains your cluster nodes.

**Procedure**

1.  From any node in the HA cluster, log in to your Azure account:

    ``` {.language-plaintext tabindex="-1"}
    $ az login
    ```

2.  Create a Basic internal load balancer with a dynamic private front-end IP address:

    ``` {.language-plaintext tabindex="-1"}
    $ az network lb create \
    --resource-group <resource_group> \
    --name <load_balancer_name> \
    --sku Basic \
    --vnet-name <vnet_name> \
    --subnet <subnet_name> \
    --frontend-ip-name <frontend_ip_name> \
    --backend-pool-name <backend_pool_name>
    ```

    Do not specify `--private-ip-address`{.literal} so Azure assigns the front-end IP address dynamically from the subnet.

    Example:

    ``` {.language-plaintext tabindex="-1"}
    $ az network lb create \
    --resource-group azrhelclirsgrp \
      --name rhelha-lb1 \
    --sku Basic \
    --vnet-name azrhelclivnet1 \
    --subnet azrhelclisubnet1 \
    --frontend-ip-name rhelha-frontend1 \
    --backend-pool-name rhelha-backend1
    ```

3.  Associate the back-end pool with the availability set that contains your cluster nodes:

    Do not add individual IP addresses to the back-end pool. Add the network interfaces for each virtual machine (VM) in the availability set to the back-end pool:

    ``` {.language-plaintext tabindex="-1"}
    $ for vm in $(az vm list-instances \
    --resource-group "<resource_group>" \
    --name "<availability_set>" \
    --query "[].name" -o tsv); do
    nic=$(az vm show \
    --resource-group "<resource_group>" \
    --name "$vm" \
    --query "networkProfile.networkInterfaces[0].id" -o tsv | xargs basename)
    az network nic ip-config address-pool add \
    --resource-group "<resource_group>" \
    --lb-name "<load_balancer_name>" \
    --address-pool "<backend_pool_name>" \
    --nic-name "$nic" \
    --ip-config-name "ipconfig1"
    done
    ```

    Replace *\<ip_config_name\>* with the IP configuration name on each cluster node network interface, for example `ipconfig1`{.literal}.

4.  Create a TCP health probe on port `61000`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ az network lb probe create \
    --resource-group <resource_group> \
    --lb-name <load_balancer_name> \
    --name <health_probe_name> \
    --protocol Tcp \
    --port 61000
    ```

    You can use any TCP port number that does not interfere with another service.

    Note

    For certain HA product applications (for example, SAP High-Performance Analytic Appliance (HANA) and SQL Server), you need to work with Microsoft to identify the correct port to use.

    Example:

    ``` {.language-plaintext tabindex="-1"}
    $ az network lb probe create \
    --resource-group azrhelclirsgrp \
    --lb-name rhelha-lb1 \
    --name rhelha-probe1 \
    --protocol Tcp \
    --port 61000
    ```

5.  Create a load balancing rule with floating IP enabled:

    ``` {.language-plaintext tabindex="-1"}
    $ az network lb rule create \
    --resource-group <resource_group> \
    --lb-name <load_balancer_name> \
    --name <load_balancer_rule_name> \
    --protocol Tcp \
    --frontend-port 61000 \
    --backend-port 61000 \
    --frontend-ip-name <frontend_ip_name> \
    --backend-pool-name <backend_pool_name> \
    --probe-name <health_probe_name> \
    --floating-ip true
    ```

    Use the same front-end and back-end port values as the health probe unless your HA application requires different ports.

    Example:

    ``` {.language-plaintext tabindex="-1"}
    $ az network lb rule create \
    --resource-group azrhelclirsgrp \
    --lb-name rhelha-lb1 \
    --name rhelha-rule1 \
    --protocol Tcp \
    --frontend-port 61000 \
    --backend-port 61000 \
    --frontend-ip-name rhelha-frontend1 \
    --backend-pool-name rhelha-backend1 \
    --probe-name rhelha-probe1 \
    --floating-ip true
    ```

**Verification**

-   Verify that the load balancer and its front-end IP address were created successfully:

    ``` {.language-plaintext tabindex="-1"}
    $ az network lb show \
    --resource-group <resource_group> \
    --name <load_balancer_name> \
    --query "{name:name, sku:sku.name, provisioningState:provisioningState}" \
    --output table
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ az network lb frontend-ip list \
    --resource-group <resource_group> \
    --lb-name <load_balancer_name> \
    --output table
    ```

    Example:

    ``` {.language-plaintext tabindex="-1"}
    $ az network lb show \
    --resource-group azrhelclirsgrp \
    --name rhelha-lb1 \
    --query "{name:name, sku:sku.name, provisioningState:provisioningState}" \
    --output table
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ az network lb frontend-ip list \
    --resource-group azrhelclirsgrp \
    --lb-name rhelha-lb1 \
    --output table
    ```

**Next steps**

-   You can [configure the load balancer resource agent for Azure](#configuring-the-load-balancer-resource-agent "4.8. Configuring the load balancer resource agent").

**Additional resources**

-   [az network lb create](https://learn.microsoft.com/en-us/cli/azure/network/lb?view=azure-cli-latest#az-network-lb-create)
-   [az network lb address-pool](https://learn.microsoft.com/en-us/cli/azure/network/lb/address-pool?view=azure-cli-latest)
-   [az network lb probe create](https://learn.microsoft.com/en-us/cli/azure/network/lb/probe?view=azure-cli-latest#az-network-lb-probe-create)
-   [az network lb rule create](https://learn.microsoft.com/en-us/cli/azure/network/lb/rule?view=azure-cli-latest#az-network-lb-rule-create)
-   [az network nic ip-config address-pool add](https://learn.microsoft.com/en-us/cli/azure/network/nic/ip-config/address-pool?view=azure-cli-latest#az-network-nic-ip-config-address-pool-add)

### [4.8. Configuring the load balancer resource agent](#configuring-the-load-balancer-resource-agent) {#configuring-the-load-balancer-resource-agent .title}

After creating a health probe, you must configure the load balancer resource agent. This resource agent runs a service that responds to health probe requests from the Azure load balancer and removes cluster nodes that do not respond.

**Prerequisites**

-   You have completed the process of [creating an Azure load balancer](#creating-an-azure-internal-load-balancer "4.7. Creating an Azure internal load balancer").

**Procedure**

1.  Install the `nmap-ncat`{.literal} resource agents on all nodes:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install nmap-ncat resource-agents-cloud
    ```

2.  Perform the following steps on a single node:

    a.  Create the `pcs`{.literal} resources and group by using the `FrontendIP`{.literal} load balancer for the `IPaddr2`{.literal} address:

        ``` {.language-plaintext tabindex="-1"}
        # pcs resource create resource-name IPaddr2 ip="10.0.0.7" --group <cluster_resources_group>
        ```

    b.  Configure the `load balancer`{.literal} resource agent:

        ``` {.language-plaintext tabindex="-1"}
        # pcs resource create resource-loadbalancer-name azure-lb port=port-number --group <cluster_resources_group>
        ```

**Verification**

-   Run `pcs status`{.literal} to see the results.

    ``` {.language-plaintext tabindex="-1"}
    [root@node01 clouduser]# pcs status

    Cluster name: clusterfence01
    Stack: corosync
    Current DC: node02 (version 1.1.16-12.el7_4.7-94ff4df) - partition with quorum
    Last updated: Tue Jan 30 12:42:35 2018
    Last change: Tue Jan 30 12:26:42 2018 by root via cibadmin on node01

    3 nodes configured
    3 resources configured

    Online: [ node01 node02 node03 ]

    Full list of resources:

    clusterfence (stonith:fence_azure_arm):      Started node01
    Resource Group: g_azure
        vip_azure  (ocf::heartbeat:IPaddr2):       Started node02
        lb_azure   (ocf::heartbeat:azure-lb):      Started node02

    Daemon Status:
      corosync: active/disabled
      pacemaker: active/disabled
      pcsd: active/enabled
    ```

**Additional resources**

-   [Load balancer distribution mode](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-distribution-mode)

### [4.9. Configuring shared block storage](#configuring-shared-block-storage) {#configuring-shared-block-storage .title}

To let multiple cluster nodes access the same data, configure Azure Shared Disks as shared block storage. This ensures consistent, simultaneous data access across all nodes for high availability (HA) clusters and applications such as databases or filesystems.

**Prerequisites**

-   You have not yet created your cluster.

-   You have three Azure virtual machines (VMs) (a three-node cluster) with a 1 TB shared disk.

-   You have [the Azure CLI](#installing-the-azure-cli "3.4. Installing the Azure CLI") on your host system and created SSH key(s).

-   You must have created the cluster environment in Azure. To do so, follow the resources in this list:

    -   Resource group
    -   Virtual network
    -   Network security group(s)
    -   Network security group rules
    -   Subnet(s)
    -   Load balancer (optional)
    -   Storage account
    -   Proximity placement group
    -   Availability set

**Procedure**

1.  Create a [shared block volume](https://learn.microsoft.com/en-us/cli/azure/disk?view=azure-cli-latest#az_disk_create):

    ``` {.language-plaintext tabindex="-1"}
    $ az disk create -g <resource_group> \ -n <shared_block_volume_name> \ --size-gb <disk_size> \ --max-shares <number_vms> \ -l <location>
    ```

    For example, the following command creates a shared block volume named `shared-block-volume.vhd`{.literal} in the resource group `sharedblock`{.literal} within the Azure Availability Zone `westcentralus`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    $ az disk create -g sharedblock-rg \ -n shared-block-volume.vhd \ --size-gb 1024 \ --max-shares 3 \ -l westcentralus
    ```

    ``` {.language-plaintext tabindex="-1"}
    {
      "creationData": {
        "createOption": "Empty",
        "galleryImageReference": null,
        "imageReference": null,
        "sourceResourceId": null,
        "sourceUniqueId": null,
        "sourceUri": null,
        "storageAccountId": null,
        "uploadSizeBytes": null
      },
      "diskAccessId": null,
      "diskIopsReadOnly": null,
      "diskIopsReadWrite": 5000,
      "diskMbpsReadOnly": null,
      "diskMbpsReadWrite": 200,
      "diskSizeBytes": 1099511627776,
      "diskSizeGb": 1024,
      "diskState": "Unattached",
      "encryption": {
        "diskEncryptionSetId": null,
        "type": "EncryptionAtRestWithPlatformKey"
      },
      "encryptionSettingsCollection": null,
      "hyperVgeneration": "V1",
      "id": "/subscriptions/12345678910-12345678910/resourceGroups/sharedblock-rg/providers/Microsoft.Compute/disks/shared-block-volume.vhd",
      "location": "westcentralus",
      "managedBy": null,
      "managedByExtended": null,
      "maxShares": 3,
      "name": "shared-block-volume.vhd",
      "networkAccessPolicy": "AllowAll",
      "osType": null,
      "provisioningState": "Succeeded",
      "resourceGroup": "sharedblock-rg",
      "shareInfo": null,
      "sku": {
        "name": "Premium_LRS",
        "tier": "Premium"
      },
      "tags": {},
      "timeCreated": "2020-08-27T15:36:56.263382+00:00",
      "type": "Microsoft.Compute/disks",
      "uniqueId": "cd8b0a25-6fbe-4779-9312-8d9cbb89b6f2",
      "zones": null
    }
    ```

2.  Verify the [shared block volume](https://learn.microsoft.com/en-us/cli/azure/disk?view=azure-cli-latest#az_disk_show):

    ``` {.language-plaintext tabindex="-1"}
    $ az disk show -g <resource_group> -n <shared_block_volume_name>
    ```

    For example, the following command shows details for the shared block volume `shared-block-volume.vhd`{.literal} within the resource group `sharedblock-rg`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    $ az disk show -g sharedblock-rg -n shared-block-volume.vhd
    ```

    ``` {.language-plaintext tabindex="-1"}
    {
      "creationData": {
        "createOption": "Empty",
        "galleryImageReference": null,
        "imageReference": null,
        "sourceResourceId": null,
        "sourceUniqueId": null,
        "sourceUri": null,
        "storageAccountId": null,
        "uploadSizeBytes": null
      },
      "diskAccessId": null,
      "diskIopsReadOnly": null,
      "diskIopsReadWrite": 5000,
      "diskMbpsReadOnly": null,
      "diskMbpsReadWrite": 200,
      "diskSizeBytes": 1099511627776,
      "diskSizeGb": 1024,
      "diskState": "Unattached",
      "encryption": {
        "diskEncryptionSetId": null,
        "type": "EncryptionAtRestWithPlatformKey"
      },
      "encryptionSettingsCollection": null,
      "hyperVgeneration": "V1",
      "id": "/subscriptions/12345678910-12345678910/resourceGroups/sharedblock-rg/providers/Microsoft.Compute/disks/shared-block-volume.vhd",
      "location": "westcentralus",
      "managedBy": null,
      "managedByExtended": null,
      "maxShares": 3,
      "name": "shared-block-volume.vhd",
      "networkAccessPolicy": "AllowAll",
      "osType": null,
      "provisioningState": "Succeeded",
      "resourceGroup": "sharedblock-rg",
      "shareInfo": null,
      "sku": {
        "name": "Premium_LRS",
        "tier": "Premium"
      },
      "tags": {},
      "timeCreated": "2020-08-27T15:36:56.263382+00:00",
      "type": "Microsoft.Compute/disks",
      "uniqueId": "cd8b0a25-6fbe-4779-9312-8d9cbb89b6f2",
      "zones": null
    }
    ```

3.  Create three [network interfaces](https://learn.microsoft.com/en-us/cli/azure/network/nic?view=azure-cli-latest#az_network_nic_create). Run the following command three times by using a different `<nic_name>`{.literal} for each node:

    ``` {.language-plaintext tabindex="-1"}
    $ az network nic create \ -g <resource_group> \ -n <nic_name> \ --subnet <subnet_name> \ --vnet-name <virtual_network> \ --location <location> \ --network-security-group <network_security_group> \ --private-ip-address-version IPv4
    ```

    For example, the following command creates a network interface with the name `shareblock-nodea-vm-nic-protected`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    $ az network nic create \ -g sharedblock-rg \ -n sharedblock-nodea-vm-nic-protected \ --subnet sharedblock-subnet-protected \ --vnet-name sharedblock-vn \ --location westcentralus \ --network-security-group sharedblock-nsg \ --private-ip-address-version IPv4
    ```

4.  Create three VMs and attach the shared block volume. Option values are the same for each VM except that each VM has its own `<vm_name>`{.literal}, `<new_vm_disk_name>`{.literal}, and `<nic_name>`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ az vm create \ -n <vm_name> \ -g <resource_group> \ --attach-data-disks <shared_block_volume_name> \ --data-disk-caching None \ --os-disk-caching ReadWrite \ --os-disk-name <new_vm_disk_name> \ --os-disk-size-gb <disk_size> \ --location <location> \ --size <virtual_machine_size> \ --image <image_name> \ --admin-username <vm_username> \ --authentication-type ssh \ --ssh-key-values <ssh_key> \ --nics <nic_name> \ --availability-set <availability_set> \ --ppg <proximity_placement_group>
    ```

    For example, the following command creates a VM named `sharedblock-nodea-vm`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ az vm create \ -n sharedblock-nodea-vm \ -g sharedblock-rg \ --attach-data-disks shared-block-volume.vhd \ --data-disk-caching None \ --os-disk-caching ReadWrite \ --os-disk-name sharedblock-nodea-vm.vhd \ --os-disk-size-gb 64 \ --location westcentralus \ --size Standard_D2s_v3 \ --image /subscriptions/12345678910-12345678910/resourceGroups/sample-azureimagesgroupwestcentralus/providers/Microsoft.Compute/images/sample-azure-rhel-10.3.0-20200713.n.0.x86_64 \ --admin-username sharedblock-user \ --authentication-type ssh \ --ssh-key-values @sharedblock-key.pub \ --nics sharedblock-nodea-vm-nic-protected \ --availability-set sharedblock-as \ --ppg sharedblock-ppg
    ```

    ``` {.language-plaintext tabindex="-1"}
    {
      "fqdns": "",
      "id": "/subscriptions/12345678910-12345678910/resourceGroups/sharedblock-rg/providers/Microsoft.Compute/virtualMachines/sharedblock-nodea-vm",
      "location": "westcentralus",
      "macAddress": "00-22-48-5D-EE-FB",
      "powerState": "VM running",
      "privateIpAddress": "198.51.100.3",
      "publicIpAddress": "",
      "resourceGroup": "sharedblock-rg",
      "zones": ""
    }
    ```

**Verification**

1.  For each VM in your cluster, verify that the block device is available. To do so, connect to the vm by using the `ssh`{.literal} command with your VM's IP address:

    ``` {.language-plaintext tabindex="-1"}
    # ssh <ip_address> "hostname ; lsblk -d | grep ' 1T '"
    ```

    For example, the following command lists details including the hostname and block device for the VM IP `198.51.100.3`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # ssh 198.51.100.3 "hostname ; lsblk -d | grep ' 1T '"
    ```

    ``` {.language-plaintext tabindex="-1"}
    nodea
    sdb    8:16   0    1T  0 disk
    ```

2.  Use the `ssh`{.literal} utility to verify that each VM in your cluster uses the same shared disk:

    ``` {.language-plaintext tabindex="-1"}
    # ssh <ip_address> "hostname ; lsblk -d | grep ' 1T ' | awk '{print \$1}' | xargs -i udevadm info --query=all --name=/dev/{} | grep '^E: ID_SERIAL='"
    ```

    For example, the following command lists details including the hostname and shared disk volume ID for the instance IP address `198.51.100.3`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # ssh 198.51.100.3 "hostname ; lsblk -d | grep ' 1T ' | awk '{print \$1}' | xargs -i udevadm info --query=all --name=/dev/{} | grep '^E: ID_SERIAL='"
    ```

    ``` {.language-plaintext tabindex="-1"}
    nodea
    E: ID_SERIAL=3600224808dd8eb102f6ffc5822c41d89
    ```

    After you verify that each VM connects to the shared disk, you can configure resilient storage for the cluster.

**Additional resources**

-   [Shared Azure disks](https://learn.microsoft.com/en-us/azure/virtual-machines/disks-shared)
-   [Resource group](https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-cli#create-a-resource-group-and-a-virtual-network)
-   [Virtual network](https://learn.microsoft.com/en-us/azure/virtual-network/quick-create-cli#create-a-resource-group-and-a-virtual-network)
-   [Network security group(s)](https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group)
-   [Network security group rules](https://learn.microsoft.com/en-us/azure/virtual-network/manage-network-security-group#view-details-of-a-network-security-group)
-   [Subnet(s)](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-manage-subnet)
-   [Load balancer (optional)](https://learn.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-portal?tabs=option-1-create-load-balancer-standard)
-   [Storage account](https://learn.microsoft.com/en-us/cli/azure/storage/account?view=azure-cli-latest#az_storage_account_create)
-   [Proximity placement group](https://learn.microsoft.com/en-us/cli/azure/ppg?view=azure-cli-latest#az_ppg_create)
-   [Availability set](https://learn.microsoft.com/en-us/cli/azure/vm/availability-set?view=azure-cli-latest#az_vm_availability_set_create)

**Additional resources**

-   [Available RHEL image types for public cloud](#available-rhel-image-types-for-public-cloud "3.1. Available RHEL image types for public cloud")

## [Chapter 5. Configuring RHEL on Azure with Secure Boot](#configuring-rhel-on-azure-with-secure-boot) {#chapter-5.-configuring-rhel-on-azure-with-secure-boot .title}

To enhance boot security for a Red Hat Enterprise Linux (RHEL) instance on Microsoft Azure, configure Secure Boot. Secure Boot verifies the digital signatures of the boot loader and other components at startup, allowing only trusted programs to load while blocking unauthorized ones.

Publicly available RHEL images on the Azure platform include Secure Boot by default. The Allowed Signature database (`db`{.literal}) has Microsoft certificates. When you register a new image version in the `Azure Compute Gallery`{.literal}, you can add custom certificates to the UEFI Secure Boot variables.

### [5.1. Overview of Secure Boot for RHEL on cloud](#overview-of-secure-boot-for-rhel-on-cloud) {#overview-of-secure-boot-for-rhel-on-cloud .title}

When Secure Boot detects any tampered components or components signed by untrusted entities, it aborts the boot process. This is where it is different from traditional boot processes. Secure Boot plays a critical role in configuring Confidential Virtual Machines (CVMs).

It ensures that only trusted entities participate in the boot chain. Secure Boot is a Unified Extensible Firmware Interface (UEFI) feature. It verifies digital signatures of boot components, such as the boot loader and kernel, against trusted keys stored in hardware.

Secure Boot prevents unauthorized or tampered software from running during boot, protecting your system from malicious code. It also:

-   Authenticates access to specific device paths through defined interfaces
-   Enforces the use of the latest configuration
-   Permanently overwrites earlier configurations

When the Red Hat Enterprise Linux (RHEL) kernel boots with Secure Boot enabled, it enters the lockdown mode. In this mode, only kernel modules signed by a trusted vendor can load. Therefore, Secure Boot strengthens the security of the operating system boot sequence.

Secure Boot components

:   

The Secure Boot mechanism consists of firmware, signature databases, cryptographic keys, boot loader, hardware modules, and the operating system. The following are the components of the UEFI trusted variables:

-   Key Exchange Key database (KEK): An exchange of public keys to establish trust between the RHEL operating system and the VM firmware. You can also update Allowed Signature database (`db`{.literal}) and Forbidden Signature database (`dbx`{.literal}) by using these keys.

-   Platform Key database (PK): A self-signed single-key database to establish trust between the VM firmware and the cloud platform. The PK also updates the KEK database.

-   Allowed Signature database (`db`{.literal}): A database that maintains a list of certificates or binary hashes. These define whether binary files can boot on the system. Additionally, all certificates from `db`{.literal} are imported to the `.platform`{.literal} keyring of the RHEL kernel. With this feature, you can add and load signed third-party kernel modules in lockdown mode.

-   Forbidden Signature database (`dbx`{.literal}): A database that maintains a list of certificates or binary hashes that are not allowed to boot on the system.

    Note

    Binary files check against the `dbx`{.literal} database and the Secure Boot Advanced Targeting (SBAT) mechanism. With SBAT, you can revoke older versions of specific binaries by keeping the certificate that has signed binaries as valid.

Secure Boot stages

:   

When a RHEL instance boots in the Unified Kernel Image (UKI) mode and with Secure Boot enabled, it interacts with the cloud service infrastructure. The steps are as follows:

1.  *Initialization*: When a RHEL instance boots, the cloud-hosted firmware initially boots and implements the Secure Boot mechanism.

2.  *Variable store initialization*: The firmware initializes UEFI variables from a variable store. This is a dedicated storage area for information that firmware needs to manage the boot process and runtime operations. When the RHEL instance boots for the first time, the store initializes from default values associated with the VM image.

3.  *Boot loader*: When booted, the firmware loads the first stage boot loader. For the RHEL instance in a x86 UEFI environment, the first stage boot loader is shim. The shim boot loader authenticates and loads the next stage of the boot process. It acts as a bridge between UEFI and GRUB.

    a.  The shim x86 binary in RHEL is signed by the `Microsoft Corporation UEFI CA 2011`{.literal} certificate.
    b.  RHEL instances use the shim binary to boot in the Secure Boot-enabled mode on various hardware and virtualized platforms.
    c.  Check that the platform has the default Microsoft certificates in its Allowed Signature database (`db`{.literal}).
    d.  The shim binary extends the list of trusted certificates with Red Hat Secure Boot CA and optionally, with Machine Owner Key (`MOK`{.literal}).

4.  *UKI*: The shim binary loads the RHEL UKI (the `kernel-uki-virt`{.literal} package). The corresponding certificate, `Red Hat Secure Boot Signing 504`{.literal} on the x86_64 architecture, signs the UKI.

    a.  You can find this certificate in the `redhat-sb-certs`{.literal} package. Red Hat Secure Boot CA signs this certificate, so the check succeeds.

5.  *UKI add-ons*: When using UKI `cmdline`{.literal} extensions, the RHEL kernel verifies their signatures against `db`{.literal}, `MOK`{.literal}, and shim certificates. This process ensures that either the operating system vendor, RHEL, or a user has signed the extensions.

When the RHEL kernel boots in Secure Boot mode, it enters lockdown mode.

After entering the lockdown mode, the RHEL kernel performs the following actions:

-   Adds `db`{.literal} keys to the `.platform`{.literal} keyring.
-   Adds `MOK`{.literal} keys to the `.machine`{.literal} keyring.

During the kernel build process, the build system uses an ephemeral key pair, consisting of a private and a public key. The build system signs standard RHEL kernel modules, such as `kernel-modules-core`{.literal}, `kernel-modules`{.literal}, and `kernel-modules-extra`{.literal}.

After each kernel build, the private key becomes obsolete for signing third-party modules. You can use certificates from `db`{.literal} and `MOK`{.literal} for this purpose.

**Additional resources**

-   [UEFI shim boot loader secure boot life-cycle improvements](https://github.com/rhboot/shim/blob/main/SBAT.md)
-   [Red Hat Enterprise Linux and Secure Boot in cloud](https://www.redhat.com/en/blog/red-hat-enterprise-linux-and-secure-boot-cloud)

### [5.2. Configuring a RHEL VM on Azure with Secure Boot](#configuring-a-rhel-vm-on-azure-with-secure-boot) {#configuring-a-rhel-vm-on-azure-with-secure-boot .title}

To ensure that your Red Hat Enterprise Linux (RHEL) instance on the Azure cloud platform has a secured booting process, use the Secure Boot mechanism. You can configure the Secure Boot during registration of a custom RHEL Azure image.

**Prerequisites**

-   You have enabled the `Enable secure boot`{.literal} option under the `Configure security features`{.literal} setting when creating a VM by using the GUI.

-   You have installed the packages:

    -   `python3`{.literal}
    -   `openssl`{.literal}
    -   `efivar`{.literal}
    -   `keyutils`{.literal}
    -   `python3-virt-firmware`{.literal}

-   You have installed the `azure-cli`{.literal} utility. For details, see [Installing the Azure CLI on Linux](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=dnf).

    Note

    This image consists of pre-stored Unified Extensible Firmware Interface (UEFI) variables. Therefore, VMs launched from this image use the Secure Boot mechanism with the required variables on the first boot. Microsoft Azure supports Secure Boot with Trusted Launch VMs. These VMs offer security mechanisms to protect against rootkits and bootkits, while providing additional features such as Virtual Trusted Platform Manager (vTPM).

**Procedure**

1.  Generate a custom certificate `custom_db.cer`{.literal} by using the `openssl`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl req -quiet \
    -newkey rsa:4096 \
    -nodes -keyout custom_db.key \
    -new -x509 \
    -sha256 -days 3650 \
    -subj "/CN=Signature Database key/" \
    --outform DER \
    -out custom_db.cer
    ```

2.  Convert the certificate into `base64`{.literal}-encoded format:

    ``` {.language-plaintext tabindex="-1"}
    $ echo `base64 -w0 custom_db.cer`
    ```

    ``` {.language-plaintext tabindex="-1"}
    MIIFIjCCAwqgAwIBAgITNf23J4k0d8c0NR ...
    ```

3.  Create and edit an `azure-example-template.json`{.literal} Azure Resource Manager (ARM) file for registering a new Azure Compute Gallery image version:

    ``` {.language-plaintext tabindex="-1"}
    $ vi azure-example-template.json
    ```

    ``` {.language-plaintext tabindex="-1"}
    {
        "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
        "contentVersion": "1.0.0.0",
        "resources": [
            {
                "type": "Microsoft.Compute/galleries/images/versions",
                "apiVersion": "2023-07-03",
                "name": "__<your compute gallery/your image definition/version>__",
                "location": "__<location of the VHD>__",
                "properties": {
                    "storageProfile": {
                        "osDiskImage": {
                            "source": {
                                "id": "__<your-storage-account-id>__",
                                "uri": "__<url-with-the-vhd>__"
                            },
                            "hostCaching": "ReadOnly"
                        }
                    },
                    "securityProfile": {
                        "uefiSettings": {
                            "signatureTemplateNames": [
                                "MicrosoftUefiCertificateAuthorityTemplate"
                            ],
                            "additionalSignatures": {
                                "db": [
                                    {
                                        "type": "x509",
                                        "value": [
                                            "__<base64 of custom_db.cer>__"
                                        ]
                                    }
                                ]
                            }
                        }
                    }
                }
            }
        ]
    }
    ```

4.  Use the `azure-cli`{.literal} utility to register the image version:

    ``` {.language-plaintext tabindex="-1"}
    $ az deployment group create --name <example_deployment> \
    --resource-group <example_resource_group> \
    --template-file <example_template.json>
    ```

5.  Reboot the instance from the Azure Portal.

**Verification**

1.  Check if the newly created RHEL instance has Secure Boot enabled:

    ``` {.language-plaintext tabindex="-1"}
    $ mokutil --sb-state
    ```

    ``` {.language-plaintext tabindex="-1"}
    SecureBoot enabled
    ```

2.  Use the `keyctl`{.literal} utility to verify the kernel keyring for the custom certificate:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo keyctl list %:.platform
    ```

    ``` {.language-plaintext tabindex="-1"}
    keys in keyring:
    ...
    586621657: ---lswrv 0 0
    asymmetric: _Signature Database key_: f064979641c24e1b935e402bdbc3d5c4672a1acc
    ...
    ```

**Additional resources**

-   [Trusted Launch in Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch)

### [5.3. Configure a RHEL VM on Azure with NoSignatureTemplate Secure Boot](#configuring-a-rhel-vm-on-azure-with-nosignaturetemplate-secure-boot) {#configure-a-rhel-vm-on-azure-with-nosignaturetemplate-secure-boot .title}

To secure an operating system booting process for Red Hat Enterprise Linux (RHEL) virtual machine (VM) on the Azure platform, you can use the NoSignatureTemplate setting. When you register a custom RHEL Azure image with Azure Compute Gallery, the launched VM uses the Secure Boot mechanism.

All publicly available RHEL images on the Azure platform have support for Secure Boot. By default, RHEL image contains the Allowed Signature database (`db`{.literal}) with Microsoft certificates. This custom image also registers the pre-stored Unified Extensible Firmware Interface (UEFI) variables to authenticate Secure Boot. With the suggested NoSignatureTemplate setting, the boot chain only loads the `Red Hat Secure Boot CA signed`{.literal} public key certificate. Additionally, it is possible to generate your own cryptographic key pair and add the public key to the SecureBoot `db`{.literal} database. With this key, you can sign your own compiled kernel modules and drivers. RHEL provides a shim package, which is also supported by Microsoft Azure. This package includes the signed shim binaries for both x86 and aarch64 architectures. These binaries are signed by both Microsoft and Red Hat. When a new RHEL image is registered with Azure Compute Gallery, you can specify UEFI Secure Boot variables on Microsoft Azure. By using NoSignatureTemplate, you can build the RHEL x86_64 images that can boot in the Secure Boot mode with `db`{.literal} and without Microsoft certificates.

**Prerequisites**

-   You have a RHEL VM image in `VHD`{.literal} format.

-   The image has the `shim-x64`{.literal} package version `16.1-4.el10`{.literal} or later.

-   You have installed the packages:

    -   `virt-sb-certs-26.6-1.el10.noarch`{.literal}
    -   `openssl`{.literal}
    -   `keyutils`{.literal}
    -   `pesign`{.literal}

-   You have installed the `azure-cli`{.literal} utility. For details, see [Installing the Azure CLI on Linux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/deploying_and_managing_rhel_on_microsoft_azure/deploying-a-rhel-image-as-a-compute-instance-on-azure#installing-the-azure-cli).

**Procedure**

1.  Create storage account and resource group, if not already exists:

    ``` {.language-plaintext tabindex="-1"}
    $ az storage account create \
      --name <example_storage_account> \
      --resource-group <example_resource_group> \
      --location <example_location> \
      --sku Standard_LRS \
      --kind StorageV2
    ```

2.  Create a container:

    ``` {.language-plaintext tabindex="-1"}
    $ az storage container create \
      --account-name <example_storage_account> \
      --name <example_container_name> \
      --auth-mode login
    ```

3.  Upload a virtual hard drive (VHD) to the container:

    ``` {.language-plaintext tabindex="-1"}
    $ az storage blob upload \
      --account-name <example_storage_account> \
      --container-name <example_container_name> \
      --name <example_vhd_name> \
      --file <example_vhd_filename> \
      --type page \
      --auth-mode key
    ```

4.  Create new Azure image gallery in the existing resource group:

    ``` {.language-plaintext tabindex="-1"}
    $ az sig create \
      --resource-group <example_resource_group> \
      --gallery-name <example_gallary_name> \
      --location <example_location>
    ```

    Important

    Use `SecurityType=TrustedLaunchSupported`{.literal} for creating image definition. Otherwise, following steps will not work.

5.  Create an image definition:

    ``` {.language-plaintext tabindex="-1"}
    $ az sig image-definition create \
     --resource-group <example_resource_group> \
     --gallery-name <example_gallary_name> \
     --gallery-image-definition <example_gallery_image_definition> \
     --publisher RedHat \
     --offer RHEL \
     --sku <example_sku> \
     --os-type Linux \
     --os-state Generalized \
     --hyper-v-generation V2 \
     --features SecurityType=TrustedLaunchSupported \
     --location <example_location>
    ```

6.  Generate a `base64`{.literal} representation of the Red Hat Platform Key (`PK`{.literal}) and Key Exchange Key (`KEK`{.literal}) by using the `openssl`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl x509 -in /usr/share/virt-sb-certs/redhat.com/rh-pk-kek-2014.pem \
    -inform PEM \
    --outform DER \
    -out - | base64 -w0
    ```

    ``` {.language-plaintext tabindex="-1"}
    MIIDoDCCAoigAwIBAgIJAP71iOjzlsDxMA0GCSqGSIb3DQEBCwUAMFExKzApBgNV ...
    ```

7.  Convert the `Red Hat UEFI CA 2024`{.literal} certificate into the `base64`{.literal}-encoded format:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl x509 -in /usr/share/virt-sb-certs/redhat.com/rh-uefi-2024.pem \
    -inform PEM \
    --outform DER \
    -out - | base64 -w0
    ```

    ``` {.language-plaintext tabindex="-1"}
    MIIEbDCCAtSgAwIBAgIJAKtScAz+alQnMA0GCSqGSIb3DQEBCwUAMEMxHTAbBgNV ...
    ```

8.  Create and edit an `azure-example-template.json`{.literal} Azure Resource Manager (ARM) file for registering a new Azure Compute Gallery image version:

    ``` {.language-plaintext tabindex="-1"}
    $ vi azure-example-template.json
    ```

    ``` {.language-plaintext tabindex="-1"}
    {
        "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",
        "contentVersion": "1.0.0.0",
        "resources": [
            {
                "type": "Microsoft.Compute/galleries/images/versions",
                "apiVersion": "2023-07-03",
                "name": "__<your compute gallery>__/__<your image definition>__/__<version>__",
                "location": "__<example_location>__",
                "properties": {
                    "storageProfile": {
                        "osDiskImage": {
                            "source": {
                                "storageAccountId": "__<your_storage_account_id>__",
                                "uri": "__<url_with_the_vhd>__"
                            },
                            "hostCaching": "ReadOnly"
                        }
                    },
                    "securityProfile": {
                        "uefiSettings": {
                            "signatureTemplateNames": [
                                "NoSignatureTemplate"
                            ],
                            "additionalSignatures": {
                                "PK": {
                                    "type": "x509",
                                    "value": [
                                        "__<base64_of_rh_pk_kek_2014.pem>__"
                                    ]
                                },
                                "KEK": [
                                    {
                                     "type": "x509",
                                     "value": [
                                         "__<base64_of_rh_pk_kek_2014.pem>__"
                                        ]
                                    }
                                ],
                                "db": [
                                    {
                                     "type": "x509",
                                     "value": [
                                            "__<base64_of_rh_uefi_2024.pem>__"
                                        ]
                                    }
                                ]
                            }
                        }
                    }
                }
            }
        ]
    }
    ```

9.  Use the `azure-cli`{.literal} utility to register the image version:

    ``` {.language-plaintext tabindex="-1"}
    $ az deployment group create --name <example_deployment> \
    --resource-group <example_resource_group> \
    --template-file <example_template.json>
    ```

10. Create the VM:

    ``` {.language-plaintext tabindex="-1"}
    $ az vm create \
     --resource-group <example_resource_group> \
     --name <example_vm_name> \
     --image "/subscriptions/<example_subscription_id>/resourceGroups/<example_resource_group>/providers/Microsoft.Compute/galleries/<example_gallery_name>/images/<example_gallery_image_definition>/versions/10.3.0" \
     --location <example_location> \
     --security-type TrustedLaunch \
     --enable-secure-boot true \
     --enable-vtpm true \
     --size Standard_D2s_v5 \
     --admin-username azureuser \
     --generate-ssh-keys
    ```

**Verification**

1.  Connect to the VM through SSH:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh azureuser@<example_public_ip_address>
    ```

2.  Check if the newly created RHEL instance has Secure Boot enabled:

    ``` {.language-plaintext tabindex="-1"}
    $ mokutil --sb-state
    ```

    ``` {.language-plaintext tabindex="-1"}
    SecureBoot enabled
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ mokutil --db | grep CN
    ```

    ``` {.language-plaintext tabindex="-1"}
    Issuer: CN=Red Hat UEFI CA 2024/emailAddress=secalert@redhat.com
    Subject: CN=Red Hat UEFI CA 2024/emailAddress=secalert@redhat.com
    ```

3.  Use the `keyctl`{.literal} utility to verify the kernel keyring for the Red Hat UEFI certificate:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo keyctl list %:.platform
    ```

    ``` {.language-plaintext tabindex="-1"}
    3 keys in keyring:
    ...
    668733663: ---lswrv     0     0 asymmetric: Red Hat UEFI CA 2024: 0ec07d6268fe359ce227e24168af0ede0c7a7ac3
    961086966: ---lswrv     0     0 asymmetric: Red Hat Secure Boot CA 8: e1c6c580aa1e21d585aad9bf20f3929e5ec1f08b
    233549574: ---lswrv     0     0 asymmetric: Red Hat Secure Boot CA 5: cc6fa5e72868ba494e939bbd680b9144769a9f8f
    ...
    ```

## [Chapter 6. Configuring RHEL on Public Cloud Platforms with Intel TDX](#configuring-rhel-on-public-cloud-platforms-with-intel-tdx) {#chapter-6.-configuring-rhel-on-public-cloud-platforms-with-intel-tdx .title}

To have a secure and isolated environment for your VM, use Intel Trust Domain Extensions (TDX) on Red Hat Enterprise Linux (RHEL) instances. It is available on public cloud platforms. Intel TDX is a security type of Confidential Virtual Machine (CVM).

### [6.1. Overview of Intel TDX](#overview-of-intel-tdx) {#overview-of-intel-tdx .title}

To enable secure boot process for your RHEL instance, use Intel Trust Domain Extensions (TDX).

Intel TDX advances the former Intel Software Guard Extensions (SGX) technology. SGX provides virtual machine (VM) isolation from hypervisors and cloud providers by creating secure memory regions called enclaves. Application code stored in enclaves has access to memory and data stored inside the enclave, making it inaccessible to outside entities. TDX is a hardware-based trusted execution environment (TEE).

TDX creates hardware-isolated VMs called Trusted Domains (TDs). TDs isolate VMs from virtual machine manager (VMM), hypervisors, other VMs, and the host. Only the VM can access its resources. This ensures TD VMs remain secure while using hypervisor and CPU resources. Data confidentiality and integrity are maintained.

The main difference between SGX and TDX is that SGX works at application level while TDX works at virtualization level by limiting hypervisor access.

Note

Before deploying Red Hat Enterprise Linux (RHEL) on a public cloud platform, always check with the corresponding cloud service provider for the support status and certification of the particular RHEL instance type.

The Intel TDX Secure Boot process

:   

To ensure that the VM is running in a trusted and secured environment, use Intel Trust Domain Extensions (TDX) on your Red Hat Enterprise Linux (RHEL) instance to use the Intel TDX Secure Boot process.

1.  **Initialization and measurement**: A TDX-enabled hypervisor sets the initial state of a VM.

    a.  This hypervisor loads the firmware binary file into the VM memory and sets the initial register state.
    b.  The Intel processor measures the initial state of the VM and provides details to verify the initial state of the VM.

2.  **Firmware**: The VM initiates the UEFI firmware. The firmware might include stateful or stateless Virtual Trusted Platform Module (vTPM) implementation.

    a.  Stateful vTPM maintains persistent cryptographic state across VM reboots and migrations.
    b.  Stateless vTPM generates fresh cryptographic state for each VM session without persistence.
    c.  Virtual Machine Privilege Levels (VMPL) technology isolates vTPM from the guest. VMPL offers hardware-enforced privilege isolation between different VM components and the hypervisor.

3.  **vTPM**: Depending on your cloud service provider, for stateful vTPM implementation, the UEFI firmware might perform a remote attestation to decrypt the persistent state of vTPM.

    a.  The vTPM also gathers data about the boot process, such as Secure Boot state, certificates used for signing boot artifacts, or UEFI binary hashes.

4.  **Shim** : When the UEFI firmware finishes the initialization process, it searches for the extended firmware interface (EFI) system partition.

    a.  Then, the UEFI firmware verifies and runs the first stage boot loader from there.
    b.  For RHEL, this is `shim`{.literal}. The `shim`{.literal} program allows non-Microsoft operating systems to load the second stage boot loader from the EFI system partition.
    c.  `shim`{.literal} uses a Red Hat certificate to verify the second stage boot loader (`grub`{.literal}) or Red Hat Unified Kernel Image (UKI).
    d.  `grub`{.literal} or `UKI`{.literal} unpacks, verifies, and runs Linux kernel and initramfs, and the kernel command line. This process ensures that the Linux kernel is loaded in a trusted and secured environment.

5.  **Initramfs**: In initramfs, vTPM information automatically unlocks the encrypted root partition in case of full disk encryption technology.

    a.  When the root volume becomes available, `initramfs`{.literal} transfers the execution flow there.

6.  **Attestation**: The VM tenant gets access to the system and can perform a remote attestation to ensure that the accessed VM is an untampered Confidential Virtual Machine (CVM).

    a.  Attestation is performed based on information from the Intel processor and vTPM.
    b.  This process confirms the authenticity and reliability of the initial CPU and memory state of the RHEL instance and Intel processor.

7.  **TEE**: This process creates a Trusted Execution Environment (TEE) to ensure that booting of the VM is in a trusted and secured environment.

### [6.2. Configuring a RHEL VM on Azure with Intel TDX](#configuring-a-rhel-vm-on-azure-with-intel-tdx) {#configuring-a-rhel-vm-on-azure-with-intel-tdx .title}

By using Intel Trusted Domain Extensions (TDX), you can create hardware-assisted isolated VMs known as trusted domains (TDs). It ensures that only the VM has access to its resources, while remaining inaccessible to hypervisors and hosts.

**Prerequisites**

-   You have installed the `openssh`{.literal} and `openssh-clients`{.literal} packages.
-   You have installed the Azure CLI utility. For details, see [Installing the Azure CLI on Linux](#installing-the-azure-cli "3.4. Installing the Azure CLI").
-   You have launched the RHEL instance from a supported Azure instance type.

**Procedure**

1.  Log in to Azure by using the Azure CLI utility:

    ``` {.language-plaintext tabindex="-1"}
    $ az login
    ```

2.  Create an Azure resource group for the selected availability zone:

    ``` {.language-plaintext tabindex="-1"}
    $ az group create --name <example_resource_group> --location westeurope
    ```

3.  Deploy a RHEL instance with TDX enabled, for example, the `Standard_DC2eds_v5`{.literal} instance type:

    ``` {.language-plaintext tabindex="-1"}
    $ az vm create --resource-group <example_resource_group> \
    --name <example_rhel_instance> \
    --image <"RedHat:rhel-cvm:10_0_cvm:latest"> \
    --size <Standard_DC2eds_v5> \
    --admin-username <example_azure_user> \
    --generate-ssh-keys \
    --security-type ConfidentialVM \
    --os-disk-security-encryption-type DiskWithVMGuestState
    ```

4.  Connect to the RHEL instance:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh <example_azure_user>@<example_ip_address_of_the_instance>
    ```

**Verification**

-   Check kernel logs to verify status of TDX:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dmesg | grep -i tdx
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    [    0.733613] Memory Encryption Features active: Intel TDX
    [    4.320222] systemd[1]: Detected confidential virtualization tdx.
    [    5.977432] systemd[1]: Detected confidential virtualization tdx.
    ...
    ```

-   Check metadata of the RHEL instance configuration:

    ``` {.language-plaintext tabindex="-1"}
    $ az vm show --resource-group <example_resource_group> \
    --name <example_rhel_instance> \
    --query "securityProfile.enableTrustedDomainExtensions" \
    --output json
    ```

**Additional resources**

-   [Azure Confidential VM options](https://learn.microsoft.com/en-us/azure/confidential-computing/virtual-machine-options#sizes)

## [Chapter 7. Configuring RHEL on Public Cloud Platforms with AMD SEV SNP](#configuring-rhel-on-public-cloud-platforms-with-amd-sev-snp) {#chapter-7.-configuring-rhel-on-public-cloud-platforms-with-amd-sev-snp .title}

To prevent VM integrity-based attacks and reduce memory integrity violations, configure AMD Secure Encrypted Virtualization with Secure Nested Paging (SEV-SNP) on Red Hat Enterprise Linux (RHEL) instances on public cloud. AMD SEV-SNP isolates VM data from the hypervisor and cloud service provider.

### [7.1. Overview of AMD SEV SNP](#overview-of-amd-sev-snp) {#overview-of-amd-sev-snp .title}

AMD Secure Encrypted Virtualization with Secure Nested Paging (SEV-SNP) aims at improving security of virtual machines (VMs) and data stored in them on public cloud platforms.

AMD processors offer three hardware-based security mechanisms: SEV, SEV-ES, and SEV-SNP.

-   **SEV**: The SEV mechanism encrypts virtual machine (VM) memory to prevent the hypervisor from accessing VM data.
-   **SEV-ES**: SEV with Encrypted State (SEV-ES) extends SEV by encrypting CPU register states. This mechanism prevents the hypervisor from accessing or modifying VM CPU registers. Despite providing isolation between hypervisor and VM, it is still vulnerable to memory integrity attacks.
-   **SEV-SNP**: SEV-SNP is an enhancement to SEV-ES that adds memory integrity protection along with VM encryption. This mechanism prevents the hypervisor from modifying page tables to redirect VM memory access. It protects against replay attacks and memory tampering.

SEV SNP components

:   

-   **Secure Processor**: The AMD `EPYC`{.literal} processor integrates a Secure Processor (SP) subsystem. The AMD SP is a dedicated hardware component to manage keys and encryption operations.

-   **Memory Integrity**: The memory management unit (MMU) utilizes page tables to translate virtual addresses to guest-physical addresses.

    -   SEV-SNP uses nested page tables for translating guest-physical addresses to host-physical addresses.
    -   Once defined, nested page tables cannot be altered by the hypervisor or the host. This prevents VM access to different pages, protecting memory integrity.
    -   SEV-SNP uses this method to offer protection against replay attacks, memory integrity violations, and malicious modifications to VM memory.

-   **Memory Encryption**: The AMD `EPYC`{.literal} processor hides the memory encryption key, which remains hidden from both host and VM.

-   **Attestation report for verification**: A CPU-generated report contains RHEL instance information in an authorized cryptographic format. This report confirms the authenticity and reliability of the initial CPU and memory state of the RHEL instance and AMD processor.

    Note

    Even if a hypervisor creates the primary memory and CPU register state of the VM, they remain hidden and inaccessible to the hypervisor after initialization of that VM.

The AMD SEV SNP Secure Boot process

:   

1.  **Initialization and measurement**: A SEV-SNP enabled hypervisor sets the initial state of a VM.

    a.  This hypervisor loads firmware binary into the VM memory and sets the initial register state.
    b.  AMD Secure Processor (SP) measures the initial state of the VM and provides details to verify the initial state of the VM.

2.  **Firmware**: The VM initiates the UEFI firmware. The firmware might include either stateful or stateless Virtual Trusted Platform Module (vTPM) implementation.

    a.  Stateful vTPM maintains persistent cryptographic state across VM reboots and migrations.
    b.  Stateless vTPM generates a new cryptographic state for each VM session without persistence.
    c.  Virtual Machine Privilege Levels (VMPL) technology isolates vTPM from the guest.
    d.  VMPL offers hardware-enforced privilege isolation between different VM components and the hypervisor.

3.  **vTPM**: For stateful vTPM implementation, the UEFI firmware might perform remote attestation.

    a.  This depends on your cloud service provider. The attestation decrypts the persistent state of vTPM.

    b.  vTPM also measures facts about the boot process

        -   Secure Boot state
        -   Certificates used for signing boot artifacts
        -   UEFI binary hashes

4.  **Shim**: When the UEFI firmware finishes the initialization process, it searches for the extended firmware interface (EFI) system partition.

    a.  The UEFI firmware verifies and executes the first stage boot loader from there.
    b.  For RHEL, this is `shim`{.literal}. The `shim`{.literal} program allows non-Microsoft operating systems to load the second stage boot loader from the EFI system partition.
    c.  `shim`{.literal} uses a Red Hat certificate to verify the second stage boot loader (`grub`{.literal}) or Red Hat Unified Kernel Image (UKI).
    d.  `grub`{.literal} or `UKI`{.literal} unpacks, verifies, and executes Linux kernel and initial RAM filesystem (`initramfs`{.literal}), and the kernel command line.
    e.  This process ensures that the Linux kernel loads in a trusted and secured environment.

5.  **Initramfs**: In `initramfs`{.literal}, vTPM information automatically unlocks the encrypted root partition in case of full disk encryption technology.

    a.  When the root volume becomes available, `initramfs`{.literal} transfers the execution flow to the root volume.

6.  **Attestation**: The VM tenant gets access to the system. They can perform remote attestation to ensure the VM is an untampered Confidential Virtual Machine (CVM).

    a.  Attestation is performed based on information from the AMD SP and vTPM.
    b.  This process confirms the authenticity and reliability of the initial CPU and memory state of the RHEL instance and the AMD processor.

7.  **TEE**: This process creates a Trusted Execution Environment (TEE) to ensure that booting of the VM is in a trusted and secured environment.

**Additional resources**

-   [Confidential Guest Reset: QEMU Hypervisor Design Choices and Approach](https://www.redhat.com/en/blog/confidential-guest-reset-qemu-hypervisor-design-choices-and-approach)
-   [AMD SEV documentation](https://www.amd.com/en/developer/sev.html)
-   [Google Cloud Confidential Computing Root of Trust](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/attestation-overview#root-of-trust)

### [7.2. Configuring a RHEL VM on Azure with AMD SEV SNP](#configuring-a-rhel-vm-on-azure-with-amd-sev-snp) {#configuring-a-rhel-vm-on-azure-with-amd-sev-snp .title}

You can configure AMD Secure Encrypted Virtualization with Secure Nested Paging (SEV-SNP) on RHEL VMs on Azure to create a trusted boot environment. SEV-SNP protects your data from access by the hypervisor and cloud service provider, and is available only for AMD EPYC processor family.

**Prerequisites**

-   You have installed the `openssh`{.literal} and `openssh-clients`{.literal} packages.
-   You have installed the Azure CLI utility. For details, see [installing the Azure CLI](#installing-the-azure-cli "3.4. Installing the Azure CLI").
-   You have created an Azure virtual machine (VM) that uses a supported AMD EPYC processor-based machine type.

**Procedure**

1.  Log in to Azure by using the Azure CLI utility:

    ``` {.language-plaintext tabindex="-1"}
    $ az login
    ```

2.  Create an azure resource group for the selected availability zone:

    ``` {.language-plaintext tabindex="-1"}
    $ az group create --name <example_resource_group> --location eastus
    ```

3.  Deploy a RHEL instance with SEV-SNP, for example, the `Standard_DC4as_V5`{.literal} instance type:

    ``` {.language-plaintext tabindex="-1"}
    $ az vm create --resource-group <example_resource_group> \
    --name <example-rhel-10-sev-snp-instance> \
    --image <RedHat:rhel:10_x64_Gen2:latest> \
    --size <Standard_DC4as_V5> \
    --admin-username <example_azure_user> \
    --generate-ssh-keys \
    --security-type ConfidentialVM \
    --os-disk-security-encryption-type DiskWithVMGuestState
    ```

4.  Connect to the RHEL instance:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh <example_azure_user>@<example_ip_address_of_VM>
    ```

**Verification**

-   Check kernel logs to verify status of SEV-SNP:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dmesg | grep -i sev
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    [    0.547223] Memory Encryption Features active: AMD SEV
    [    4.843171] kvm-guest: setup_efi_kvm_sev_migration : EFI live migration variable not found
    ...
    ```

**Additional resources**

-   [Supported VM sizes for Confidential Virtual Machine](https://learn.microsoft.com/en-us/azure/confidential-computing/confidential-vm-overview#size-support)

## [Chapter 8. Configuring RHEL on Public Cloud Platforms with UKI](#configuring-rhel-on-public-cloud-platforms-with-uki) {#chapter-8.-configuring-rhel-on-public-cloud-platforms-with-uki .title}

To ensure that a Red Hat Enterprise Linux (RHEL) instance has a secured boot process from an untrusted storage, use Unified Kernel Image (UKI). This applies to Confidential Virtual Machines (CVMs) on public cloud platforms.

### [8.1. Overview of Unified Kernel Image](#overview-of-uki) {#overview-of-unified-kernel-image .title}

To extend the secure boot protection throughout the entire boot chain, use Unified Kernel Image (UKI).

UKI components

:   

Unified Kernel Image (UKI) is a Unified Extensible Firmware Interface (UEFI) Portable Executable (PE) binary. It bundles together the essential components of an operating system for the UEFI environment. UKI binary components extend the Secure Boot coverage by including the `initramfs`{.literal} and the kernel command line. `Initramfs`{.literal} is part of the Linux startup process. The kernel command line gives you limited access to define parameters. The primary components contained within the UKI binary are:

-   The `.linux`{.literal} section stores the Linux kernel image.
-   The `.initrd`{.literal} section stores the initial RAM filesystem `initramfs`{.literal}.
-   The `.cmdline`{.literal} section stores the kernel command line.
-   Additional sections, such as `.sbat`{.literal}.
-   The Red Hat signature.

Features of RHEL UKI with pre-built `initramfs`{.literal}

:   

-   Prohibits any malicious agent or component to alter any objects in the boot chain.
-   Due to pre-built `initramfs`{.literal}, the user does not need to build its custom `initramfs`{.literal}, which results in a faster kernel installation.
-   Provides support for the pre-built `initramfs`{.literal} systems as it is similar in all installations such as virtual machine (VMs), containers, or cloud instances.
-   Provides support for the `x86_64`{.literal} architecture.
-   Includes the `kernel-uki-virt`{.literal} package.
-   Built for virtual machines and cloud instances.

Limitation of UKI because of the reduced flexibility of the boot process

:   

-   When building the UKI, the operating system vendor creates `initramfs`{.literal}. As a consequence, the listed and included kernel modules are static. You can use the `systemd`{.literal} system and configuration extensions to address this limitation.
-   The kernel command line parameters are static, which limits the use of parameters for different instance sizes or debugging options.

You can use the UKI command line extensions to overcome this limitation.

The UKI Secure Boot process

:   

To protect your system against unauthorized boot-time modifications, use the secure boot mechanism with Unified Kernel Image (UKI). When using UKI with secure boot, the system verifies each component in the boot chain to ensure system integrity and prevent malicious code execution. Secure boot process for Red Hat Enterprise Linux (RHEL) on cloud is as follows:

1.  **UEFI Firmware**: The boot process starts from the Unified Extensible Firmware Interface (UEFI) firmware.

    a.  For boot, Red Hat Enterprise Linux (RHEL) UKI requires UEFI firmware, because legacy basic input/output system (BIOS) firmware is not supported.

2.  **Shim boot loader**: Use the `shim`{.literal} boot loader for booting rather than directly booting the UKI (a PE binary) from the UEFI firmware.

    a.  `shim`{.literal} includes additional security mechanisms such as Machine Owner Key (`MOK`{.literal}) and Secure Boot Advanced Targeting (SBAT).

3.  **Signature verification (Secure Boot UEFI mechanism)**: During boot, `shim`{.literal} reads the UKI binary and the secure boot UEFI mechanism verifies the signature of UKI.

    a.  This signature verification is against trusted keys stored in the Secure Boot Allowed Signature Database (`db`{.literal}) of the system, the `MOK`{.literal} database, and the built-in database of the `shim`{.literal} binary.
    b.  If the signature key is valid, the verification passes.

4.  **SBAT verification**: Immediately after signature verification, the `shim`{.literal} boot loader verifies the SBAT rules at startup.

    a.  During SBAT verification, the system compares generation numbers, for components such as `systemd.rhel`{.literal} or `linux.rhel`{.literal}, embedded in the UKI by using the `.sbat`{.literal} section against values in the `shim`{.literal} boot loader.

    b.  If the generation number for a component in the `shim`{.literal} is higher than the generation number in the UKI, the binary gets automatically discarded, even if it was signed by a trusted key.

        Note that the generation number is a version identifier for UEFI applications, such as `shim`{.literal} and `grub`{.literal}.

5.  **Unpacking and Execution**: If verification passes, control passes from `shim`{.literal} to the `systemd-stub`{.literal} code in the UKI to continue the boot process.

6.  **systemd-stub add-ons**: During execution, `systemd-stub`{.literal} unpacks and extracts the contents of the `.cmdline`{.literal} section, the plain text kernel command line, and the `.initrd`{.literal} section, the temporary root file system, for the boot process.

    Note that `systemd-stub`{.literal} reads UKI add-ons, which are also PE binaries, and verifies their signatures to safely extend the kernel command line of UKI by appending the `.cmdline`{.literal} content from add-ons. `systemd-stub`{.literal} reads add-ons from two locations:

    -   Global (UKI-independent) add-ons from the `/loader/addons/`{.literal} directory on the Extensible Firmware Interface (EFI) System Partition (ESP).
    -   Per-UKI add-ons from the `/EFI/Linux/<UKI-name>.extra.d/`{.literal} directory on the ESP.

7.  Control passes from `systemd-stub`{.literal} to the Linux kernel and the operating system boot process continues.

    From this point, secure boot with UKI mechanism follows the standard kernel boot process.

**Additional resources**

-   [Extending Red Hat Unified Kernel Images By Using Add-ons](https://www.redhat.com/en/blog/extending-red-hat-unified-kernel-images-using-addons)
-   [Boot Loader Specification](https://systemd.io/BOOT_LOADER_SPECIFICATION/)
-   [Unified Kernel Image specification](https://uapi-group.org/specifications/specs/unified_kernel_image/)

## [Legal Notice](#idm140065998123664) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
