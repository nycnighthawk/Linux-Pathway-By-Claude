---
{"title": "Deploying and managing RHEL on Amazon Web Services", "guide": "deploying_and_managing_rhel_on_amazon_web_services", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/deploying_and_managing_rhel_on_amazon_web_services/index", "retrieved": "2026-11-02", "license": "CC-BY-SA-3.0"}
---

# Deploying and managing RHEL on Amazon Web Services {#deploying-and-managing-rhel-on-amazon-web-services .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Obtaining Red Hat Enterprise Linux system images and creating RHEL instances on AWS {#obtaining-red-hat-enterprise-linux-system-images-and-creating-rhel-instances-on-aws .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140185698370224)

**Abstract**

To use Red Hat Enterprise Linux (RHEL) on Amazon Web Services (AWS), you can create and deploy RHEL system images.

This also involves:

-   Registering, deploying, and provisioning RHEL images on AWS

-   Managing networking configurations for RHEL AWS EC2 instances

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

    This document specifically addresses the process of deploying RHEL on AWS.

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

## [Chapter 2. Preparing and uploading AMI images to AWS](#preparing-and-uploading-ami-images-to-aws) {#chapter-2.-preparing-and-uploading-ami-images-to-aws .title}

You can create custom images and update them, either manually or automatically, on the AWS cloud with RHEL image builder.

### [2.1. Preparing to manually upload AWS AMI images](#preparing-to-manually-upload-aws-ami-images) {#preparing-to-manually-upload-aws-ami-images .title}

Before uploading an Amazon Machine Image (AMI) to Amazon Web Services (AWS), you must configure a system for uploading the images.

**Prerequisites**

-   A writable [S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html#creating-bucket) prepared.

-   AWS authentication configured using one of the following methods:

    -   **Static credentials**: An Access Key ID and Secret Access Key configured in the AWS IAM account manager. You must have an Access Key ID configured in the [AWS IAM account manager](https://aws.amazon.com/iam/).
    -   **Dynamic credentials**: Short-lived credentials managed by using AWS IAM Identity Center (SSO).

**Procedure**

1.  Install Python 3 and the `pip`{.literal} tool:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install python3 python3-pip
    ```

2.  Install the [AWS command-line tools](https://aws.amazon.com/cli/) with `pip`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ pip3 install awscli
    ```

3.  Configure your AWS CLI authentication profile:

    -   **Configuring static credentials (AWS Access Keys)**: The command line prompts you to provide your credentials, region, and output format:

        ``` {.language-plaintext tabindex="-1"}
        $ aws configure
        ```

        ``` {.language-plaintext tabindex="-1"}
        AWS Access Key ID [None]:
        AWS Secret Access Key [None]:
        Default region name [None]:
        Default output format [None]:
        ```

    -   **Configuring dynamic credentials (AWS SSO / IAM Identity Center)**: If your organization uses short-lived dynamic credentials, log in to a separate profile. If you are running the CLI over a remote SSH session, include the `--remote`{.literal} flag:

        ``` {.language-plaintext tabindex="-1"}
        $ aws login --region eu-central-1 --profile auth --remote
        ```

        Follow the prompt link to authenticate in your browser. This creates an entry in your `~/.aws/config`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        [profile auth]
        region = eu-central-1
        login_session = arn:aws:sts::12345678910:assumed-role/12345678910-admin/<username>
        ```

        Important

        `image-builder`{.literal} uses the AWS SDK for Go v2, which does not natively support dynamic credentials. If you attempt to upload by using only the profile above, the credentials are silently ignored, resulting in the following error: \"Getting: operation error S3: CreateMultipartUpload, get identity: get credentials: failed to refresh cached credentials, no EC2 IMDS role found...​\" To bypass this limitation, configure your `[default]`{.literal} or another designated profile to use `credential_process`{.literal}. This maps the dynamic session tokens to static-style credentials that `image-builder`{.literal} can read. Add the following to your `~/.aws/config`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        [default]
        region = eu-central-1
        credential_process = aws configure export-credentials --profile auth --format process
        ```

4.  Define a name for your bucket and create a bucket:

    ``` {.language-plaintext tabindex="-1"}
    $ BUCKET=<bucketname>
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ aws s3 mb s3://$BUCKET
    ```

    Replace *`<bucketname>`{.literal}* with the actual bucket name. It must be a globally unique name.

5.  To grant Simple Storage Service (S3) access permission, create a `vmimport`{.literal} role in the AWS Identity and Access Management (IAM), if not already.

    a.  Create a `trust-policy.json`{.literal} file with the trust policy configuration in JSON format. For example:

        ``` {.language-plaintext tabindex="-1"}
        {
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": {
                    "Service": "vmie.amazonaws.com"
                },
                "Action": "sts:AssumeRole",
                "Condition": {
                    "StringEquals": {
                        "sts:Externalid": "vmimport"
                    }
                }
            }]
        }
        ```

    b.  Create a `role-policy.json`{.literal} file with the role policy configuration in JSON format:

        ``` {.language-plaintext tabindex="-1"}
        {
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Action": ["s3:GetBucketLocation", "s3:GetObject", "s3:ListBucket"],
                "Resource": ["arn:aws:s3:::%s", "arn:aws:s3:::%s/"] }, { "Effect": "Allow", "Action": ["ec2:ModifySnapshotAttribute", "ec2:CopySnapshot", "ec2:RegisterImage", "ec2:Describe"],
                "Resource": "*"
            }]
        }
        ```

        ``` {.language-plaintext tabindex="-1"}
        $BUCKET $BUCKET
        ```

    c.  Create a role for your Amazon Web Services account, by using the `trust-policy.json`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        $ aws iam create-role --role-name vmimport --assume-role-policy-document \file://trust-policy.json
        ```

    d.  Embed an inline policy document by using the `role-policy.json`{.literal} file:

        ``` {.language-plaintext tabindex="-1"}
        $ aws iam put-role-policy --role-name vmimport --policy-name vmimport --policy-document \file://role-policy.json
        ```

**Verification**

-   Verify the bucket was created:

    ``` {.language-plaintext tabindex="-1"}
    $ aws s3 ls | grep $BUCKET
    ```

-   Verify the `vmimport`{.literal} role was created:

    ``` {.language-plaintext tabindex="-1"}
    $ aws iam get-role --role-name vmimport
    ```

**Additional resources**

-   [Using high-level S3 commands with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html)
-   [Best practices for IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
-   [Security best practices for S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)

### [2.2. Manually uploading an AMI image to AWS by using the CLI](#manually-uploading-an-ami-image-to-aws-by-using-the-cli) {#manually-uploading-an-ami-image-to-aws-by-using-the-cli .title}

You can use RHEL image builder to build AMI images and manually upload them directly to the Amazon AWS Cloud service provider by using the CLI.

**Prerequisites**

-   You have created static or dynamic credentials by using the `credential_process`{.literal} workaround configured on the local system. See [Preparing to manually upload AWS AMI images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/preparing-and-uploading-ami-images-to-aws#preparing-to-manually-upload-aws-ami-images).
-   You have an `Access Key ID`{.literal} configured in the [AWS IAM](https://aws.amazon.com/iam/) account manager.
-   You have a writable [S3 bucket](https://aws.amazon.com/s3/) prepared.
-   You have a defined blueprint.

**Procedure**

1.  Build the image:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo image-builder build ami \
      --blueprint <blueprint_name> \
      --aws-region us-east-1 \
      --aws-bucket <example_bucket> \
      --aws-ami-name <image_name>
    ```

2.  Upload the image to AWS. For standalone raw images, use the upload command:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo image-builder upload rhel-10.1-ami-x86_64.raw \
    --to=aws --aws-region=eu-central-1 \
    --aws-bucket=<my_bucket> --aws-ami-name <image_name>
    ```

    If you configured dynamic credentials with the default profile workaround, the `upload`{.literal} command automatically uses the configured `credential_process`{.literal} flow.

**Verification**

1.  Check the image available [EC2](https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#Images:sort=name) in the AWS console and selecting the correct region.
2.  On the dashboard, select your image and click Launch.

**Troubleshooting**

-   If the build or upload command fails with an authentication or permission error, you must confirm that your AWS CLI profile has valid credentials and that your IAM user or role can access the S3 bucket and the EC2 VM Import/Export API.
-   If the command reports that the bucket is missing, not accessible, or in the wrong location, you must verify that the bucket name matches `--aws-bucket`{.literal} and that the bucket exists in the same AWS Region you pass to `--aws-region`{.literal}.
-   If AWS rejects the import with a service role error, you must create the `vmimport`{.literal} IAM role and trust policy that VM Import/Export requires, as described in [Required service role to import a VM](https://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html#vmimport-role).

**Additional resources**

-   [Required service role to import a VM](https://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html#vmimport-role)

### [2.3. Creating and automatically uploading images to the AWS Cloud AMI](#creating-and-automatically-uploading-images-to-the-aws-cloud-ami) {#creating-and-automatically-uploading-images-to-the-aws-cloud-ami .title}

You can create a RAW image by using the RHEL image builder and select **Upload to AWS** to automatically upload the image to the Amazon AWS Cloud AMI service provider.

**Prerequisites**

-   You must have `root`{.literal} or `wheel`{.literal} group user access to the system.
-   You have opened the RHEL image builder interface of the RHEL web console in a browser.
-   You have created a RHEL image builder blueprint.
-   You must have an Access Key ID configured in the AWS Identity and Access Management (IAM) account manager.
-   You must have a writable AWS Simple Storage Service (S3) bucket prepared.

**Procedure**

1.  In the RHEL image builder dashboard, select your blueprint in **blueprint name**. Select the **Images** tab, and click **Create Image**.

2.  From the **Type** drop-down menu list, select `Amazon Machine Image Disk (.raw)`{.literal}, check **Upload to AWS**, and click **Next**.

    Note

    If you do not know your `Secret Key`{.literal}, generate a new `Access Key ID`{.literal}.

3.  Enter your `AWS access key ID`{.literal} and `AWS secret access key`{.literal} in the corresponding fields. Click **Next**.

4.  Enter the `Image name`{.literal}, `Amazon S3 bucket`{.literal} name, and `AWS region`{.literal}, then click **Next**.

5.  Review the information and click **Finish**. Wait for the **Image build complete** status.

6.  In the AWS console, navigate to [Service→EC2](https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#Images:sort=name), select the correct region, and verify your image shows `Available`{.literal} status.

7.  Select your image, click **Launch**, choose an instance type, and click **Review and Launch**.

8.  Review instance details, select or create a key pair, click **Launch**, and wait for the instance status to change to **running**:

    -   To create a new key pair, select **Create a new key pair**, enter a name, and click **Download Key Pair**.

**Verification**

-   Connect to your instance by using SSH:

    ``` {.language-plaintext tabindex="-1"}
    $ chmod 400 <your_instance_name>.pem
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -i <your-instance_name>.pem \\
    ec2-user@<your-instance-IP-address>
    ```

    a.  Type `yes`{.literal} to confirm the connection.

-   Check if you can perform any actions while connected to your instance by using SSH.

**Additional resources**

-   [Open a case on Red Hat Customer Portal](https://access.redhat.com/support/cases/#/case/new/open-case?intcmp=hp%7Ca%7Ca3%7Ccase&caseCreate=true)
-   [Connecting to your Linux instance by using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)
-   [Required Permissions for IAM Users](https://docs.aws.amazon.com/vm-import/latest/userguide/vmie_prereqs.html#iam-permissions-image)
-   [Creating a blueprint in the web console interface](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/creating-system-images-with-cli#creating-a-blueprint-by-using-the-command-line-interface)
-   [AWS IAM account manager](https://aws.amazon.com/iam/)
-   [AWS S3 bucket](https://aws.amazon.com/s3/)

## [Chapter 3. Deploying a RHEL image as an EC2 instance on AWS](#deploying-a-rhel-image-as-an-ec2-instance-on-aws) {#chapter-3.-deploying-a-rhel-image-as-an-ec2-instance-on-aws .title}

To use a Red Hat Enterprise Linux (RHEL) image on Amazon Web Services (AWS), convert the RHEL image to an AWS-compatible format, Amazon Machine Image (AMI). Use RHEL image builder or manual configuration for customization. From an AMI, you can launch an Elastic Cloud Compute (EC2) instance.

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

To convert an *on-demand, license-included* EC2 instance to a *bring-your-own-license (BYOL)* EC2 instance of RHEL.

Important

You cannot convert an on-demand instance to a custom RHEL instance. For migrating from an on-demand image to a custom RHEL bring your own subscription (BYOS) image, do the following:

-   Create a new custom RHEL instance, then migrate data from your on-demand instance.
-   When you complete data migration, terminate the on-demand instance to avoid additional billing.

**Additional resources**

-   [Composing a Customized RHEL System Image](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/installing-rhel-image-builder)
-   [Red Hat Ecosystem Catalog](https://catalog.redhat.com/)
-   [Red Hat Cloud Access Reference Guide](https://www.redhat.com/en/technologies/cloud-computing/cloud-access)
-   [Red Hat Cloud Access program overview](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_rhel_system_registration/con-red-hat-cloud-access-program-overview)
-   [Convert a license type for Linux in License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/conversion-procedures-linux.html)
-   [Amazon Web Services Red Hat Ecosystem Catalogue](https://catalog.redhat.com/partners/detail/40acada9835742eeaf67fd43c5a7d559)
-   [Red Hat Enterprise Linux on Amazon EC2 FAQs](https://aws.amazon.com/partners/redhat/faqs/)

### [3.2. Deploying a RHEL instance by using a custom base image](#deploying-a-rhel-instance-by-using-a-custom-base-image) {#deploying-a-rhel-instance-by-using-a-custom-base-image .title}

To manually configure a virtual machine (VM) on cloud platforms, create a base (starter) image, modify configuration settings, and add the packages to the VM. This VM is customizable, flexible, and lightweight. After uploading the image, you can change settings for these specific applications.

**Prerequisites**

-   You have access to the command line interface (CLI) or the web console for creating and configuring VM. If you do not have access to the CLI or the web console, you can use the Red Hat Cloud Access portal to create and configure VM.
-   Secure Shell (SSH) - Enable SSH to give remote access to your VM.
-   Dynamic Host Configuration Protocol (DHCP) - Configure the primary virtual adapter to use DHCP.
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

6.  For AMD64 or Intel 64 (x86_64) VMs, install the `nvme`{.literal}, `xen-netfront`{.literal}, and `xen-blkfront`{.literal} drivers:

    ``` {.language-plaintext tabindex="-1"}
    # dracut -f --add-drivers "nvme xen-netfront xen-blkfront"
    ```

7.  For ARM 64 (aarch64) VMs, install the `nvme`{.literal} driver:

    ``` {.language-plaintext tabindex="-1"}
    # dracut -f --add-drivers "nvme"
    ```

    Including these drivers prevents a `dracut`{.literal} time-out.

    Alternatively, you can add the drivers to `/etc/dracut.conf.d/`{.literal} and then enter `dracut -f`{.literal} to overwrite the existing `initramfs`{.literal} file.

8.  Install the `cloud-init`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install cloud-init
    ```

9.  Enable and start the `cloud-init`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now cloud-init.service
    ```

10. Reboot the VM to apply the changes.

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

### [3.3. Uploading a RHEL image to AWS by using the command line](#uploading-a-rhel-image-to-aws-by-using-cli) {#uploading-a-rhel-image-to-aws-by-using-the-command-line .title}

To run a RHEL instance on Amazon Web Services (AWS), you must first upload a RHEL image to AWS. To configure and manage a RHEL EC2 instance on AWS, use the `awscli2`{.literal} utility.

#### [3.3.1. Installing AWSCLI2](#installing-awscli2) {#installing-awscli2 .title}

You can use the Amazon Web Services (AWS) command line interface `awscli2`{.literal} utility to configure and manage Red Hat Enterprise Linux (RHEL) images and Red Hat high availability (HA) cluster on AWS.

**Prerequisites**

-   You have created a [Red Hat account](https://www.redhat.com/wapps/ugc/register.html).
-   You have [signed up and configured an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started-prerequisites.html).
-   You have access to an AWS Access Key ID and an AWS Secret Access Key. For details, see [manage access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html).

**Procedure**

-   Install `awscli2`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install awscli2
    ```

**Verification**

1.  Verify the installation:

    ``` {.language-plaintext tabindex="-1"}
    $ aws --version
    ```

    ``` {.language-plaintext tabindex="-1"}
    aws-cli/1.19.77 Python/3.6.15 Linux/5.14.16-201.fc34.x86_64 botocore/1.20.77
    ```

2.  Configure `awscli2`{.literal} for AWS credentials and settings:

    ``` {.language-plaintext tabindex="-1"}
    $ aws configure
    ```

    ``` {.language-plaintext tabindex="-1"}
    AWS Access Key ID [None]:
    AWS Secret Access Key [None]:
    Default region name [None]:
    Default output format [None]:
    ```

#### [3.3.2. Converting and pushing an image to Amazon S3](#converting-and-pushing-an-image-to-amazon-s3) {#converting-and-pushing-an-image-to-amazon-s3 .title}

You can convert a Red Hat Enterprise Linux (RHEL) image in the `qcow2`{.literal} image format to `OVA`{.literal}, `VHD`{.literal}, `VHDX`{.literal}, `VMDK`{.literal}, or `raw`{.literal} by using the `qemu-img`{.literal} utility, and then upload it to Amazon S3 storage.

**Prerequisites**

-   You have created a [Red Hat account](https://www.redhat.com/wapps/ugc/register.html).
-   You have [signed up and configured an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started-prerequisites.html).
-   You have created [an Amazon S3 bucket by using awscli2](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html#create-bucket-settings) to upload the RHEL image.

**Procedure**

1.  Run `qemu-img`{.literal} to convert `.qcow2`{.literal} image to `.raw`{.literal} image format:

    ``` {.language-plaintext tabindex="-1"}
    # qemu-img convert -f qcow2 -O raw rhel-10.0-sample.qcow2 rhel-10.0-sample.raw
    ```

2.  Upload the image to the Amazon S3 bucket:

    ``` {.language-plaintext tabindex="-1"}
    $ aws s3 cp rhel-10.0-sample.raw s3://<example-s3-bucket-name>
    ```

**Verification**

-   Check the [AWS S3 Console](https://console.aws.amazon.com/s3/) to confirm successful upload.

**Additional resources**

-   [Create a S3 bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html)
-   [Supported image formats by AWS](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-differences.html)

#### [3.3.3. Managing a RHEL VM on AWS by using the command line](#managing-a-rhel-vm-on-aws-by-using-the-command-line) {#managing-a-rhel-vm-on-aws-by-using-the-command-line .title}

You can use the Amazon Web Services (AWS) command line interface `awscli2`{.literal} utility to manage a Red Hat Enterprise Linux (RHEL) Elastic Cloud Compute (EC2) VM on AWS through the command line. You can import a RHEL EC2 image snapshot, create an Amazon Machine Image (AMI), launch, and connect to a RHEL EC2 instance.

**Prerequisites**

-   You have created a Red Hat account.
-   You have signed up and configured an AWS account.
-   You have installed the `awscli2`{.literal} package and configured AWS credentials for your account.

**Procedure**

1.  Use the `vmimport`{.literal} role:

    ``` {.language-plaintext tabindex="-1"}
    $ aws iam create-role --role-name vmimport \
    --assume-role-policy-document file://<example_vmimport_trust_policy_file>
    ```

2.  Embed an inline policy document by using the `vmimport`{.literal} role policy file:

    ``` {.language-plaintext tabindex="-1"}
    $ aws iam put-role-policy --role-name vmimport \
    --policy-name vmimport-access \
    --policy-document file://<example_vmimport_role_policy_file>
    ```

    Also, you can grant VM Import/Export permissions by creating an IAM role (often named `vmimport`{.literal}) with a trust policy for `vmie.amazonaws.com`{.literal} and attaching the JSON policy from the AWS guide.

3.  Import RHEL image as a snapshot:

    ``` {.language-plaintext tabindex="-1"}
    $ aws ec2 import-snapshot --disk-container file://<example_containers_json_file>
    ```

4.  Confirm that the snapshot import finished successfully with the `completed`{.literal} status:

    ``` {.language-plaintext tabindex="-1"}
    $ aws ec2 describe-import-snapshot-tasks --import-task-ids <example_import_task_id>
    ```

    You can import a RHEL VM image from Amazon S3 as a snapshot to Amazon EC2. Prepare a *`<example_containers_json_file>`{.literal}* file that points to your S3 bucket and object key, then start the import and monitor the task ID that the command returns.

5.  Register a RHEL AMI from the completed snapshot:

    ``` {.language-plaintext tabindex="-1"}
    $ aws ec2 register-image \
    --name <example_rhel_custom_ami_name> \
    --architecture x86_64 \
    --virtualization-type hvm \
    --root-device-name /dev/sda1 \
    --block-device-mappings "[{\"DeviceName\": \"/dev/sda1\",\"Ebs\": {\"SnapshotId\": \"<example_snapshot_id>\"}}]" \
    --ena-support
    ```

6.  Create a key pair for the RHEL EC2 instance:

    ``` {.language-plaintext tabindex="-1"}
    $ aws ec2 create-key-pair --key-name <example_key_pair_name> \
    --query 'KeyMaterial' --output text > <example_key_file>.pem
    ```

    This key pair is per region and save a `.pem`{.literal} file.

7.  Restrict permissions on the key file:

    ``` {.language-plaintext tabindex="-1"}
    $ chmod 400 <example_key>.pem
    ```

8.  Launch a RHEL EC2 instance from the registered AMI:

    ``` {.language-plaintext tabindex="-1"}
    $ aws ec2 run-instances \
    --image-id <example_registered_ami_id> \
    --instance-type <example_instance_type> \
    --key-name <example_key_pair_name>
    ```

9.  Connect to the RHEL EC2 instance where the default user is `ec2-user`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -i <example_key>.pem ec2-user@<instance_public_dns_or_ip>
    ```

**Verification**

-   Verify that the snapshot import finished successfully with the `completed`{.literal} status:

    ``` {.language-plaintext tabindex="-1"}
    $ aws ec2 describe-import-snapshot-tasks --import-task-ids <example_import_task_id>
    ```

-   Verify that the AMI is available with the `available`{.literal} state:

    ``` {.language-plaintext tabindex="-1"}
    $ aws ec2 describe-images --image-ids <example_registered_ami_id>
    ```

-   Verify that the instance is running with the `running`{.literal} state:

    ``` {.language-plaintext tabindex="-1"}
    $ aws ec2 describe-instances --instance-ids <example_instance_id>
    ```

    The `State.Name`{.literal} value is `running`{.literal} when the instance has finished starting.

-   Verify that the SSH connection works:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -i <example_key>.pem ec2-user@<instance_public_dns_or_ip> 'echo connected'
    ```

**Additional resources**

-   [Amazon S3 general purpose buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html)
-   [Amazon Web Services Red Hat Ecosystem Catalog](https://catalog.redhat.com/partners/detail/40acada9835742eeaf67fd43c5a7d559)
-   [Red Hat Enterprise Linux on Amazon EC2 FAQs](https://aws.amazon.com/partners/redhat/faqs/)
-   [Red Hat account](https://www.redhat.com/wapps/ugc/register.html)
-   [Signed up and configured an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started-prerequisites.html)
-   [Required permissions for VM Import/Export](https://docs.aws.amazon.com/vm-import/latest/userguide/required-permissions.html)
-   [Start an import snapshot task](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-import-snapshot.html#start-import-task)
-   [Monitor an import snapshot task](https://docs.aws.amazon.com/vm-import/latest/userguide/check-status-import-task.html)
-   [Creating an AMI from snapshot by using awscli2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/creating-an-ami-ebs.html#creating-launching-ami-from-snapshot)
-   [Launching, listing, and deleting RHEL instance by using awscli2](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-ec2-instances.html)
-   [Create a key pair using Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html#having-ec2-create-your-key-pair)
-   [Connect using the AWS CLI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-connect-methods.html#connect-linux-inst-eic-cli-ssh)

#### [3.3.4. Attaching Red Hat subscriptions](#attaching-red-hat-subscriptions) {#attaching-red-hat-subscriptions .title}

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

#### [3.3.5. Configuring automatic registration on AWS gold images](#setting-up-automatic-registration-on-aws-gold-images) {#configuring-automatic-registration-on-aws-gold-images .title}

You can deploy Red Hat Enterprise Linux (RHEL) virtual machines (VMs) more efficiently on Amazon Web Services (AWS) by using gold images of RHEL. This ensures that the VMs are automatically registered to the Red Hat Subscription Manager (RHSM).

**Prerequisites**

-   You have created a [Red Hat account](https://www.redhat.com/wapps/ugc/register.html).

-   You have [signed up and configured an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started-prerequisites.html).

-   You have downloaded the latest RHEL gold image for AWS. For details, see Additional resources.

    Note

    You can only attach an AWS account to a single Red Hat account at a time. Therefore, ensure no other users require access to the AWS account before attaching it to your Red Hat one.

**Procedure**

1.  Upload the gold image to AWS. For details, see one of the following:

    -   [Uploading a RHEL image to AWS by using the command line](#uploading-a-rhel-image-to-aws-by-using-cli "3.3. Uploading a RHEL image to AWS by using the command line")
    -   [Uploading a RHEL image to AWS by using the AWS console](#uploading-a-rhel-image-to-aws-by-using-the-aws-console "3.4. Uploading a RHEL image to AWS by using the AWS console")

2.  Create VMs by using the uploaded image. If your RHSM settings are correct, they will be automatically subscribed to RHSM.

**Verification**

-   In a RHEL VM created using the earlier instructions, verify the system is registered to RHSM by running the `subscription-manager identity`{.literal} command. On a successfully registered system, this displays the UUID of the system. For example:

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

-   [AWS Management Console](https://aws.amazon.com/console/)
-   [Adding cloud integrations to the Hybrid Cloud Console](https://docs.redhat.com/en/documentation/red_hat_hybrid_cloud_console/1-latest/html/configuring_cloud_integrations_for_red_hat_services/assembly-adding-cloud-integrations_crc-cloud-integrations)
-   [Using gold images on AWS](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/getting_started_with_rhel_system_registration/con-red-hat-cloud-access-program-overview)

### [3.4. Uploading a RHEL image to AWS by using the AWS console](#uploading-a-rhel-image-to-aws-by-using-the-aws-console) {#uploading-a-rhel-image-to-aws-by-using-the-aws-console .title}

To run a RHEL instance on Amazon Web Services (AWS), you must first upload the RHEL image to AWS. To configure and manage the RHEL EC2 instance on AWS, use the `awscli2`{.literal} utility.

#### [3.4.1. Converting and pushing an image to S3 by using the AWS console](#converting-and-pushing-an-image-to-s3-by-using-the-aws-console) {#converting-and-pushing-an-image-to-s3-by-using-the-aws-console .title}

You can convert a RHEL image in the `qcow2`{.literal} image format to `OVA`{.literal}, `VHD`{.literal}, `VHDX`{.literal}, `VMDK`{.literal}, or `raw`{.literal} by using the `qemu-img`{.literal} utility, and then upload it to Amazon S3 storage by using the AWS console.

**Prerequisites**

-   You have created a [Red Hat account](https://www.redhat.com/wapps/ugc/register.html).
-   You have [signed up and configured an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started-prerequisites.html).
-   You have created [an Amazon S3 bucket by using the Amazon S3 console](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html#create-bucket-settings) to upload the RHEL image.

**Procedure**

1.  Run `qemu-img`{.literal} to convert `.qcow2`{.literal} image to `.raw`{.literal} image format:

    ``` {.language-plaintext tabindex="-1"}
    # qemu-img convert -f qcow2 -O raw rhel-10.0-sample.qcow2 rhel-10.0-sample.raw
    ```

2.  Upload the image to the S3 bucket by using [Amazon S3 console](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html)

**Verification**

-   Check the [AWS S3 Console](https://console.aws.amazon.com/s3/) to confirm successful upload.

**Additional resources**

-   [Create a S3 bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html)

#### [3.4.2. Managing a RHEL VM on AWS by using the AWS console](#managing-a-rhel-vm-on-aws-by-using-the-aws-console) {#managing-a-rhel-vm-on-aws-by-using-the-aws-console .title}

You can manage RHEL Elastic Cloud Compute (EC2) virtual machines (VMs) on Amazon Web Services (AWS) by using the AWS console. You can create RHEL EC2 image snapshots, manage Amazon Machine Image (AMI), launch, and connect to a RHEL EC2 instance.

**Prerequisites**

-   You have created a Red Hat account.
-   You have signed up and configured an AWS account.
-   You have pushed your RHEL image to the Amazon S3 bucket by using the AWS console.

**Procedure**

1.  Open the AWS Management Console. Search for `IAM`{.literal}, open **IAM**, choose **Roles**, then choose **Create role** for `vmimport`{.literal}.

2.  In the **Trusted entity type** field, choose **Custom trust policy**. Paste the `vmie.amazonaws.com`{.literal} trust policy from the VM Import/Export documentation, then choose **Next**.

    **Add permissions**: skip managed policies if you add an inline VM Import/Export policy next; otherwise attach required policies, then **Next**.

3.  **Role name** `vmimport`{.literal}, **Create role**.

    In case of adding permissions, open the role. Choose the **Permissions** tab, choose **Add permissions**, choose **Create inline policy**, then choose the **JSON** tab. Paste the `vmimport`{.literal} access policy with your S3 bucket ARNs, then choose **Create policy**.

4.  Open **CloudShell** from the toolbar or global search.

    In the CloudShell pane, set the **Region** selector to the same Region as your S3 object.

    At the CloudShell (where the shell accepts `aws`{.literal} commands, not the console **Search** field), enter `aws ec2 import-snapshot`{.literal} with your disk container file, then `aws ec2 describe-import-snapshot-tasks`{.literal} until the import status is `completed`{.literal}.

5.  In the Amazon EC2 console, open **Elastic Block Store**, choose **Snapshots**, and confirm the snapshot ID.

    On **Snapshots**, select the snapshot, open **Actions**, choose **Create image from snapshot**, then finish the wizard.

6.  Open **Images**, choose **AMIs**, select the AMI, choose **Launch instance from AMI**, then finish the wizard.

7.  If you need a key pair, choose **Network & Security**, **Key pairs**, then **Create key pair**, and choose `.pem`{.literal}.

    Save *`<example_key>`{.literal}*`.pem`{.literal} with restrictive file permissions.

8.  Choose **Instances**, select the instance, choose **Connect**, then open **EC2 Instance Connect** or **SSH client**.

9.  On the instance, register Red Hat subscriptions.

**Verification**

-   Verify that the snapshot import finished successfully with the `completed`{.literal} status:

    ``` {.language-plaintext tabindex="-1"}
    $ aws ec2 describe-import-snapshot-tasks --import-task-ids <example_import_task_id>
    ```

-   Verify that the AMI is available with the `available`{.literal} state:

    ``` {.language-plaintext tabindex="-1"}
    $ aws ec2 describe-images --image-ids <example_registered_ami_id>
    ```

-   Verify that the instance is running with the `running`{.literal} state:

    ``` {.language-plaintext tabindex="-1"}
    $ aws ec2 describe-instances --instance-ids <example_instance_id>
    ```

    The `State.Name`{.literal} value is `running`{.literal} when the instance has finished starting.

-   Verify that the SSH connection works:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -i <example_key>.pem ec2-user@<instance_public_dns_or_ip> 'echo connected'
    ```

**Additional resources**

-   [Required permissions for VM Import/Export](https://docs.aws.amazon.com/vm-import/latest/userguide/required-permissions.html)
-   [Importing a disk as a snapshot using VM Import/Export](https://docs.aws.amazon.com/vm-import/latest/userguide/vmimport-import-snapshot.html)
-   [Red Hat Cloud Access Reference Guide](https://www.redhat.com/en/technologies/cloud-computing/cloud-access)
-   [Red Hat Enterprise Linux on Amazon EC2 - FAQs](https://aws.amazon.com/partners/redhat/faqs/)
-   [Red Hat on Amazon Web Services](https://access.redhat.com/public-cloud/aws)
-   [Red Hat account](https://www.redhat.com/wapps/ugc/register.html)
-   [Converting and pushing an image to S3 by using the AWS console](#converting-and-pushing-an-image-to-s3-by-using-the-aws-console "3.4.1. Converting and pushing an image to S3 by using the AWS console")
-   [Attaching Red Hat subscriptions](#attaching-red-hat-subscriptions "3.3.4. Attaching Red Hat subscriptions")

## [Chapter 4. Configuring a Red Hat High Availability cluster on AWS](#configuring-a-red-hat-high-availability-cluster-on-aws) {#chapter-4.-configuring-a-red-hat-high-availability-cluster-on-aws .title}

To group Red Hat Enterprise Linux (RHEL) nodes on Amazon Web Services (AWS) and automatically redistribute workloads if a node fails, configure a high availability (HA) cluster on AWS. The process for HA clusters setup on AWS is comparable to traditional, non-cloud HA configuration.

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

### [4.2. Installing the High Availability packages and agents](#installing-the-high-availability-packages-and-agents) {#installing-the-high-availability-packages-and-agents .title}

To configure a Red Hat High Availability cluster on Amazon Web Services (AWS), install the High Availability packages and agents on each node in the cluster.

**Prerequisites**

-   You have created a [Red Hat account](https://www.redhat.com/wapps/ugc/register.html).
-   You have [signed up and configured an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started-prerequisites.html).
-   You have completed the configuration for [Uploading RHEL image to AWS by using the command line](#uploading-a-rhel-image-to-aws-by-using-cli "3.3. Uploading a RHEL image to AWS by using the command line").

**Procedure**

1.  Remove the AWS Red Hat Update Infrastructure (RHUI) client.

    ``` {.language-plaintext tabindex="-1"}
    # dnf -y remove rh-amazon-rhui-client
    ```

2.  Register the VM with Red Hat.

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager register
    ```

3.  Disable all repositories.

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --disable=
    ```

4.  Enable the Red Hat Enterprise Linux (RHEL) 10 Server HA repositories.

    ``` {.language-plaintext tabindex="-1"}
    # subscription-manager repos --enable=rhel-10-for-x86_64-highavailability-rpms
    ```

5.  Update the RHEL AWS instance.

    ``` {.language-plaintext tabindex="-1"}
    # dnf update -y
    ```

6.  Install the Red Hat High Availability Add-On software packages, along with the AWS fencing agent from the High Availability channel.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install pcs pacemaker fence-agents-aws
    ```

7.  The user `hacluster`{.literal} was created during the `pcs`{.literal} and `pacemaker`{.literal} installation in the earlier step. Create a password for `hacluster`{.literal} on all cluster nodes. Use the same password for all nodes.

    ``` {.language-plaintext tabindex="-1"}
    # passwd hacluster
    ```

8.  Add the `high availability`{.literal} service to the RHEL Firewall if `firewalld.service`{.literal} is installed.

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --permanent --add-service=high-availability
    ```

    ``` {.language-plaintext tabindex="-1"}
    # firewall-cmd --reload
    ```

9.  Start the `pcs`{.literal} service and enable it to start on boot:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl enable --now pcsd.service
    ```

10. Edit `/etc/hosts`{.literal} and add RHEL hostnames and internal IP addresses. See [How should the /etc/hosts file be configured on RHEL cluster nodes?](https://access.redhat.com/solutions/81123) for details.

**Verification**

-   Ensure the `pcs`{.literal} service is running.

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status pcsd.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    pcsd.service - PCS GUI and remote configuration interface
    Loaded: loaded (/usr/lib/systemd/system/pcsd.service; enabled; vendor preset: disabled)
    Active: active (running) since Thu 2018-03-01 14:53:28 UTC; 28min ago
    Docs: man:pcsd(8)
    man:pcs(8)
    Main PID: 5437 (pcsd)
    CGroup: /system.slice/pcsd.service
         └─5437 /usr/bin/ruby /usr/lib/pcsd/pcsd > /dev/null &
    Mar 01 14:53:27 ip-10-0-0-48.ec2.internal systemd[1]: Starting PCS GUI and remote configuration interface…
    Mar 01 14:53:28 ip-10-0-0-48.ec2.internal systemd[1]: Started PCS GUI and remote configuration interface.
    ```

### [4.3. Creating a high availability cluster](#creating-a-high-availability-cluster) {#creating-a-high-availability-cluster .title}

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

### [4.4. Configuring fencing in a Red Hat High Availability cluster](#configuring-fencing) {#configuring-fencing-in-a-red-hat-high-availability-cluster .title}

When a node becomes unresponsive, the cluster must isolate it to prevent data corruption. Configure fencing since the node cannot be contacted directly. An external fence device cuts off the node's access to shared resources or performs a hard reboot.

Without a fence device, you do not know if the disconnected node has released its resources. This could prevent services from running on other nodes. Conversely, the system might wrongly assume resources are released, leading to data corruption. As a consequence, data integrity cannot be guaranteed and the cluster configuration will be unsupported.

When fencing is in progress, no other cluster operation is allowed to run. Normal operation of the cluster cannot resume until fencing has completed or the cluster node rejoins the cluster after the cluster node has been rebooted.

#### [4.4.1. Displaying available fence agents and their options](#displaying-fence-agents) {#displaying-available-fence-agents-and-their-options .title}

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

#### [4.4.2. Creating a fence device](#creating-fence-devices) {#creating-a-fence-device .title}

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

#### [4.4.3. General properties of fencing devices](#general-fence-device-properties) {#general-properties-of-fencing-devices .title}

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
| `pcmk_delay_base`{.literal}      | string  | 0s      | Enables a base delay for fencing actions and specifies a base delay value. You can specify different values for different nodes with the `pcmk_delay_base`{.literal} parameter. For general information about fencing delay parameters and their interactions, see [Fencing delays](#fence-delays "4.4.4. Fencing delays").                                                                                                          |
+----------------------------------+---------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `pcmk_delay_max`{.literal}       | time    | 0s      | Enables a random delay for fencing actions and specifies the maximum delay, which is the maximum value of the combined base delay and random delay. For example, if the base delay is 3 and `pcmk_delay_max`{.literal} is 10, the random delay will be between 3 and 10. For general information about fencing delay parameters and their interactions, see [Fencing delays](#fence-delays "4.4.4. Fencing delays").                 |
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
| `priority-fencing-delay`{.literal}   | 0 (disabled)      | Sets a fencing delay that allows you to configure a two-node cluster so that in a split-brain situation the node with the fewest or least important resources running is the node that gets fenced. For general information about fencing delay parameters and their interactions, see [Fencing delays](#fence-delays "4.4.4. Fencing delays").                                                                                                  |
+--------------------------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 4.3. Cluster Properties that Determine Fencing Behavior

Show more

For information about setting cluster properties, see [Setting Cluster properties](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_high_availability_clusters/index#setting-cluster-properties).

#### [4.4.4. Fencing delays](#fence-delays) {#fencing-delays .title}

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

#### [4.4.5. Testing a fence device](#testing-fence-devices) {#testing-a-fence-device .title}

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

#### [4.4.6. Configuring fencing levels](#configuring-fencing-levels) {#configuring-fencing-levels .title}

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

#### [4.4.7. Removing a fence level](#removing-a-fence-level) {#removing-a-fence-level .title}

You can remove the fence level for the specified node and device. If no nodes or devices are specified then the fence level you specify is removed from all nodes.

**Procedure**

-   Remove the fence level for the specified node and device:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level remove level [node_id] [stonith_id] ... [stonith_id]
    ```

#### [4.4.8. Clearing fence levels](#clearing-fence-levels) {#clearing-fence-levels .title}

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

#### [4.4.9. Verifying nodes and devices in fence levels](#verifying-nodes-and-devices-in-fence-levels_general-fence) {#verifying-nodes-and-devices-in-fence-levels .title}

You can verify that all fence devices and nodes specified in fence levels exist.

**Procedure**

-   Use the following command to verify that all fence devices and nodes specified in fence levels exist:

    ``` {.language-plaintext tabindex="-1"}
    # pcs stonith level verify
    ```

#### [4.4.10. Specifying nodes in fencing topology](#specifying-nodes-in-fencing-topology) {#specifying-nodes-in-fencing-topology .title}

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

#### [4.4.11. Configuring fencing for redundant power supplies](#configuring-fencing-for-redundant-power) {#configuring-fencing-for-redundant-power-supplies .title}

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

#### [4.4.12. Administering fence devices](#administering-fence-devices) {#administering-fence-devices .title}

The `pcs`{.literal} command-line interface provides a variety of commands you can use to administer your fence devices after you have configured them.

##### [4.4.12.1. Displaying configured fence devices](#displaying_configured_fence_devices) {#displaying-configured-fence-devices .title}

The following command shows all currently configured fence devices. If a *stonith_id* is specified, the command shows the options for that configured fencing device only. If the `--full`{.literal} option is specified, all configured fencing options are displayed.

``` {.language-plaintext tabindex="-1"}
# pcs stonith config [stonith_id] [--full]
```

##### [4.4.12.2. Exporting fence devices as pcs commands](#exporting_fence_devices_as_pcs_commands) {#exporting-fence-devices-as-pcs-commands .title}

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

##### [4.4.12.3. Exporting fence level configuration](#exporting_fence_level_configuration) {#exporting-fence-level-configuration .title}

The `pcs stonith config`{.literal} and the `pcs stonith level config`{.literal} commands support the `--output-format=`{.literal} option to export the fencing level configuration in JSON format and as `pcs`{.literal} commands.

-   Specifying `--output-format=cmd`{.literal} displays the `pcs`{.literal} commands created from the current cluster configuration that configure fencing levels. You can use these commands to re-create configured fencing levels on a different system.
-   Specifying `--output-format=json`{.literal} displays the fencing level configuration in JSON format, which is suitable for machine parsing.

##### [4.4.12.4. Modifying and deleting fence devices](#modifying_and_deleting_fence_devices) {#modifying-and-deleting-fence-devices .title}

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

##### [4.4.12.5. Manually fencing a cluster node](#manually_fencing_a_cluster_node) {#manually-fencing-a-cluster-node .title}

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

##### [4.4.12.6. Disabling a fence device](#disabling_a_fence_device) {#disabling-a-fence-device .title}

To disable a fencing device, run the `pcs stonith disable`{.literal} command.

The following command disables the fence device `myapc`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs stonith disable myapc
```

##### [4.4.12.7. Preventing a node from using a fencing device](#preventing_a_node_from_using_a_fencing_device) {#preventing-a-node-from-using-a-fencing-device .title}

To prevent a specific node from using a fencing device, you can configure location constraints for the fencing resource.

The following example prevents fence device `node1-ipmi`{.literal} from running on `node1`{.literal}.

``` {.language-plaintext tabindex="-1"}
# pcs constraint location node1-ipmi avoids node1
```

#### [4.4.13. Additional resources](#configuring-fencing_4413-additional-resources) {#additional-resources .title}

-   [Fencing in a Red Hat High Availability Cluster (Red Hat Knowledgebase)](https://access.redhat.com/solutions/15575)

### [4.5. Configuring ACPI for use with integrated fence devices](#configuring-acpi-for-use-with-integrated-fence-devices) {#configuring-acpi-for-use-with-integrated-fence-devices .title}

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

#### [4.5.1. Disabling ACPI Soft-Off with the BIOS](#disabling-acpi-soft-off-with-the-bios) {#disabling-acpi-soft-off-with-the-bios .title}

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

5.  Verify that the node turns off immediately when fenced. For information about testing a fence device, see [Testing a fence device](#testing-fence-devices "4.4.5. Testing a fence device").

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

#### [4.5.2. Disabling ACPI Soft-Off in the logind.conf file](#disabling-acpi-soft-off-in-the-logind-conf-file) {#disabling-acpi-soft-off-in-the-logind.conf-file .title}

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

1.  Verify that the node turns off immediately when fenced. For information about testing a fence device, see [Testing a fence device](#testing-fence-devices "4.4.5. Testing a fence device").

#### [4.5.3. Disabling ACPI completely in the GRUB 2 file](#disabling-acpi-completely-in-the-grub-2-file) {#disabling-acpi-completely-in-the-grub-2-file .title}

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

1.  Verify that the node turns off immediately when fenced. For details, see [Testing a fence device](#testing-fence-devices "4.4.5. Testing a fence device").

### [4.6. Configuring IP address resources on AWS](#setting-up-ip-address-resources-on-aws) {#configuring-ip-address-resources-on-aws .title}

To manage network access for cluster resources during failover in a high availability (HA) cluster, you can configure IP address resources. The Red Hat High Availability Add-On offers resource agents for different Amazon Web Services (AWS) IP address types.

This includes internet-exposed addresses, single-zone addresses, and multi-zone addresses.

-   Exposed to the internet: Use the `awseip`{.literal} network resource.

-   Limited to a single AWS Availability Zone (AZ): Use the `awsvip`{.literal} and `IPaddr2`{.literal} network resources.

-   Reassigns to many AWS AZs within the same AWS region: Use the `aws-vpc-move-ip`{.literal} network resource.

    Note

    If the HA cluster does not manage any IP addresses, the resource agents for managing virtual IP addresses on AWS are not required. If you need further guidance for your specific deployment, consult with AWS.

#### [4.6.1. Creating an IP address resource to manage an IP address exposed to the internet](#creating-an-ip-address-resource-to-manage-an-ip-address-exposed-to-the-internet) {#creating-an-ip-address-resource-to-manage-an-ip-address-exposed-to-the-internet .title}

To ensure that high-availability (HA) clients can access a Red Hat Enterprise Linux (RHEL) node that uses public-facing internet connections, configure an *AWS Secondary Elastic IP Address* (`awseip`{.literal}) resource to use an elastic IP address.

**Prerequisites**

-   You have a configured cluster.
-   Your cluster nodes must have access to the RHEL HA repositories. For details, see [Installing the High Availability packages and agents](#installing-the-high-availability-packages-and-agents "4.2. Installing the High Availability packages and agents").
-   You have configured the AWS CLI2. For details, see [Installing AWSCLI2](#installing-awscli2 "3.3.1. Installing AWSCLI2").

**Procedure**

1.  Add the two resources to the [same group](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_high_availability_clusters/configuring-cluster-resources#creating-resource-groups) that you have already created to enforce `order`{.literal} and `colocation`{.literal} constraints.

2.  Install the `resource-agents`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install resource-agents
    ```

3.  Create an elastic IP address:

    ``` {.language-plaintext tabindex="-1"}
    [root@ip-10-0-0-48 ~]# aws ec2 allocate-address --domain vpc --output text
    ```

    ``` {.language-plaintext tabindex="-1"}
    eipalloc-4c4a2c45   vpc 35.169.153.122
    ```

4.  Optional: Display the description of `awseip`{.literal}. This shows the options and default operations for this agent.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource describe awseip
    ```

5.  Create the Secondary Elastic IP address resource with the allocated IP address in the 2nd step:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create <resource_id> awseip elastic_ip=<elastic_ip_address> allocation_id=<elastic_ip_association_id> --group networking-group
    ```

    Example:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create elastic awseip elastic_ip=35.169.153.122 allocation_id=eipalloc-4c4a2c45 --group networking-group
    ```

**Verification**

1.  Verify the cluster status to ensure resources are available:

    ``` {.language-plaintext tabindex="-1"}
    [root@ip-10-0-0-58 ~]# pcs status
    ```

    ``` {.language-plaintext tabindex="-1"}
    Cluster name: newcluster
    Stack: corosync
    Current DC: ip-10-0-0-58 (version 1.1.18-11.el7-2b07d5c5a9) - partition with quorum
    Last updated: Mon Mar  5 16:27:55 2018
    Last change: Mon Mar  5 15:57:51 2018 by root via cibadmin on ip-10-0-0-46

    3 nodes configured
    4 resources configured

    Online: [ ip-10-0-0-46 ip-10-0-0-48 ip-10-0-0-58 ]

    Full list of resources:

     clusterfence   (stonith:fence_aws):    Started ip-10-0-0-46
     Resource Group: networking-group
         vip (ocf::heartbeat:IPaddr2): Started ip-10-0-0-48
         elastic (ocf::heartbeat:awseip): Started ip-10-0-0-48

    Daemon Status:
      corosync: active/disabled
      pacemaker: active/disabled
      pcsd: active/enabled
    ```

    In this example, `newcluster`{.literal} is an active cluster where resources such as `vip`{.literal} and `elastic`{.literal} are part of the `networking-group`{.literal} resource group.

2.  Launch an SSH session from your local workstation to the elastic IP address that you have already created:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -l ec2-user -i ~/.ssh/cluster-admin.pem 35.169.153.122
    ```

3.  Verify that the SSH connected host is same as the host with the elastic resources.

#### [4.6.2. Creating an IP address resource to manage a private IP address limited to a single AWS Availability Zone](#creating-an-ip-address-resource-to-manage-a-private-ip-address-limited-to-a-single-aws-availability-zone) {#creating-an-ip-address-resource-to-manage-a-private-ip-address-limited-to-a-single-aws-availability-zone .title}

In an Amazon Web Services (AWS) Availability Zone (AZ), you can use a private IP address. This address is limited to that zone in a Red Hat Enterprise Linux (RHEL) high-availability (HA) cluster. Use this address to configure an *AWS Secondary Private IP Address* (`awsvip`{.literal}) resource.

**Prerequisites**

-   You have a configured cluster.
-   Your cluster nodes have access to the RHEL HA repositories. For details,see [Installing the High Availability packages and agents](#installing-the-high-availability-packages-and-agents "4.2. Installing the High Availability packages and agents").
-   You have configured the AWS CLI. For details, see [Installing AWSCLI2](#installing-awscli2 "3.3.1. Installing AWSCLI2").

**Procedure**

1.  Install the `resource-agents`{.literal} package.

    ``` {.language-plaintext tabindex="-1"}
    # dnf install resource-agents
    ```

2.  Optional: View the options and default operations for `awsvip`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource describe awsvip
    ```

3.  Create a Secondary Private IP address with an unused private IP address in the `VPC CIDR`{.literal} block:

    ``` {.language-plaintext tabindex="-1"}
    [root@ip-10-0-0-48 ~]# pcs resource create privip awsvip secondary_private_ip=10.0.0.68 --group networking-group
    ```

    The secondary private IP address is included in a resource group.

4.  Create a virtual IP resource with the `vip`{.literal} resource ID and the `networking-group`{.literal} group name:

    ``` {.language-plaintext tabindex="-1"}
    root@ip-10-0-0-48 ~]# pcs resource create vip IPaddr2 ip=10.0.0.68 --group networking-group
    ```

    A Virtual Private Cloud (VPC) IP address maps from the fence node to the failover node and masks the failure of the fence node within the subnet. Ensure that the virtual IP belongs to the same resource group as the Secondary Private IP address you created in the previous step.

**Verification**

-   Verify the cluster status to ensure resources are available:

    ``` {.language-plaintext tabindex="-1"}
    [root@ip-10-0-0-48 ~]# pcs status
    Cluster name: newcluster
    Stack: corosync
    Current DC: ip-10-0-0-46 (version 1.1.18-11.el7-2b07d5c5a9) - partition with quorum
    Last updated: Fri Mar  2 22:34:24 2018
    Last change: Fri Mar  2 22:14:58 2018 by root via cibadmin on ip-10-0-0-46

    3 nodes configured
    3 resources configured

    Online: [ ip-10-0-0-46 ip-10-0-0-48 ip-10-0-0-58 ]

    Full list of resources:

    clusterfence    (stonith:fence_aws):    Started ip-10-0-0-46
     Resource Group: networking-group
         privip (ocf::heartbeat:awsvip): Started ip-10-0-0-48
         vip (ocf::heartbeat:IPaddr2): Started ip-10-0-0-58

    Daemon Status:
      corosync: active/disabled
      pacemaker: active/disabled
      pcsd: active/enabled
    ```

    In this example, `newcluster`{.literal} is an active cluster where resources such as `vip`{.literal} and `elastic`{.literal} are part of the `networking-group`{.literal} resource group.

**Additional resources**

-   [Amazon VPC Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

#### [4.6.3. Creating an IP address resource to manage an IP address that can move across multiple AWS Availability Zones](#creating-an-ip-address-resource-to-manage-an-ip-address-that-can-move-across-multiple-aws-availability-zones) {#creating-an-ip-address-resource-to-manage-an-ip-address-that-can-move-across-multiple-aws-availability-zones .title}

To use an elastic IP address on Amazon Web Services (AWS), you can configure a Red Hat Enterprise Linux (RHEL) Overlay IP (`aws-vpc-move-ip`{.literal}) resource agent. With `aws-vpc-move-ip`{.literal}, you can move a RHEL node within a single region of AWS across multiple availability zones (AZ) to ensure high-availability (HA) clients.

**Prerequisites**

-   You have an already configured cluster.

-   Your cluster nodes have access to the RHEL HA repositories. For details, see [installing the High Availability packages and agents](#installing-the-high-availability-packages-and-agents "4.2. Installing the High Availability packages and agents").

-   You have configured the AWS CLI. For details, see [installing AWSCLI2](#installing-awscli2 "3.3.1. Installing AWSCLI2").

-   You have configured an Identity and Access Management (IAM) user on your cluster with the following permissions:

    -   Modify routing tables
    -   Create security groups
    -   Create IAM policies and roles

**Procedure**

1.  Install the `resource-agents`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    # dnf install resource-agents
    ```

2.  Optional: View the options and default operations for `awsvip`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource describe aws-vpc-move-ip
    ```

3.  Configure an `OverlayIPAgent`{.literal} IAM policy for the IAM user.

    a.  In the AWS console, navigate to **Services** → **IAM** → **Policies** → **Create `OverlayIPAgent`{.literal} Policy**

    b.  Input the following configuration, and change the *\<region\>*, *\<account_id\>*, and *\<cluster_route_table_id\>* values to correspond with your cluster.

        ``` {.language-plaintext tabindex="-1"}
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Sid": "Stmt1424870324000",
                    "Effect": "Allow",
                    "Action":  "ec2:DescribeRouteTables",
                    "Resource": "*"
                },
                {
                    "Sid": "Stmt1424860166260",
                    "Action": [
                        "ec2:CreateRoute",
                        "ec2:ReplaceRoute"
                    ],
                    "Effect": "Allow",
                    "Resource": "arn:aws:ec2:_<region>_:_<account_id>_:route-table/_<cluster_route_table_id>_"
                }
            ]
        }
        ```

4.  In the AWS console, disable the `Source/Destination Check`{.literal} function on all nodes in the cluster.

    To do this, right-click each node → **Networking** → **Change Source/Destination Checks**. In the pop-up message that is displayed, click **Yes, Disable**.

5.  Create a route table for the cluster. To do so, use the following command on one node in the cluster:

    ``` {.language-plaintext tabindex="-1"}
    # aws ec2 create-route --route-table-id <cluster_route_table_id> --destination-cidr-block <new_cidr_block_ip/net_mask> --instance-id <cluster_node_id>
    ```

    In the command, replace values as follows:

    -   `ClusterRouteTableID`{.literal}: The route table ID for the existing cluster Virtual Private Cloud (VPC) route table.
    -   `NewCIDRblockIP`{.literal}: A new IP address and netmask outside of the VPC classless inter-domain routing (CIDR) block. For example, if the VPC CIDR block is `172.31.0.0/16`{.literal}, the new IP address or netmask can be `192.168.0.15/32`{.literal}.
    -   `ClusterNodeID`{.literal}: The instance ID for another node in the cluster.

6.  On one of the nodes in the cluster, create a `aws-vpc-move-ip`{.literal} resource that uses a free IP address that is accessible to the client. The following example creates a resource named `vpcip`{.literal} that uses IP `192.168.0.15`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource create vpcip aws-vpc-move-ip ip=192.168.0.15 interface=eth0 routing_table=<cluster_route_table_id>
    ```

7.  On all nodes in the cluster, edit the `/etc/hosts/`{.literal} file, and add a line with the IP address of the newly created resource. For example:

    ``` {.language-plaintext tabindex="-1"}
    192.168.0.15 vpcip
    ```

**Verification**

1.  Test the failover ability of the new `aws-vpc-move-ip`{.literal} resource:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource move vpcip
    ```

2.  If the failover succeeded, remove the automatically created constraint after the move of the `vpcip`{.literal} resource:

    ``` {.language-plaintext tabindex="-1"}
    # pcs resource clear vpcip
    ```

**Additional resources**

-   [Configure the OverlayIP Resource Agent (Red Hat Knowledgebase)](https://access.redhat.com/articles/3569621#configure-overlayip)
-   [IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)

### [4.7. Configuring shared block storage](#configuring-shared-block-storage) {#configuring-shared-block-storage .title}

To create extra storage resources, you can use Amazon Elastic Block Storage (EBS) Multi-Attach volumes to configure shared block storage for a Red Hat High Availability cluster.

**Prerequisites**

-   You have created a [Red Hat account](https://www.redhat.com/wapps/ugc/register.html).
-   You have [signed up and configured an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started-prerequisites.html).
-   You have 3 RHEL instances running in a cluster as a three-node cluster with a 1 TB shared disk.
-   You have access to an [AWS Nitro System-based Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances).

**Procedure**

1.  Create a shared block volume in the `us-east-1a`{.literal} availability zone:

    ``` {.language-plaintext tabindex="-1"}
    $ aws ec2 create-volume --availability-zone <us_east_1a> --no-encrypted --size <1024> --volume-type <io1> --iops <51200> --multi-attach-enabled
    ```

    ``` {.language-plaintext tabindex="-1"}
    {
        "AvailabilityZone": "us-east-1a",
        "CreateTime": "2020-08-27T19:16:42.000Z",
        "Encrypted": false,
        "Size": 1024,
        "SnapshotId": "",
        "State": "creating",
        "VolumeId": "vol-042a5652867304f09",
        "Iops": 51200,
        "Tags": [ ],
        "VolumeType": "io1"
    }
    ```

2.  For each instance in your cluster, attach a shared block volume. Use your *`<instance_id>`{.literal}* and *`<volume_id>`{.literal}*, for example `vol-042a5652867304f09`{.literal} to `instance i-0eb803361c2c887f2`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ aws ec2 attach-volume --device /dev/xvdd --instance-id i-0eb803361c2c887f2 --volume-id vol-042a5652867304f09
    ```

    ``` {.language-plaintext tabindex="-1"}
    {
        "AttachTime": "2020-08-27T19:26:16.086Z",
        "Device": "/dev/xvdd",
        "InstanceId": "i-0eb803361c2c887f2",
        "State": "attaching",
        "VolumeId": "vol-042a5652867304f09"
    }
    ```

**Verification**

1.  Verify the block device is available by using the `ssh`{.literal} command with your instance IP `198.51.100.3`{.literal} for each instance in the cluster:

    ``` {.language-plaintext tabindex="-1"}
    # ssh 198.51.100.3 "hostname ; lsblk -d | grep ' 1T '"
    ```

    ``` {.language-plaintext tabindex="-1"}
    node a
    nvme2n1 259:1    0   1T  0 disk
    ```

2.  Use the `ssh`{.literal} command to verify that each instance in your cluster uses the same shared disk:

    ``` {.language-plaintext tabindex="-1"}
    # ssh 198.51.100.3 "hostname ; lsblk -d | grep ' 1T ' | awk '{print \$1}' | xargs -i udevadm info --query=all --name=/dev/{} | grep '^E: ID_SERIAL='"
    ```

    ``` {.language-plaintext tabindex="-1"}
    nodea
    E: ID_SERIAL=Amazon Elastic Block Store_vol0fa5342e7aedf09f7
    ```

## [Chapter 5. Configuring RHEL on AWS with Secure Boot](#configuring-rhel-on-aws-with-secure-boot) {#chapter-5.-configuring-rhel-on-aws-with-secure-boot .title}

To enhance boot security for a Red Hat Enterprise Linux (RHEL) instance on Amazon Web Services (AWS), configure Secure Boot. Secure Boot verifies the digital signatures of the boot loader and other components at startup, allowing only trusted programs to load while blocking unauthorized ones.

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

### [5.2. Configuring a RHEL instance on the AWS Marketplace with Secure Boot](#configuring-a-rhel-instance-on-the-aws-marketplace-with-secure-boot) {#configuring-a-rhel-instance-on-the-aws-marketplace-with-secure-boot .title}

To ensure a secure booting process for a Red Hat Enterprise Linux (RHEL) instance on Amazon Web Services (AWS), configure Secure Boot on a RHEL instance. This instance is launched from a pre-configured Amazon Machine Image (AMI) from the AWS Marketplace.

**Prerequisites**

1.  You have installed the following packages on the RHEL instance:

    -   `awscli2`{.literal}
    -   `python3`{.literal}
    -   `openssl`{.literal}
    -   `efivar`{.literal}
    -   `keyutils`{.literal}
    -   `edk2-ovmf`{.literal}
    -   `python3-virt-firmware`{.literal}

2.  You have verified that the RHEL AMI has the `uefi-preferred`{.literal} option enabled in boot settings:

    ``` {.language-plaintext tabindex="-1"}
    $ aws ec2 describe-images \
    --image-id ami-0a951f007be151ff9 \
    --region us-east-2 \
    | grep -E '"ImageId"|"Name"|"BootMode"'
    ```

    ``` {.language-plaintext tabindex="-1"}
    "Name": "RHEL-10.1.0_HVM-20260217-x86_64-0-Hourly2-GP3",
    "BootMode": "uefi-preferred",
    "ImageId": "ami-0a951f007be151ff9",
    ```

    Warning

    Store your private keys separately from the RHEL instance where you use them. If an intruder gains access to the instance, they could use the stored secrets to escalate their privileges and compromise your system security.

3.  You have verified the platform status of the RHEL Marketplace AMI instance:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo mokutil --sb-state
    ```

    ``` {.language-plaintext tabindex="-1"}
    SecureBoot disabled
    Platform is in Setup Mode
    ```

    The `setup`{.literal} mode allows updating the Secure Boot UEFI variables within the instance.

**Procedure**

1.  Generate a `custom_db.cer`{.literal} custom certificate:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl req -quiet \
    -newkey rsa:3072 \
    -nodes -keyout custom_db.key \
    -new -x509 -sha256 \
    -days 3650 \
    -subj "/CN=Signature Database key/" \
    --outform DER -out custom_db.cer
    ```

2.  Generate UEFI variables file by using the `virt-fw-vars`{.literal} utility:

    ``` {.language-plaintext tabindex="-1"}
    $ virt-fw-vars --enroll-redhat \
    --add-db-cert OvmfEnrollDefaultKeys custom_db.cer \
    --set-dbx /usr/share/edk2/ovmf/DBX* \
    --output-auth .
    ```

    For details, see the `virt-fw-vars(1)`{.literal} man page on your system.

3.  Convert Public Key (PK) variable to the Extensible Firmware Interface (EFI) Signature List (ESL) format:

    ``` {.language-plaintext tabindex="-1"}
    $ tail -c +41 PK.auth > PK.esl
    ```

    Note

    Each GUID is an assigned value and represents an EFI parameter:

    -   `8be4df61-93ca-11d2-aa0d-00e098032b8c`{.literal}: `EFI_GLOBAL_VARIABLE_GUID`{.literal}
    -   `d719b2cb-3d3a-4596-a3bc-dad00e67656f`{.literal}: `EFI_IMAGE_SECURITY_DATABASE_GUID`{.literal}

    The `EFI_GLOBAL_VARIABLE_GUID`{.literal} parameter maintains settings of the bootable devices and boot managers, while the `EFI_IMAGE_SECURITY_DATABASE_GUID`{.literal} parameter represents the image security database for Secure Boot variables `db`{.literal}, `dbx`{.literal}, and storage of required keys and certificates.

4.  Transfer the database certificates to the target instance, use the `efivar`{.literal} utility to manage UEFI environment variables.

    a.  To transfer Key Exchange Key (`KEK.auth`{.literal}), enter:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo efivar -w -A 0x67 -n 8be4df61-93ca-11d2-aa0d-00e098032b8c-KEK -f KEK.auth
        ```

    b.  To transfer allowed signature database (`db.auth`{.literal}), enter:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo efivar -w -A 0x67 -n d719b2cb-3d3a-4596-a3bc-dad00e67656f-db -f db.auth
        ```

    c.  To transfer forbidden signature database (`dbx.auth`{.literal}) for x64 architecture, enter:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo efivar -w -A 0x67 -n d719b2cb-3d3a-4596-a3bc-dad00e67656f-dbx -f dbx.auth
        ```

    d.  To transfer `PK.esl`{.literal}, enter:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo efivar -w -n 8be4df61-93ca-11d2-aa0d-00e098032b8c-PK -f PK.esl
        ```

5.  Reboot the instance from the AWS console.

**Verification**

-   Verify if Secure Boot is enabled:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo mokutil --sb-state
    ```

    ``` {.language-plaintext tabindex="-1"}
    SecureBoot enabled
    ```

-   Use the `keyctl`{.literal} utility to verify the kernel keyring for the custom certificate:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo keyctl list %:.platform
    ```

    ``` {.language-plaintext tabindex="-1"}
    7 keys in keyring:
    741159788: ---lswrv     0     0 asymmetric: Microsoft Windows Production PCA 2011: a92902398e16c49778cd90f99e4f9ae17c55af53
    941772267: ---lswrv     0     0 asymmetric: Red Hat Secure Boot CA 8: e1c6c580aa1e21d585aad9bf20f3929e5ec1f08b
    979739129: ---lswrv     0     0 asymmetric: Red Hat Secure Boot CA 5: cc6fa5e72868ba494e939bbd680b9144769a9f8f
    303712700: ---lswrv     0     0 asymmetric: Signature Database key: 7dff9c7433d40daa6cb2cdbdb4c2b7c93f5252a4
    747313470: ---lswrv     0     0 asymmetric: Microsoft UEFI CA 2023: 81aa6b3244c935bce0d6628af39827421e32497d
    710788326: ---lswrv     0     0 asymmetric: Microsoft Corporation UEFI CA 2011: 13adbf4309bd82709c8cd54f316ed522988a1bd4
    163192: ---lswrv     0     0 asymmetric: Microsoft Corporation: Windows UEFI CA 2023: aefc5fbbbe055d8f8daa585473499417ab5a5272
    ```

**Additional resources**

-   [Get started with Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
-   [UEFI Revocation List File](https://uefi.org/revocationlistfile)
-   [NitroTPM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html)

### [5.3. Configuring a RHEL instance from a custom RHEL image with Secure Boot](#configuring-a-rhel-instance-from-a-custom-rhel-image-with-secure-boot) {#configuring-a-rhel-instance-from-a-custom-rhel-image-with-secure-boot .title}

To secure boot a Red Hat Enterprise Linux (RHEL) instance on Amazon Web Services (AWS), configure Secure Boot when registering a custom RHEL Amazon Machine Image (AMI). As this AMI consists of pre-stored UEFI variables, instances launched from it use the Secure Boot mechanism during the first boot.

**Prerequisites**

-   You have created and uploaded an AWS AMI image. For details, see [Preparing and uploading AWS AMI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/deploying_and_managing_rhel_on_amazon_web_services/preparing-and-uploading-ami-images-to-aws).

-   You have installed the following packages:

    -   `awscli2`{.literal}
    -   `python3`{.literal}
    -   `openssl`{.literal}
    -   `efivar`{.literal}
    -   `keyutils`{.literal}
    -   `python3-virt-firmware`{.literal}

**Procedure**

1.  Generate a custom certificate `custom_db.cer`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ openssl req -quiet \
    -newkey rsa:3072 \
    -nodes -keyout custom_db.key \
    -new -x509 -sha256 \
    -days 3650 -subj "/CN=Signature Database key/" \
    --outform DER -out custom_db.cer
    ```

2.  Use the `virt-fw-vars`{.literal} utility to generate the `aws_blob.bin`{.literal} binary file from keys, database certificates, and the UEFI variable store:

    ``` {.language-plaintext tabindex="-1"}
    $ virt-fw-vars --enroll-redhat \
    --add-db-cert OvmfEnrollDefaultKeys custom_db.cer \
    --set-dbx /usr/share/edk2/ovmf/DBX* \
    --output-aws aws_blob.bin
    ```

    The customized blob consists of:

    -   Public Key (`PK.cer`{.literal}), Key Exchange Key (`KEK.cer`{.literal}), allowed signature database (`db`{.literal}), and forbidden signature database (`dbx`{.literal}) from the `edk2-ovmf`{.literal} package
    -   `custom_db.cer`{.literal} the generated certificate

3.  Use the `awscli2`{.literal} utility to create and register the AMI from a disk snapshot with the required Secure Boot variables:

    ``` {.language-plaintext tabindex="-1"}
    $ aws ec2 register-image \
    --name rhel-10.0-secure-boot \
    --architecture x86_64 \
    --virtualization-type hvm \
    --root-device-name "/dev/sda1" \
    --block-device-mappings "{\"DeviceName\": \"/dev/sda1\",\"Ebs\": {\"SnapshotId\": \"<snap-02d4db3813ff9b98e>\"}}" \
    --ena-support --boot-mode uefi \
    --region eu-central-1 \
    --uefi-data $(cat aws_blob.bin)
    --output json
    ```

    ``` {.language-plaintext tabindex="-1"}
    {
        "ImageId": "example-ami-id"
    }
    ```

4.  Reboot the instance from the AWS Console.

**Verification**

-   Verify the Secure Boot functionality:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo mokutil --sb-state
    ```

    ``` {.language-plaintext tabindex="-1"}
    SecureBoot enabled
    ```

-   Use the `keyctl`{.literal} utility to verify the kernel keyring for the custom certificate:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo keyctl list %:.platform
    ```

    ``` {.language-plaintext tabindex="-1"}
    7 keys in keyring:
    741159788: ---lswrv     0     0 asymmetric: Microsoft Windows Production PCA 2011: a92902398e16c49778cd90f99e4f9ae17c55af53
    941772267: ---lswrv     0     0 asymmetric: Red Hat Secure Boot CA 8: e1c6c580aa1e21d585aad9bf20f3929e5ec1f08b
    979739129: ---lswrv     0     0 asymmetric: Red Hat Secure Boot CA 5: cc6fa5e72868ba494e939bbd680b9144769a9f8f
    303712700: ---lswrv     0     0 asymmetric: Signature Database key: 7dff9c7433d40daa6cb2cdbdb4c2b7c93f5252a4
    747313470: ---lswrv     0     0 asymmetric: Microsoft UEFI CA 2023: 81aa6b3244c935bce0d6628af39827421e32497d
    710788326: ---lswrv     0     0 asymmetric: Microsoft Corporation UEFI CA 2011: 13adbf4309bd82709c8cd54f316ed522988a1bd4
       163192: ---lswrv     0     0 asymmetric: Microsoft Corporation: Windows UEFI CA 2023: aefc5fbbbe055d8f8daa585473499417ab5a5272
    ```

## [Chapter 6. Configuring RHEL on Public Cloud Platforms with AMD SEV SNP](#configuring-rhel-on-public-cloud-platforms-with-amd-sev-snp) {#chapter-6.-configuring-rhel-on-public-cloud-platforms-with-amd-sev-snp .title}

To prevent VM integrity-based attacks and reduce memory integrity violations, configure AMD Secure Encrypted Virtualization with Secure Nested Paging (SEV-SNP) on Red Hat Enterprise Linux (RHEL) instances on public cloud. AMD SEV-SNP isolates VM data from the hypervisor and cloud service provider.

### [6.1. Overview of AMD SEV SNP](#overview-of-amd-sev-snp) {#overview-of-amd-sev-snp .title}

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
-   [AMD SEV documentation](https://www.amd.com/en/processors/amd-secure-encrypted-virtualization)
-   [Google Cloud Confidential Computing Root of Trust](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/attestation-overview#root-of-trust)

### [6.2. Configuring a RHEL instance on Amazon Web Services with AMD SEV SNP](#configuring-a-rhel-instance-on-amazon-web-services-with-amd-sev-snp) {#configuring-a-rhel-instance-on-amazon-web-services-with-amd-sev-snp .title}

To create a trusted boot environment, configure AMD Secure Encrypted Virtualization with Secure Nested Paging (SEV-SNP) for a Red Hat Enterprise Linux (RHEL) instance on Amazon Web Services (AWS). SEV-SNP isolates VM data from the hypervisor and AWS, supported on AMD EPYC processor-based hosts only.

**Prerequisites**

-   You have installed the `awscli2`{.literal}, `openssh`{.literal}, and `openssh-clients`{.literal} packages.

-   You have created an AWS EC2 instance using an AMD EPYC processor-based machine type from the supported list. For details, see [supported instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sev-snp.html#snp-requirements).

-   You have checked if SEV-SNP is enabled for the RHEL instance:

    ``` {.language-plaintext tabindex="-1"}
    $ aws ec2 describe-instances --instance-ids <example_instance_id> \
    --region <example_region>
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    "CpuOptions": {
    "CoreCount": 2,
    "ThreadsPerCore": 2,
    "AmdSevSnp": "enabled"
    },
    ...
    ```

    Note

    Before configuring a RHEL instance on AWS with AMD SEV-SNP, check with your cloud service provider. Verify the support status and certification of your particular RHEL instance type.

**Procedure**

1.  Get ID of a RHEL AMI if SEV-SNP is not enabled:

    ``` {.language-bash tabindex="-1"}
    $ aws ec2 describe-images \
    --owners 309956199498 \
    --query 'sort_by(Images, &Name)[*].[CreationDate,Name,ImageId]' \
    --filters "Name=name,Values=RHEL-10*" \
    --region us-east-1
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    "RHEL-10.0_HVM-amd64-..",
    "ami-0a1b2c3d4e5f67890"
    ...
    ```

    Warning

    Do not modify the command option `--owners 309956199498`{.literal}. This is the account ID for displaying Red Hat images. If you need to list images for AWS GovCloud, use `--region us-gov-west-1`{.literal} and `--owners 219670896067`{.literal}.

2.  Launch a RHEL instance with AMD SEV-SNP enabled:

    ``` {.language-plaintext tabindex="-1"}
    $ aws ec2 run-instances \
    --image-id <example-rhel-10-ami-id> \
    --instance-type m6a.4xlarge \
    --key-name <example_key_pair_name> \
    --subnet-id <example_subnet_id> \
    --cpu-options AmdSevSnp=enabled
    ```

**Verification**

-   Check kernel logs to verify status of SEV-SNP:

    ``` {.language-plaintext tabindex="-1"}
    $ dmesg | grep -i sev
    ```

    ``` {.language-plaintext tabindex="-1"}
    ...
    [    7.509546] Memory Encryption Features active: AMD SEV SEV-ES SEV-SNP
    [    8.469487] SEV: Using SNP CPUID table, 64 entries present.
    [    9.433348] SEV: SNP guest platform device initialized.
    [   33.314380] sev-guest sev-guest: Initialized SEV guest driver (using vmpck_id 0)
    ...
    ```

**Additional resources**

-   [RHEL AMI on Amazon Web Services (Red Hat Knowledgebase)](https://access.redhat.com/solutions/15356)

## [Chapter 7. Configuring RHEL on Public Cloud Platforms with UKI](#configuring-rhel-on-public-cloud-platforms-with-uki) {#chapter-7.-configuring-rhel-on-public-cloud-platforms-with-uki .title}

To ensure that a Red Hat Enterprise Linux (RHEL) instance has a secured boot process from an untrusted storage, use Unified Kernel Image (UKI). This applies to Confidential Virtual Machines (CVMs) on public cloud platforms.

### [7.1. Overview of Unified Kernel Image](#overview-of-uki) {#overview-of-unified-kernel-image .title}

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

## [Legal Notice](#idm140185698370224) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
