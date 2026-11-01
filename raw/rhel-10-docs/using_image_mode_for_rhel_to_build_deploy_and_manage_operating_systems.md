---
{"title": "Using image mode for RHEL to build, deploy, and manage operating systems", "guide": "using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems", "url": "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html-single/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index", "retrieved": "2026-11-01", "license": "CC-BY-SA-3.0"}
---

# Using image mode for RHEL to build, deploy, and manage operating systems {#using-image-mode-for-rhel-to-build-deploy-and-manage-operating-systems .chapter-title data-id="content_chapter" v-ccb3d6a4=""}

------------------------------------------------------------------------

Red Hat Enterprise Linux 10

## Using RHEL bootc images on Red Hat Enterprise Linux 10 {#using-rhel-bootc-images-on-red-hat-enterprise-linux-10 .subtitle}

Red Hat Customer Content Services

[Legal Notice](#idm140335710530848)

**Abstract**

By using RHEL bootc images, you can build, deploy, and manage the operating system as a container. With image mode for RHEL, you can manage your application as well as the underlying OS in a single container-native workflow.

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

## [Chapter 1. Introduction of image mode for RHEL](#introducing-image-mode-for-rhel) {#chapter-1.-introduction-of-image-mode-for-rhel .title}

Use image mode for RHEL to build, test, and deploy operating systems by using the same tools and techniques as application containers. Image mode for RHEL is available by using the `registry.redhat.io/rhel10/rhel-bootc`{.literal} bootc image.

The RHEL bootc images include additional necessary components, such as, the kernel, initrd, boot loader, and firmware to boot that you can traditionally excluded from the existing application Universal Base Images (UBI).

Note

The `rhel-bootc`{.literal} and user-created containers based on `rhel-bootc`{.literal} container image are subject to the Red Hat Enterprise Linux user license agreement (EULA). You are not allowed to publicly redistribute these images.

### [1.1. Overview of image mode for RHEL](#overview-of-image-mode-for-rhel) {#overview-of-image-mode-for-rhel .title}

RHEL Image mode is a deployment method that uses container technology to manage the operating system as an Open Container Initiative (OCI) container image.

Red Hat provides `bootc`{.literal} image for the following computer architectures:

-   AMD and Intel 64-bit architectures (`x86_64-v2`{.literal})
-   The 64-bit ARM architecture (`ARMv8.0-A`{.literal})
-   IBM Power® 64-bit Little Endian architecture (`ppc64le`{.literal})
-   IBM Z® 64-bit architecture (`s390x`{.literal})

Warning

Anaconda cannot work correctly on `s390x`{.literal} and `ppc64le`{.literal} architectures.

The benefits of image mode for RHEL occur across the lifecycle of a system. The following list contains some of the most important advantages:

Container images are easier to understand and use than other image formats and are fast to build
:   The `Containerfile`{.literal} provide a straightforward approach to defining the content and build instructions for an image. Container images are often significantly faster to build and iterate on compared to other image creation tools.

Consolidate process, infrastructure, and release artifacts
:   As you distribute applications as containers, you can use the same infrastructure and processes to manage the underlying operating system.

Immutable updates

:   Just as containerized applications are updated in an immutable way, with image mode for RHEL, the operating system is also. You can boot into updates and roll back when needed in the same way that you use `rpm-ostree`{.literal} systems.

    Warning

    The use of `rpm-ostree`{.literal} to make changes, or install content, is not supported.

Portability across hybrid cloud environments

:   You can use bootc images across physical, virtual, cloud, and edge environments. Although the containers build, transport, and run images, the system does not run as a container after you deploy or convert these bootc images to a disk image.

    -   Bootc supports the following container image formats and disk image formats:

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| Image type                        | Target environment                                                                                                                                  |
+:==================================+:====================================================================================================================================================+
| `OCI container format`{.literal}  | Physical, virtual, cloud, and edge environments.                                                                                                    |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| `ami`{.literal}                   | Amazon Machine Image.                                                                                                                               |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| `qcow2`{.literal} (default)       | QEMU (targeted for environments such as Red Hat OpenStack, Red Hat OpenStack services for OpenShift, and OpenShift Virtualization), Libvirt (RHEL). |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| `vmdk`{.literal}                  | VMDK for vSphere.                                                                                                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| `anaconda-iso`{.literal}          | An unattended Anaconda installer that installs to the first disk found.                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| `raw`{.literal}                   | Unformatted raw disk. Also supported in QEMU and Libvirt                                                                                            |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| `vhd`{.literal}                   | VHD for Virtual PC, among others.                                                                                                                   |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| `gce`{.literal}                   | Google Compute Engine (GCE) environment.                                                                                                            |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 1.1. bootc supported image types

Show more

Containers help streamline the lifecycle of a RHEL system by offering the following possibilities:

Building container images
:   You can configure your operating system at a build time by modifying the `Containerfile`{.literal}. Image mode for RHEL is available by using the `registry.redhat.io/rhel10/rhel-bootc`{.literal} container image.

You can use Podman, OpenShift Container Platform, or other standard container build tools to manage your containers and container images. You can automate the build process by using CI/CD pipelines.

Versioning, mirroring, and testing container images
:   You can version, mirror, introspect, and sign your derived `bootc`{.literal} image by using any container tools such as Podman or OpenShift Container Platform.

Deploying container images to the target environment

:   You have several options on how to deploy your image:

    -   **Anaconda**: is the installation program used by RHEL. You can deploy all image types to the target environment by using Anaconda and Kickstart to automate the installation process.
    -   **`bootc-image-builder`{.literal}**: is a containerized tool that converts the container image to different types of disk images, and optionally uploads them to an image registry or object storage.
    -   **`bootc`{.literal}**: is a tool responsible for fetching container images from a container registry and installing them to a system, updating the operating system, or switching from an existing ostree-based system. The RHEL bootc image contains the `bootc`{.literal} utility by default and works with all image types. It is intended to supersede `rpm-ostree`{.literal}.

Updating your operating system
:   The system supports in-place transactional updates with rollback after deployment. Automatic updates are on by default. A systemd service unit and systemd timer unit files check the container registry for updates and apply them to the system. As the updates are transactional, a reboot is required. For environments that require more sophisticated or scheduled rollouts, disable auto updates and use the `bootc`{.literal} utility to update your operating system.

**Additional resources**

-   [Anaconda might not work correctly on s390x and ppc64le architectures](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/10.0_release_notes/known-issues#known-issues-installer-and-image-creation)

### [1.2. Deployment modes for image mode in RHEL](#deployment-modes-for-image-mode-in-rhel) {#deployment-modes-for-image-mode-in-rhel .title}

Image mode for RHEL enables container-native management of the operating system by using OCI-compliant container images (bootc) for deployment, building, and updates.

RHEL has two deployment modes. Both provide the same stability, reliability, and performance during deployment. See their differences:

1.  **Package Mode**: the operating system uses RPM packages and is updated by using the `dnf`{.literal} package manager. The root filesystem is mutable. However, the operating system cannot be managed as a containerized application.
2.  **Image Mode**: A container-native approach to build, deploy, and manage RHEL. The same RPM packages are delivered as a base image, and updates are deployed as a container image. The root filesystem is immutable by default, except for `/etc`{.literal} and `/var`{.literal}, with most content coming from the container image.

You can choose to use either the **Image Mode** or the **Package Mode** deployment to build, test, and share your operating system. **Image Mode** additionally supports managing your operating system in the same way as any other containerized application.

**Additional resources**

-   [Automatically installing RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automatically_installing_rhel)
-   [Composing, installing, and managing RHEL for Edge images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_installing_and_managing_rhel_for_edge_images)

### [1.3. Available local container registries options for image mode for RHEL](#available-local-container-registries-options-for-image-mode-for-RHEL) {#available-local-container-registries-options-for-image-mode-for-rhel .title}

For a local environment using image mode for RHEL, both Red Hat Quay and Red Hat Satellite serve as local container registries to store, mirror, and distribute bootable container images (bootc).

You can create a local container registry by using one of the following methods:

-   **Standalone Red Hat Quay**: This method installs Red Hat Quay in a standalone environment or within a Red Hat OpenShift environment. For advanced features such as vulnerability scanning and geo-replication, Red Hat Quay can be deployed on-premise as a dedicated registry for bootable containers.

-   **Red Hat Satellite**: Satellite provides a native path for managing image-based clients. It can mirror the base `rhel10/rhel-bootc`{.literal} image from the Red Hat Ecosystem Catalog and publish derived images through Content Views.

    -   You can build a local container registry for Image mode by using Red Hat Satellite 6.17 and later.

**Additional resources**

-   [Managing container images](https://docs.redhat.com/documentation/red_hat_satellite/6.18/html/managing_content/managing_container_images_content-management)
-   [Deploy Red Hat Quay in a standalone environment - High Availability](https://docs.redhat.com/en/documentation/red_hat_quay/3.17/html/deploy_red_hat_quay_-_high_availability/index)
-   [Deploying the Red Hat Quay Operator on OpenShift Container Platform](https://docs.redhat.com/en/documentation/red_hat_quay/3.17/html/deploying_the_red_hat_quay_operator_on_openshift_container_platform/index)
-   [Managing container images for Image mode by using Red Hat Satellite](https://docs.redhat.com/documentation/red_hat_satellite/6.18/html/managing_content/managing_container_images_content-management)

**Additional resources**

-   [Introducing image mode for RHEL and bootc in Podman Desktop](https://developers.redhat.com/articles/2024/05/07/image-mode-rhel-bootable-containers)
-   [Image mode for Red Hat Enterprise Linux quick start: AI inference](https://developers.redhat.com/articles/2024/05/07/image-mode-rhel-quick-start-ai-inference)
-   [Getting Started with Podman AI Lab](https://developers.redhat.com/articles/2024/04/24/getting-started-podman-ai-lab)
-   [Automatically installing RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automatically_installing_rhel)
-   [Composing, installing, and managing RHEL for Edge images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_installing_and_managing_rhel_for_edge_images)
-   [Red Hat Enterprise Linux user license agreement (EULA)](https://www.redhat.com/en/about/eulas)

## [Chapter 2. Building and testing RHEL bootc images](#building-and-testing-rhel-bootc-images) {#chapter-2.-building-and-testing-rhel-bootc-images .title}

You can build, test, and deploy RHEL `bootc`{.literal} images by using the same container-native tools and techniques as application containers, such as Podman, `Containerfile`{.literal}, and OpenShift Container Platform, to manage everything from your applications to the underlying operating system.

### [2.1. Building and configuring bootc-based images from a Containerfile](#building-and-configuring-bootc-based-images-from-a-containerfile) {#building-and-configuring-bootc-based-images-from-a-containerfile .title}

You can build and configure Red Hat Enterprise Linux bootc-based images by defining your system specifications in a Containerfile. You can generate customized, reproducible, and scalable container-native operating systems tailored to your specific deployment requirements.

A general `Containerfile`{.literal} structure is the following:

``` {.language-plaintext tabindex="-1"}
FROM quay.io/<namespace>/<image>:latest

RUN dnf -y install [software] [dependencies] && dnf clean all

ADD [application]
ADD [configuration files]
RUN [config scripts]
```

The following commands in a `Containerfile`{.literal} are ignored when the `rhel-10-bootc`{.literal} image is installed to a system:

-   `ENTRYPOINT`{.literal} and `CMD`{.literal} (OCI: `Entrypoint/Cmd`{.literal}): you can set `CMD /sbin/init`{.literal} instead.
-   `ENV`{.literal} (OCI: `Env`{.literal}): change the `systemd`{.literal} configuration to configure the global system environment.
-   `EXPOSE`{.literal} (OCI: `exposedPorts`{.literal}): it is independent of how the system firewall and network function at runtime.
-   `USER`{.literal} (OCI: `User`{.literal}): configure individual services inside the RHEL bootc to run as unprivileged users instead.

The `rhel-10-bootc`{.literal} container image reuses the OCI image format.

-   The `rhel-10-bootc`{.literal} container image ignores the container config section (`Config`{.literal}) when it is installed to a system.
-   The `rhel-10-bootc`{.literal} container image does not ignore the container config section (`Config`{.literal}) when you run this image by using container runtimes such as `podman`{.literal} or `docker`{.literal}.

### [2.2. Building reproducible container images with container tools](#building-reproducible-container-images-with-container-tools) {#building-reproducible-container-images-with-container-tools .title}

You can build reproducible container images in RHEL by using `podman`{.literal} and `buildah`{.literal} with consistent inputs. This process reduces image changes over time, minimizes data pulled from registries during updates, and improves supply chain security, software deployment reliability, and debugging.

Previously, challenges with `tar`{.literal} file creation and escalating container image sizes led to increased storage burdens and unnecessary layer pulls. This challenge persisted even when underlying data remained unchanged, hindering faster updates in environments, such as, `rhel-bootc`{.literal} and RHEL AI. By using reproducible builds for RHEL containers reduces registry storage, creates smaller update payloads, and enables faster downloads by ensuring image layers remain consistent.

**Additional resources**

-   [Introduction to reproducible container builds](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/building_running_and_managing_containers/introduction-to-reproducible-container-builds)

### [2.3. Building a container image](#building-a-container-image) {#building-a-container-image .title}

You can build a RHEL container image to encapsulate your operating system configuration and applications in a single artifact. Managing your system lifecycle by using standard container tools ensures consistent deployments across hybrid infrastructure.

**Prerequisites**

-   The `container-tools`{.literal} meta-package is installed.

**Procedure**

1.  Create a `Containerfile`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    FROM quay.io/<namespace>/<image>:latest
    RUN dnf -y install cloud-init && \
        ln -s ../cloud-init.target /usr/lib/systemd/system/default.target.wants && \
        dnf clean all
    ```

    This `Containerfile`{.literal} example adds the `cloud-init`{.literal} tool, so it automatically fetches SSH keys and can run scripts from the infrastructure. The tool gathers configuration and secrets from the instance metadata. For example, you can use this container image for pre-generated AWS or KVM guest systems.

2.  Build the *`<image>`{.literal}* image by using `Containerfile`{.literal} in the current directory:

    ``` {.language-plaintext tabindex="-1"}
    $ podman build -t quay.io/<namespace>/<image>:<tag> .
    ```

**Verification**

-   List all images:

    ``` {.language-plaintext tabindex="-1"}
    $ podman images
    REPOSITORY                                  TAG      IMAGE ID       CREATED              SIZE
    localhost/<image>                           latest   b28cd00741b3   About a minute ago   2.1 GB
    ```

**Additional resources**

-   [Working with container registries](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/building_running_and_managing_containers/working-with-container-registries)
-   [Building an image from a Containerfile with Buildah](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/building_running_and_managing_containers/running-skopeo-buildah-and-podman-in-a-container#running-buildah-in-a-container)

### [2.4. Running a container image](#running-a-container-image) {#running-a-container-image .title}

You can run a Red Hat Enterprise Linux container image to run your application or validate your operating system build in an isolated environment. By launching the container, you can verify the system behavior and configurations without modifying the host infrastructure.

**Prerequisites**

-   The `container-tools`{.literal} meta-package is installed.

**Procedure**

-   Run the container by using the `podman run`{.literal} command with the appropriate options. For example, to run the container named `mybootc`{.literal} based on the `quay.io/`{.literal}*`<namespace>`{.literal}*`/`{.literal}*`<image>`{.literal}*`:`{.literal}*`<tag>`{.literal}* container image:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman run -it --rm --name mybootc quay.io/<namespace>/<image>:<tag> /bin/bash
    ```

    -   The `-i`{.literal} option creates an interactive session. Without the `-i`{.literal} option, the shell opens and then exits.
    -   The `-t`{.literal} option opens a command-line session. Without the `-t`{.literal} option, the shell stays open, but you cannot type anything to the shell.
    -   The `--rm`{.literal} option removes the `quay.io/`{.literal}*`<namespace>`{.literal}*`/`{.literal}*`<image>`{.literal}*`:`{.literal}*`<tag>`{.literal}* container image after the container exits.

**Verification**

-   List all running containers:

    ``` {.language-plaintext tabindex="-1"}
    $ podman ps
    CONTAINER ID  IMAGE                                    COMMAND          CREATED        STATUS            PORTS   NAMES
    7ccd6001166e  quay.io/<namespace>/<image>:<tag>  /sbin/init  6 seconds ago  Up 5 seconds ago          mybootc
    ```

**Additional resources**

-   [Podman run command](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/building_running_and_managing_containers/working-with-containers#podman-run-command)

### [2.5. Overriding the version of bootc images](#overriding-the-version-of-bootc-images) {#overriding-the-version-of-bootc-images .title}

Red Hat Enterprise Linux (RHEL) base images, Universal Base Images (UBI), and `rhel-bootc`{.literal} use version numbers that track only the major operating system version. To define a specific version number for a derived image, you can override this value by adding the `version`{.literal} label to your Containerfile.

**Prerequisites**

-   The `container-tools`{.literal} meta-package is installed.

**Procedure**

1.  Create a Containerfile:

    ``` {.language-plaintext tabindex="-1"}
    FROM registry.redhat.io/rhel10/rhel-bootc:latest
    # In this example, the custom operating system has its own
    # version scheme.
    # The operating system major version is copied
    # and a sub-version of it is added, which represents a point-in-time
    # snapshot of the base OS content.
    # This just changes the output of bootc status. A deeper level
    # of customization is available by also changing the contents of /usr/lib/os-release.
    # Define the custom version and release metadata
    LABEL org.opencontainers.image.version=”10.1.1”
    ```

2.  Build the *`<image>`{.literal}* image by using `Containerfile`{.literal} from the current directory:

    ``` {.language-plaintext tabindex="-1"}
    $ podman build -t quay.io/<namespace>/<image>:<tag> .
    ```

**Verification**

-   Verify that the override was applied:

    ``` {.language-plaintext tabindex="-1"}
    $ podman inspect <image-name> --format '{{index .Labels "org.opencontainers.image.version"}}'
    ```

### [2.6. Benefits of custom bootable images with multi-stage builds](#benefits-of-custom-bootable-images-with-multi-stage-builds) {#benefits-of-custom-bootable-images-with-multi-stage-builds .title}

The deployment image must include only the application and its required runtime, without adding any build tools or unnecessary libraries. To achieve this, use a two-stage `Containerfile`{.literal}: one stage for building the artifacts and another for hosting the application.

With multi-stage builds, you use multiple `FROM`{.literal} instructions in your `Containerfile`{.literal}. Each `FROM`{.literal} instruction can use a different base and starts a new stage of the build. You can selectively copy artifacts from one stage to another and exclude everything you do not need in the final image.

**Multi-stage builds offer several advantages:**

Smaller image size
:   By separating the build environment from the runtime environment, only the necessary files and dependencies are included in the final image, significantly reducing its size.

Improved security
:   The attack surface is reduced, leading to a more secure container because the build tools and unnecessary libraries are excluded from the final image.

Optimized performance
:   A smaller image size means faster download, deployment, and startup times, improving the overall efficiency of the containerized application.

Simplified maintenance
:   With the build and runtime environments separated, the final image is cleaner and easier to maintain, containing only what is needed to run the application.

Cleaner builds
:   Multi-stage builds help avoid clutter from intermediate files, which could accumulate during the build process, ensuring that only essential artifacts make it into the final image.

Resource efficiency
:   The ability to build in one stage and discard unnecessary parts minimizes the use of storage and bandwidth during deployment.

Better layer caching
:   With defined stages, Podman can efficiently cache the results of previous stages, potentially speeding up future builds.

The following `Containerfile`{.literal} consists of two stages. The first stage is typically named `builder`{.literal} and it compiles a golang binary. The second stage copies the binary from the first stage. The default working directory for the go-toolset builder is `opt/ap-root/src`{.literal}.

``` {.language-plaintext tabindex="-1"}
FROM registry.access.redhat.io/ubi10/go-toolset:latest as builder
RUN echo 'package main; import "fmt"; func main() { fmt.Println("hello world") }' > helloworld.go
RUN go build helloworld.go

FROM registry.redhat.io/rhel10/rhel-bootc:latest
COPY --from=builder /opt/app-root/src/helloworld /
CMD ["/helloworld"]
```

As a result, the final container image includes the `helloworld`{.literal} binary but no data from the previous stage.

You can also use multi-stage builds to perform the following scenarios:

Stopping at a specific build stage
:   When you build your image, you can stop at a specified build stage. For example:

``` {.language-plaintext tabindex="-1"}
$ podman build --target build -t hello .
```

For example, you can use this approach to debug a specific build stage.

Using an external image as a stage
:   You can use the `COPY --from`{.literal} instruction to copy from a separate image. You can use the local image name, a tag available locally or on a container registry, or a tag ID. For example:

``` {.language-plaintext tabindex="-1"}
COPY --from=<image> <source_path> <destination_path>
```

Using a previous stage as a new stage
:   You can continue where a previous stage ended by using the `FROM`{.literal} instruction. For example:

``` {.language-plaintext tabindex="-1"}
FROM ubi10 AS stage1
[...]

FROM stage1 AS stage2
[...]

FROM ubi10 AS final-stage
[...]
```

**Additional resources**

-   [How to build multi-architecture container images](https://developers.redhat.com/articles/2023/11/03/how-build-multi-architecture-container-images)

### [2.7. Pushing a container image to the registry](#pushing-a-container-image-to-the-registry) {#pushing-a-container-image-to-the-registry .title}

Push your Red Hat Enterprise Linux container image to a remote registry to make it accessible for deployment. By uploading the image, you can distribute your customized operating system across your infrastructure or share it with collaborators for testing.

**Prerequisites**

-   The `container-tools`{.literal} meta-package is installed.
-   An image is built and available on the local system.
-   You have created the Red Hat Quay registry. For more information, see [Proof of Concept - Deploying Red Hat Quay](https://docs.redhat.com/en/documentation/red_hat_quay/3.10/html/proof_of_concept_-_deploying_red_hat_quay/index).

**Procedure**

-   Push the `quay.io/`{.literal}*`<namespace>`{.literal}*`/`{.literal}*`<image>`{.literal}*`:`{.literal}*`<tag>`{.literal}* container image from your local storage to the registry:

    ``` {.language-plaintext tabindex="-1"}
    $ podman push quay.io/<namespace>/<image>:<tag>
    ```

    For more information, see the `podman-tag(1)`{.literal} and `podman-push(1)`{.literal} man pages on your system.

## [Chapter 3. Adapting RPM packages for image mode builds](#adapting-rpm-packages-for-image-mode-builds) {#chapter-3.-adapting-rpm-packages-for-image-mode-builds .title}

When you install RPM packages in `bootc`{.literal} container images, you can encounter failures because the build environment differs from a live, mutable system. When you use package mode, you run the `dnf install`{.literal} command on a fully booted system with running services. In image mode, you run the `dnf install`{.literal} command inside a container build where `systemd`{.literal} remains inactive and certain file system semantics change. Additionally, the build environments lack the runtime context that the RPM scriptlets expect.

### [3.1. RPM build environment differences in image mode](#rpm-build-environment-differences-in-image-mode) {#rpm-build-environment-differences-in-image-mode .title}

When you install RPM packages in image mode, the system builds the packages inside a container by using the `podman build`{.literal} command rather than on a live booted system. This environment changes the context that RPM scriptlets receive during the installation process and alters how the resulting file system behaves after you deploy the image.

The following table summarizes the key differences that RPM scriptlets encounter:

+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Aspect                                      | Package mode (`dnf install`{.literal} at runtime)                                                                                                                                                                                                                                                                                                                  | Image mode (`dnf install`{.literal} at build time)                                                                                                                                                                                                                                                                                                                                                                                                                                |
+:============================================+:===================================================================================================================================================================================================================================================================================================================================================================+:==================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| **`systemd`{.literal} availability**        | The `systemd`{.literal} system and service manager is active, which means that commands such as `systemctl`{.literal} can interact with D-Bus. However, manually enabling or starting services in scriptlets is disallowed by the Packaging software by using the RPM package management system guidelines, and packages must rely on `systemd`{.literal} presets. | The `systemd`{.literal} system and service manager is not active during image builds. Any scriptlet commands that depend on an active `systemd`{.literal} instance or a running D-Bus daemon fail or produce errors.                                                                                                                                                                                                                                                              |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Network access**                          | Full network access is available during package installation. However, scriptlets that require network access at runtime are strongly discouraged because the RPM Package Manager is moving toward disabling network access during transactions by default.                                                                                                        | Network access is available by default during the `podman build`{.literal} process. However, network access during the package build process is explicitly disallowed by official standards, such as the Packaging software by using the RPM package management system guidelines. Furthermore, scriptlets that rely on services in the target environment, such as license servers or registration endpoints, fail because the build host cannot reach these external endpoints. |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Interactive input**                       | A teletypewriter (TTY) interface can be available. Scriptlets can prompt for user input.                                                                                                                                                                                                                                                                           | No TTY interface is available. Scriptlets that prompt for input hang indefinitely or fail.                                                                                                                                                                                                                                                                                                                                                                                        |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Hardware context**                        | Scriptlets can detect the physical hardware of the target system, such as graphics processing units (GPUs), network interface controllers (NICs), and the disk layout.                                                                                                                                                                                             | Scriptlets detect the container environment of the build host rather than the target deployment hardware.                                                                                                                                                                                                                                                                                                                                                                         |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **`/var`{.literal} directory semantics**    | Content that you write to the `/var`{.literal} directory persists normally.                                                                                                                                                                                                                                                                                        | Content that you write to the `/var`{.literal} directory during the build process applies only during the initial installation. Subsequent image updates do not overwrite existing content in the `/var`{.literal} directory on the deployed system.                                                                                                                                                                                                                              |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **`/run`{.literal} directory availability** | The `/run`{.literal} directory is a live temporary file system (`tmpfs`{.literal}) that is populated by `systemd`{.literal} at boot time.                                                                                                                                                                                                                          | The `/run`{.literal} directory is mostly empty. Paths such as the `/run/systemd/system`{.literal} directory do not exist because `systemd`{.literal} is not running.                                                                                                                                                                                                                                                                                                              |
+---------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 3.1. Comparison of RPM installation contexts

Show more

Filesystem behavior during and after image builds
:   During the container build, the entire filesystem is writable. You can write to `/usr`{.literal}, `/etc`{.literal}, `/var`{.literal}, and any other path. RPM scriptlets and `RUN`{.literal} directives in the Containerfile operate on a fully mutable filesystem.

After you deploy the resulting bootc image to a target system:

-   `/usr`{.literal} (and the core operating system filesystem) becomes read-only at runtime.
-   `/etc`{.literal} is writable at runtime but uses a three-way merge strategy during image updates.
-   `/var`{.literal} is the only fully writable and persistent area, but its content from the image only seeds the initial installation.

**Additional resources**

-   [Overview of physical and logical root with /sysroot](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#physical-and-logical-root-with-sysroot)
-   [Using DNF with image mode for RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#using-dnf-with-image-mode-for-RHEL)
-   [Packaging software by using the RPM package management system](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/packaging_and_distributing_software/index/)

### [3.2. Common RPM scriptlet patterns that fail in image mode builds](#common-rpm-scriptlet-patterns-that-fail-in-image-mode-builds) {#common-rpm-scriptlet-patterns-that-fail-in-image-mode-builds .title}

When you install an RPM package during a RHEL image mode build, some standard RPM scriptlet patterns can fail or cause unexpected behaviors. This reference table helps you identify incompatible scriptlet patterns and implement compliant alternatives for your image builds.

+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Scriptlet pattern                                                                                                                                     | Why it fails in image builds                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Alternative action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+:======================================================================================================================================================+:===============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+:======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| `%post`{.literal} runs `systemctl enable --now myservice`{.literal}                                                                                   | The `systemd`{.literal} system and service manager is not active during the build process. The `--now`{.literal} flag attempts to start the service immediately, which fails. The `enable`{.literal} step can also fail if the scriptlet conditionally checks for the `/run/systemd/system`{.literal} directory.                                                                                                                                                                               | Use `systemctl enable`{.literal} without the `--now`{.literal} flag. If the scriptlet conditionally checks for the `systemd`{.literal} service manager, create the symbolic link manually in the `Containerfile`{.literal} file:\                                                                                                                                                                                                                                                                                                                     |
|                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `RUN ln -s ../myservice.service /usr/lib/systemd/system/multi-user.target.wants/`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%post`{.literal} runs `systemctl restart myservice`{.literal}                                                                                        | The `systemd`{.literal} system and service manager is not active during the build process, which causes the restart command to fail.                                                                                                                                                                                                                                                                                                                                                           | Remove the restart action from the scriptlet. The service starts automatically during the first boot of the deployed image if you enable the service correctly.                                                                                                                                                                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| The `%{post}`{.literal} scriptlet conditionally copies `systemd`{.literal} unit files only when the `/run/systemd/system`{.literal} directory exists. | The `/run/systemd/system`{.literal} directory does not exist during the container build process, which causes the scriptlet to skip the copy operation. Consequently, the deployed image lacks the required service unit file. Additionally, conditionally copying unit files in the `%{post}`{.literal} scriptlet is an outdated packaging pattern. An RPM spec file must install unit files directly to the `/usr/lib/systemd/system/`{.literal} directory during the package build process. | Place the unit file in the `/usr/lib/systemd/system/`{.literal} directory during the package build process, or copy the file explicitly in the `Containerfile`{.literal} file by using a `RUN`{.literal} instruction:\                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `RUN cp /usr/lib/myapp/myservice.service /usr/lib/systemd/system/myservice.service`{.literal}.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%post`{.literal} creates users or groups with `useradd`{.literal} or `groupadd`{.literal}                                                            | The commands can succeed at build time, but user identifier (UID) and group identifier (GID) allocation is tied to the build environment. Rebuilding the image can allocate different UIDs, which causes file ownership mismatches on persistent data in the `/var`{.literal} directory.                                                                                                                                                                                                       | Use the `systemd-sysusers`{.literal} service by creating a configuration file in the `/usr/lib/sysusers.d/`{.literal} directory. The system then allocates users and groups consistently during the boot process.                                                                                                                                                                                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%post`{.literal} creates directories under `/var`{.literal} with `mkdir`{.literal}                                                                   | The directories are created during the build, but `/var`{.literal} content from the image only applies during the initial installation. Subsequent image updates do not re-create missing directories under the `/var`{.literal} directory.                                                                                                                                                                                                                                                    | Use the `systemd-tmpfiles`{.literal} service by creating a configuration file in the `/usr/lib/tmpfiles.d/`{.literal} directory to declare the required directory structure. The system creates the directories at every boot.                                                                                                                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%post`{.literal} prompts for a license key or user input                                                                                             | Because no teletypewriter (TTY) interface is available during the build process, prompting for user input causes the scriptlet to hang indefinitely or fail. RPM scriptlets must be noninteractive and must run without TTY access.                                                                                                                                                                                                                                                            | Postpone interactive configurations until after you deploy the image. You can defer configuration until the first launch of your software through a command-line interface (CLI), graphical user interface (GUI), or web interface. Alternatively, you can use a first-boot `systemd`{.literal} service that is explicitly configured for TTY access. To do this, configure the service unit by using the `ConditionFirstBoot=yes`{.literal} parameter and by setting the `StandardInput=tty`{.literal} and `TTYPath=/dev/tty1`{.literal} parameters. |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%post`{.literal} writes configuration to `/etc`{.literal} based on the current hostname or IP                                                        | The scriptlet reads the hostname of the container build host rather than the target system. The resulting configuration is incorrect for the deployed system.                                                                                                                                                                                                                                                                                                                                  | Defer host-specific configuration to a first-boot `systemd`{.literal} service, or use a `systemd`{.literal} generator.                                                                                                                                                                                                                                                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%post`{.literal} writes a PID file to `/var/run/myapp.pid`{.literal}                                                                                 | The `/var/run`{.literal} directory is a symbolic link to the `/run`{.literal} directory, which is a temporary file system (`tmpfs`{.literal}). Content that you write during the build is lost during the boot process.                                                                                                                                                                                                                                                                        | Let the service manager to handle process identifier (PID) tracking. Use `Type=notify`{.literal} or `Type=exec`{.literal} in the `systemd`{.literal} service unit instead of using PID files.                                                                                                                                                                                                                                                                                                                                                         |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `%post`{.literal} runs `firewall-cmd --add-port`{.literal}                                                                                            | The `firewalld`{.literal} daemon is not running during the build. The command fails.                                                                                                                                                                                                                                                                                                                                                                                                           | Configure firewall rules declaratively in the image by placing an XML file in the `/usr/lib/firewalld/services/`{.literal} or `/etc/firewalld/zones/`{.literal} directory.                                                                                                                                                                                                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 3.2. RPM scriptlet patterns that fail in RHEL image builds

Show more

### [3.3. Adapting RPM scriptlets for bootc image-based builds](#adapting-rpm-scriptlets-for-bootc-image-based-builds) {#adapting-rpm-scriptlets-for-bootc-image-based-builds .title}

You can identify and work around problematic RPM scriptlets by extracting them from the RPM file and applying compensating actions in your `Containerfile`{.literal}. You can inspect an RPM, identify build-time failures, and implement fixes.

**Prerequisites**

-   You have the RPM file or access to the repository that provides the file.
-   You have the `rpm`{.literal} and `podman`{.literal} utilities installed on your build host.

**Procedure**

1.  Download the RPM package and extract its scriptlets:

    ``` {.language-plaintext tabindex="-1"}
    $ dnf download https://repo.example.com/<my-package>.rpm
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ rpm -qp --scripts <my-package>.rpm
    ```

    Review the output for the `preinstall`{.literal} and `postinstall`{.literal} scriptlet sections. Focus on the commands that interact with the `systemd`{.literal} service manager, create users, write to the `/var`{.literal} directory, or expect interactive input.

2.  Identify patterns that fail in image builds by comparing the scriptlet commands against the failure patterns that are listed in [Common RPM scriptlet patterns that fail in image mode builds](#common-rpm-scriptlet-patterns-that-fail-in-image-mode-builds "3.2. Common RPM scriptlet patterns that fail in image mode builds").

3.  For RPMs that create users or groups by using the `useradd`{.literal} or `groupadd`{.literal} commands, replace the scriptlet logic by using a `systemd-sysusers`{.literal} configuration file. Add the following instruction to your `Containerfile`{.literal} file :

    ``` {.language-plaintext tabindex="-1"}
    RUN cat > /usr/lib/sysusers.d/myapp.conf << 'EOF'
    u myappuser 900 "My Application Service Account" /var/lib/myapp /sbin/nologin
    EOF
    ```

4.  For RPMs that create directories under the `/var`{.literal} directory, replace the scriptlet logic by using a `systemd-tmpfiles`{.literal} configuration file:

    ``` {.language-plaintext tabindex="-1"}
    RUN cat > /usr/lib/tmpfiles.d/myapp.conf << 'EOF'
    d /var/log/myapp 0755 myappuser myappuser -
    d /var/lib/myapp 0750 myappuser myappuser -
    EOF
    ```

    Note

    The use of the `systemd-tmpfiles`{.literal} service does not conflict with packages that manually run the `useradd`{.literal} or `groupadd`{.literal} commands in scriptlets. However, ensure that any `useradd`{.literal} commands run in the `%pre`{.literal} scriptlet before the `systemd-tmpfiles`{.literal} service runs during package installation or system boot so that the system can apply the specified ownership successfully.

5.  For RPMs that conditionally skip the installation of `systemd`{.literal} unit files because the `/run/systemd/system`{.literal} directory does not exist, copy the unit file explicitly:

    ``` {.language-plaintext tabindex="-1"}
    RUN cp /usr/lib/myapp/scripts/myapp.service /usr/lib/systemd/system/myapp.service
    RUN systemctl enable myapp.service
    ```

6.  For RPMs that generate host-specific configuration at install time, create a first-boot `systemd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    RUN cat > /usr/lib/systemd/system/myapp-firstboot.service << 'EOF'
    [Unit]
    Description=Generate my application configuration on first boot
    ConditionFirstBoot=yes
    Before=myapp.service

    [Service]
    Type=oneshot
    ExecStart=/usr/libexec/myapp/generate-config.sh
    RemainAfterExit=yes

    [Install]
    WantedBy=multi-user.target
    EOF
    RUN systemctl enable myapp-firstboot.service
    ```

7.  List all files in the RPM to verify that no additional `systemd`{.literal} units, timers, or configuration files are missing:

    ``` {.language-plaintext tabindex="-1"}
    $ rpm -qlp mypackage.rpm
    ```

    Compare this list against the files present in the built container image. If any files are missing, such as `systemd`{.literal} units that the scriptlet conditionally installed, copy them explicitly in the `Containerfile`{.literal}.

**Verification**

-   Build the container image and verify that no scriptlet errors appear in the build output:

    ``` {.language-plaintext tabindex="-1"}
    $ podman build -t myapp-bootc .
    ```

-   Boot the resulting image on a test system and verify that the application service starts correctly:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl status myapp.service
    ```

### [3.4. Verifying RPM compatibility with bootc image builds](#verifying-rpm-compatibility-with-bootc-image-builds) {#verifying-rpm-compatibility-with-bootc-image-builds .title}

After you adapt an RPM for image mode, verify that the package installs correctly during the container build and that the application operates correctly on a deployed `bootc`{.literal} system.

**Prerequisites**

-   You have built a `bootc`{.literal} container image that contains the adapted RPM package.
-   You have configured a test environment where you can deploy and boot the image, such as a virtual machine or a bare-metal system.

**Procedure**

1.  Build the `bootc`{.literal} image and capture the build output:

    ``` {.language-plaintext tabindex="-1"}
    $ podman build -t myapp-bootc . 2>&1 | tee build.log
    ```

2.  Search the build log for scriptlet warnings or errors:

    ``` {.language-plaintext tabindex="-1"}
    $ grep -iE '(warning|error|failed|cannot)' build.log
    ```

    Investigate any messages that relate to user creation, directory creation, service enablement, or file permissions.

3.  Inspect the built image to confirm that the expected files exist:

    -   To list the files in the package, choose one of these options:

        -   Open an interactive shell inside the container image:

            ``` {.language-plaintext tabindex="-1"}
            $ podman run --rm -it myapp-bootc /bin/bash
            ```

        -   Run the inspection commands directly:

            ``` {.language-plaintext tabindex="-1"}
            # rpm -ql mypackage
            ```

            ``` {.language-plaintext tabindex="-1"}
            # ls -la /var/log/myapp
            ```

    -   To verify the `systemd`{.literal} service file path:

        ``` {.language-plaintext tabindex="-1"}
        $ podman run --rm myapp-bootc ls -la /usr/lib/systemd/system/myapp.service
        ```

    -   To verify the `systemd-sysusers`{.literal} configuration:

        ``` {.language-plaintext tabindex="-1"}
        $ podman run --rm myapp-bootc cat /usr/lib/sysusers.d/myapp.conf
        ```

    -   To verify the `systemd-tmpfiles`{.literal} configuration:

        ``` {.language-plaintext tabindex="-1"}
        $ podman run --rm myapp-bootc cat /usr/lib/tmpfiles.d/myapp.conf
        ```

4.  Deploy the image to your test system and boot the image.

**Verification**

Perform the following steps on your booted target system to confirm that the configuration was applied successfully:

1.  After the system boots, verify that `systemd-sysusers`{.literal} created the required users:

    ``` {.language-plaintext tabindex="-1"}
    $ getent passwd myappuser
    ```

2.  Verify that `systemd-tmpfiles`{.literal} created the required directories:

    ``` {.language-plaintext tabindex="-1"}
    $ ls -la /var/log/myapp/
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ ls -la /var/lib/myapp/
    ```

3.  Verify that the application service starts and runs without errors:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl start myapp.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl status myapp.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ journalctl -u myapp.service --no-pager
    ```

### [3.5. Checklist for adapting RPMs for image mode](#checklist-for-adapting-rpms-for-image-mode) {#checklist-for-adapting-rpms-for-image-mode .title}

Use the following checklist before you embed an existing RPM package in a `bootc`{.literal} container image. Each item identifies a packaging pattern that requires adaptation for image-based builds.

+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Check                                                                 | Action                                                                                                                                                                                                                                                                                                                                                                                    |
+:======================================================================+:==========================================================================================================================================================================================================================================================================================================================================================================================+
| **Scriptlet `systemd`{.literal} calls**                               | Search the `%pre`{.literal} and `%post`{.literal} scriptlets for the `systemctl`{.literal} or `systemd-*`{.literal} commands, or for checks for the `/run/systemd/system`{.literal} directory. Replace conditional service installation with explicit file copies in the `Containerfile`{.literal} file. Use the `systemctl enable`{.literal} command without the `--now`{.literal} flag. |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **User and group creation**                                           | Search scriptlets for the `useradd`{.literal}, `groupadd`{.literal}, or `getent`{.literal} commands. Replace these commands by using `systemd-sysusers`{.literal} configuration files in the `/usr/lib/sysusers.d/`{.literal} directory.                                                                                                                                                  |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Directory creation under `/var`{.literal}**                         | Search scriptlets for the `mkdir`{.literal} commands that target the `/var`{.literal} directory. Replace these commands by using `systemd-tmpfiles`{.literal} configuration files in the `/usr/lib/tmpfiles.d/`{.literal} directory.                                                                                                                                                      |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Interactive prompts**                                               | Search scriptlets for the `read`{.literal} or `dialog`{.literal} commands, or any command that expects user input. Move interactive configurations to a first-boot `systemd`{.literal} service.                                                                                                                                                                                           |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Host-specific configuration**                                       | Search scriptlets for references to the `hostname`{.literal} command, IP addresses, or hardware detection. Defer host-specific logic to a first-boot `systemd`{.literal} service that contains the `ConditionFirstBoot=yes`{.literal} parameter.                                                                                                                                          |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Hard-coded writable paths in `/usr`{.literal} or `/opt`{.literal}** | Identify any runtime write operations to paths that become read-only after deployment. Redirect writable paths to the `/var`{.literal} directory by using symbolic links or `systemd`{.literal} `BindPaths=`{.literal} directives.                                                                                                                                                        |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **SELinux contexts**                                                  | Verify that SELinux security contexts are correct after the build process. If it is required, add the `RUN restorecon -R <path>`{.literal} instruction in the `Containerfile`{.literal} file.                                                                                                                                                                                             |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **PID files and `/run`{.literal} content**                            | Search for commands that write to the `/run`{.literal} or `/var/run`{.literal} directories. This content does not persist across boots. Use `systemd`{.literal} service management features instead of process identifier (PID) files.                                                                                                                                                    |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Full RPM file list**                                                | Run the `rpm -qlp <package_file>`{.literal} command and compare the output against the files that are present in the built image. Identify any missing files that the scriptlet conditionally installed.                                                                                                                                                                                  |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 3.3. RPM adaptation checklist

Show more

#### [3.5.1. Additional resources](#checklist-for-adapting-rpms-for-image-mode_351-additional-resources) {#additional-resources .title}

-   [Packaging software by using the RPM package management system](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/packaging_and_distributing_software/index/)

## [Chapter 4. Building and managing logically bound images](#building-and-managing-logically-bound-images) {#chapter-4.-building-and-managing-logically-bound-images .title}

You can use logically bound images to bind container images to the lifecycle of a base `bootc`{.literal} image. You can manage multiple container images for system installations and upgrade lifecycle-bound workloads such as security agents and monitoring tools by using the `bootc upgrade`{.literal} command.

### [4.1. Introduction to logically bound images](#introduction-to-logically-bound-images) {#introduction-to-logically-bound-images .title}

You can associate container application images to a base bootc system image, by using logically bound images. By default, application containers as run by, for example, `podman`{.literal} have a lifecycle independent of host upgrades.

Logically bound images offer a key benefit that the application containers bound in this way tie their lifecycle to the host upgrade and are available before the host reboots into the new operating system. These container images remain present if a bootc container references them.

The following are examples for lifecycle bound workloads which are usually not updated outside of the host:

-   Logging, for example, journald→remote log forwarder container
-   Monitoring, for example, Prometheus node_exporter
-   Configuration management agents
-   Security agents

For these types of workloads it is important that the container start from early stage in the boot process, for example, networking might be available. Logically bound images help you to start containers (often by systemd) with the same reliability of using `ExecStart=`{.literal} of a binary in the base bootc image.

When using logically bound images, you can manage multiple container images for the system to install the logically bound images. This is an advantage and also a disadvantage. For example, for a disconnected or offline installation, you mirror all the containers, not just one. The application images are only referenced from the base image as `.image`{.literal} files or an equivalent.

Logically bound images installation
:   When you run `bootc install`{.literal}, logically bound images are present in the default `/var/lib/containers`{.literal} container store. The images are copied into the target system and present directly at boot, alongside the bootc base image.

Logically bound images lifecycle
:   Logically bound images are referenced by the bootc and have guaranteed availability when the bootc based server starts. The image is always upgraded by using `bootc upgrade`{.literal} and is available as `read-only`{.literal} to other processes, such as Podman.

Logically bound images management on upgrades, rollbacks, and garbage collection

:   -   During upgrades, the logically bound images are managed exclusively by bootc.
    -   During rollbacks, the logically bound images corresponding to rollback deployments are retained.
    -   bootc performs garbage collection of unused bound images.

### [4.2. Creating logically bound images](#creating-logically-bound-images) {#creating-logically-bound-images .title}

You can create logically bound images by using `podman`{.literal} Quadlet `.image`{.literal} or `.container`{.literal} files to link application container images to the lifecycle of a base `bootc`{.literal} image. This allows you to manage applications and the operating system as a cohesive unit.

**Prerequisites**

-   The `container-tools`{.literal} meta-package is installed.

**Procedure**

1.  Select the image that you want to logically bound.

2.  Create a `Containerfile`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ cat Containerfile
    FROM quay.io/<namespace>/<image>:latest
    COPY ./<app_1>.image /usr/share/containers/systemd/<app_1>.image
    COPY ./<app_2>.container /usr/share/containers/systemd/<app_2>.container

    RUN ln -s /usr/share/containers/systemd/<app_1>.image \
        /usr/lib/bootc/bound-images.d/<app_1>.image && \
        ln -s /usr/share/containers/systemd/<app_2>.container \
            /usr/lib/bootc/bound-images.d/<app_2>.container
    ```

3.  In the `.container`{.literal} definition, use:

    ``` {.language-plaintext tabindex="-1"}
    GlobalArgs=--storage-opt=additionalimagestore=/usr/lib/bootc/storage
    ```

    In the `Containerfile`{.literal} example, the image is selected to be logically bound by creating a symlink in the `/usr/lib/bootc/bound-images.d`{.literal} directory pointing to either an `.image`{.literal} or a `.container`{.literal} file.

4.  Run the `bootc upgrade`{.literal} command.

    ``` {.language-plaintext tabindex="-1"}
    $ bootc upgrade
    ```

    The bootc upgrade performs the following overall steps:

    a.  Fetches the new base image from the image repository. See [Configuring container pull secrets](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/managing-users-groups-ssh-keys-and-secrets-in-image-mode-for-rhel#configuring-container-pull-secrets).
    b.  Reads the new base image root file system to discover logically bound images.
    c.  Automatically pulls any discovered logically bound images defined in the new bootc image into the bootc-owned `/usr/lib/bootc/storage`{.literal} image storage.

5.  Make the bound images become available to container runtimes such as Podman. For that, you must explicitly configure bound images to point to the bootc storage as an \"additional image store\". For example:

    ``` {.language-plaintext tabindex="-1"}
    podman --storage-opt=additionalimagestore=/usr/lib/bootc/storage run <image>
    ```

    Important

    Do not attempt to globally enable the `/usr/lib/bootc/storage`{.literal} image storage in `/etc/containers/storage.conf`{.literal}. Only use the bootc storage for logically bound images.

    \+ The `bootc image store`{.literal} is owned by `bootc`{.literal}. The logically bound images will be garbage collected when they are no longer referenced by a file in the `/usr/lib/bootc/bound-images.d`{.literal} directory.

## [Chapter 5. Building and managing physically bound images](#building-and-managing-physically-bound-images) {#chapter-5.-building-and-managing-physically-bound-images .title}

Physically bound images embed application containers, configurations, and Quadlet files directly into the root file system during the `bootc`{.literal} build process. This ensures applications are immediately available on boot and enables disconnected and offline deployments.

### [5.1. Introduction to physically bound images](#introduction-to-physically-bound-images) {#introduction-to-physically-bound-images .title}

RHEL `bootc`{.literal} physically binds images to the base operating system image, directly embedding containerized applications. This process creates a fully self-contained and immutable system that can be pre-pulled during image build time and made available at runtime.

Physically bound images contain the data in the final `tar`{.literal} of the image, while logically bound images only reference the image and pull it during a bootc upgrade. Physically bound images offer strict offline reliability, while logically bound images accelerate development by avoiding an update to the entire base image for a small application change.

The key benefits of physically bound images include:

-   Because the base operating system and all required application containers ship as one artifact, you have pre-installed application availability right at boot.
-   You gain resilience against registry downtime, simplify your offline deployments, and secure atomic updates for both the operating system and applications.

### [5.2. Creating physically bound images by using system roles](#creating-physically-bound-images-by-using-system-roles) {#creating-physically-bound-images-by-using-system-roles .title}

You can use system roles to create physically bound images to detect the non-booted environment and adjust their behaviour. The images must not, for example, try to start systemd units or talk to network services; instead, they must defer all of that to the first boot.

**Prerequisites**

-   [You have prepared the control node and the managed nodes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automating_system_administration_by_using_rhel_system_roles/preparing-a-control-node-and-managed-nodes-to-use-rhel-system-roles).
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.
-   The account you use to connect to the managed nodes has `sudo`{.literal} permissions for these nodes.
-   You are logged in to the control node as a user who can run playbooks on the managed nodes.

**Procedure**

1.  Create a playbook file, for example `./setup.yml`{.literal}, with the following content:

    ``` {.language-yaml tabindex="-1"}
    ---
    - name: Configure physically bound images with RHEL system roles
      hosts: all
      vars:
        podman_registries_conf:
          unqualified-search-registries:
            - "registry.access.redhat.com"
            - "docker.io"
            - "my-company-registry.com"
          registry:
            - location: "my-company-registry.com"
            - location: "my-local-registry:5000"
              insecure: true
        podman_quadlet_specs:
          - file_src: my-quadlet.container
            state: started
      tasks:
          - name: Run the podman role
            include_role:
              name: redhat.rhel_system_roles.podman
    ```

    The Podman system role in the Ansible Playbook configures the system with registries and a quadlet application.

2.  Validate the playbook syntax:

    ``` {.language-plaintext tabindex="-1"}
    $ ansible-playbook --syntax-check ./setup.yml
    ```

    This command only validates the syntax and does not protect against a wrong but valid configuration.

3.  Create a `quadlet.container`{.literal} file to configures the container application, for example:

    ``` {.language-plaintext tabindex="-1"}
    [Install]
    WantedBy=default.target

    [Container]
    Image=quay.io/my_org/my_image:20260326
    ContainerName=my-quadlet
    ```

4.  Create a `Containerfile`{.literal} file with the following content:

    ``` {.language-plaintext tabindex="-1"}
    FROM quay.io/centos-bootc/centos-bootc:stream10
    RUN dnf -y install ansible-core rhel-system-roles
    COPY ./setup.yml .
    COPY ./quadlet.container .
    RUN ansible-playbook -c local setup.yml
    ```

    You perform every action inside the image build, running the playbooks against localhost. You can use a multi-stage build to keep Ansible and the roles out of your final image. Because this process is entirely self-contained, it works well in your automatic container build pipelines.

    Note

    The images must be copied over before any container or service (for example, Quadlet) depending on such an image is started.

5.  Build the `bootc`{.literal} image, for example:

    ``` {.language-plaintext tabindex="-1"}
    $ podman build -t quay.io/<namespace>/<image>:<tag> .
    ```

**Additional resources**

-   [Available methods for deploying RHEL bootc images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#available-methods-for-deploying-rhel-bootc-images)

## [Chapter 6. Creating bootc-compatible base disk images by using bootc-image-builder](#creating-bootc-compatible-base-disk-images-by-using-bootc-image-builder) {#chapter-6.-creating-bootc-compatible-base-disk-images-by-using-bootc-image-builder .title}

Create disk images from bootc images by using the `bootc-image-builder`{.literal} tool. These artifacts help you to provision your containerized operating system across diverse infrastructure, including physical hardware, virtual machines, edge and cloud environments.

### [6.1. About image mode for RHEL for bootc-image-builder](#about-image-mode-for-rhel-for-bootc-image-builder) {#about-image-mode-for-rhel-for-bootc-image-builder .title}

You can convert `bootc`{.literal} images into disk images for various platforms and formats by using the `bootc-image-builder`{.literal} tool. This process is equivalent to installing a `bootc`{.literal} image and enables you to update images directly from the container registry after deployment.

You can build your base images by using one of the following methods:

-   Use a local RHEL system, install the Podman tool, and build your image locally. Then, you can push the images to your private registry.

-   Use a CI/CD pipeline: Create a CI/CD pipeline that uses a RHEL-based system to build images and push them to your private registry.

    The `bootc-image-builder`{.literal} tool supports generating the following image types:

-   Disk image formats, such as ISO, that are suitable for disconnected installations.

-   Virtual disk image formats, such as:

    -   QEMU copy-on-write (QCOW2)

    -   Amazon Machine Image (AMI)

    -   Unformatted raw disk (Raw)

    -   Virtual Machine Image (VMI)

        The `bootc-image-builder`{.literal} tool uses the local container storage by default. It cannot pull container images from remote registries itself.

        To build the disk images, you can make the base bootc container image available in the system's local container registry. Mount the system's container storage into the `bootc-image-builder`{.literal} tool so it can use containers from the system storage.

        Deploying from a container image is beneficial when you run VMs or servers because you can achieve the same installation result. The consistency extends across multiple different image types and platforms when you build them from the same container image.

        Consequently, you can minimize the effort in maintaining operating system images across platforms. You can also update systems that you deploy from these disk images by using the `bootc`{.literal} tool, instead of re-creating and uploading new disk images with `bootc-image-builder`{.literal}.

        Although you can deploy a `rhel-10-bootc`{.literal} image directly, you can also create your own customized images that are derived from this bootc image. The `bootc-image-builder`{.literal} tool takes the `rhel-10-bootc`{.literal} OCI container image as an input.

        Note

        Generic base container images do not include any default passwords or SSH keys. Also, the disk images that you create by using the `bootc-image-builder`{.literal} tool do not contain the tools that are available in common disk images, such as `cloud-init`{.literal}. These disk images are transformed container images only.

**Additional resources**

-   [Red Hat products that use cloud-init](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_cloud-init_for_rhel/index)

### [6.2. Installing bootc-image-builder](#installing-bootc-image-builder) {#installing-bootc-image-builder .title}

To install the `bootc-image-builder`{.literal}, use the Red Hat Container Registry. The `bootc-image-builder`{.literal} is intended to be used as a container and it is not available as an RPM package in RHEL.

**Prerequisites**

-   The `container-tools`{.literal} meta-package is installed. The meta-package contains all container tools, such as Podman, Buildah, and Skopeo.
-   You are authenticated to `registry.redhat.io`{.literal}. For details, see [Red Hat Container Registry Authentication](https://access.redhat.com/RegistryAuthentication).

**Procedure**

1.  Log in to authenticate to `registry.redhat.io`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman login registry.redhat.io
    ```

2.  Install the `bootc-image-builder`{.literal} tool:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman pull registry.redhat.io/rhel10/bootc-image-builder
    ```

**Verification**

-   List all images pulled to your local system:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman images
    REPOSITORY                                    TAG         IMAGE ID      CREATED       SIZE
    registry.redhat.io/rhel10/bootc-image-builder  latest      b361f3e845ea  24 hours ago  676 MB
    ```

**Additional resources**

-   [Red Hat Container Registry Authentication](https://access.redhat.com/RegistryAuthentication)
-   [Pulling images from registries](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/building_running_and_managing_containers/index#pulling-images-from-registries)

### [6.3. Supported image customizations for a configuration file](#supported-image-customizations-for-a-configuration-file) {#supported-image-customizations-for-a-configuration-file .title}

You can use a build configuration file in the `TOML`{.literal} or `JSON`{.literal} format to add customizations for your resulting disk image. The container directory maps the configuration file to `/config.toml`{.literal}. The customizations object defines the image modifications.

Additionally, you can embed a build configuration file, either as `config.json`{.literal} or `config.toml`{.literal} in the `/usr/lib/bootc-image-builder`{.literal} directory. The system uses these default customizations unless explicitly overridden. For the `JSON`{.literal} format, you can also pass the configuration by using `stdin`{.literal} when you use the `--config`{.literal} argument.

User customization

:   Add a user to your disk image, and optionally set an SSH key. All fields for this section are optional except for the `name`{.literal}.

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      TOML                                                                                                                                                      JSON
      --------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      `[[customizations.user]] name = "user" password = "password" key = "ssh-rsa AAA ... user@email.com" groups = ["wheel"]`{.programlisting .language-toml}   `{ "customizations": { "user": [ { "name": "user", "password": "password", "key": "ssh-rsa AAA ... user@email.com", "groups": [ "wheel", "admins" ] } ] } }`{.programlisting .language-json}

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    Show more

Kernel configuration

:   You can customize the kernel boot parameters in the configuration file.

      -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      TOML                                                                                                     JSON
      -------------------------------------------------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------
      `[customizations.kernel] name = "kernel-debug" append = "nosmt=force"`{.programlisting .language-toml}   `{ "customizations": { "kernel": { "append": "mitigations=auto,nosmt" } } }`{.programlisting .language-json}

      -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    Show more

File systems configuration

:   You can use the file system section of the customizations to set the minimum size of the base partitions, such as `/`{.literal} and `/boot`{.literal}, and to create extra partitions with mount points under `/var`{.literal}.

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      TOML                                                                                                                                                                            JSON
      ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      `[[customizations.filesystem]] mountpoint = "/" minsize = "10 GiB" [[customizations.filesystem]] mountpoint = "/var/data" minsize = "20 GiB"`{.programlisting .language-toml}   `{ "customizations": { "filesystem": [ { "mountpoint": "/", "minsize": "10 GiB" }, { "mountpoint": "/var/data", "minsize": "20 GiB" } ] } }`{.programlisting .language-json}

      --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    Show more

File system type interaction with rootfs

:   The root file system type (`--rootfs`{.literal}) argument overrides the default value from the source container. It also sets the file system types for all additional mount points for the `ext4`{.literal}, `xfs`{.literal}, and `btrfs`{.literal} types.

    For supported mount points and sizes, the following restrictions and rules apply, unless the `rootfs`{.literal} is `btrfs`{.literal}:

    -   You can specify `/`{.literal} to set the minimum size of the root file system. The final size of the file system, mounted at `/sysroot`{.literal} on a booted system, equals the value you specify in this configuration or 2x the size of the base container, whichever is larger.
    -   You can specify `/boot`{.literal} to set the minimum size of the boot partition. You can also specify subdirectories of `/var`{.literal}, but you cannot specify symlinks in `/var`{.literal}. For example, `/var/home`{.literal} and `/var/run`{.literal} are symlinks and cannot be file systems on their own.
    -   `/var`{.literal} itself cannot be a mount point. The `rootfs`{.literal} option defines the file system type for the root file system.
    -   Currently, there is no support for creating `btrfs`{.literal} subvolumes during build time. Therefore, if the `rootfs`{.literal} is `btrfs`{.literal}, no custom mount points are supported under `/var`{.literal}. You can only configure `/`{.literal} and `/boot`{.literal}.

Anaconda ISO (installer) configuration options

:   Create a Kickstart file that contains the installation commands of your choice. Then, add a Kickstart file to your ISO build to create a fully customized and automated installation medium.

    Note

    The following combined customizations are not supported: `[customizations.user]`{.literal} and `[customizations.installer.kickstart]`{.literal}. When you add a Kickstart, use a configuration file in the `TOML`{.literal} format, because multi-line strings are prone to error.

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      TOML                                                                                                                                                                                                                                                              JSON
      ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      `[customizations.installer.kickstart] contents = """ text --non-interactive zerombr clearpart --all --initlabel --disklabel=gpt autopart --noswap --type=lvm network --bootproto=dhcp --device=link --activate --onboot=on """`{.programlisting .language-toml}   `{ "customizations": { "installer": { "kickstart": { "contents": "text --non-interactive\nzerombr\nclearpart --all --initlabel --disklabel=gpt\nautopart --noswap --type=lvm\nnetwork --bootproto=dhcp --device=link --activate --onboot=on" } } } }`{.programlisting .language-json}

      ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    Show more

    Warning

    The `bootc-image-builder`{.literal} does not add additional Kickstart commands besides the container image, which the system adds automatically to the container image. See [Creating Kickstart files](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/automatically_installing_rhel/creating-kickstart-files) for more information.

### [6.4. Creating QEMU disk images by using bootc-image-builder](#creating-qcow2-images-by-using-bootc-image-builder) {#creating-qemu-disk-images-by-using-bootc-image-builder .title}

To prepare a pre-configured RHEL image that is bootable with the KVM hypervisor, you can build a RHEL `bootc`{.literal} image into a QEMU (QCOW2) image. Then, you can run the QCOW2 image in a virtual machine.

**Prerequisites**

-   You have Podman installed on your host machine.
-   You have root access to run the containers in `--privileged`{.literal} mode.
-   You have root or sudo access.`bootc-image-builder`{.literal} requires rootful Podman to build images. Running it in rootless mode causes the build to fail.
-   You have the base bootc container image available in the systems root container registry.

**Procedure**

1.  Optional: Create a `config.toml`{.literal} file to prepare a user configuration for the QCOW2 image.

    The RHEL base image does not include a default user. To add a user configuration, populate the file with content similar to the following:

    ``` {.language-plaintext tabindex="-1"}
    [[customizations.user]]
    name = "user"
    password = "pass"
    key = "ssh-rsa AAA ... user@email.com"
    groups = ["wheel"]
    ```

    Later, you can use this file to inject the user configuration when running the `bootc-image-builder`{.literal} container.

    Alternatively, you can configure the base image by using `cloud-init`{.literal} to inject users and SSH keys on first boot. See [Users and groups configuration](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/managing-users-groups-ssh-keys-and-secrets-in-image-mode-for-rhel#users-and-groups-configuration).

2.  Before running the container, you must initialize the `output`{.literal} directory. Use the `-p`{.literal} argument to ensure that the command does not fail if the directory already exists:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir -p ./output
    ```

3.  Ensure that the required image is pulled to the system storage:

    ``` {.language-plaintext tabindex="-1"}
    $ quay.io/<namespace>/<image>:<tag>
    ```

    The local image can be one of the following:

    -   An image that you built by using a Containerfile
    -   An image that you pulled from a private, access-controlled registry that required a login
    -   An image that you loaded from a `.tar`{.literal} file

4.  Run the `bootc-image-builder`{.literal} container. Optionally, if you want to use user access configuration, pass the `config.toml`{.literal} as an argument. For example:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman run \
        --rm \
        -it \
        --privileged \
        --pull=newer \
        --security-opt label=type:unconfined_t \
        -v /var/lib/containers/storage:/var/lib/containers/storage:Z \
        -v ./config.toml:/config.toml:Z \
        -v ./output:/output:Z \
        registry.redhat.io/rhel10/bootc-image-builder:latest \
        --type qcow2 \
        --config /config.toml \
        localhost/<local-image>:latest
    ```

**Verification**

-   Check that the `.qcow2`{.literal} image has been created in the specified output folder.

**Next steps**

-   You can find the `.qcow2`{.literal} image in the output directory.You can use the image to deploy your image. See [Deploying a container image using KVM with a QCOW2 disk image](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/deploying-the-rhel-bootc-images#deploying-a-container-image-by-using-kvm-with-a-qcow2-disk-image).
-   You can make updates to the image and push the changes to a registry. See [Managing RHEL bootc images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/managing-rhel-bootc-images).

**Additional resources**

-   [Build and run a bootable container image](https://developers.redhat.com/learn/rhel/build-and-run-bootable-container-image-image-mode-rhel-and-podman-desktop)

### [6.5. Creating VMDK images by using bootc-image-builder](#creating-vmdk-images-by-using-bootc-image-builder) {#creating-vmdk-images-by-using-bootc-image-builder .title}

You can use `bootc-image-builder`{.literal} to generate a Virtual Machine Disk (VMDK) from a RHEL `bootc`{.literal} image to deploy bootable container images as virtual machines on VMware vSphere or Oracle VirtualBox. You can use a registry image directly or mount local storage for a locally built image.

**Prerequisites**

-   You have Podman installed on your host machine.
-   You have authenticated to the Red Hat Registry by using the `podman login registry.redhat.io`{.literal}.
-   You have pulled the `rhel10/bootc-image-builder`{.literal} container image.

**Procedure**

1.  Optional: Create a `Containerfile`{.literal} to customize your base image. For example, to include `cloud-init`{.literal} and `open-vm-tools`{.literal} for VMware vSphere environments:

    ``` {.language-plaintext tabindex="-1"}
    FROM registry.redhat.io/rhel10/rhel-bootc:latest
    RUN dnf -y install cloud-init open-vm-tools && \
    ln -s /usr/lib/systemd/system/cloud-init.target /usr/lib/systemd/system/default.target.wants/cloud-init.target && \
    rm -rf /var/{cache,log} /var/lib/{dnf,rhsm} && \
    systemctl enable vmtoolsd.service
    ```

    If you already have a target `bootc`{.literal} image built locally or in a remote registry, you can skip this and the next step.

2.  Build the `bootc`{.literal} image:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman build . -t localhost/rhel-bootc-vmdk
    ```

3.  Optional: If you want to customize your image configuration, such as adding users or configuring filesystems, create a `config.toml`{.literal} file in your current working directory.

    ``` {.language-plaintext tabindex="-1"}
    [[customizations.user]]
    name = "user"
    password = "pass"
    key = "ssh-rsa AAA ... user@email.com"
    groups = ["wheel"]
    ```

4.  Before running the container, initialize the `output`{.literal} directory. Use the `-p`{.literal} argument to ensure that the command does not fail if the directory already exists:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir -p ./output
    ```

5.  Run `bootc-image-builder`{.literal} and specify `--type vmdk`{.literal} to generate the VMDK disk image from your container image. The image must be accessible from a registry, such as `registry.redhat.io/rhel10/bootc-image-builder:latest`{.literal}.

    Note

    The `--config`{.literal} option and volume mount `-v ./config.toml:/config.toml:ro`{.literal} are only required if you created a `config.toml`{.literal} file. If not, omit the `--config /config.toml`{.literal} line and its corresponding `-v ./config.toml:/config.toml:ro`{.literal} volume mount.

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman run \
        --rm \
        --privileged \
        -v /var/lib/containers/storage:/var/lib/containers/storage \
        -v ./output:/output \
        -v ./config.toml:/config.toml:ro \
        --security-opt label=type:unconfined_t \
        --pull newer \
        registry.redhat.io/rhel10/bootc-image-builder:latest \
        --type vmdk \
        --config /config.toml \
        localhost/rhel-bootc-vmdk:latest
    ```

    A VMDK disk file for the bootc image is stored in the `output/vmdk`{.literal} directory.

**Next steps**

-   Deploy your VMDK image to VMware vSphere or VirtualBox.
-   Update your bootc container image in the registry to apply updates to deployed instances. See [Managing RHEL bootc images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#managing-rhel-bootc-images).

**Additional resources**

-   [Build and run a bootable container image](https://developers.redhat.com/learn/rhel/build-and-run-bootable-container-image-image-mode-rhel-and-podman-desktop)

### [6.6. Creating GCE images by using bootc-image-builder](#creating-gce-images-by-using-bootc-image-builder) {#creating-gce-images-by-using-bootc-image-builder .title}

Build a RHEL bootc image into a GCE image for the architecture on which you are running the commands.

The RHEL base image does not include a default user. Optionally, you can inject a user configuration by using the `--config`{.literal} option to run the `bootc-image-builder`{.literal} container. Alternatively, you can configure the base image with `cloud-init`{.literal} to inject users and SSH keys on first boot. See [Injecting users and SSH keys by using cloud-init](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/managing-users-groups-ssh-keys-and-secrets-in-image-mode-for-rhel#users-and-groups-configuration).

**Prerequisites**

-   You have Podman installed on your host machine.
-   You have root access to run the `bootc-image-builder`{.literal} tool, and run the containers in `--privileged`{.literal} mode, to build the images.

**Procedure**

1.  Optional: Create a `config.toml`{.literal} to configure user access, for example:

    ``` {.language-plaintext tabindex="-1"}
    [[customizations.user]]
    name = "user"
    password = "pass"
    key = "ssh-rsa AAA ... user@email.com"
    groups = ["wheel"]
    ```

2.  Before running the container, initialize the `output`{.literal} directory. Use the `-p`{.literal} argument to ensure that the command does not fail if the directory already exists:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir -p ./output
    ```

3.  Run `bootc-image-builder`{.literal}. Optionally, if you want to use user access configuration, pass the `config.toml`{.literal} as an argument. The image must be accessible from a registry, such as `registry.redhat.io/rhel10/bootc-image-builder:latest`{.literal}.

    a.  The following is an example of creating a `gce`{.literal} image:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo podman run \
            --rm \
            --it \
            --privileged \
            --pull=newer \
            --security-opt label=type:unconfined_t \
            -v ./config.toml:/config.toml \
            -v ./output:/output \
            -v /var/lib/containers/storage:/var/lib/containers/storage \
            registry.redhat.io/rhel10/bootc-image-builder:latest \
            --type gce \
            --config /config.toml \
          quay.io/<namespace>/<image>:<tag>
        ```

        You can find the `gce`{.literal} image in the output directory.

**Next steps**

-   You can make updates to the image and push the changes to a registry. See [Managing RHEL bootc images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#managing-file-systems-in-image-mode-for-rhel).

**Additional resources**

-   [Build and run a bootable container image](https://developers.redhat.com/learn/rhel/build-and-run-bootable-container-image-image-mode-rhel-and-podman-desktop)

### [6.7. Creating AMI images by using bootc-image-builder and uploading them to AWS](#creating-ami-images-by-using-bootc-image-builder-and-uploading-them-to-aws) {#creating-ami-images-by-using-bootc-image-builder-and-uploading-them-to-aws .title}

You can use `bootc-image-builder`{.literal} to generate an Amazon Machine Image (AMI) from a RHEL `bootc`{.literal} image to deploy container-native operating systems as EC2 instances on AWS. For a registry image, mount local storage and for a locally built image, include the `-v /var/lib/containers/storage:/var/lib/containers/storage`{.literal} argument.

**Prerequisites**

-   You have Podman installed on your host machine.
-   You have an existing `AWS S3`{.literal} bucket within your AWS account.
-   You have root access to run the `bootc-image-builder`{.literal} tool, and run the containers in `--privileged`{.literal} mode, to build the images.
-   You have the `vmimport`{.literal} service role configured on your account to import an AMI into your AWS account.

**Procedure**

1.  Create a disk image from the bootc image.

    -   Configure the user details in the Containerfile. Ensure that you assign it with sudo access.
    -   Build a customized operating system image with the configured user from the Containerfile. It creates a default user without password sudo access.

2.  Optional: Configure the machine image with `cloud-init`{.literal}. See [Managing file systems in image mode for RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#managing-file-systems-in-image-mode-for-rhel). The following is an example:

    ``` {.language-plaintext tabindex="-1"}
    FROM quay.io/<namespace>/<image>:latest

    RUN dnf -y install cloud-init && \
        ln -s ../cloud-init.target /usr/lib/systemd/system/default.target.wants && \
        rm -rf /var/{cache,log} /var/lib/{dnf,rhsm}
    ```

    Note

    You can also use `cloud-init`{.literal} to add users and additional configuration by using instance metadata.

3.  Build the bootc image. For example, to deploy the image to an `x86_64`{.literal} AWS machine, use the following commands:

    ``` {.language-plaintext tabindex="-1"}
    $ podman build -t quay.io/<namespace>/<image>:<tag> .
    $ podman push quay.io/<namespace>/<image>:<tag> .
    ```

4.  Before running the container, initialize the `output`{.literal} directory. Use the `-p`{.literal} argument to ensure that the command does not fail if the directory already exists:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir -p ./output
    ```

5.  Use the `bootc-image-builder`{.literal} tool to create a public AMI image from the bootc container image. The image must be accessible from a registry, such as `registry.redhat.io/rhel10/bootc-image-builder:latest`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman run \
      --rm \
      --it \
      --privileged \
      --pull=newer \
      -v ./config.toml:/config.toml \
      -v /var/home/<user>/.aws:/root/.aws \
      --env AWS_PROFILE=default \
      registry.redhat.io/rhel10/bootc-image-builder:latest \
      --type ami \
      --config /config.toml \
      --aws-ami-name rhel-bootc-x86 \
      --aws-bucket rhel-bootc-bucket \
      --aws-region us-east-1 \
    quay.io/<namespace>/<image>:<tag>
    ```

    The following flags must be specified all together. If you do not specify any flag, the AMI is exported to your output directory.

    -   `--aws-ami-name`{.literal} - The name of the AMI image in AWS

    -   `--aws-bucket`{.literal} - The target S3 bucket name for intermediate storage when you are creating the AMI

    -   `--aws-region`{.literal} - The target region for AWS uploads

        The `bootc-image-builder`{.literal} tool uses your AWS credentials to build, upload, and register an AMI image to your AWS S3 bucket.

**Next steps**

-   You can deploy your image. See [Deploying a container image to AWS with an AMI disk image](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#deploying-the-rhel-bootc-images).
-   You can make updates to the image and push the changes to a registry. See [Managing RHEL bootc images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#managing-file-systems-in-image-mode-for-rhel).

**Troubleshooting**

If you have any issues configuring the requirements for your AWS image, see the following documentation:

-   [AWS IAM account manager](https://aws.amazon.com/iam/)
-   [Using high-level (s3) commands with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html).
-   [S3 buckets](https://aws.amazon.com/s3/).
-   [Regions and Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-regions).
-   [Launching a customized RHEL image on AWS](https://docs.redhat.com/en/documentation/red_hat_lightspeed/1-latest/html/deploying_and_managing_rhel_systems_in_hybrid_clouds/launching-customized-rhel-images-to-the-cloud-platforms-with-the-public-cloud-provider-tools_host-management-services#launching-images-on-aws-web-console_launching-customized-rhel-images-to-the-cloud-platforms-with-the-public-cloud-provider-tools).

**Additional resources**

-   [AWS CLI documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html)
-   [Building and testing bootc images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#building-and-testing-rhel-bootc-images)

### [6.8. Creating raw disk images by using bootc-image-builder](#creating-raw-disk-images-by-using-bootc-image-builder) {#creating-raw-disk-images-by-using-bootc-image-builder .title}

You can convert a bootc image to a raw image with an MBR or GPT partition table by using the `bootc-image-builder`{.literal}.

The RHEL base image does not include a default user. You can inject a user configuration by using the `--config`{.literal} option to run the `bootc-image-builder`{.literal} container. Alternatively, you can configure the base image with `cloud-init`{.literal} to inject users and SSH keys on first boot. See [Users and groups configuration - Injecting users and SSH keys by using cloud-init](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/managing-users-groups-ssh-keys-and-secrets-in-image-mode-for-rhel#users-and-groups-configuration).

**Prerequisites**

-   You have Podman installed on your host machine.
-   You have root access to run the `bootc-image-builder`{.literal} tool, and run the containers in `--privileged`{.literal} mode, to build the images.
-   You have pulled your target container image in the container storage.

**Procedure**

1.  Optional: Create a `config.toml`{.literal} to configure user access, for example:

    ``` {.language-plaintext tabindex="-1"}
    [[customizations.user]]
    name = "user"
    password = "pass"
    key = "ssh-rsa AAA ... user@email.com"
    groups = ["wheel"]
    ```

2.  Before running the container, initialize the `output`{.literal} directory. Use the `-p`{.literal} argument to ensure that the command does not fail if the directory already exists:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir -p ./output
    ```

3.  Run `bootc-image-builder`{.literal}. If you want to use user access configuration, pass the `config.toml`{.literal} as an argument. The image must be accessible from a registry, such as `registry.redhat.io/rhel10/bootc-image-builder:latest`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman run \
        --rm \
        --it \
        --privileged \
        --pull=newer \
        --security-opt label=type:unconfined_t \
        -v /var/lib/containers/storage:/var/lib/containers/storage \
        -v ./config.toml:/config.toml \
        -v ./output:/output \
        registry.redhat.io/rhel10/bootc-image-builder:latest \
        --type raw \
        --config /config.toml \
      quay.io/<namespace>/<image>:<tag>
    ```

    You can find the `.raw`{.literal} image in the output directory.

**Next steps**

-   You can deploy your image. See [Deploying a container image by using KVM with a QCOW2 disk image](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#deploying-a-container-image-using-kvm-qemu-with-a-qcow2-disk-image_deploying-the-rhel-bootc-images).
-   You can make updates to the image and push the changes to a registry. See [Managing RHEL bootc images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#managing-rhel-bootc-images).

**Additional resources**

-   [Build and run a bootable container image](https://developers.redhat.com/learn/rhel/build-and-run-bootable-container-image-image-mode-rhel-and-podman-desktop)

### [6.9. Creating bootable ISOs with Kickstart and partitioning](#creating-iso-images-by-using-bootc-image-builder) {#creating-bootable-isos-with-kickstart-and-partitioning .title}

You can use `bootc-image-builder`{.literal} to create an installable ISO image. The `anaconda-iso`{.literal} or `iso`{.literal} image type creates a bootable installation program that uses the Anaconda installation program to deploy your bootc image to a target system.

By providing a custom Kickstart file in your `config.toml`{.literal}, you can define advanced partitioning, such as LVM, custom mount points, or swap space, and automate the installation process.

Important

The creation and deployment of bootable ISO images by using `bootc-image-builder`{.literal} is provided as a Technology Preview. This workflow relies on the `%ostreecontainer`{.literal} Kickstart command, which is a Technology Preview feature. Technology Preview features are not supported with Red Hat production Service Level Agreements (SLAs), might not be functionally complete, and Red Hat does not recommend using them for production. See Technology Preview Features Support Scope for more information.

**Prerequisites**

-   You have Podman installed on your host machine.
-   Your host system is subscribed or you have injected repository configuration by using bind mounts to ensure the image build process can fetch RPMs.
-   You have an image accessible from a registry, such as `registry.redhat.io/rhel10/bootc-image-builder:latest`{.literal}.
-   You have root access to run the `bootc-image-builder`{.literal} tool, and run the containers in `--privileged`{.literal} mode, to build the images.

**Procedure**

1.  Create a `config.toml`{.literal} to define your custom partitioning, enabling the localization module, and Kickstart instructions.

    ``` {.language-plaintext tabindex="-1"}
    [customizations.installer.kickstart]
    contents = """
    text --non-interactive
    zerombr
    clearpart --all --initlabel --disklabel=gpt

    # Advanced Partitioning
    part /boot --fstype="xfs" --size=1024
    part pv.01 --grow --size=1
    volgroup rhel pv.01
    logvol / --fstype="xfs" --name=root --vgname=rhel --size=10240
    logvol /var --fstype="xfs" --name=var --vgname=rhel --size=5120
    logvol swap --name=swap --vgname=rhel --size=2048

    network --bootproto=dhcp --device=link --activate --onboot=on
    reboot
    """
    ```

    This example defines an LVM-based partitioning scheme with a custom `/var`{.literal} partition and a `swap`{.literal} volume:

2.  Before running the container, initialize the `output`{.literal} directory. Use the `-p`{.literal} argument to ensure that the command does not fail if the directory already exists:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir -p ./output
    ```

3.  Run `bootc-image-builder`{.literal} to create the ISO image. Use the `--type anaconda-iso`{.literal} flag to ensure the installation program is generated with your Kickstart overrides.

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman run \
        --rm \
        --it \
        --privileged \
        --pull=newer \
        --security-opt label=type:unconfined_t \
        -v /var/lib/containers/storage:/var/lib/containers/storage \
        -v ./config.toml:/config.toml \
        -v ./output:/output \
        registry.redhat.io/rhel10/bootc-image-builder:latest \
        --type anaconda-iso \
        --config /config.toml \
      quay.io/<namespace>/<image>:<tag>
    ```

**Verification**

-   Verify the output:

    ``` {.language-plaintext tabindex="-1"}
    $ ls ./output/bootiso/install.iso
    ```

    You can find the `.anaconda-iso`{.literal} image in the output directory.

**Next steps**

-   You can use the ISO image on unattended installation methods, such as USB sticks or Install-on-boot. The installable boot ISO contains a configured Kickstart file. See [Deploying a container image by using Anaconda and Kickstart](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#deploying-a-container-image-by-using-anaconda-and-kickstart).

    Warning

    Booting the ISO on a machine with an existing operating system or data can be destructive, because the Kickstart is configured to automatically reformat the first disk on the system.

-   You can make updates to the image and push the changes to a registry. See [Managing file system in image mode for RHEL bootable](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#managing-file-systems-in-image-mode-for-rhel).

**Additional resources**

-   [Build and run a bootable container image](https://developers.redhat.com/learn/rhel/build-and-run-bootable-container-image-image-mode-rhel-and-podman-desktop)

### [6.10. Using bootc-image-builder to build ISO images with a Kickstart file](#using-bootc-image-builder-to-build-iso-images-with-a-kickstart-file) {#using-bootc-image-builder-to-build-iso-images-with-a-kickstart-file .title}

You can create an installable ISO image by using the `bootc-image-builder`{.literal} tool. The `anaconda-iso`{.literal} or `iso`{.literal} image type creates a bootable program that uses the Anaconda installer to deploy your `bootc`{.literal} image to a target system.

Important

The creation and deployment of bootable ISO images by using `bootc-image-builder`{.literal} is provided as a Technology Preview. This workflow relies on the `%ostreecontainer`{.literal} Kickstart command, which is a Technology Preview feature. Technology Preview features are not supported with Red Hat production Service Level Agreements (SLAs), might not be functionally complete, and Red Hat does not recommend using them for production. See Technology Preview Features Support Scope for more information.

**Prerequisites**

-   You have Podman installed on your host machine.
-   You have root access to run the `bootc-image-builder`{.literal} tool, and run the containers in `--privileged`{.literal} mode, to build the images.

**Procedure**

1.  Create your Kickstart file. The following Kickstart file is an example of a fully unattended Kickstart file configuration that contains user creation, enables the localization module, and partition instructions.

    ``` {.language-plaintext tabindex="-1"}
    #Enable the Anaconda Localization module on RHEL to enable keyboard or locale changes
    [customizations.installer.modules]
    enable = ["org.fedoraproject.Anaconda.Modules.Localization"]

    [customizations.installer.kickstart]
    contents = """
    lang en_GB.UTF-8
    keyboard uk
    timezone CET

    user --name <user> --password <password> --plaintext --groups <groups>
    sshkey --username <user> ssh-<type> <public key>
    rootpw --lock

    zerombr
    clearpart --all --initlabel
    autopart --type=plain
    reboot --eject
    """
    ```

2.  Save the Kickstart configuration in the `toml`{.literal} format to inject the Kickstart content. For example, `config.toml`{.literal}.

3.  Run `bootc-image-builder`{.literal}, and include the Kickstart file configuration that you want to add to the ISO build. The `bootc-image-builder`{.literal} automatically adds the `ostreecontainer`{.literal} command that installs the container image.

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman run \
        --rm \
        -it \
        --privileged \
        --pull=newer \
        --security-opt label=type:unconfined_t \
        -v /var/lib/containers/storage:/var/lib/containers/storage \
        -v ./config.toml:/config.toml \
        -v ./output:/output \
        registry.redhat.io/rhel10/bootc-image-builder:latest \
        --type iso \
        --config /config.toml \
      quay.io/<namespace>/<image>:<tag>
    ```

    You can find the `.iso`{.literal} image in the output directory.

**Next steps**

-   You can use the ISO image on unattended installation methods, such as USB sticks or Install-on-boot. The installable boot ISO contains a configured Kickstart file. The installation program runs automatically based on the `--non-interactive`{.literal} flag in your Kickstart file, applying the custom LVM partitioning that you defined. See [Deploying a container image by using Anaconda and Kickstart](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#deploying-a-container-image-by-using-anaconda-and-kickstart).

    Warning

    Booting the ISO on a machine with an existing operating system or data can be destructive, because the Kickstart is configured to automatically reformat the first disk on the system.

-   You can make updates to the image and push the changes to a registry. See [Managing RHEL bootable images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#managing-file-systems-in-image-mode-for-rhel).

### [6.11. Building stateless PXE images with bootc-image-builder](#building-stateless-pxe-images-with-bootc-image-builder) {#building-stateless-pxe-images-with-bootc-image-builder .title}

You can use the `bootc-image-builder`{.literal} tool to convert a bootc container image into a `pxe-tar-xz`{.literal} image type with a set of artifacts, such as kernel, initrd, and squashfs rootfs, that is suitable for network booting.

**Prerequisites**

-   A bootc container.
-   The `dracut-live`{.literal} and `squashfs-tools`{.literal} packages are included within your Containerfile.
-   The container image is built with the `dmsquash-live`{.literal} module built into the `initramfs`{.literal}. See the Containerfile for an example.
-   A functional TFTP or HTTP server to host the generated artifacts.

**Procedure**

1.  Create a Containerfile:

    ``` {.language-plaintext tabindex="-1"}
    FROM quay.io/<namespace>/<image>:latest
    RUN dnf -y install dracut-live squashfs-tools && dnf clean all
    # Override using composefs for ostree (it is incompatible with the squashfs rootfs)
    RUN cat <<EOF > /usr/lib/ostree/prepare-root.conf
    [composefs]
    enabled = no
    [sysroot]
    readonly = true
    EOF
    # Include the dmsquash-live module in the initramfs
    RUN cat <<EOF > /usr/lib/dracut/dracut.conf.d/40-pxe.conf
    compress="xz"
    add_dracutmodules+=" qemu qemu-net livenet dmsquash-live "
    early_microcode="no"
    EOF

    # Rebuild the initrd
    RUN set -xe; kver=$(ls /usr/lib/modules); env DRACUT_NO_XATTR=1 dracut -vf /usr/lib/modules/$kver/initramfs.img "$kver"

    # Mask services that aren't compatible with running from the rootfs
    RUN systemctl mask bootc-generic-growpart.service bootc-publish-rhsm-facts.service
    RUN bootc container lint
    ```

2.  Build the container image:

    ``` {.language-plaintext tabindex="-1"}
    $ podman build -f ./Containerfile -t bootc-dracut
    ```

3.  Run `bootc-image-builder`{.literal} to create the `tar`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir -p ./output
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman run \
        --rm \
        -it \
        --privileged \
        --pull=newer \
        --security-opt label=type:unconfined_t \
        -v ./config.toml:/config.toml:ro \
        -v ./output:/output \
        registry.redhat.io/rhel10/bootc-image-builder:latest \
        --type pxe-tar-xz \
        --local \
        localhost/bootc-dracut:latest
    ```

    If your Containerfile is on a remote system, replace the `localhost/bootc-dracut:latest`{.literal} with the correct URL.

    The resulting `tar`{.literal} file is the same as for the package-based `pxe-tar-xz`{.literal} image. The only difference is that the `grub.cfg`{.literal} file also has `ostree=…​`{.literal} added to the kernel command line, and the `rootfs.img`{.literal} file is an OSTree system instead of a package-based system.

**Verification**

Before deploying, verify that the container image was built correctly and contains the necessary configuration files and modules.

1.  Inspect the container you built:

    ``` {.language-plaintext tabindex="-1"}
    $ podman run --rm -it localhost/bootc-dracut:latest /usr/bin/bash
    ```

2.  Verify that the `/usr/lib/ostree/prepare-root.conf`{.literal} and `/usr/lib/dracut/dracut.conf.d/40-pxe.conf`{.literal} files were created correctly.

3.  Check initramfs modules to ensure that `dmsquash-live`{.literal} and `ostree`{.literal} modules are present:

    ``` {.language-plaintext tabindex="-1"}
    $ lsinitrd --mod /usr/lib/modules//initramfs.img*
    ```

**Troubleshooting**

The GRUB menu is not available

:   -   Cause: The EFI binaries or configuration files are misplaced.
    -   Resolution: Verify that the `grub.cfg`{.literal} file is in the same directory as the `grubx64.efi`{.literal} file. Place the `BOOTX64.EFI`{.literal}, `grubx64.efi`{.literal}, and `grub.cfg`{.literal} files at the root of the directory that your TFTP server points to.

The `rootfs.img`{.literal} file fails to load

:   -   Cause: `[FAILED] Failed to start initrd-switch-root.service - Switch Root.`{.literal}
    -   Resolution: Verify that the initramfs includes the `dmsquash-live`{.literal} module.
    -   Cause: `curl`{.literal} is stuck in a loop trying to download the `rootfs.img`{.literal} file: `Warning: failed to download live image: error 253`{.literal}
    -   Resolution: Ensure that the `rootfs.img`{.literal} file is in the location specified by `root=live:…​`{.literal} in the `grub.cfg`{.literal} file. Check the HTTP server logs to verify that the request path matches the expected location.

The OSTree root fails to mount

:   -   Cause: `ostree-prepare-root: Couldn’t find specified OSTree root`{.literal}
    -   Resolution: Ensure that the `grub.cfg`{.literal} file matches the `rootfs.img`{.literal} file, that is, they originate from the same `tar`{.literal} file. The `ostree=…​`{.literal} entry in the `grub.cfg`{.literal} file must point to the path in the `rootfs.img`{.literal} file. A mismatch usually occurs when the `rootfs.img`{.literal} file does not match the `grub.cfg`{.literal} file because the build process sets this UUID from the OSTree directory.
    -   Cause: `Failed to mount composefs: composefs: failed to mount: Input/output error`{.literal}
    -   Resolution: Verify that `composefs`{.literal} is disabled in the `prepare-root.conf`{.literal} file.

### [6.12. Building bootc images in offline and air-gapped environments](#creating-an-image-mode-in-offline-and-air-gapped-environments) {#building-bootc-images-in-offline-and-air-gapped-environments .title}

You can build bootc container images without connecting to the internet or the Red Hat content delivery network. Use the local mirror registries and the RPM repositories, then convert the container images into VM formats of your choice, such as `raw`{.literal}, AMI, or ISO.

Using a disconnected infrastructure requires configuring your build to source container images and RPM content from local registries, for example:

-   Private container registries and RPM repositories hosted on private web servers or Red Hat Satellite.
-   Pull the base image from a local repository instead of from the internet.
-   Your Containerfile must point to a local mirror registry for the base image and use local HTTP servers for RPM content.

After using the `bootc-image-builder`{.literal} command to transform the container into a disk image, you can deploy bootable RHEL-based systems in an air-gapped environment.

Important

Define repository configurations inside the container image you are building. You cannot use the host machine's repository settings with `bootc-image-builder`{.literal}. Instead, you must provide the repository configurations directly within the container image.

**Prerequisites**

-   A running RHEL system with Red Hat Enterprise Linux 10 deployed on the target hardware.
-   The `container-tools`{.literal} meta-package is installed.
-   Access to a registry or a locally stored container.

**Procedure**

1.  Create a Containerfile. For example:

    ``` {.language-plaintext tabindex="-1"}
    # Base image to point to your internal registry
    FROM example.com:1234/rhel10/rhel-bootc:10.2

    # Configure the local repo to use the files already present in the image
    # Assuming the repo data is located at /etc/pki/repos or similar inside the image
    RUN echo -e "[local-baseos]\n\
    name=Local RHEL 10 BaseOS\n\
    baseurl=file:///path/to/repo/in/image/BaseOS\n\
    enabled=1\n\
    gpgcheck=0" > /etc/yum.repos.d/local.repo

    # Install your required packages using the local file source
    RUN dnf install -y firewalld && \
       dnf clean all

    # Ensure the kernel and bootloader are present
    # In air-gapped bootc, BIB often fails because it expects to download these.
    # Pre-installing them ensures they are part of the 'bootc' transition.
    RUN dnf install -y kernel-bootc anaconda-dracut-modules && dnf clean all
    ```

2.  Use the `bootc-image-builder`{.literal} tool to transform the Containerfile into a bootable format, such as ISO, `raw`{.literal}, QCOW2. See [Creating bootc-compatible base disk images by using bootc-image-builder](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/creating-bootc-compatible-base-disk-images-by-using-bootc-image-builder).

**Troubleshooting**

The `raw`{.literal} disk images might succeed if the packages are already cached. If you build an ISO, it might trigger the `osbuild-depsolve-dnf`{.literal} dependency solving process.

If your `.repo`{.literal} files contain a gpgkey URL, `bootc-image-builder`{.literal} tool attempts to fetch the gpg key during the manifest generation phase. In an air-gapped environment, check the following information:

-   Ensure the `gpgkey`{.literal} parameter points to a reachable local HTTP server or a file path already present in the image, such as `/etc/pki/rpm-gpg/`{.literal}.
-   Even if the `dnf install`{.literal} command worked during the container build, because the key was already cached or skipped, the ISO creation process can re-validate these keys. An incorrect URL results in errors such as `GPGKeyReadError`{.literal} or `404 Not Found`{.literal}.
-   To solve these issues, store GPG Keys locally: Instead of referencing remote URLs for GPG keys, include the keys in your container image and reference them by `file:/`{.literal} in your `.repo`{.literal} files.
-   If you encounter a `cannot build manifest`{.literal} error, double-check that every repository URL and GPG URL inside the container's `/etc/yum.repos.d/`{.literal} are reachable from the network on which `bootc-image-builder`{.literal} is running.

**Next steps**

-   You can deploy your image. See [Deploying an image mode update in offline and air-gapped environments](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/deploying-the-rhel-bootc-images#deploying-an-image-mode-update-in-offline-and-air-gapped-environments).

## [Chapter 7. Best practices for running containers by using local sources](#best-practices-for-running-containers-using-local-sources) {#chapter-7.-best-practices-for-running-containers-by-using-local-sources .title}

You can access content hosted in an internal registry that requires a custom Transport Layer Security (TLS) root certificate, when running RHEL bootc images.

You can install content to a container by using only local resources in two way: \* By using the bind mounts: This option overrides the container's store with the host's. \* By using the derived image option: This option creates a new container image with your custom certificates by building it with a `Containerfile`{.literal}.

You can use the same techniques to run a `bootc-image-builder`{.literal} container or a `bootc`{.literal} container when appropriate.

### [7.1. Importing custom certificate to a container by using bind mounts](#importing-custom-certificate-to-a-container-by-using-bind-mounts) {#importing-custom-certificate-to-a-container-by-using-bind-mounts .title}

You can import custom certificates into RHEL containers by using bind mounts to establish trust for private certificate authorities. This allows applications to connect without rebuilding the container image for every credential update.

**Procedure**

-   Run the `bootc-image-builder`{.literal} container and use a bind mount, such as `-v /etc/pki:/etc/pki`{.literal}, to override the container's store with the host's:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman run \
      --rm \
      -it \
      --privileged \
      --pull=newer \
      --security-opt label=type:unconfined_t \
      -v ./output:/output \
      -v /etc/pki:/etc/pki \
      registry.redhat.io/rhel10/bootc-image-builder:latest \
      --type iso \
      --config /config.toml \
      quay.io/<namespace>/<image>:<tag>
    ```

**Verification**

-   The disk image build process can access internal certificates.

### [7.2. Importing custom certificates to an image by using a Containerfile](#importing-custom-certificates-to-a-container-by-using-containerfile) {#importing-custom-certificates-to-an-image-by-using-a-containerfile .title}

You can import custom certificates into your RHEL container image by defining them in a `Containerfile`{.literal}. This enables containerized applications to establish trusted connections with internal services or private certificate authorities.

**Procedure**

1.  Create a `Containerfile`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    FROM <internal_repository>/<image>
    # Add certificate to the input set of anchors
    COPY additional-certificate-root.pem /etc/pki/ca-trust/source/anchors
    RUN update-ca-trust
    ```

2.  Build the custom image:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman build -t <your_image> .
    ```

3.  Run the `<your_image>`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman run -it --rm <your_image>
    ```

**Verification**

-   Verify your certificate is in the generated merged store:

    ``` {.language-plaintext tabindex="-1"}
    # cat etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
    ...
    ```

## [Chapter 8. Deploying RHEL bootc images](#deploying-the-rhel-bootc-images) {#chapter-8.-deploying-rhel-bootc-images .title}

Deploy Red Hat Enterprise Linux bootc images to provision your operating system on physical hardware, virtual machines, or cloud platforms. By using container-native images for deployment, you can standardize system configurations and simplify lifecycle management across your hybrid infrastructure.

### [8.1. Available methods for deploying RHEL bootc images](#available-methods-for-deploying-rhel-bootc-images) {#available-methods-for-deploying-rhel-bootc-images .title}

You can identify the available installation paths for RHEL bootc images to determine the optimal deployment strategy for provisioning containerized operating systems across physical, virtual, or cloud environments.

You can choose the installation method that best fits your infrastructure and deployment requirements.

-   `bootc install`{.literal}: Install a bootc image onto a target system. The `bootc install`{.literal} command handles tasks such as partitioning, configuring the boot loader, and extracting the content of the image to make it bootable.

-   `bootc-image-builder`{.literal}: Use the `bootc-image-builder`{.literal} to convert container images to a bootc image, or create pre-configured disk images to deploy them to a bare metal or to a cloud environment. The following bootc image types are available:

    -   ISO (Technology Preview): Unattended installation method, by using a USB drive or `Install-on-boot`{.literal}.
    -   QCOW2 (QEMU copy-on-write, virtual disk)
    -   Raw (`.dmg`{.literal})
    -   AMI (Amazon Cloud)

-   `Anaconda`{.literal} (Technical Preview): You can use RHEL installer and Kickstart to install the layered image directly to bare metal or virtual machines by using Anaconda with Kickstart automation. This does not required a customized ISO image.

    -   Anaconda installation - Suitable for bare metal, virtual machines, and cloud instances deployment.
    -   PXE (Technology Preview): - You can use existing Anaconda PXE boot environments with modified Kickstart configurations.

Important

Using `bootc-image-builder`{.literal} to create bootable ISOs, the Anaconda and Kickstart workflow are provided as a Technology Preview. These methods are dependent on the `ostreecontainer`{.literal} Kickstart command which is currently a Technology Preview feature only. Technology Preview features are not supported with Red Hat production Service Level Agreements (SLAs), might not be functionally complete, and Red Hat does not recommend using them for production. These previews provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

The installation method happens only one time. After you deploy your image, any future updates will apply directly from the container registry as the updates are published.

**Additional resources**

-   [Deploying a container image from the network by using Anaconda and Kickstart](https://access.redhat.com/articles/7140406)
-   [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview)

### [8.2. Deploying an ISO bootc image over PXE boot](#deploying-an-iso-bootc-image-over-pxe-boot) {#deploying-an-iso-bootc-image-over-pxe-boot .title}

Provision bare metal systems by deploying Red Hat Enterprise Linux bootc ISO images by using PXE boot. By using network-based deployment, you can install bootable container images efficiently without requiring physical media for every machine.

**Prerequisites**

-   You have downloaded a RHEL 10 Boot ISO for your architecture from Red Hat. See [Downloading RHEL boot images](https://access.redhat.com/downloads/content/rhel).

-   You have configured the server for the PXE boot. Choose one of the following options:

    -   For HTTP clients, see [Configuring the DHCPv4 server for HTTP and PXE boot](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/preparing-network-based-repositories#creating-an-installation-source-using-http-or-https).
    -   For UEFI-based clients, see [Configuring a TFTP server for UEFI-based clients](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/preparing-a-uefi-http-installation-source).
    -   For BIOS-based clients, see [Configuring a TFTP server for BIOS-based clients](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/preparing-a-pxe-installation-source#configuring-a-tftp-server-for-bios-based-clients).

-   You have a client, also known as the system to which you are installing your ISO image.

**Procedure**

1.  Export the RHEL installation ISO image to the HTTP server. The PXE boot server is now ready to serve PXE clients.
2.  Boot the client and start the installation.
3.  Select PXE Boot when prompted to specify a boot source. If the boot options are not displayed, press the Enter key on your keyboard or wait until the boot window opens.
4.  From the Red Hat Enterprise Linux boot window, select the boot option that you want, and press Enter.
5.  Start the network installation.

**Next steps**

-   You can push an updated version of this container image to the registry to deliver operating system updates to your running systems. See [Managing RHEL bootc images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#managing-file-systems-in-image-mode-for-rhel).

**Additional resources**

-   [Preparing to install from the network using PXE](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/index#network-install-overview_PXE-installation)
-   [Booting the installation from a network by using PXE](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/interactively_installing_rhel_over_the_network/index#booting-the-installation-from-a-network-using-pxe)

### [8.3. Deploying a container image by using KVM with a QEMU disk image](#deploying-a-container-image-by-using-kvm-with-a-qcow2-disk-image) {#deploying-a-container-image-by-using-kvm-with-a-qemu-disk-image .title}

After you use the `bootc-image-builder`{.literal} tool to convert a bootable RHEL bootc container image into a QEMU disk image (QCOW2), you can use virtualization software to boot the disk image in a virtual machine (VM).

**Prerequisites**

-   You created a QEMU disk image (QCOW2) by using `bootc-image-builder`{.literal}. For instructions, see [Creating QCOW2 images by using bootc-image-builder](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/creating-bootc-compatible-base-disk-images-by-using-bootc-image-builder#creating-qcow2-images-by-using-bootc-image-builder).

**Procedure**

-   Create a VM that uses the disk image that you previously created from the container image.

    The following example uses the `virt-install`{.literal} utility to create a VM named `bootc`{.literal}, with 2 virtual CPUs and 4 GB RAM. Replace *`<qcow2/disk.qcow2>`{.literal}* with the path to your QCOW2 disk image:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo virt-install \
      --name bootc \
      --memory 4096 \
      --vcpus 2 \
      --disk <qcow2/disk.qcow2> \
      --import
    ```

**Verification**

-   Connect to the VM in which you are running the disk image. For instructions, see [Connecting to virtual machines](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/connecting-to-virtual-machines).

**Next steps**

-   You can push an updated version of this container image to the registry to deliver operating system updates to your running systems. See [Managing RHEL bootc images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/managing-rhel-bootc-images).

**Additional resources**

-   [Creating virtual machines by using the command line](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/creating-virtual-machines#creating-virtual-machines-by-using-the-command-line-interface)

### [8.4. Deploying a container image and creating a RHEL virtual machine in vSphere](#deploying-a-container-image-and-creating-a-rhel-virtual-machine-in-vsphere) {#deploying-a-container-image-and-creating-a-rhel-virtual-machine-in-vsphere .title}

After creating a Virtual Machine Disk (VMDK) from a RHEL bootc image by using the `bootc-image-builder`{.literal} tool, you can deploy it to VMware vSphere by using the vSphere GUI client. The deployment creates a VM which can be customized further before booting.

**Prerequisites**

-   You created a container image. See [Creating QCOW2 images by using bootc-image-builder](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/creating-bootc-compatible-base-disk-images-by-using-bootc-image-builder#creating-qcow2-images-by-using-bootc-image-builder).

-   You pushed the container image to an accessible repository.

-   You configured the govc VMware CLI tool client. To use the govc VMware CLI tool client, you must set the following values in the environment:

    -   GOVC_URL
    -   GOVC_DATACENTER
    -   GOVC_FOLDER
    -   GOVC_DATASTORE
    -   GOVC_RESOURCE_POOL
    -   GOVC_NETWORK

**Procedure**

1.  Create a `metadata.yaml`{.literal} file and add the following information to this file:

    ``` {.language-plaintext tabindex="-1"}
    instance-id: cloud-vm
    local-hostname: vmname
    ```

2.  Create a `userdata.yaml`{.literal} file and add the following information to the file:

    ``` {.language-plaintext tabindex="-1"}
    #cloud-config
    users:
    - name: admin
      sudo: "ALL=(ALL) NOPASSWD:ALL"
      ssh_authorized_keys:
      - ssh-rsa AAA...fhHQ== your.email@example.com
    ```

    `ssh_authorized_keys`{.literal} is your SSH public key. You can find your SSH public key in `~/.ssh/id_rsa.pub`{.literal}.

3.  Export the `metadata.yaml`{.literal} and `userdata.yaml`{.literal} files to the environment, compressed with `gzip`{.literal}, encoded in `base64`{.literal} as follows. You will use these files in further steps.

    ``` {.language-plaintext tabindex="-1"}
    export METADATA=$(gzip -c9 <metadata.yaml | { base64 -w0 2>/dev/null || base64; }) \
    USERDATA=$(gzip -c9 <userdata.yaml | { base64 -w0 2>/dev/null || base64; })
    ```

4.  Launch the image on vSphere with the `metadata.yaml`{.literal} and `userdata.yaml`{.literal} files:

    a.  Import the `.vmdk`{.literal} image in to vSphere:

        ``` {.language-plaintext tabindex="-1"}
        $ govc import.vmdk ./composer-api.vmdk <foldername>
        ```

    b.  Create the VM in vSphere without powering it on:

        ``` {.language-plaintext tabindex="-1"}
        govc vm.create \
        -net.adapter=vmxnet3 \
        -m=4096 -c=2 -g=rhel8_64Guest \
        -firmware=bios -disk="foldername/composer-api.vmdk” \
        -disk.controller=ide -on=false \
        vmname
        ```

    c.  Change the VM to add ExtraConfig variables, the cloud-init config:

        ``` {.language-plaintext tabindex="-1"}
        govc vm.change -vm vmname \
        -e guestinfo.metadata="${METADATA}" \
        -e guestinfo.metadata.encoding="gzip+base64" \
        -e guestinfo.userdata="${USERDATA}" \
        -e guestinfo.userdata.encoding="gzip+base64"
        .. Power-on the VM:
        govc vm.power -on vmname
        ```

    d.  Retrieve the VM IP address:

        ``` {.language-plaintext tabindex="-1"}
        HOST=$(govc vm.ip vmname)
        ```

**Verification**

-   Connect to the VM in which you are running the container image. See Connecting to virtual machines for more details.

    a.  Use SSH to log in to the VM, using the user-data specified in `cloud-init`{.literal} file configuration:

        ``` {.language-plaintext tabindex="-1"}
        $ ssh admin@HOST
        ```

**Next steps**

-   You can push an updated version of this container image to the registry to deliver operating system updates to your running systems. See [Managing RHEL bootc images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/managing-rhel-bootc-images).

**Additional resources**

-   [Configuring and managing Linux virtual machines](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_linux_virtual_machines/index)

### [8.5. Deploying a container image to AWS by using an AMI disk image](#deploying-a-container-image-to-aws-with-an-ami-disk-image) {#deploying-a-container-image-to-aws-by-using-an-ami-disk-image .title}

After using the `bootc-image-builder`{.literal} tool to create an AMI from a bootc image, and uploading it to a AWS s3 bucket, you can deploy a container image to AWS by using the AMI disk image.

**Prerequisites**

-   You created an Amazon Machine Image (AMI) from a bootc image. See [Creating AMI images by using bootc-image-builder and uploading them to AWS](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/creating-bootc-compatible-base-disk-images-by-using-bootc-image-builder#creating-ami-images-by-using-bootc-image-builder-and-uploading-them-to-aws).
-   `cloud-init`{.literal} is available in the Containerfile that you previously created so that you can create a layered image for your use case.

**Procedure**

1.  In a browser, access [Service→EC2](https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#Images:sort=name) and log in.

2.  On the AWS console dashboard menu, choose the correct region. The image must have the **Available** status, to indicate that it was correctly uploaded.

3.  On the AWS dashboard, select your image and click Launch.

4.  In the new window that opens, choose an instance type according to the resources you need to start your image. Click Review and Launch.

5.  Review your instance details. You can edit each section if you need to make any changes. Click Launch.

6.  Before you start the instance, select a public key to access it. You can either use the key pair you already have or you can create a new key pair.

7.  Click Launch Instance to start your instance. You can check the status of the instance, which displays as **Initializing**.

    After the instance status is **Running**, the Connect button becomes available.

8.  Click Connect. A window is displayed with instructions on how to connect by using SSH.

9.  Run the following command to set the permissions of your private key file so that only you can read it. See [Connect to your Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html).

    ``` {.language-plaintext tabindex="-1"}
    $ chmod 400 <your-instance-name.pem>
    ```

10. Connect to your instance by using its Public DNS:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -i <your-instance-name.pem>ec2-user@<your-instance-IP-address>
    ```

    Note

    Your instance continues to run unless you stop it.

**Verification**

After launching your image, you can:

-   Try to connect to http://*\<your_instance_ip_address\>* in a browser.
-   Check if you are able to perform any action while connected to your instance by using SSH.

**Next steps**

-   You can push an updated version of this container image to the registry to deliver operating system updates to your running systems.

**Additional resources**

-   [Managing RHEL bootc images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/managing-rhel-bootc-images)
-   [Creating and automatically uploading images to the AWS Cloud AMI](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/composing_a_customized_rhel_system_image/preparing-and-uploading-ami-images-to-aws#creating-and-automatically-uploading-images-to-the-aws-cloud-ami)

### [8.6. Deploying a custom ISO container image in disconnected environments](#deploying-a-custom-iso-container-image) {#deploying-a-custom-iso-container-image-in-disconnected-environments .title}

You can convert a `bootc`{.literal} image to an ISO disk image with your container image content embedded by using the `bootc-image-builder`{.literal} tool. This process enables bare-metal installations without requiring network access.

**Prerequisites**

-   You have created a customized container image.

**Procedure**

1.  Create a custom installer ISO disk image with `bootc-image-builder`{.literal}. See [Creating ISO images by using bootc-image-builder](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/creating-bootc-compatible-base-disk-images-by-using-bootc-image-builder#creating-iso-images-by-using-bootc-image-builder).
2.  Copy the ISO disk image to a USB flash drive.
3.  Perform a bare-metal installation by using the content in the USB stick into a disconnected environment.

**Next steps**

-   After you deploy your container image, you can push an updated version of this container image to the registry to deliver operating system updates to your running systems. See [Managing RHEL bootc images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/managing-rhel-bootc-images).

### [8.7. Advanced installation with to-filesystem and to-disk](#advanced-installation-with-to-filesystem) {#advanced-installation-with-to-filesystem-and-to-disk .title}

You can install RHEL image mode content directly to a mounted file system to support advanced provisioning. You can populate custom partition layouts or generate bootable disk images without requiring a standard installer boot process by using the `bootc-install-to-filesystem`{.literal} command.

The `bootc install`{.literal} command contains two subcommands:

-   The `bootc-install-to-filesystem`{.literal} performs installation to the target filesystem.

-   The `bootc install to-disk`{.literal} subcommand consists of a set of opinionated lower-level tools that you can also call independently. The command consists of the following tools:

    -   `mkfs.$fs /dev/disk`{.literal}
    -   `mount /dev/disk /mnt`{.literal}
    -   `bootc install to-filesystem --karg=root=UUID=`{.literal}*`<uuid of /mnt>`{.literal}*` --imgref $self /mnt`{.literal}

### [8.8. Deploy a bootc image on bare metal by using the Red Hat Enterprise Linux 10 boot ISO](#deploying-a-container-image-by-using-bootc) {#deploy-a-bootc-image-on-bare-metal-by-using-the-red-hat-enterprise-linux-10-boot-iso .title}

To deploy a `bootc`{.literal} container image to a bare-metal system manually by using the `RHEL 10`{.literal} boot `ISO`{.literal} environment, you can perform the steps from an interactive console while accounting for the `RAM`{.literal}-backed environment.

**Prerequisites**

-   The target bare-metal host is booted into the `RHEL 10`{.literal} installation `ISO`{.literal} environment.
-   You have network connectivity configured to reach `registry.redhat.io`{.literal} or your internal container registry.
-   You have a target storage disk available, such as `/dev/vda`{.literal} or `/dev/sda`{.literal}.
-   You have a secondary physical disk or storage device available for scratch space, separate from the target installation disk.
-   You have a custom `bootc`{.literal} container image available in a reachable registry, for example, `quay.io/<namespace>/my-rhel-bootc:latest`{.literal}.

**Procedure**

1.  Boot the target system by using the RHEL 10 boot `ISO`{.literal} environment.

2.  When the initial Anaconda graphical or text installer screen is displayed, press `Ctrl+Alt+F2`{.literal} to switch to a virtual console.

3.  Press **Enter** to activate the root shell prompt:

    ``` {.language-plaintext tabindex="-1"}
    [anaconda root@localhost /]#
    ```

4.  Prepare the physical storage for temporary scratch space.

    Warning

    The `Anaconda`{.literal} live environment runs entirely on a memory-constrained `RAM`{.literal} disk (`tmpfs`{.literal}). Extracting large `bootc`{.literal} container images into `RAM`{.literal}-backed paths, such as the default `/var/tmp`{.literal}, can cause `No space left on device`{.literal} errors during `ostree`{.literal} layer write operations.

    To prevent out-of-space errors, you **must** mount a secondary physical disk to `/var/lib/containers`{.literal}. This disk must be separate from the target installation disk. If the secondary disk is on the same physical disk used by `bootc install to-disk`{.literal}, the scratch partition is overwritten during the installation process.

    This means that installation to a single-disk system by using this method is not supported unless you have additional storage available for scratch space.

5.  Format and mount the secondary disk directly to `/var/lib/containers`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo mkfs.xfs -f /dev/vdb
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ sudo mkdir -p /var/lib/containers
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ sudo mount /dev/vdb /var/lib/containers
    ```

    Replace `/dev/vdb`{.literal} with your secondary disk device path.

6.  Create a temporary directory on the same physical storage and set the `TMPDIR`{.literal} environment variable:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo mkdir -p /var/lib/containers/tmp
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ sudo export TMPDIR=/var/lib/containers/tmp
    ```

7.  Install the required `fuse-overlayfs`{.literal} package inside the LiveOS environment:

    Important

    In the `RHEL`{.literal} boot `ISO`{.literal} runtime environment, the root filesystem is already available on an `overlayfs`{.literal} mount. Standard Linux kernel overlay mounts cannot be nested over existing overlay filesystems. You must use `fuse-overlayfs`{.literal} for user-space mounting. Because `fuse-overlayfs`{.literal} is not included in the default boot ISO image, you must install it by using `dnf`{.literal} before executing container commands.

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dnf install -y fuse-overlayfs
    ```

8.  Authenticate to your container registry:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman --storage-driver=overlay \
           --storage-opt overlay.mount_program=/usr/bin/fuse-overlayfs \
           login registry.redhat.io
    ```

9.  Run the `bootc`{.literal} installation to deploy the target container image. Replace `<your-bootc-container-image>`{.literal} with your container image registry URL and `<target-device>`{.literal} with your target disk path, for example, `/dev/sda`{.literal} or `/dev/vda`{.literal}:

    Note

    -   The `--network=host`{.literal} flag is required to avoid `netavark`{.literal} or `nftables`{.literal} errors in the Anaconda environment. This allows the container to use the existing network configuration rather than attempting to create a new network namespace.
    -   The bind mount `-v /var/lib/containers:/var/lib/containers`{.literal} ensures the `bootc`{.literal} installer container can access the container layers pulled in the previous steps.

    -   **Option A**: To install directly to a target disk without custom partitioning, use `bootc install to-disk`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo podman --storage-driver=overlay \
               --storage-opt overlay.mount_program=/usr/bin/fuse-overlayfs \
               run --rm --privileged --pid=host --network=host \
               -v /dev:/dev \
               -v /var/lib/containers:/var/lib/containers \
               --security-opt label=type:unconfined_t \
               <your-bootc-container-image> \
               bootc install to-disk <target-device>
        ```

    -   **Option B**: To install to a pre-configured target directory with custom filesystem layout, partition scheme, or LVM setup, use `bootc install to-filesystem`{.literal}:

        Important

        When using `bootc install to-filesystem`{.literal}, you must prepare and mount both the root file system and any platform-specific partitions required for your boot mode, such as the EFI System Partition for UEFI systems, before running the installation. The boot loader installation will fail if required platform partitions are not mounted at the expected locations under the target directory.

        a.  Bind-mount `/var/tmp`{.literal} to storage on the secondary disk to provide additional temporary space for the image import process:

            ``` {.language-plaintext tabindex="-1"}
            $ sudo mkdir -p /var/lib/containers/var-tmp
            ```

            ``` {.language-plaintext tabindex="-1"}
            $ sudo chmod 1777 /var/lib/containers/var-tmp
            ```

            ``` {.language-plaintext tabindex="-1"}
            $ sudo mount --bind /var/lib/containers/var-tmp /var/tmp
            ```

            Note

            This additional bind mount is required for `bootc install to-filesystem`{.literal} because the image import process writes temporary files to `/var/tmp/container_images_*`{.literal}, which cannot be redirected by the `TMPDIR`{.literal} environment variable alone.

        b.  Prepare your target partitions and filesystems. For UEFI systems, create both an ESP partition and root partition:

            ``` {.language-plaintext tabindex="-1"}
            $ sudo parted /dev/vda --script mklabel gpt
            ```

            ``` {.language-plaintext tabindex="-1"}
            $ sudo parted /dev/vda --script mkpart primary fat32 1MiB 601MiB
            ```

            ``` {.language-plaintext tabindex="-1"}
            $ sudo parted /dev/vda --script set 1 esp on
            ```

            ``` {.language-plaintext tabindex="-1"}
            $ sudo parted /dev/vda --script mkpart primary xfs 601MiB 100%
            ```

            ``` {.language-plaintext tabindex="-1"}
            $ sudo mkfs.vfat -F32 /dev/vda1
            ```

            ``` {.language-plaintext tabindex="-1"}
            $ sudo mkfs.xfs /dev/vda2
            ```

        c.  Mount the target filesystems at `/target`{.literal}:

            ``` {.language-plaintext tabindex="-1"}
            $ sudo mkdir -p /target
            ```

            ``` {.language-plaintext tabindex="-1"}
            $ sudo mount /dev/vda2 /target
            ```

            ``` {.language-plaintext tabindex="-1"}
            $ sudo mkdir -p /target/boot/efi
            ```

            ``` {.language-plaintext tabindex="-1"}
            $ sudo mount /dev/vda1 /target/boot/efi
            ```

            Note

            For firmware systems, you do not need to create or mount an ESP partition. Only the root filesystem mount at `/target`{.literal} is required. Consult your platform's boot requirements to determine which partitions are necessary.

        d.  Run the installation:

            ``` {.language-plaintext tabindex="-1"}
            $ sudo podman --storage-driver=overlay \
                   --storage-opt overlay.mount_program=/usr/bin/fuse-overlayfs \
                   run --rm --privileged --pid=host --network=host \
                   -v /target:/target \
                   -v /dev:/dev \
                   -v /var/lib/containers:/var/lib/containers \
                   --security-opt label=type:unconfined_t \
                   <your-bootc-container-image> \
                   bootc install to-filesystem /target
            ```

        e.  Unmount the temporary scratch directory after the installation completes:

            ``` {.language-plaintext tabindex="-1"}
            $ sudo umount /var/tmp
            ```

            ``` {.language-plaintext tabindex="-1"}
            $ sudo umount /var/lib/containers
            ```

        f.  Reboot the system to initialize your new RHEL `bootc`{.literal} operating system:

            ``` {.language-plaintext tabindex="-1"}
            $ reboot
            ```

**Next steps**

-   After you deploy your container image to a bare-metal environment, you can push an updated version of this container image to the registry to deliver operating system updates to your running systems. See [Managing RHEL bootable images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#managing-file-systems-in-image-mode-for-rhel).

### [8.9. Deploying a container image by using a single command](#deploying-a-container-image-by-using-a-single-command) {#deploying-a-container-image-by-using-a-single-command .title}

Deploy a container image to a RHEL cloud instance by using the `system-reinstall-bootc`{.literal} command. With a single command, you can deploy a bootc image to a new RHEL instance, such as RHEL 10 on AWS. It requires you to select or create an SSH key during instance launch for secure access.

The `system-reinstall-bootc`{.literal} command provides an interactive CLI that wraps the `bootc install to-existing root`{.literal} command and can perform two actions: 

-   Pull the supplied image to configure SSH keys or access the system.
-   Run the `bootc install to-existing-root`{.literal} command with all the bind mounts and SSH keys configured.

**Prerequisites**

-   A Red Hat Account or Access to Red Hat RPMs.
-   A package-based RHEL (9.6 / 10.0 or higher) virtual system running in an AWS environment.
-   Ability and permissions to SSH into the package system and make destructive changes.

**Procedure**

1.  After the instance starts, connect to it by using SSH using the key you selected when creating the instance:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh -i <ssh-key-file> <cloud-user@ip>
    ```

2.  Ensure the `system-reinstall-bootc`{.literal} subpackage is installed:

    ``` {.language-plaintext tabindex="-1"}
    # rpm -q system-reinstall-bootc
    ```

    If not, install the `system-reinstall-bootc`{.literal} subpackage:

    ``` {.language-plaintext tabindex="-1"}
    # dnf -y install system-reinstall-bootc
    ```

3.  Convert the system to use a bootc image:

    ``` {.language-plaintext tabindex="-1"}
    # system-reinstall-bootc <image>
    ```

    You can use the container image from the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/search?gs&q=bootc) or the customized bootc image built from a Containerfile.

4.  Select users to import to the bootc image by pressing the `a`{.literal} key.

5.  Confirm your selection twice and wait until the image is downloaded.

6.  Reboot the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

7.  Remove the stored SSH host key for the given `<ip>`{.literal} from your `/.ssh/known_hosts`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # ssh-keygen -R <ip>
    ```

    The bootc system is using a new public SSH host key. When attempting to connect to the same IP address with a different key than what is stored locally, SSH issues a warning or refuse the connection due to a host key mismatch. Since this change is expected, the existing host key entry can be safely removed from the `~/.ssh/known_hosts`{.literal} file using the following command:

8.  Connect to the bootc system:

    ``` {.language-plaintext tabindex="-1"}
    # ssh -i <ssh-key-file> root@<ip>
    ```

**Verification**

-   Confirm that the system operating system has changed:

    ``` {.language-plaintext tabindex="-1"}
    # bootc status
    ```

### [8.10. Accessing private bootc container registries](#accessing-private-bootc-container-registries) {#accessing-private-bootc-container-registries .title}

You can use private container registries on your bootc deployments. The bootc images use pull secrets, enabling you to use private images to manage your system provisioning.

#### [8.10.1. Enabling bootc to access private registries](#enabling-bootc-to-access-private-registries) {#enabling-bootc-to-access-private-registries .title}

The `bootc`{.literal} has no way to disable TLS verification when accessing a registry. You can globally disable TLS verification when accessing a private registry by using the `/etc/containers/registries.conf.d`{.literal} configuration.

**Prerequisites**

-   You have access to a private registry.

**Procedure**

-   Disable the TLS verification:

    ``` {.language-plaintext tabindex="-1"}
    # /etc/containers/registries.conf.d/local-registry.conf
    [[registry]]
    location="localhost:5000"
    insecure=true
    ```

**Verification**

-   Check if you disabled TLS verification.

**Next steps**

-   Configure bootc to access private registries.

#### [8.10.2. Configuring bootc to access private registries](#configuring-bootc-to-access-private-registries) {#configuring-bootc-to-access-private-registries .title}

You can pull container images from private registries by symlinking the `bootc`{.literal} and Podman credential paths to a common persistent file embedded in your container image. This maintains a single source of truth for pull secrets across your environment.

**Prerequisites**

-   `Bootc`{.literal} provides private access to registries.

**Procedure**

1.  Create the `/usr/lib/container-auth.json`{.literal} registry authentication file and add the following content:

    ``` {.language-plaintext tabindex="-1"}
    # Make /run/containers/0/auth.json (a transient runtime file)
    # a symlink to our /usr/lib/container-auth.json (a persistent file)
    # which is also symlinked from /etc/ostree/auth.json.
    d /run/containers/0 0755 root root -
    L /run/user/0/containers/auth.json - - - - ../../../../usr/lib/container-auth.json
    ```

2.  In the same directory, create a Containerfile. For example:

    ``` {.language-plaintext tabindex="-1"}
    # This example expects a secret named "creds" to contain
    # the registry pull secret.  To build, for example
    # podman build --secret id=creds,src=$HOME/.docker/config.json ...
    FROM quay.io/<namespace>/<image>:_<tag>_
    # Use a single pull secret for bootc and podman by symlinking both locations
    # to a common persistent file embedded in the container image.
    # We just make up /usr/lib/container-auth.json
    COPY containers-auth.conf /usr/lib/tmpfiles.d/link-podman-credentials.conf
    RUN --mount=type=secret,id=creds,required=true cp /run/secrets/creds /usr/lib/container-auth.json && \
        chmod 0600 /usr/lib/container-auth.json && \
        ln -sr /usr/lib/container-auth.json /etc/ostree/auth.json
    ```

    Embedding these settings ensures that specific kernel options are consistently applied to any system provisioned from the container image, eliminating the need for post-deployment configuration.

3.  Place the `container-auth.json`{.literal} file at `/etc/ostree/auth.json`{.literal} to configure the private registry authentication.

#### [8.10.3. Configuring private bootc container registries with an Anaconda Kickstart script](#configuring-private-bootc-container-registries-with-an-anaconda-script) {#configuring-private-bootc-container-registries-with-an-anaconda-kickstart-script .title}

To install a bootable container from a private registry by using Anaconda, configure authentication for the runtime and target systems. Automate this by adding `%pre`{.literal} and `%post`{.literal} scripts to your Kickstart file that generate the `/etc/ostree/auth.json`{.literal} file.

Warning

Kickstart files that contain registry credentials or other secrets can expose sensitive information if they are stored insecurely.

Set file permissions to `600`{.literal} on any Kickstart file that contains secrets. After installation, Anaconda saves a copy of the Kickstart file to `/root/anaconda-ks.cfg`{.literal} on the target system. Remove credential values from that file, restrict its permissions, or delete it if you no longer need it.

**Prerequisites**

-   You have access to a private registry, such as `quay.io`{.literal}, that hosts your `bootc`{.literal} container image.
-   You have the registry user name and password or a service account token, that can pull the `bootc`{.literal} image.

**Procedure**

1.  Optional: You can obtain a ready-made authentication string through the web interface of your container registry. If you do not have the string, you can generate it from your registry credentials by running the following command on your local machine to generate a base64-encoded authentication string without saving your credentials to your shell history or environment variables:

    ``` {.language-plaintext tabindex="-1"}
    $ read -rsp "Enter credentials (user:pass): " creds && echo && echo -n "$creds" | base64 -w0 && echo && unset creds
    ```

2.  Copy the generated base64-encoded output string.

3.  Open your Kickstart file in a text editor, and add the `%pre`{.literal} script section to configure registry authentication for the Anaconda installation runtime. Replace *`<your_base64_secret>`{.literal}* with your generated string and `quay.io`{.literal} with your target registry host:

    ``` {.language-plaintext tabindex="-1"}
    %pre
    mkdir -p /etc/ostree
    cat > /etc/ostree/auth.json << 'EOF'
    {
            "auths": {
                    "quay.io": {
                            "auth": "<your_base64_secret>"
                    }
            }
    }
    EOF
    %end
    ```

4.  Add the `%post`{.literal} script section to your Kickstart file to configure registry authentication for the installed target system to enable post-boot updates. Replace `<your_base64_secret>`{.literal} with your generated string and `quay.io`{.literal} with your target registry host:

    ``` {.language-plaintext tabindex="-1"}
    %post
    mkdir -p /etc/ostree
    cat > /etc/ostree/auth.json << 'EOF'
    {
            "auths": {
                    "quay.io": {
                            "auth": "<your_base64_secret>"
                    }
            }
    }
    EOF
    %end
    ```

#### [8.10.4. Accessing private registries with pull secrets on Anaconda](#accessing-private-registries-with-pull-secrets-on-anaconda) {#accessing-private-registries-with-pull-secrets-on-anaconda .title}

You can use the Anaconda `%pre`{.literal} command to perform arbitrary changes to the installation environment, including providing a duplicate bootstrap configuration to authenticate and fetch the target `bootc`{.literal} container image from the registry over the network.

**Prerequisites**

-   `Bootc`{.literal} provides private access to registries.

**Procedure**

1.  Configure the pull secret. The following is an example:

    ``` {.language-plaintext tabindex="-1"}
    %pre
    mkdir -p /etc/ostree
    cat > /etc/ostree/auth.json << 'EOF'
    {
            "auths": {
                    "quay.io": {
                            "auth": "<your secret here>"
                    }
            }
    }
    EOF
    %end
    ```

2.  Disable TLS for an insecure registry:

    ``` {.language-plaintext tabindex="-1"}
    %pre
    mkdir -p /etc/containers/registries.conf.d/
    cat > /etc/containers/registries.conf.d/local-registry.conf << 'EOF'
    [[registry]]
    location="[IP_Address]:5000"
    insecure=true
    EOF
    %end
    ```

#### [8.10.5. Anaconda access to private bootc container registries](#anaconda-access-to-private-bootc-container-registries) {#anaconda-access-to-private-bootc-container-registries .title}

When performing a network-based installation by using a default Anaconda ISO, the installation environment itself cannot access the target bootc container registry if it is private or insecure.

The Anaconda runs first, then it fetches the bootc container image to install. The Anaconda fails if the image is on a private registry that requires authentication or an insecure registry that requires disabled TLS, because it lacks a default bootstrap configuration.

To solve this, you can inject a duplicate copy of the necessary configuration into the installation environment before it pulls the image.

You can solve this issue by following one of the following solutions:

-   Use Anaconda `%pre`{.literal} scripts to configure a pull secret.
-   Use Anaconda `%pre`{.literal} scripts to disable TLS for an insecure registry.

### [8.11. Deploying an image mode update in offline and air-gapped environments](#deploying-an-image-mode-update-in-offline-and-air-gapped-environments) {#deploying-an-image-mode-update-in-offline-and-air-gapped-environments .title}

With image mode for Red Hat Enterprise Linux, you can deploy updates to RHEL systems in offline and air-gapped environments by using external storage to transfer container images.

To deploy an image mode update onto a host machine, you need a network connection to access a registry and get updates. However, when your operational environment requires specific architectural factors, such as hardware specifications, stringent security mandates, location-based network limitations, or scheduled updates when remote access is unavailable, you can perform system updates fully offline and air-gapped.

Note

Offline updates can be time-consuming when you use them on many devices and might require on-site capability to deploy the updates.

**Prerequisites**

-   A running RHEL system containing the updates that you want to make to the system.
-   A running RHEL system with Red Hat Enterprise Linux 10 deployed on the target hardware.
-   The `container-tools`{.literal} meta-package is installed. The `meta-package`{.literal} contains all container tools, such as Podman, Buildah, and Skopeo.
-   Access to a registry or a locally stored container.
-   An external storage device for the container requires an update.

**Procedure**

1.  Verify which storage devices are already connected to your system.

    ``` {.language-plaintext tabindex="-1"}
    $ lsblk
    NAME          MAJ:MIN     SIZE   RO TYPE  MOUNTPOINTS
    zram0           251:0       8G    0 disk  [SWAP]
    nvme0n1         259:0   476.9G    0 disk
    ├─nvme0n1p1    259:1     600M    0 part  /boot/efi
    ├─nvme0n1p2    259:2       1G    0 part  /boot
    └─nvme0n1p3    259:3   475.4G    0 part
    ```

2.  Connect your external storage and run the same command. Compare the two outputs to find the name of your external storage device on your system.

    ``` {.language-plaintext tabindex="-1"}
    $ lsblk
    NAME        MAJ:MIN   SIZE   RO TYPE  MOUNTPOINTS
    sda             8:0   28.9G    0 disk
    └─sda1         8:1   28.9G    0 part
    zram0         251:0      8G    0 disk  [SWAP]
    nvme0n1       259:0  476.9G    0 disk
    ├─nvme0n1p1  259:1    600M    0 part  /boot/efi
    ├─nvme0n1p2  259:2      1G    0 part  /boot
    └─nvme0n1p3  259:3  475.4G    0 part
    ```

    In this case, the USB drive whose name is `sda`{.literal} has an `sda1`{.literal} partition.

    The `MOUNTPOINTS`{.literal} column lists the mount points of the partitions on your external storage. If your system automatically mounts external storage, then valid mount points already exist. However, if there are no mount points, you must mount it yourself before you can store anything on the device.

3.  Create an empty directory, or use an existing one, to mount your partition:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo mkdir /mnt/usb/
    ```

    a.  Mount your device partition.

        ``` {.language-plaintext tabindex="-1"}
        $ sudo mount /dev/sda1 /mnt/usb
        ```

    b.  Optional: Verify if the partition was correctly created:

        ``` {.language-plaintext tabindex="-1"}
        $ lsblk
        NAME         MAJ:MIN    SIZE   RO TYPE  MOUNTPOINTS
        sda              8:0   28.9G    0 disk
        └─sda1          8:1   28.9G    0 part  /mnt/usb
        [...]
        ```

        Your external storage device is ready for copying files onto it.

4.  Copy the container stored locally to your mounted device by using the `skopeo`{.literal} command, and adapting the paths and names of the container for your own environment:

    -   For local storage:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo skopeo copy --preserve-digests --all \
          containers-storage:localhost/rhel-container:latest \
          oci://mnt/usb/
        ```

    -   For a container stored on a remote registry:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo skopeo copy --preserve-digests --all \
          docker://quay.io/example:latest \
          oci://mnt/usb/
        ```

        Note

        Depending on the size of the container, these commands might take a few minutes to complete.

5.  Unmount and eject the external storage:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo umount /dev/sda1
    $ sudo eject /dev/sda1
    ```

6.  Apply the update to the container on the offline system.

7.  Plug the external storage device into your offline system. If the storage device does not mount automatically, use the `mkdir`{.literal} and `mount`{.literal} commands to locate the external storage and mount it.

8.  Copy the container from the external device over to the offline system's local container registry. Copy the container to the offline machine's local container storage:

    ``` {.language-plaintext tabindex="-1"}
    $ skopeo copy --preserve-digests --all \
      oci://mnt/usb \
      containers-storage:rhel-update:latest
    ```

    In this case, the mount point of the external storage is the path to the `OCI`{.literal} section. The `containers-storage`{.literal} section varies depending on the name and tag you want the container to have.

9.  Use Podman to verify that your container is now local:

    ``` {.language-plaintext tabindex="-1"}
    $ podman images
    REPOSITORY                  TAG     IMAGE ID  CREATED  SIZE
    example.io/library/rhel-update   latest  cdb6d...  1 min    1.48 GB
    ```

10. Deploy the update to the container on the offline system by using `bootc`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ bootc switch --transport containers-storage \
    example.io/library/rhel-update:latest
    ```

    a.  If you cannot copy your container to local storage, use the *`oci transport`{.literal}* flag and the path to your storage device instead:

        ``` {.language-plaintext tabindex="-1"}
        $ bootc switch --transport oci /mnt/usb
        ```

        With the `--transport`{.literal} flag in the `bootc switch`{.literal} command, you can specify an alternative source for the container.

        By default, `bootc`{.literal} attempts to pull from a registry because the `bootc-image-builder`{.literal} uses a registry to build the original image. When using `bootc upgrade`{.literal}, you cannot specify where an update is located. By using the `bootc switch`{.literal} and specifying that you are using local container storage, you cannot only remove the requirement of a remote registry, but also deploy updates by using this local container in the future.

        You can now successfully use the `bootc upgrade`{.literal}, provided that your local container and the update share the same location. If you want to switch to updates on a remote repository in the future, you must use `bootc switch`{.literal} again.

**Verification**

1.  Ensure that the update was properly deployed:

    ``` {.language-plaintext tabindex="-1"}
    $ bootc status
    Staged image: containers-storage:example.io/library/rhel-update:latest
      Digest: sha256: 05b1dfa791...
      Version: 10.0 (2025-07-07 18:33:19.380715153 UTC)
    Booted Image: localhost/rhel-intel:base
      Digest: sha256: 7d6f312e09...
      Version: 10.0 (2025-06-23 15:58:12.228704562 UTC)
    ```

    The output shows your current booted image, along with any changes staged to happen. The container you used earlier is visible, but the staged changes do not happen until the next reboot. The output also confirms that updates will be pulled from your container storage.

2.  Reboot the system:

    ``` {.language-plaintext tabindex="-1"}
    $ bootc status
    Booted image: containers-storage:example.io/library/rhel-update:latest
        Digest: sha256: 05b1dfa791...
        Version: 10.0 (2025-07-07 18:33:19.380715153 UTC)
    Rollback image: localhost/rhel-intel:base
        Digest: sha256: 7d6f312e09...
        Version: 10.0 (2025-06-23 15:58:12.228704562 UTC)
    ```

    You can verify that you have booted into the correct image:

    -   The booted image is your updated image.
    -   The rollback image is your previous image. You have successfully performed an offline image mode update.

**Additional resources**

-   [Image mode for Red Hat Enterprise Linux: A quick start guide](https://www.redhat.com/en/blog/image-mode-red-hat-enterprise-linux-quick-start-guide)
-   [How to manage Linux container registries](https://www.redhat.com/en/blog/manage-container-registries)

## [Chapter 9. Creating bootc images from scratch](#generating-a-custom-minimal-base-image) {#chapter-9.-creating-bootc-images-from-scratch .title}

You can create a `bootc`{.literal} image from scratch by using an existing `bootc`{.literal} base image as a build environment with RPM packages as input. This provides you control over the underlying image content and allows you to reduce the system footprint and attack surface by including only the packages essential for your workload.

### [9.1. Using pinned content to build images](#using-pinned-content-to-build-images) {#using-pinned-content-to-build-images .title}

To maintain reproducible builds, you can use repository snapshot tools to pin a base image to specific package versions. This ensures that `rpm-md`{.literal} or `yum`{.literal} repositories remain consistent with the lockfiles of your project.

With the `bootc image from scratch`{.literal} feature, you can configure and override package information in source RPM repositories, while referencing mirrored, pinned, or snapshotted repository content. Consequently, you gain control over package versions and their dependencies.

**Prerequisites**

-   A standard bootc base image.

**Procedure**

-   The following example creates a bootc image from scratch with pinned content:

    ``` {.language-plaintext tabindex="-1"}
    # Begin with a standard bootc base image that serves as a "builder" for our custom image.
    FROM registry.redhat.io/rhel10/rhel-bootc:latest as builder
    # Configure and override source RPM repositories, if necessary. The following step is required when referencing specific content views or target mirrored/snapshotted/pinned versions of content.
    RUN rm -rvf /etc/yum.repos.d; mkdir -p /etc/yum.repos.d/
    COPY mypinnedcontent.repo /etc/yum.repos.d/
    # The file must be copied to the /etc/yum.repos.d/ directory.
    # The mypinnedcontent.repo is your standard repository that ensures that your container will always be built with the exact same versions of software, preventing unexpected bugs or security issues from new updates.
    # Build the root file system using the specified repositories and non-RPM content from the "builder" base image.
    # If no repositories are defined, the default build will be used. You can modify the scope of packages in the base image by changing the manifest between the "standard" and "minimal" sets.
    # Add additional repositories to apply customizations to the image. However, referencing a custom manifest in this step is not currently supported without forking the code.
    RUN /usr/libexec/bootc-base-imagectl build-rootfs --manifest=standard /target-rootfs
    # Create a new, empty image from scratch.
    FROM scratch
    # Copy the root file system built in the previous step into this image.
    COPY --from=builder /target-rootfs/ /
    # Apply customizations to the image. This syntax uses "heredocs" https://www.docker.com/blog/introduction-to-heredocs-in-dockerfiles/ to pass multi-line arguments in a more readable format.
    RUN <<EORUN
    # Set pipefail to display failures within the heredoc and avoid false-positive successful builds.
    set -xeuo pipefail
    # Install necessary packages, run scripts, etc.
    dnf -y install NetworkManager emacs
    # Remove leftover build artifacts from installing packages in the final built image.
    dnf clean all
    rm /var/{log,cache,lib}/* -rf
    EORUN
    # Define required labels for this bootc image to be recognized as such.
    LABEL containers.bootc 1
    LABEL ostree.bootable 1
    # Optional labels that only apply when running this image as a container. These keep the default entry point running under systemd.
    STOPSIGNAL SIGRTMIN+3
    CMD ["/sbin/init"]
    # Run the bootc linter to avoid encountering certain bugs and maintain content quality. Place this command last in your Containerfile.
    RUN bootc container lint
    ```

**Verification**

1.  Save and build your image.

    ``` {.language-plaintext tabindex="-1"}
    $ podman build -t quay.io/<namespace>/<image>:<tag> . --cap-add=all --security-opt=label=type:container_runtime_t --device /dev/fuse
    ```

2.  Build \<\_image\_\> image by using the `Containerfile`{.literal} in the current directory:

    ``` {.language-plaintext tabindex="-1"}
    $ podman build -t quay.io/<namespace>/<image>:<tag> .
    ```

### [9.2. Building a base image up from minimal](#building-up-from-minimal) {#building-a-base-image-up-from-minimal .title}

To control the final image content, generate a minimal `bootc`{.literal} image that contains only the `bootc`{.literal} utility, the kernel, and the DNF package manager. You can use this lightweight image as a foundational layer for multi-stage builds.

**Prerequisites**

-   A standard bootc base image.

**Procedure**

-   The following example creates a custom minimal base image:

    ``` {.language-plaintext tabindex="-1"}
    # Begin with a standard bootc base image that is reused as a "builder" for the custom image.
    FROM registry.redhat.io/rhel10/rhel-bootc:latest as builder
    # Configure and override source RPM repositories, if necessary. This step is not required when building up from minimal unless referencing specific content views or target mirrored/snapshotted/pinned versions of content.
    # Add additional repositories to apply customizations to the image. However, referencing a custom manifest in this step is not currently supported without forking the code.
    # Build the root file system by using the specified repositories and non-RPM content from the "builder" base image.
    # If no repositories are defined, the default build will be used. You can modify the scope of packages in the base image by changing the manifest between the "standard" and "minimal" sets.
    RUN /usr/libexec/bootc-base-imagectl build-rootfs --manifest=minimal /target-rootfs
    # Create a new, empty image from scratch.
    FROM scratch
    # Copy the root file system built in the previous step into this image.
    COPY --from=builder /target-rootfs/ /
    # Apply customizations to the image. This syntax uses "heredocs" https://www.docker.com/blog/introduction-to-heredocs-in-dockerfiles/ to pass multi-line arguments in a more readable format.
    RUN <<EORUN
    # Set pipefail to display failures within the heredoc and avoid false-positive successful builds.
    set -xeuo pipefail
    # Install required packages for our custom bootc image.
    # Note that using a minimal manifest means we need to add critical components specific to our use case and environment.
    dnf -y install NetworkManager openssh-server
    # Remove package caches
    dnf clean all
    # Clean up all logs and caches
    rm /var/{log,cache,lib}/* -rf
    # Run the bootc linter to perform build-time verification. Keep this as the last command in your build instructions.
    bootc container lint
    # Close the shell command.
    EORUN
    # Define required labels for this bootc image to be recognized as such.
    LABEL containers.bootc 1
    LABEL ostree.bootable 1
    # Optional labels that only apply when running this image as a container. These keep the default entry point running under systemd.
    STOPSIGNAL SIGRTMIN+3
    CMD ["/sbin/init"]
    ```

    Note

    This minimal image is currently not shipped pre-built in the registry and must be generated locally.

### [9.3. Building required privileges](#building-required-privileges) {#building-required-privileges .title}

Generating a root filesystem from scratch requires the inner build process to use some nested containerization (such as mount namespacing) that are not enabled by default.

**Prerequisites**

-   The `container-tools`{.literal} meta-package is installed.

**Procedure**

-   Generate a new root file system, providing these arguments at a minimum to `podman build`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    --cap-add=all --security-opt=label=type:container_runtime_t --device /dev/fuse
    ```

### [9.4. Generating your bootc images from scratch](#generating-your-custom-minimal-base-image) {#generating-your-bootc-images-from-scratch .title}

You can generate a custom minimal base image for your RHEL applications. This reduces the system footprint and attack surface by ensuring that only essential packages are included in the final deployment.

**Prerequisites**

-   The `container-tools`{.literal} metapackage is installed.

**Procedure**

-   Create a `Containerfile`{.literal}. The following is an example:

    ``` {.language-plaintext tabindex="-1"}
    # The following example reuses the default base image as a "builder" image. Optionally,  you can use the commented instructions to configure or override the RPM repositories in /etc/yum.repos.d to, for example, refer to pinned versions
    FROM registry.redhat.io/rhel10/rhel-bootc:latest as builder
    # RUN rm -rf /etc/yum.repos.d/*
    # COPY mycustom.repo /etc/yum.repos.d
    RUN dnf repolist && /usr/libexec/bootc-base-imagectl build-rootfs --manifest=minimal /target-rootfs
    # Create a new, empty image from scratch.
    FROM scratch
    # Copy the root file system built in the previous step into this image.
    COPY --from=builder /target-rootfs/ /
    # You can make arbitrary changes such as copying the systemd units and other tweaks from the baseconfig container image. This example uses the heredocs syntax, to improve and make it easy to add complex instructions, and install critical components
    RUN <<EORUN
    set -xeuo pipefail
    # Install networking support and SSH which are not in minimal
    dnf -y install NetworkManager openssh-server
    dnf clean all
    rm /var/{log,cache,lib}/* -rf
    bootc container lint
    EORUN
    # This label is required
    LABEL containers.bootc 1
    LABEL ostree.bootable 1
    # These labels are optional but useful if you want to keep the default of running under systemd when run as a container image.
    STOPSIGNAL SIGRTMIN+3
    CMD ["/sbin/init"]
    ```

**Next steps**

-   After creating your `Containerfile`{.literal}, you get an image with a single tar file large layer. Every change, such as pushing to the registry, pulling for clients, results in copying the single large tar file, and increases the container image size. You can optimize the container image that you created for a smaller version.

### [9.5. Optimizing container images to a smaller version](#optimizing-container-images-to-a-smaller-version) {#optimizing-container-images-to-a-smaller-version .title}

You can optimize a container image by using the `bootc-base-imagectl rechunk`{.literal} subcommand to split its file system into content-addressed, reproducible layers with precomputed SELinux labeling. This maximizes layer reuse and minimizes data transfer during image pushes and pulls.

**Prerequisites**

-   You have a previously-built base image.

**Procedure**

-   Run the following command to rechunk your base image.

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman run --rm --privileged -v /var/lib/containers:/var/lib/containers \
          registry.redhat.io/rhel10/rhel-bootc:latest \
          /usr/libexec/bootc-base-imagectl rechunk \
              quay.io/exampleos/rhel-bootc:single \
              quay.io/exampleos/rhel-bootc:chunked
    ```

    The `rechunk`{.literal} operation works on an image produced by the default mode of creating new images `FROM <rhel-bootc>`{.literal}. It is useful in combination with the scratch builds that output only a single large `tar`{.literal} layer.

    Without `rechunk`{.literal} operation every change to the input, for example a kernel update, results in a new layer including the entire contents of the bootc image. This new layer must be pushed, stored by registries, and pulled by clients.

    The `bootc-base-imagectl`{.literal} utility, included within bootc images, runs inside a container. However, it requires mapping the host's containers-storage into the container to function.

## [Chapter 10. Testing and deploying bootable containers with bcvk](#managing-image-updates-with-the-bootc-virtualization-kit-bcvk) {#chapter-10.-testing-and-deploying-bootable-containers-with-bcvk .title}

To manage containerized system updates effectively, install the `bootc`{.literal} virtualization kit (`bcvk`{.literal}). The `bcvk`{.literal} tool helps you launch ephemeral virtual machines (VMs) directly from `bootc`{.literal} containers, simplifying your development and deployment process.

### [10.1. The bootc container virtualization kit](#overview-of-the-bootc-container-virtualization-kit) {#the-bootc-container-virtualization-kit .title}

The `bootc`{.literal} virtualization kit (`bcvk`{.literal}) bridges the gap between container development and hardware deployment. With the `bcvk`{.literal} tool, you can launch ephemeral virtual machines (VMs) from `bootc`{.literal} containers to test bootable images locally or generate disk images for production frameworks.

Using `bcvk`{.literal} maintains consistency across your environment because your VMs run the same containerized bootable images used in development.

Choosing a virtualization mode
:   Before deploying, determine which `bcvk`{.literal} mode fits your use case.

+-----------------+---------------------------------+-------------------------------------------------------------+----------------------------------+
| Feature         | Ephemeral (`run`{.literal})     | Persistent (`libvirt`{.literal})                            | Disk image (`to-disk`{.literal}) |
+:================+:================================+:============================================================+:=================================+
| Primary use     | Rapid testing or iteration      | Long-term development                                       | Create bootable disk images      |
+-----------------+---------------------------------+-------------------------------------------------------------+----------------------------------+
| Persistence     | None (wiped on exit)            | Full (survives reboots, supports `bootc`{.literal} upgrade) | N/A (Output artifact)            |
+-----------------+---------------------------------+-------------------------------------------------------------+----------------------------------+
| Privileges      | No sudo required                | No sudo required                                            | No sudo required                 |
+-----------------+---------------------------------+-------------------------------------------------------------+----------------------------------+
| Launch speed    | O(1); independent of image size | Slower; requires disk image creation (first run)            | Slower; creates full disk image  |
+-----------------+---------------------------------+-------------------------------------------------------------+----------------------------------+
| Default memory  | 4GB (4096MB)                    | 4GB RAM (4096MB)                                            | N/A                              |
+-----------------+---------------------------------+-------------------------------------------------------------+----------------------------------+

Show more

### [10.2. Installing the bcvk tool](#installing-the-bcvk-tool) {#installing-the-bcvk-tool .title}

Install bcvk from the EPEL repository to bridge container development and hardware deployment. Use it to test bootable images in local VMs or create disk images for production. A virtualization stack is required to maintain consistency from development to deployment.

**Prerequisites**

-   You have a host environment with a virtualization stack (QEMU, `virtiofsd`{.literal}).
-   You have installed Podman.
-   Optional: You have the `libvirt`{.literal} daemon for persistent virtual machine (VM) management.

**Procedure**

1.  Enable the Red Hat Enterprise Linux (RHEL) Extra Packages for Enterprise Linux (EPEL) repository:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dnf install epel-release
    ```

2.  Install the `bcvk`{.literal} package:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dnf install bcvk
    ```

**Verification**

1.  Verify the installation:

    ``` {.language-plaintext tabindex="-1"}
    $ bcvk --version
    ```

2.  Optional: If you are using `libvirt`{.literal} for persistent VM management, start the `libvirtd`{.literal} service:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo systemctl enable --now libvirtd
    ```

    This command initializes the virtualization daemon to ensure that the back-end infrastructure is active for VM orchestration.

### [10.3. Discovering bootable container images](#discovering-bootable-container-images) {#discovering-bootable-container-images .title}

To maintain an efficient environment, identify which local container images are compatible with the `bootc`{.literal} workflow.

**Procedure**

1.  List the images on your local system that are explicitly labeled for use with `bootc`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    $ bcvk images list
    ```

    The command scans the metadata of all local images and returns a list of those containing the `containers.bootc=1`{.literal} label:

    -   If the command lists images, it verifies them as bootable, and you can use them with the `bcvk ephemeral`{.literal}, `bcvk libvirt`{.literal}, or `bcvk to-disk`{.literal} commands.

    -   If the command do not lists images, ensure that you have pulled a compatible image (for example, `registry.redhat.io/rhel10/rhel-bootc`{.literal}) or that your custom-built image includes the required label in its `Containerfile`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        LABEL containers.bootc=1
        ```

2.  Optional: If a specific image is missing, manually verify its labels:

    ``` {.language-plaintext tabindex="-1"}
    $ podman inspect --format '{{.Config.Labels}}' <image_name>
    ```

### [10.4. Managing ephemeral virtual machines](#managing-ephemeral-virtual-machines) {#managing-ephemeral-virtual-machines .title}

You can launch temporary virtual machines (VMs) for rapid iteration and testing by using the `bcvk ephemeral run`{.literal} command. These VMs use user-space virtualization and do not require root privileges.

**Prerequisites**

-   You have installed the `bcvk`{.literal} utility on the host system.
-   You have a host environment with a functional virtualization stack (QEMU, `virtiofsd`{.literal}).
-   You have installed and configured Podman for the current user.
-   You have authenticated to `registry.redhat.io`{.literal} by using the `podman login`{.literal} command.

**Procedure**

1.  Run a `bootc`{.literal} container as an ephemeral VM:

    ``` {.language-plaintext tabindex="-1"}
    $ bcvk ephemeral run -d --rm -K --name my-test-vm registry.redhat.io/rhel10/rhel-bootc:latest
    ```

    `-d`{.literal}
    :   Runs the VM in detached mode (background).

    `--rm`{.literal}
    :   Automatically removes the VM and cleans up resources once it is stopped.

    `-K`{.literal}
    :   Automatically injects the host's SSH keys into the VM for immediate access.

    `--name`{.literal}
    :   Assigns a custom name (`my-test-vm`{.literal}) to the instance.

2.  Optional: Use the `run-ssh`{.literal} command to launch and enter the VM in a single step:

    ``` {.language-plaintext tabindex="-1"}
    $ bcvk ephemeral run-ssh registry.redhat.io/rhel10/rhel-bootc:latest
    ```

    In this mode, the VM is treated as a session-based resource. It automatically terminates when you exit the SSH shell.

3.  Perform your required tasks within the VM environment.

4.  Exit the session:

    ``` {.language-plaintext tabindex="-1"}
    $ exit
    ```

    Note

    Upon exit, all changes within the ephemeral VM are discarded, and the resources are reclaimed by the host.

### [10.5. Configuring persistent virtualization with libvirt and bcvk](#configuring-persistent-virtualization-with-libvirt-and-bcvk) {#configuring-persistent-virtualization-with-libvirt-and-bcvk .title}

Use `libvirt`{.literal} with `bcvk`{.literal} to gain the stability and control required for production. This configuration maintains system state across reboots and provides granular resource allocation to ensure that your bootable images mirror the performance and constraints of target hardware.

**Prerequisites**

-   You have installed the `bcvk`{.literal} utility on the host system.
-   You have installed, enabled, and started the `libvirtd`{.literal} daemon.
-   You have permissions to manage `libvirt`{.literal} domains. The typical membership in the `libvirt`{.literal} group.
-   You have access to the `registry.redhat.io`{.literal} container registry.

To configure persistent virtualization, complete the following steps.

**Procedure**

1.  Create a persistent `libvirt`{.literal} VM by using one of the following methods:

    -   To create a basic VM with default settings:

        The `libvirt run`{.literal} command automates VM provisioning, including networking and SSH configuration.

        ``` {.language-plaintext tabindex="-1"}
        $ bcvk libvirt run registry.redhat.io/rhel10/rhel-bootc:latest
        ```

    -   To create a customized VM with specific resource constraints:

        Use flags to define the name, memory (in MB), CPU count, and disk size (in GB).

        ``` {.language-plaintext tabindex="-1"}
        $ bcvk libvirt run --name dev-vm --memory 4096 --cpus 4 --filesystem btrfs --disk-size 50G registry.redhat.io/rhel10/rhel-bootc:latest
        ```

2.  After the VM is provisioned, manage its state by using the `bcvk libvirt`{.literal} subcommands:

    +-----------------------------------+--------------------------------------------------------+
    | Task                              | Command                                                |
    +:==================================+:=======================================================+
    | List VMs                          | `bcvk libvirt list`{.literal}                          |
    +-----------------------------------+--------------------------------------------------------+
    | Start a VM                        | `bcvk libvirt start `{.literal}*`<vm_name>`{.literal}* |
    +-----------------------------------+--------------------------------------------------------+
    | Stop a VM                         | `bcvk libvirt stop `{.literal}*`<vm_name>`{.literal}*  |
    +-----------------------------------+--------------------------------------------------------+
    | Remove a VM                       | `bcvk libvirt rm -f `{.literal}*`<vm_name>`{.literal}* |
    +-----------------------------------+--------------------------------------------------------+
    | Access by SSH                     | `bcvk libvirt ssh `{.literal}*`<vm_name>`{.literal}*   |
    +-----------------------------------+--------------------------------------------------------+

    Show more

    Important

    The `bcvk`{.literal} utility handles secure access by injecting SSH keys using `systemd`{.literal} credentials. The private key generated during the provisioning process is unique to which specific VM and is stored securely within the domain metadata. For production environments or longer-term development, `bcvk`{.literal} integrates directly with `libvirt`{.literal}.

### [10.6. Generating disk images from bootc containers](#generating-disk-images-from-bootc-containers) {#generating-disk-images-from-bootc-containers .title}

Use the `bcvk`{.literal} utility together with the to-disk command to convert `bootc`{.literal} container images into physical or virtual disk formats for bare metal or cloud deployments. Create specific virtual disk files, such as `.qcow2`{.literal} or write the image directly to a block device.

**Prerequisites**

-   You have installed the `bcvk`{.literal} utility on the host system.
-   You have a local or remote `bootc`{.literal} container image available.
-   You have sufficient disk space on the host to store the generated image.
-   You have `root`{.literal} or `sudo`{.literal} privileges to write directly to block devices or system paths.

**Procedure**

-   Generate a disk image by using one of the following methods:

    -   Create a virtual disk image:

        ``` {.language-plaintext tabindex="-1"}
        $ bcvk to-disk --format=qcow2 --disk-size 20G localhost/my-image output-disk.qcow2
        ```

-   `--format`{.literal}: Specifies the output disk type. Supported formats: `qcow2`{.literal}, and `raw`{.literal} (default).

-   `output-disk.qcow2`{.literal}: Specifies the destination file name for the generated disk image.

    -   Write directly to a physical device:

        ``` {.language-plaintext tabindex="-1"}
        $ bcvk to-disk registry.redhat.io/rhel10/rhel-bootc:latest /path/to/disk.img
        ```

        Warning

        Writing directly to a block device, for example, `/dev/sdX`{.literal}, overwrites all existing data on that device. Verify the target path before running the command.

## [Chapter 11. Enabling FIPS mode in a bootc image build](#enabling-the-fips-mode-while-building-a-bootc-image) {#chapter-11.-enabling-fips-mode-in-a-bootc-image-build .title}

The Federal Information Processing Standard (FIPS) 140 defines requirements for cryptographic modules. To fulfill these requirements, you must enable FIPS mode. You can enable FIPS mode during the bootc container image build.

### [11.1. Creating a bootable disk image for a FIPS-enabled system](#enabling-the-fips-mode-to-perform-an-anaconda-installation) {#creating-a-bootable-disk-image-for-a-fips-enabled-system .title}

You can create a disk image and enable FIPS mode when performing an Anaconda installation. You must add the `fips=1`{.literal} kernel argument when booting the disk image.

**Prerequisites**

-   You have Podman installed on your host machine.
-   You have `virt-install`{.literal} installed on your host machine.
-   You have root access to run the `bootc-image-builder`{.literal} tool, and run the containers in `--privileged`{.literal} mode, to build the images.

**Procedure**

1.  Create a `01-fips.toml`{.literal} to configure FIPS enablement, for example:

    ``` {.language-plaintext tabindex="-1"}
    # Enable FIPS
    kargs = ["fips=1"]
    ```

2.  Create a Containerfile with the following instructions to enable the `fips=1`{.literal} kernel argument and adjust the cryptographic policies:

    ``` {.language-plaintext tabindex="-1"}
    FROM quay.io/<namespace>/<image>:latest
    # Enable fips=1 kernel argument: https://bootc-dev.github.io/bootc/building/kernel-arguments.html
    COPY 01-fips.toml /usr/lib/bootc/kargs.d/
    # Install and enable the FIPS crypto policy
    RUN dnf install -y crypto-policies-scripts && update-crypto-policies --no-reload --set FIPS
    ```

3.  Before running the container, initialize the `output`{.literal} folder. Use the `-p`{.literal} argument to ensure that the command does not fail if the directory already exists:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir -p ./output
    ```

4.  Create your bootc *`<image>`{.literal}* compatible base disk image by using `Containerfile`{.literal} in the current directory:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman run \
        --rm \
        -it \
        --privileged \
        --pull=newer \
        --security-opt label=type:unconfined_t \
        -v ./config.toml:/config.toml \
        -v ./output:/output \
        -v /var/lib/containers/storage:/var/lib/containers/storage \
        registry.redhat.io/rhel10/bootc-image-builder:latest \
        --type iso \
        quay.io/<namespace>/<image>:<tag>
    ```

5.  Enable FIPS mode during the system installation:

    a.  When booting the RHEL Anaconda installer, on the installation screen, press the TAB key and add the `fips=1`{.literal} kernel argument. After the installation, the system starts in FIPS mode automatically.

**Verification**

-   After login in to the system, check that FIPS mode is enabled:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /proc/sys/crypto/fips_enabled
    1
    $ update-crypto-policies --show
    FIPS
    ```

**Additional resources**

-   [Installing the system with FIPS mode enabled](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/switching-rhel-to-fips-mode#installing-the-system-with-fips-mode-enabled)

## [Chapter 12. Security hardening and compliance of bootable images](#security-hardening-and-compliance-of-bootable-images) {#chapter-12.-security-hardening-and-compliance-of-bootable-images .title}

Image mode for RHEL provides security-compliance features and supports workloads that require compliant configuration. However, the process of hardening systems and verifying compliance status is different from in package mode.

The key part of using Image mode for RHEL is creating a bootable container image. The deployed system mirrors the image. Therefore, the built image must contain all packages and configuration settings that are required by the security policy.

Important

When a bootable image is run as a container, some of the hardening configuration is not in effect. To get a system that is fully configured in accordance with the security profile, you must boot the image in a bare metal or virtual machine instead of running as a container. Main differences of a container deployment include the following:

-   Systemd services that are required by security profiles do not run on containers because systemd is not running in the container. Therefore, the container cannot comply with the related policy requirements.
-   Other services cannot run in containers, although they are configured correctly. This means that `oscap`{.literal} reports them as correctly configured, even if they are not running.
-   Configurations defined by the compliance profile are not enforcing. Requests from other packages or installation prescripts can change the compliance state. Always check the compliance of the installed product and alter your Containerfile to fit your requirements.

### [12.1. Building hardened bootable images](#building-hardened-bootable-images) {#building-hardened-bootable-images .title}

To establish a highly secure foundation for your Red Hat Enterprise Linux deployments, you can build hardened bootable images. You can also embed security configurations directly into the base image to ensures compliance with strict organizational standards.

You can build hardened bootable images by including the `oscap-im`{.literal} tool in the `Containerfile`{.literal} that is used to build your bootable container image. Although `oscap-im`{.literal} tool can consume any SCAP content, the SCAP source data streams in `scap-security-guide`{.literal} are specifically adjusted and tested to be compatible with bootable containers.

**Prerequisites**

-   The `container-tools`{.literal} meta-package is installed.
-   You know the ID of the profile within the baseline with which the system should comply. To find the ID, see the [Viewing profiles for configuration compliance](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/scanning-the-system-for-configuration-compliance#viewing-profiles-for-configuration-compliance) section.

**Procedure**

1.  Create a `Containerfile`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    FROM quay.io/<namespace>/<image>:latest

    # Install OpenSCAP scanner and security content to the image
    RUN dnf install -y openscap-utils scap-security-guide && dnf clean all

    # Run scan and hardening
    RUN oscap-im --profile <profile_ID> /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml

    # Because certain profiles prevent ssh root logins, add a separate sudo user with a password
    # Alternatively, you can add users with Kickstart, cloud-init, or other methods
    RUN useradd -G wheel -p "<password_hash>" <admin_user>
    ```

    Replace *`<admin_user>`{.literal}* with the user name and *`<password_hash>`{.literal}* with the hash of the selected password.

    This `Containerfile`{.literal} performs the following tasks:

    -   Installs the `openscap-utils`{.literal} package that provides the `oscap-im`{.literal} tool and the `scap-security-guide`{.literal} package that provides the data streams with the Security Content Automation Protocol (SCAP) content.
    -   Adds a user with `sudoer`{.literal} privileges for profiles that prevent SSH root logins.
    -   Scans and remediates the image for compliance with the selected profile.

2.  Build the image by using the `Containerfile`{.literal} in the current directory:

    ``` {.language-plaintext tabindex="-1"}
    $ podman build -t quay.io/<namespace>/<image>:<tag> .
    ```

**Verification**

-   List all images:

    ``` {.language-plaintext tabindex="-1"}
    $ podman images
    REPOSITORY                                  TAG      IMAGE ID       CREATED              SIZE
    quay.io/<namespace>/<image>                 <tag>   b28cd00741b3   About a minute ago   2.1 GB
    ```

**Next steps**

-   You can deploy hardened bootable images by using any of the normal bootable image deployment methods. For more information, see [Deploying the RHEL bootc images](#deploying-the-rhel-bootc-images "Chapter 8. Deploying RHEL bootc images").

    The deployment method, however, can affect the compliance state of the target system.

-   You can verify the compliance of a running system in Image Mode RHEL by using the `oscap`{.literal} tool with the same syntax and usage as in package mode RHEL. For more information, see [Configuration compliance scanning](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/scanning-the-system-for-configuration-compliance#configuration-compliance-scanning).

### [12.2. Customizing hardened bootable images](#customizing-hardened-bootable-images) {#customizing-hardened-bootable-images .title}

You can apply a customized profile to a bootable image by using the `oscap-im`{.literal} tool. You can customize a security profile by changing parameters in certain rules, for example, minimum password length, removing rules that you cover in a different way, and selecting additional rules, to implement internal policies. You cannot define new rules by customizing a profile.

**Prerequisites**

-   The `container-tools`{.literal} meta-package is installed.
-   You have a customization file for your profile. For more information, see [Customizing a security profile with autotailor](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/scanning-the-system-for-configuration-compliance#customizing-a-security-profile-with-autotailor).

**Procedure**

1.  Create a `Containerfile`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    FROM quay.io/<namespace>/<image>:latest

    # Copy a tailoring file into the Containerfile
    COPY tailoring.xml /usr/share/

    # Install OpenSCAP scanner and security content to the image
    RUN dnf install -y openscap-utils scap-security-guide && dnf clean all

    # Add sudo user 'admin' with password 'admin123'.
    # The user can be used with profiles that prevent
    # ssh root logins.
    RUN useradd -G wheel -p "\$6\$Ga6Zn
    IlytrWpuCzO\$q0LqT1USHpahzUafQM9jyHCY9BiE5/ahXLNWUMiVQnFGblu0WWGZ1e6icTaCGO4GNgZNtspp1Let/qpM7FMVB0" admin

    # Run scan and hardening including the tailoring file
    RUN oscap-im --tailoring-file /usr/share/tailoring.xml --profile stig_customized /usr/share/xml/scap/ssg/content/ssg-rhel10-ds.xml
    ```

    This `Containerfile`{.literal} performs the following tasks:

    -   Injects the tailoring file to your image.
    -   Installs the `openscap-utils`{.literal} package that provides the `oscap-im`{.literal} tool and the `scap-security-guide`{.literal} package that provides the data streams with the Security Content Automation Protocol (SCAP) content.
    -   Adds a user with `sudoer`{.literal} privileges for profiles that prevent SSH root logins.
    -   Scans and remediates the image for compliance with the selected profile.

2.  Build the image by using the `Containerfile`{.literal} in the current directory:

    ``` {.language-plaintext tabindex="-1"}
    $ podman build -t quay.io/<namespace>/<image>:<tag> .
    ```

**Verification**

-   List all images:

    ``` {.language-plaintext tabindex="-1"}
    $ podman images
    REPOSITORY                                  TAG      IMAGE ID       CREATED              SIZE
    quay.io/<namespace>/<image>                 <tag>   b28cd00741b3   About a minute ago   2.1 GB
    ```

**Next steps**

-   You can deploy hardened bootable images by using any of the normal bootable image deployment methods. For more information, see [Deploying the RHEL bootc images](#deploying-the-rhel-bootc-images "Chapter 8. Deploying RHEL bootc images").

    The deployment method, however, can affect the compliance state of the target system.

    Note

    Some customizations performed during the deployment, in blueprint for `bootc-image-builder`{.literal} or in Kickstart for Anaconda, can interfere with the configuration present in the container image. Do not use customizations that conflict with the security policy requirements.

-   You can verify the compliance of a running system in Image Mode RHEL by using the `oscap`{.literal} tool with the same syntax and usage as in package mode RHEL. For more information, see [Configuration compliance scanning](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/scanning-the-system-for-configuration-compliance#configuration-compliance-scanning).

## [Chapter 13. Cryptographic sealing of bootc images (Technology Preview)](#cryptographic-sealing-of-bootc-images-technology-preview) {#chapter-13.-cryptographic-sealing-of-bootc-images-technology-preview .title}

To ensure tamper-proof code integrity from hardware to operating system and meet compliance, you can cryptographically seal a bootc container image by using your organizations UEFI Secure Boot keys. This verifies the entire operating system image through build, distribution, and runtime.

### [13.1. Understanding cryptographic sealing of bootc images](#understanding-cryptographic-sealing-of-bootc-images) {#understanding-cryptographic-sealing-of-bootc-images .title}

You use cryptographic sealing to create an end-to-end integrity chain from firmware to the file system for your RHEL `bootc`{.literal} deployments. This ensures that your operating system boots only when the root file system matches the build-time signature exactly.

Important

Cryptographic sealing of `bootc`{.literal} images is available as a Technology Preview. Technology Preview features are not supported with Red Hat production Service Level Agreements (SLAs), might not be functionally complete, and Red Hat does not recommend using them for production. These previews provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

You can protect your image integrity through these combined components:

Unified Kernel Images (UKIs)
:   A Unified Kernel Image (UKI) bundles the kernel, the `initramfs`{.literal} filesystem , and the kernel command-line into a single signed EFI binary to prevent tampering with individual boot components. Unlike the traditional boot chain, which only verifies the kernel signature, a UKI protects the `initramfs`{.literal} filesystem and command-line with the same signature. This architecture proves critical for sealed images, as the kernel command-line contains the `composefs`{.literal} digest, a cryptographic commitment to the exact `root`{.literal} filesystem the system must mount.

Composefs integration

:   A `composefs`{.literal} digest integrates EROFS, overlayfs, and `fs-verity`{.literal} to provide cryptographic verification for the entire filesystem. When you build a sealed image, the system processes the operating system into an EROFS metadata image that describes every file, directory, and permission without including the actual data.

    Instead, it records an `fs-verity`{.literal} digest for each file entry, while a separate content-addressed object store holds the actual data with kernel-enabled `fs-verity`{.literal}. At mount time, the kernel uses overlayfs to stitch these components together, while the `verity=require`{.literal} option forces the kernel to verify that every served file matches its corresponding `fs-verity`{.literal} digest in the EROFS metadata.

    The `fs-verity`{.literal} feature ensures per-file integrity by computing and storing a cryptographic hash tree of the file's contents on disk. During operation, the kernel verifies reads at the block level and caches the results to maintain performance.

    If corruption or tampering causes a verification failure, the kernel immediately blocks the data and returns an I/O error (EIO). Because this mechanism prevents the system from serving compromised data, any subsequent read operations on corrupted portions fail, even if the initial open call succeeds.

Secure Boot signatures
:   Secure Boot, a UEFI firmware feature, ensures only signed code runs during the boot process by maintaining a database of trusted keys and verifying the boot loader signature. For sealed images, it provides a hardware root of trust, guaranteeing that the software executing immediately after the firmware is trusted.

**Additional resources**

-   [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview)

### [13.2. Understanding the UEFI Secure Boot key hierarchy](#understanding-the-uefi-secure-boot-key-hierarchy) {#understanding-the-uefi-secure-boot-key-hierarchy .title}

Cryptographic sealing of `bootc`{.literal} images relies on UEFI Secure Boot to verify the integrity of boot artifacts. Secure Boot uses a hierarchy of three key types to build a chain of trust.

Platform Key (PK)
:   The PK serves as the root of the Secure Boot trust hierarchy. Every system contains exactly one PK, which controls access to the Secure Boot key databases and signs updates to the KEK database. Enrolling the PK transitions the firmware from Setup Mode to User Mode, which enables Secure Boot enforcement.

Key Exchange Key (KEK)
:   Systems can enroll one or more KEKs. A KEK authorizes updates to the signature database (`db`{.literal}). This key enables delegation: the PK owner authorizes other parties to manage trusted signing keys without relinquishing full control over the Secure Boot configuration.

Signature Database (`db`{.literal})

:   The `db`{.literal} contains the keys or hashes that the firmware uses to verify boot binaries. When the firmware loads a boot loader or a Unified Kernel Image (UKI), it checks the binary's signature against the keys in the `db`{.literal}. If the signature matches a `db`{.literal} entry, the binary executes.

    Note

    If your infrastructure already uses provisioned Secure Boot keys, skip generating new ones. You only need access to a `db`{.literal} key, or the ability to add your signing key to the existing `db`{.literal}, to sign your UKIs.

#### [13.2.1. Generating Secure Boot keys for image sealing](#generating-secure-boot-keys-for-image-sealing) {#generating-secure-boot-keys-for-image-sealing .title}

To sign and verify sealed `bootc`{.literal} images, generate a complete set of UEFI Secure Boot keys. This procedure creates a Platform Key (PK), a Key Exchange Key (KEK), and a Signature Database (db) key.

**Prerequisites**

-   The `openssl`{.literal} package is installed.
-   The `uuidgen`{.literal} command from the `util-linux`{.literal} package on RHEL is available to generate a UUID.
-   A secure location to store private key files is available.

Important

For production deployments, use a hardware security module (HSM) or a dedicated key management system instead of storing private keys on the file system. The examples in this procedure use `openssl`{.literal} directly for simplicity.

**Procedure**

1.  Generate a Globally Unique Identifier (GUID) to identify the key owner:

    ``` {.language-shell-session tabindex="-1"}
    $ uuidgen --random > <GUID.txt>
    ```

2.  Generate the Platform Key (PK):

    ``` {.language-shell-session tabindex="-1"}
    $ openssl req -newkey rsa:2048 -nodes -keyout PK.key -new -x509 -sha256 -days 3650 -subj '/CN=<My Platform Key>/' -out PK.crt
    ```

3.  Convert GUID to a DER-encoded certificate for firmware enrollment:

    ``` {.language-shell-session tabindex="-1"}
    $ openssl x509 -outform DER -in PK.crt -out PK.cer
    ```

    The command generates a private key (`PK.key`{.literal}) for signing, a PEM certificate (`PK.crt`{.literal}) for signing operations, and a DER-encoded certificate (`PK.cer`{.literal}) for firmware enrollment. You must protect the private key file with appropriate access controls.

4.  Generate the Key Exchange Key (KEK):

    ``` {.language-shell-session tabindex="-1"}
    $ openssl req -newkey rsa:2048 -nodes -keyout KEK.key -new -x509 -sha256 -days 3650 -subj '/CN=<My Key Exchange Key>/' -out KEK.crt
    ```

5.  Convert KEK to a DER-encoded certificate for firmware enrollment:

    ``` {.language-shell-session tabindex="-1"}
    $ openssl x509 -outform DER -in KEK.crt -out KEK.cer
    ```

6.  Generate the Signature Database (db) key:

    ``` {.language-shell-session tabindex="-1"}
    $ openssl req -newkey rsa:2048 -nodes -keyout db.key -new -x509 -sha256 -days 3650 -subj '/CN=<MySignature Database Key>/' -out db.crt
    ```

7.  Convert it to a DER-encoded certificate for firmware enrollment:

    ``` {.language-shell-session tabindex="-1"}
    $ openssl x509 -outform DER -in db.crt -out db.cer
    ```

**Verification**

-   Verify that the system generated all key and text files successfully:

    ``` {.language-shell-session tabindex="-1"}
    $ ls -1 PK.key PK.crt PK.cer KEK.key KEK.crt KEK.cer db.key db.crt db.cer <GUID.txt>
    ```

### [13.3. Sealing a bootc container image with Secure Boot keys](#sealing-a-bootc-container-image-with-secure-boot-keys) {#sealing-a-bootc-container-image-with-secure-boot-keys .title}

You can seal a RHEL `bootc`{.literal} container image by computing a cryptographic digest of the root file system and embedding it in a signed Unified Kernel Image (UKI). The sealed image provides end-to-end integrity verification from firmware through the file system at boot time.

Note

Use `ext4`{.literal} file system for sealed images because XFS does not support `fsverity`{.literal}.

**Prerequisites**

-   The container includes a kernel in the `/usr/lib/modules/<kver>/`{.literal} directory.
-   The container does not include a pre-built UKI as the build process generates one.

**Procedure**

1.  Create a multi-stage `Containerfile`{.literal}:

    ``` {.language-shell-session tabindex="-1"}
    # Build your rootfs with all packages and configuration
    FROM registry.redhat.io/rhel10/rhel-bootc as rootfs
    RUN dnf install_<package name>_

    # Install the ukify tool
    $ dnf install -y systemd-ukify sbsigntools

    # Generate the sealed UKI in a tools stage
    FROM registry.redhat.io/rhel10/rhel-bootc:latest as sealed-uki
    RUN --mount=type=bind,from=rootfs,src=/,target=/target \
        --mount=type=secret,id=secureboot_key \
        --mount=type=secret,id=secureboot_cert <<EORUN
    set -euo pipefail

    # Find the kernel version
    kver=$(ls /target/usr/lib/modules)

    # Create the /out directory
    $ mkdir /out

    # Generate and sign the UKI with the digest embedded
    bootc container ukify --rootfs /target -- \
      --signtool sbsign \
      --secureboot-private-key /run/secrets/secureboot_key \
      --secureboot-certificate /run/secrets/secureboot_cert \
      --output "/out/${kver}.efi"
    EORUN

    # Final image: copy the sealed UKI into place
    FROM rootfs
    COPY --from=sealed-uki /out/*.efi /boot/EFI/Linux/
    ```

    The `--mount=type=bind`{.literal} and `from=rootfs`{.literal} provides read-only access to the target filesystem, where `bootc`{.literal} container `compute-composefs-digest`{.literal} computes the SHA-512 hash of the `rootfs`{.literal}, `bootc container ukify`{.literal} creates the UKI with that digest in the kernel command line (`composefs=<digest>`{.literal}), and the final stage copies the signed UKI into the `rootfs`{.literal} without modifying any files used in the digest calculation.

    A multi-stage build approach is necessary because you must compute the `composefs`{.literal} digest without including the UKI. Since this digest effectively reduces the entire file system to a single hash that resides inside the UKI, including the UKI in the computation would alter the digest. To prevent this, you build the UKI in a separate layer, avoiding file system pollution, and then copy the UKI into the `/boot`{.literal} directory of the current layer, where it remains masked off during EROFS image generation.

2.  Build the `bootc`{.literal} composefs-enabled container image:

    ``` {.language-shell-session tabindex="-1"}
    $ podman build --secret=id=secureboot_key,src=db.key --secret=id=secureboot_cert,src=db.crt -t composefs-bootc .
    ```

3.  Determine the `composefs`{.literal} digest for a file system:

    ``` {.language-shell-session tabindex="-1"}
    $ bootc container compute-composefs-digest <path>
    ```

**Verification**

1.  Verify that the command successfully lists the signed Unified Kernel Image (UKI) at `/boot/efi/systemd-boot*.efi`{.literal} and the signed `systemd-boot`{.literal} files:

    ``` {.language-shell-session tabindex="-1"}
    $ podman run --rm -ti composefs-bootc ls /usr/lib/systemd/boot/efi/systemd-boot*.efi
    ```

    Note

    You must check for the existence of the systemd-boot and UKI inside the final build container image before running the verification steps as the `sbsigntools`{.literal} is installed in the `build-uki`{.literal} stage.

2.  List the signatures and verify the UKI configuration:

    ``` {.language-shell-session tabindex="-1"}
    $ sbverify --list <path-to-uki>
    ```

    Sealed images provide continuous runtime verification through `fsverity`{.literal}, which extends validation beyond initial boot-time checks. Unlike standard Secure Boot that only validates the kernel, sealed images immediately return input or output errors if a file is tampered with, rather than serving corrupted content.

### [13.4. Deploying sealed bootc images](#deploying-sealed-bootc-images) {#deploying-sealed-bootc-images .title}

You can deploy the sealed `bootc`{.literal} image by using standard methods to ensure seamless compatibility with target systems. When your image includes a UKI and `systemd-boot`{.literal}, the system automatically detects the `composefs`{.literal} backend.

**Prerequisites**

-   A sealed `bootc`{.literal} image is built and pushed to a container registry.
-   UEFI Secure Boot is enabled on the target system with your organization's certificate enrolled.
-   Ensure the target system has an EFI System Partition (ESP) of at least 2 GB to accommodate Unified Kernel Images and composefs metadata.
-   The target system uses a filesystem with `fs-verity`{.literal} support, such as `ext4`{.literal} or `btrfs`{.literal}, for the root partition.

**Procedure**

1.  Install the `bcvk`{.literal} tool to run `bootc`{.literal} container images as virtual machines:

    ``` {.language-shell-session tabindex="-1"}
    $ dnf install bcvk
    ```

    The `bcvk`{.literal} tool calls `bootc install to-disk`{.literal} to create a bootable disk image and uses `libvirt`{.literal} to manage the virtual machine lifecycle.

    Note

    Run the `bootc install --composefs-backend`{.literal} command for your production bare metal deployments. The Anaconda integration will happen in a future release.

2.  Deploy the image:

    ``` {.language-shell-session tabindex="-1"}
    $ bcvk libvirt run --ssh-wait --name <sealed-demo> --firmware=uefi-secure --filesystem=ext4 --secure-boot-keys target/keys localhost/sealed-host:latest
    ```

    -   The `--filesystem=ext4`{.literal} flag instructs `bootc install`{.literal} to use ext4 for the root filesystem, as it supports `fs-verity`{.literal} unlike the default XFS.
    -   The `--secure-boot-keys`{.literal} target or keys flag directs `bcvk`{.literal} to the directory with our PK, KEK, and db certificates, enabling `bcvk`{.literal} to use `virt-fw-vars`{.literal} to enroll these keys into the OVMF firmware variable store for Secure Boot.
    -   The `--ssh-wait`{.literal} flag causes `bcvk`{.literal} to wait for SSH availability before it returns, confirming the system boot.

**Additional resources**

-   [The bootc container virtualization kit](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#overview-of-the-bootc-container-virtualization-kit)

### [13.5. Managing sealed image lifecycle operations](#managing-sealed-image-lifecycle-operations) {#managing-sealed-image-lifecycle-operations .title}

To recompute the digest and generate a new signed UKI that matches the updated filesystem, you must re-seal the image. If you modify the `root`{.literal} filesystem of a sealed `bootc`{.literal} image, the modification invalidates the `composefs`{.literal} digest embedded in the Unified Kernel Image (UKI).

**Prerequisites**

-   You have a multi-stage `Containerfile`{.literal}.
-   You have access to the Secure Boot private key (`secureboot.key`{.literal}) and certificate (`secureboot.crt`{.literal}).

**Procedure**

1.  Apply your changes to the `rootfs`{.literal} stage of the `Containerfile`{.literal}.

2.  Rebuild the sealed image by running the `podman build`{.literal} command with your Secure Boot secrets:

    ``` {.language-shell-session tabindex="-1"}
    $ podman build --secret id=secureboot_key,src=/path/to/secureboot.key --secret id=secureboot_cert,src=/path/to/secureboot.crt -t quay.io/<namespace>/my-sealed-bootc:latest .
    ```

3.  Push the updated image to your registry:

    ``` {.language-shell-session tabindex="-1"}
    $ podman push quay.io/<namespace>/my-sealed-bootc:latest
    ```

4.  Upgrade the deployed systems to fetch and apply the newly sealed image:

    ``` {.language-shell-session tabindex="-1"}
    $ sudo bootc upgrade
    ```

**Verification**

-   Verify that the system boots successfully and shows the updated image:

    ``` {.language-shell-session tabindex="-1"}
    $ sudo bootc status
    ```

-   Verify the `composefs`{.literal} digest is correctly applied:

    ``` {.language-shell-session tabindex="-1"}
    $ sudo journalctl -b | grep composefs
    ```

-   Verify `fsverity`{.literal} enforcement is active:

    ``` {.language-shell-session tabindex="-1"}
    $ sudo dmesg | grep fsverity
    ```

## [Chapter 14. Creating root level directories and symlinks at runtime with image mode for RHEL](#creating-root-level-directories-and-symlinks-at-runtime-with-image-mode-for-rhel) {#chapter-14.-creating-root-level-directories-and-symlinks-at-runtime-with-image-mode-for-rhel .title}

As a privileged user, you can create dynamic, top-level mountpoints at runtime while the filesystem remains read-only by default by using the `transient-ro`{.literal} option. This is useful for applications that require bind-mount host paths that can be platform-specific or dynamic.

This feature addresses the following use cases:

-   Applications that require specific, absolute host paths for bind-mounts.
-   Platforms that require specific mountpoints, for example, `/users`{.literal}.
-   Requirement to create dynamic mountpoints after deployment, but before an application starts.
-   A security requirement to keep the root filesystem read-only for all regular processes.

### [14.1. Working of the transient-ro true option](#working-of-the-transient-ro-true-option) {#working-of-the-transient-ro-true-option .title}

Enable the `transient-ro=true`{.literal} option in Red Hat Enterprise Linux bootc images to implement stateless deployments. This configuration directs file system writes to temporary storage, discarding runtime changes upon system reboot.

The following workflow describes the boot process changes:

-   `transient-ro=true`{.literal} mounts the `overlayfs`{.literal} upper directory in `read-only`{.literal} mode by default.

    -   With this, a privileged process, such as `root`{.literal} or a `systemd`{.literal} service, can remount the root filesystem as `read-write`{.literal}, but only within a new, private mount namespace.

-   Within the private namespace, the process can perform changes, such as creating new top-level directories to serve as mountpoints.

-   The mountpoints persist for the current boot, but do not persist through reboots or upgrades.

-   All other regular processes on the system continue to see the original, unmodified, `read-only`{.literal} root filesystem.

For security reasons, only privileged users (root) can create these mountpoints:

-   The mountpoints are transient and do not persist across reboots.
-   The filesystem remains `read-only`{.literal} for non-privileged processes.

Important

Because of a limitation in `util-linux`{.literal}, you must set the `LIBMOUNT_FORCE_MOUNT2=always`{.literal} environment variable when you perform mount operations with the `transient-ro`{.literal} option. This variable affects the mount namespace functionality that `transient-ro`{.literal} requires.

### [14.2. Creating dynamic mountpoints with transient-ro](#creating-dynamic-mountpoints-with-transient-ro) {#creating-dynamic-mountpoints-with-transient-ro .title}

As a `root`{.literal} user, you can use the bootc `root.transient-ro`{.literal} feature to build a transient overlay on top of the root file system that is `read-only`{.literal} by default, create dynamic top-level mountpoints, and remount the filesystem as `read-write`{.literal} when needed.

When using the `root.transient-ro`{.literal} feature, to ensure applications can properly access host directories and create necessary mountpoints on `read-only`{.literal} filesystems, several considerations apply:

-   Applications need to bind-mount host directories that match the host's absolute paths.
-   Platform-specific mountpoints are required, such as `/Users`{.literal} on macOS.
-   Creation of dynamic mount points after deployment but before application startup.
-   The filesystem remains `read-only`{.literal} for regular processes.

**Prerequisites**

-   The `container-tools`{.literal} meta-package is installed.

**Procedure**

1.  Create a `transient-root-example.service`{.literal} service to create the directory with `read`{.literal} and `write`{.literal} permissions. In the following example, `/etc/afs`{.literal} exists.

    ``` {.language-plaintext tabindex="-1"}
    [Unit]
    Description=Transient Root Example - Dynamic Mount Point Creation
    After=local-fs.target
    ConditionPathExists=/etc/afs
    DefaultDependencies=no

    [Service]
    Type=oneshot
    RemainAfterExit=yes
    MountFlags=slave
    # LIBMOUNT_FORCE_MOUNT2=always is required for mount command compatibility
    # See: https://github.com/util-linux/util-linux/issues/3171
    Environment=LIBMOUNT_FORCE_MOUNT2=always
    ExecStart=/usr/bin/bash -c "echo 'Transient root example: Detected /etc/afs, remounting root as read-write'; mount -o remount,rw /; mkdir -p /afs; echo 'Created /afs directory for AFS mount point'"

    [Install]
    WantedBy=multi-user.target
    ```

2.  Add the following configuration to the ContainerFile:

    ``` {.language-plaintext tabindex="-1"}
    # Copy the systemd service unit that demonstrates dynamic mount point creation
    # The service will:
    # 1. Check for existence of /etc/afs (ConditionPathExists)
    # 2. Use MountFlags=slave for proper mount propagation
    # 3. Set LIBMOUNT_FORCE_MOUNT2=always for mount command compatibility
    # 4. Remount root as read-write and create /afs directory when triggered
    COPY transient-root-example.service /usr/lib/systemd/system/

    # Enable the service to start automatically on boot
    RUN systemctl enable transient-root-example.service
    ```

3.  To enable the `transient-ro`{.literal} option during the container build process, create the following configuration to the `/usr/lib/ostree/prepare-root.conf`{.literal} file inside the image:

    ``` {.language-plaintext tabindex="-1"}
    RUN echo -e '[root]\ntransient=true' > /usr/lib/ostree/prepare-root.conf && \
        set -x; kver=$(cd /usr/lib/modules && echo *); dracut -vf /usr/lib/modules/$kver/initramfs.img $kver
    ```

    Note

    When you make changes to the file system configuration, you must regenerate the initramfs image.

4.  Build the bootc image with the transient root file system:

    ``` {.language-plaintext tabindex="-1"}
    $ podman build --cap-add SYS_ADMIN -t transient-root-ro:test .
    ```

    This adds the `SYS_ADMIN`{.literal} capability that `bootc`{.literal} requires for `ostree`{.literal} operations during the build.

**Verification**

1.  Verify that `transient-ro = true`{.literal} configuration file was correctly set in the built image:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman run --rm transient-root-ro:test cat /usr/lib/ostree/prepare-root.conf
    ```

    You can see an output similar to the following:

    ``` {.language-plaintext tabindex="-1"}
    [root]
    transient-ro = true
    ```

2.  On the running system, verify the runtime functionality:

    a.  Boot the image.

    b.  Create the `/etc/afs`{.literal} test directory.

        ``` {.language-plaintext tabindex="-1"}
        $ sudo mkdir -p /etc/afs
        ```

    c.  Restart the service to trigger dynamic mount point creation:

        ``` {.language-plaintext tabindex="-1"}
        $ systemctl restart transient-root-example.service
        ```

        The service remounts root as `read-write`{.literal} and creates the `/afs`{.literal} directory.

3.  To test the functionality without a `systemd`{.literal} service, create a test directory as root on the running system:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo export LIBMOUNT_FORCE_MOUNT2=always
    $ sudo unshare -m -- /bin/sh -c 'mount -o remount,rw / && mkdir /transient-test'
    ```

4.  Verify if the directory was created:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo ls -d /transient-test /transient-test
    ```

5.  Verify the `read-only`{.literal} status for other processes by attempting to write to the root filesystem:

    ``` {.language-plaintext tabindex="-1"}
    $ touch /another-test-file
    touch: cannot touch '/another-test-file': Read-only file system
    ```

## [Chapter 15. Managing RHEL bootc images](#managing-rhel-bootc-images) {#chapter-15.-managing-rhel-bootc-images .title}

You can perform Day 2 management operations on deployed RHEL `bootc`{.literal} images. These operations include transactional in-place updates fetched from a container registry, booting into the updated images, and performing manual or automated rollbacks in case of failures.

Note

The `rhel-bootc`{.literal} images are rebuilt whenever their underlying inputs, such as RPM packages, are updated. These rebuilds occur at least monthly, or more frequently if critical updates are released. You maintain full control over when to push the update images. A newly published base image does not trigger automatic rebuilds or redeployments of your custom images, which allows you to configure the update cadence and only push changes as required.

### [15.1. Switching the container image reference](#switching-the-container-image-reference) {#switching-the-container-image-reference .title}

You can change the container image reference used for upgrades by using the `bootc switch`{.literal} command. For example, you can switch from the stage to the production tag. To manually switch an existing `ostree-based`{.literal} container image reference, use the `bootc switch`{.literal} command.

**Prerequisites**

-   A booted system using `bootc`{.literal}.

**Procedure**

-   Run the following command:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo bootc switch [--apply] quay.io/<namespace>/<image>:<tag>
    ```

    Optionally, you can use the `--apply`{.literal} option when you want to automatically take actions, such as rebooting if the system has changed.

    Note

    The `bootc switch`{.literal} command has the same effect as `bootc upgrade`{.literal}. The only difference is the container image reference is changed. This enables preserving the existing states in `/etc`{.literal} and `/var`{.literal}, for example, host SSH keys and home directories.

### [15.2. Adding or changing content in the bootc image initramfs](#adding-modules-to-the-bootc-image-initramfs) {#adding-or-changing-content-in-the-bootc-image-initramfs .title}

The `rhel10/rhel-bootc`{.literal} image uses the `dracut`{.literal} infrastructure to build an initial RAM disk (`initrd`{.literal}) during the image build time. A default `initrd`{.literal} is built and included in the `/usr/lib/modules/`{.literal}*`<kernel_version>`{.literal}*`/initramfs.img`{.literal} location inside the container image.

You can use a drop-in configuration file to extend the `dracut`{.literal} configuration, and place it in a file in the `` /usr/lib/dracut/dracut.conf.d/ directory. This re-creates `initrd ``{.literal} with the modules you want to add.

**Prerequisites**

-   A booted system using bootc.

**Procedure**

-   Re-create the `initrd`{.literal} as part of a container build:

    ``` {.language-plaintext tabindex="-1"}
    FROM <baseimage>
    COPY <custom_modules_list>.conf /usr/lib/dracut/dracut.conf.d
    RUN set -x; kver=$(cd /usr/lib/modules && echo *); dracut -vf /usr/lib/modules/$kver/initramfs.img $kver
    ```

    Note

    By default the `dracut`{.literal} command attempts to pull the running kernel version, which causes an error. Explicitly pass to dracut the kernel version of the target to avoid errors.

### [15.3. Performing manual updates from an installed operating system](#performing-manual-updates-from-an-installed-operating-system) {#performing-manual-updates-from-an-installed-operating-system .title}

With image mode for RHEL, you can perform any other management task, such as changing or updating the system, by pushing the changes to the container registry.

When using image mode for RHEL, you can choose to perform manual updates for your systems. If you have automatic updates enabled, you must turn them off to perform a manual update. To do so, use one of the following options:

-   Running the `bootc upgrade`{.literal} command
-   Modifying the `systemd`{.literal} timer file

#### [15.3.1. Turning off automatic updates](#turning-off-automatic-updates) {#turning-off-automatic-updates .title}

To perform manual updates you must turn off automatic updates. You can do this by disabling the timer of the container build, by using one of the following options described in the procedure.

**Prerequisites**

-   A booted system using bootc.

**Procedure**

-   Disable the timer of a container build.

    -   By running the `systemctl mask`{.literal} command:

        ``` {.language-plaintext tabindex="-1"}
        $ systemctl mask bootc-fetch-apply-updates.timer
        ```

    -   By modifying the `systemd`{.literal} timer file. Use `systemd`{.literal} \"drop-ins\" to override the timer. In the following example, updates are scheduled for once a week.

        1.  Create an `updates.conf`{.literal} file with the following content:

            ``` {.language-plaintext tabindex="-1"}
            [Timer]
            # Clear previous timers
            OnBootSec= OnBootSec=1w OnUnitInactiveSec=1w
            ```

        2.  Add you file to the directory that you created:

            ``` {.language-plaintext tabindex="-1"}
            $ mkdir -p /usr/lib/systemd/system/bootc-fetch-apply-updates.timer.d
            $ cp updates.conf /usr/lib/systemd/system/bootc-fetch-apply-updates.timer.d
            ```

#### [15.3.2. Manually updating an installed operating system](#manually-updating-an-installed-operating-system) {#manually-updating-an-installed-operating-system .title}

To manually fetch updates from a registry and boot the system into the new updates, use `bootc upgrade`{.literal} command. This command fetches the transactional in-place updates from the installed operating system to the container image registry.

The command queries the registry and queues an updated container image for the next boot. It stages the changes to the base image, but does not change the running system by default.

**Prerequisites**

-   A booted system using bootc.

**Procedure**

-   Run the following command:

    ``` {.language-plaintext tabindex="-1"}
    $ bootc upgrade [--apply]
    ```

    The `apply`{.literal} argument is optional and you can use it when you want to automatically take actions, such as rebooting if the system has changed.

    Note

    The `bootc upgrade`{.literal} command is an alias for `bootc update`{.literal}. Both commands have the same effect.

    For more information, see the `bootc-upgrade`{.literal} man page on your system.

#### [15.3.3. Upgrading images by using download-only mode](#upgrading-images-by-using-download-only-mode) {#upgrading-images-by-using-download-only-mode .title}

You can download and stage an update without automatically applying it on reboot by using the `bootc upgrade --download-only`{.literal} flag. This flag gives you control over when updates are applied in production environments.

**Prerequisites**

-   The system is booted system by using bootc.
-   Automatic updates are turned off. See [Turning off automatic updates](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/managing-rhel-bootc-images#turning-off-automatic-updates).

**Procedure**

1.  Download the update in download-only mode:

    ``` {.language-plaintext tabindex="-1"}
    $ bootc upgrade --download-only
    ```

    You can use the download-only mode to validate updates before application, manage fleet-wide rollouts that include network-intensive downloads, and handle scenarios where system-altering reboots occur at different times.

2.  Verify the mode of the staged deployment:

    ``` {.language-plaintext tabindex="-1"}
    $ bootc status --verbose
    ```

    ``` {.language-plaintext tabindex="-1"}
    Staged:
    Image: quay.io/example/rhel-guest:latest
    Version: 10.2.20260126
    download-only: yes
    ```

    You cannot automatically switch to this version on the next boot, as confirmed by `download-only: yes`{.literal} line in the output.

3.  In the maintenance window, you can apply staged updates in one of the following ways in the download-only mode:

    -   Apply staged update without fetching from image source:

        ``` {.language-plaintext tabindex="-1"}
        $ bootc upgrade --from-downloaded
        ```

    -   Apply the staged update and reboot immediately:

        ``` {.language-plaintext tabindex="-1"}
        $ bootc upgrade --from-downloaded --apply
        ```

    -   Check for newer updates and apply:

        ``` {.language-plaintext tabindex="-1"}
        $ bootc upgrade
        ```

        Running the `bootc upgrade`{.literal} command without flags pulls from the container image source to check for updates. If the staged deployment matches the latest available update, it unlocks the staged deployment. If a newer update is available, the newer version replaces the staged deployment.

**Verification**

-   Verify that the staged deployment is in the download-only mode by checking that the output shows the `download-only: yes`{.literal} line:

    ``` {.language-plaintext tabindex="-1"}
    $ bootc status --verbose
    ```

    ``` {.language-plaintext tabindex="-1"}
    Staged:
    Image: quay.io/example/rhel-guest:latest
    Version: 10.2.20260126
    download-only: yes
    ```

### [15.4. Performing rollbacks from an updated operating system](#performing-rollbacks-from-a-updated-operating-system) {#performing-rollbacks-from-an-updated-operating-system .title}

You can roll back to a previous boot entry to revert changes in the system by using the `bootc rollback`{.literal} command. This command changes the boot loader entry ordering by making the deployment under `rollback`{.literal} queued for the next boot. The current deployment then becomes the rollback.

Any staged changes, such as a queued upgrade that was not applied, are discarded. After a rollback completes, the update timer run within 1 to 3 hours which automatically update and reboot your system to the image you just rolled back from.

Warning

If you perform a rollback, the system will automatically update again unless you turn off auto-updates. See [Turning off automatic updates](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/managing-rhel-bootc-images#turning-off-automatic-updates).

When performing a rollback, for example, by using the `bootc rollback`{.literal} command, changes made to files in the `/etc`{.literal} directory do not carry over to the rolled-back deployment. Instead, the files in the `/etc`{.literal} directory revert to the state they were in during the previous deployment.

The `bootc rollback`{.literal} command reorders existing deployments but does not create new ones. The `/etc`{.literal} directory is merged when new deployments are created.

To preserve a modified `/etc`{.literal} file for use after a rollback, copy it to a directory under `/var`{.literal}, such as `/var/home/`{.literal}*`<user>`{.literal}* for a specific *`<user>`{.literal}*, or under `/var/root/`{.literal}, for the root user. These directories are unaffected by rollbacks, as they store user content.

When returning to the original state, either through a temporary rollback or another bootc rollback, the `/etc`{.literal} directory reverts to its state from the original deployment.

Alternatively, if the issue you are rolling back does not involve configuration files in the `/etc`{.literal} directory, use the `bootc switch`{.literal} command to revert to an older deployment. This command performs the necessary `/etc`{.literal} merge and deploy the previous version of the software.

**Prerequisites**

-   You performed an update to the system.

**Procedure**

-   Run the following command:

    ``` {.language-plaintext tabindex="-1"}
    $ bootc rollback [-h|--help] [-V|--version]
    ```

    Note

    The `bootc rollback`{.literal} command has the same effect as `bootc upgrade`{.literal}. The only difference is the container image being tracked. This enables preserving the existing states in /etc and /var, for example, host SSH keys and home directories.

**Verification**

-   Use `systemd journal`{.literal} to check the logged message for the detected rollback invocation.

    ``` {.language-plaintext tabindex="-1"}
    $ journalctl -b
    ```

    You can see a log similar to:

    ``` {.language-plaintext tabindex="-1"}
    MESSAGE_ID=26f3b1eb24464d12aa5e7b544a6b5468
    ```

    For more information, see the `bootc-rollback(8)`{.literal} man page on your system.

### [15.5. Deploying updates to system groups](#deploying-updates-to-system-groups) {#deploying-updates-to-system-groups .title}

You can change the configuration of your operating system by modifying the `Containerfile`{.literal}. The update is applied after you build and push your container image to the registry, and reboot the operating system.

You can also change the container image source by using the `bootc switch`{.literal} command. The content in the container registry determines the specific configuration of the RHEL Image Mode operating system. See [Switching the container image reference](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/managing-rhel-bootc-images#switching-the-container-image-reference).

Usually, when deploying updates to system groups, you can use a central management service to provide a client to be installed on each system which connects to the central service. Often, the management service requires the client to perform a one time registration.

The following is an example of deploying updates to system groups. You can modify, by injecting the credentials for the management service into the image, to create a persistent `systemd`{.literal} service, if required.

Note

For clarity reasons, the Containerfile in the example is not optimized. For example, a better optimization to avoid creating multiple layers in the image is by invoking `RUN`{.literal} a single time.

You can install a client into an image mode for RHEL image and run it at startup to register the system.

**Prerequisites**

-   The management-client handles future connections to the server, by using a `cron`{.literal} job or a separate `systemd`{.literal} service.

**Procedure**

-   Create a management service with the following characteristics. It determines when to upgrade the system.

    ``` {.language-plaintext tabindex="-1"}
    FROM registry.redhat.io/rhel10/rhel-bootc:latest
    # Management services determine when to upgrade the system.
    # Disable bootc-fetch-apply-updates.timer if it is included in the base image.
    RUN systemctl disable bootc-fetch-apply-updates.timer

    # Install the client from dnf, or some other method that applies for your client
    RUN dnf install management-client -y && dnf clean all

    # Inject the credentials for the management service into the image
    ARG activation_key=

    # The existence of .run_next_boot acts as a flag to determine if the
    # registration is required to run when booting
    RUN touch /etc/management-client/.run_next_boot

    COPY <<"EOT" /usr/lib/systemd/system/management-client.service
    [Unit]
    Description=Run management client at boot
    After=network-online.target
    ConditionPathExists=/etc/management-client/.run_client_next_boot

    [Service]
    Type=oneshot
    EnvironmentFile=/etc/management-client/.credentials
    ExecStart=/usr/bin/management-client register --activation-key ${CLIENT_ACTIVATION_KEY}
    ExecStartPre=/bin/rm -f /etc/management-client/.run_next_boot
    ExecStop=/bin/rm -f /etc/management-client/.credentials

    [Install]
    WantedBy=multi-user.target
    EOT

    # Link the service to run at startup
    RUN ln -s /usr/lib/systemd/system/management-client.service /usr/lib/systemd/system/multi-user.target.wants/management-client.service

    # Store the credentials in a file to be used by the systemd service
    RUN echo -e "CLIENT_ACTIVATION_KEY=${activation_key}" > /etc/management-client/.credentials

    # Set the flag to enable the service to run one time
    # The systemd service will remove this file after the registration completes the first time
    RUN touch /etc/management-client/.run_next_boot
    ```

    1.  Disable `bootc-fetch-apply-updates.timer`{.literal} if it is included in the base image.
    2.  Install the client by using `dnf`{.literal}, or some other method that applies for your client.
    3.  Inject the credentials for the management service into the image.

### [15.6. Checking inventory health](#checking-inventory-health) {#checking-inventory-health .title}

You can assess the status of your RHEL managed nodes to verify they are online and reachable. You can also manually check the health of container images and events running inside the container to ensure systems are ready to receive updates or configuration changes.

**Prerequisites**

-   You pushed the container image to an accessible repository.
-   The `container-tools`{.literal} meta-package is installed.

**Procedure**

-   Display the health check status of a container.

    -   By using the `podman inspect`{.literal}: or `podman ps`{.literal} commands.

        ``` {.language-plaintext tabindex="-1"}
        $ podman inspect --format='{{json .State.Health.Status}}' <container>
        healthy
        ```

    -   By using the `podman ps`{.literal} commands.

        ``` {.language-plaintext tabindex="-1"}
        $ podman healthcheck run <container>
        healthy
        ```

-   Monitor and print events that occur in Podman by using the `podman events`{.literal} command. Each event includes a timestamp, a type, a status, a name, if applicable, and an image, if applicable.

    ``` {.language-plaintext tabindex="-1"}
    $ now=$(date --iso-8601=seconds)
    $ podman events --since=now --stream=false
    healthy
    ```

**Additional resources**

-   [Monitoring containers](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/building_running_and_managing_containers/monitoring-containers)

### [15.7. Automation and GitOps](#automation-and-gitops) {#automation-and-gitops .title}

You can use CI/CD (Continuous Integration and Continuous Delivery) pipelines to automate the building process of your RHEL bootc images. By using a CI/CD , an event can trigger an update, such as updating an application.

You can use automation tools that track these updates and trigger the CI/CD pipelines, such as GitHub Actions, and GitLab CI. The pipeline keeps the systems up to date by using the transactional background operating system updates.

**Additional resources**

-   [Resources to create image mode for RHEL instances in RHEL Image Mode CI/CD](https://gitlab.com/redhat/cop/rhel/rhel-image-mode-cicd)

### [15.8. Performing a factory reset of an image mode system](#performing-a-factory-reset-of-an-image-mode-system) {#performing-a-factory-reset-of-an-image-mode-system .title}

You can perform a non-destructive factory reset of your `bootc`{.literal} system to restore `/etc`{.literal} and `/var`{.literal} to the container image's original state, undoing any modifications. After the reset, the system reboots into a fresh state where `/etc`{.literal} contains only the configuration from the container image and `/var`{.literal} is empty.

Important

Performing a factory reset of an image mode system is provided as a Technology Preview. Technology Preview features are not supported with Red Hat production Service Level Agreements (SLAs), might not be functionally complete, and Red Hat does not recommend using them for production. These previews provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

**Prerequisites**

-   You have a bootable container system.

-   You have access to the container image you want to reset to in a container registry.

    Warning

    You might lose users that Anaconda, or other tools like `cloud-init`{.literal}, added. Any installer, such as the `bootc-image-builder`{.literal} tool and Anaconda, adds state on top of the image that the `bootc install reset`{.literal} command removes.

**Procedure**

1.  Perform a factory reset. Depending on your goal, run one of the following commands:

    -   To reset to the same image currently running:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo bootc install reset --experimental
        ```

    -   To reset and switch to a different image:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo bootc install reset --experimental --target-imgref quay.io/example/myimage:latest
        ```

    -   To reset and immediately reboot:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo bootc install reset --experimental --apply
        ```

    -   To add custom kernel arguments:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo bootc install reset --experimental --karg=console=ttyS0,115200n8
        ```

    -   To skip inheriting root filesystem kernel arguments:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo bootc install reset --experimental --no-root-kargs
        ```

        After you reboot into the new deployment, you can still access your old system's data by examining the files in `/sysroot/ostree/deploy/<old-stateroot>/`{.literal}.

        Note

        After you perform a factory reset and reboot into the new stateroot, you still keep the old stateroot on disk at `/sysroot/ostree/deploy/`{.literal}*`<old-stateroot>`{.literal}*`/`{.literal}. You can access files from your previous system if you need them.

**Additional resources**

-   [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview)
-   [Cleaning up the old stateroot](https://bootc.dev/bootc/experimental-install-reset.html#cleaning-up-the-old-stateroot)

## [Chapter 16. Managing kernel arguments in bootc systems](#managing-kernel-arguments-in-bootc-systems) {#chapter-16.-managing-kernel-arguments-in-bootc-systems .title}

You can customize the boot process of your Red Hat Enterprise Linux bootc systems by managing kernel arguments. By configuring these parameters, you can tune performance and ensure hardware compatibility by applying settings during the image build or installation phase.

You can use `bootc`{.literal} to configure kernel arguments. By default, `bootc`{.literal} uses the boot loader configuration files stored in `/boot/loader/entries`{.literal}. This directory defines arguments provided to the Linux kernel. The set of kernel arguments is machine-specific state, but you can also manage the kernel arguments by using container updates. The boot loader menu entries are shared between multiple operating systems, and boot loaders are installed on one device.

Note

Currently, the boot loader entries are written by an OSTree back end.

### [16.1. Adding support to inject kernel arguments by using bootc](#how-to-add-support-to-inject-kernel-arguments-with-bootc) {#adding-support-to-inject-kernel-arguments-by-using-bootc .title}

The `bootc`{.literal} tool uses generic operating system kernels. You can add support to inject kernel arguments by adding a custom configuration, in the TOML format, in `/usr/lib/bootc/kargs.d`{.literal}.

**Prerequisites**

-   You created a container image.

**Procedure**

-   Add support to inject kernels, for example:

    ``` {.language-plaintext tabindex="-1"}
    # /usr/lib/bootc/kargs.d/10-example.toml
    kargs = ["mitigations=auto,nosmt"]
    ```

-   Optional: You can also make these kernel arguments architecture-specific by using the `match-architectures`{.literal} key. For example:

``` {.language-plaintext tabindex="-1"}
# /usr/lib/bootc/kargs.d/00-console.toml
kargs = ["console=ttyS0,115200n8"]
match-architectures = ["x86_64"]
```

### [16.2. Modifying kernel arguments by using bootc install configurations](#how-to-modify-kernel-arguments-by-using-bootc-install-configs) {#modifying-kernel-arguments-by-using-bootc-install-configurations .title}

To modify kernel arguments by using the bootc install configurations, you can customize the startup behavior of your Red Hat Enterprise Linux deployments. These parameters enable specific hardware settings or performance optimizations that persist through system updates and reboots.

You can use the `bootc install`{.literal} command with the `--karg`{.literal} option to inject kernel arguments during installation time in the following ways:

-   Adding kernel arguments into the container image.
-   Adding kernel arguments by using the `bootc install --karg`{.literal} command.

Use the kernel arguments on Day 2 operations, by adding the arguments and applying them on a switch, upgrade, or edit.

**Prerequisites**

-   You created a container image.

**Procedure**

1.  Create files within `/usr/lib/bootc/kargs.d`{.literal} with kernel arguments.

    ``` {.language-plaintext tabindex="-1"}
    $ sudo tee /usr/lib/bootc/kargs.d/console.kargs << EOF
    console=tty0 console=ttyS0,115200n8
    EOF
    ```

2.  Fetch the container image to get the OSTree commit.

    ``` {.language-plaintext tabindex="-1"}
    $ podman pull quay.io/<your_org>/<your_bootc_image>:latest
    ```

3.  Use the OSTree commit to return the file tree.

    ``` {.language-plaintext tabindex="-1"}
    # bootc install to-filesystem --karg=root=<UUID>=<uuid of /mnt> --imgref $self /mnt
    ```

4.  Navigate to the `/usr/lib/bootc/kargs.d`{.literal} kernel arguments directory.

    ``` {.language-plaintext tabindex="-1"}
    cd /usr/lib/bootc/kargs.d
    ```

5.  Read each file within the kernel arguments directory.

    ``` {.language-plaintext tabindex="-1"}
    $ find /usr/lib/bootc/kargs.d -name ".kargs" -exec cat {} \;*
    ```

6.  Push the contents of each `kargs`{.literal} file into a file containing all the needed `kargs`{.literal}.

    ``` {.language-plaintext tabindex="-1"}
    $ CONSOLIDATED_KARGS="/tmp/all-kargs.txt"
    ```

7.  Pass the `kargs`{.literal} to the *`stage()`{.literal}* function.

    ``` {.language-plaintext tabindex="-1"}
    $ bootc kargs --append="$KARGS_STRING"
    ```

8.  Apply the kernel arguments to switch, upgrade, or edit during operations.

    ``` {.language-plaintext tabindex="-1"}
    $ bootc switch --transport=registry quay.io/<your_org>/<your_bootc_image>:latest
    ```

### [16.3. Injecting kernel arguments in the Containerfile](#how-to-inject-kernel-arguments-in-the-containerfile) {#injecting-kernel-arguments-in-the-containerfile .title}

Inject kernel arguments into your Red Hat Enterprise Linux Containerfile to configure boot parameters during the image build process. Embedding these settings consistently applies specific kernel options to any provisioned system from the container image, eliminating post-deployment configuration.

**Prerequisites**

-   You created a container image.

**Procedure**

-   Inject kernel arguments:

    ``` {.language-plaintext tabindex="-1"}
    FROM registry.redhat.io/rhel10/rhel-bootc:latest

    RUN mkdir -p /usr/lib/bootc/kargs.d
    RUN cat <<EOF >> /usr/lib/bootc/kargs.d/console.toml
    kargs = ["console=ttyS0,115200n8"]
    match-architectures = ["x86_64"]
    EOF

    RUN cat <<EOF >> /usr/lib/bootc/kargs.d/01-mitigations.toml
    kargs = ["mitigations=on", "systemd.unified_cgroup_hierarchy=0"]
    match-architectures = ["x86_64", "aarch64"]
    EOF
    ```

### [16.4. Injecting kernel arguments at installation time](#how-to-inject-kernel-arguments-at-installation-time) {#injecting-kernel-arguments-at-installation-time .title}

You can use `boot install`{.literal} with the `--karg`{.literal} to inject kernel arguments during installation time. As a result, the kernel arguments become the machine-local state, that is, they became the persistent configuration unique to that specific machine.

**Prerequisites**

-   You created a container image.

**Procedure**

-   Inject kernel arguments:

    ``` {.language-plaintext tabindex="-1"}
    # bootc install to-filesystem --karg=root=<UUID>=<uuid of /mnt> --imgref $self /mnt
    ```

### [16.5. Adding install-time kernel arguments by using bootc-image-builder](#how-to-add-install-time-kernel-arguments-with-bootc-image-builder) {#adding-install-time-kernel-arguments-by-using-bootc-image-builder .title}

Use the `bootc-image-builder`{.literal} to add install-time kernel arguments to Red Hat Enterprise Linux bootc images. Defining the kernel parameters by using the `customizations.kernel.append`{.literal} to configure hardware-specific settings or console outputs required during the initial provisioning process.

**Prerequisites**

-   You created a container image.

**Procedure**

-   Add kernel arguments with `bootc-image-builder`{.literal} by using the following customization:

    ``` {.language-plaintext tabindex="-1"}
    {
      "customizations": {
        "kernel": {
          "append": "mitigations=auto,nosmt"
        }
      }
    }
    ```

### [16.6. Post-installation kernel argument changes with kargs.d](#post-installation-kernel-argument-changes-with-kargs.d) {#post-installation-kernel-argument-changes-with-kargs.d .title}

The changes that you make to `kargs.d`{.literal} files and include in a container build are applied after the installation. The difference between the set of kernel arguments is applied to the current boot loader configuration. This preserves any machine-local kernel arguments.

You can use any tool to edit the `/boot/loader/entries`{.literal} files, which are in a standardized format. The `/boot`{.literal} directory is read-only, which limits the set of tools that can write to the file system.

### [16.7. Editing kernel arguments in bootc systems](#how-to-edit-kernel-arguments-in-bootc-systems) {#editing-kernel-arguments-in-bootc-systems .title}

To perform machine local changes, you also can edit kernel arguments on a bootc system or an `rpm-ostree`{.literal} system, by using the `rpm-ostree kargs`{.literal} command. The changes are made through the `user/lib/bootc/kargs.d`{.literal} path, which also handles `Day 2`{.literal} changes, besides the first boot changes.

**Prerequisites**

-   You created a container image.

**Procedure**

-   Append a kernel argument, for example:

    ``` {.language-plaintext tabindex="-1"}
    # rpm-ostree kargs --append debug
    Staging deployment... done
    Freed: 40.1 MB (pkgcache branches: 0)
    Changes queued for next boot. Run "systemctl reboot" to start a reboot
    ```

-   Check the help for more information:

    ``` {.language-plaintext tabindex="-1"}
    # rpm-ostree kargs --help
    ```

    The following are the options that you can use to add, modify or remove kernel arguments.

    `rpm-ostree kargs`{.literal}

    \--append=KEY=VALUE 
    :   Appends a kernel argument. It is useful with, for example, `console=`{.literal} that can be used multiple times. You can use an empty value for an argument.

    \--replace=KEY=VALUE=NEWVALUE 
    :   Replaces an existing kernel argument. You can replace an argument with `KEY=VALUE`{.literal} only if one value already exists for that argument.

    \--delete=KEY=VALUE 
    :   Deletes a specific kernel key-value pair argument or an entire argument with a single key-value pair.

    \--append-if-missing=KEY=VALUE 
    :   Appends a kernel argument. Does nothing if the key is already present.

    \--delete-if-present=KEY=VALUE 
    :   Deletes a specific kernel key-value pair argument. Does nothing if the key is missing.

    \--editor 
    :   Uses an editor to modify the kernel arguments.

## [Chapter 17. Integrating third-party drivers in image mode for RHEL](#integrating-third-party-drivers-in-image-mode-for-rhel) {#chapter-17.-integrating-third-party-drivers-in-image-mode-for-rhel .title}

To ensure that networking, storage, and security drivers persist across image updates and reboots, you can include third-party kernel modules directly in the container build process.

### [17.1. Differences between package mode and image mode for third-party providers](#differences-between-package-mode-and-image-mode-for-third-party-providers) {#differences-between-package-mode-and-image-mode-for-third-party-providers .title}

When transitioning from traditional package-based deployments to image mode, you must adapt third-party provider installation logic to account for the move from mutable live systems to immutable build-time environments.

+---------------------+----------------------------------------------------+-------------------------------------------------------------------------+
| Feature             | Traditional package mode                           | Image mode (bootc)                                                      |
+:====================+:===================================================+:========================================================================+
| Installation Timing | On the running hardware (Post-deployment).         | During the container build (Pre-deployment).                            |
+---------------------+----------------------------------------------------+-------------------------------------------------------------------------+
| Filesystem Status   | Mutable (read/write).                              | Immutable by default, except for `/etc`{.literal} and `/var`{.literal}. |
+---------------------+----------------------------------------------------+-------------------------------------------------------------------------+
| Hardware Access     | Direct access to firmware/DMI data.                | No access to the target server hardware during image build.             |
+---------------------+----------------------------------------------------+-------------------------------------------------------------------------+
| Driver Persistence  | Managed by using `dnf`{.literal} on the live host. | Integrated/embedded into the layered container image.                   |
+---------------------+----------------------------------------------------+-------------------------------------------------------------------------+

Show more

In image mode, the operating system content available in `/usr`{.literal} is managed as part of the `bootc`{.literal} image and treated as an immutable area at runtime. Conversely, `/etc`{.literal} and `/var`{.literal} are treated as persistent runtime states.

Because the file system is treated as immutable, networking, file system, or security modules that are not included in the default RHEL kernel must be included in the image to remain available across upgrades and reboots. Unlike the traditional package mode, where drivers are installed on a live system by using `dnf`{.literal}, you can use the image mode for RHEL to include custom drivers. Consequently, you must integrate the driver itself and files under `/usr/lib/modules`{.literal} during image build, and create hardware-dependent configurations and state files after the target system has booted.

Choosing an installation strategy for custom drivers

:   When integrating custom drivers into your image, you can choose between two primary methods, which differ significantly in how they handle kernel updates:

    -   Multi-stage build: This approach compiles the driver directly against the kernel headers included in the base image during the container build process. Every time the base image updates its kernel, the system automatically rebuilds the driver against it, which guarantees compatibility.
    -   Copying a pre-built RPM: Do not use for automated pipelines This approach copies a pre-compiled driver RPM from an external source directly into a single-stage `Containerfile`{.literal}. The RPM is not automatically rebuilt when the base image kernel updates, which can lead to silent boot failures if the driver becomes incompatible. If you use this method, manually verify, rebuild, and retest the driver RPM against the new kernel version outside of the container build before copying it in.
    -   Technical constraints for third-party drivers

The image mode build process occurs within a containerized environment, which introduces specific constraints that can cause legacy RPM scripts to fail:

No hardware presence
:   Commands such as `dmidecode`{.literal} and `lspci`{.literal}, or queries to `/sys/class/dmi/…​`{.literal}, do not return information about the final production hardware.

Restricted firmware access
:   If your drivers attempt to validate firmware versions or UUIDs during the `%post`{.literal} or `%pre`{.literal} installation scripts, the scripts fail or incorrectly detect the build host's environment instead of the target server.

Immutable `/usr`{.literal} directory
:   In the final bootable image, the `/usr`{.literal} directory is read-only. Ensure that you place all driver files in the image during the `Containerfile`{.literal} build stage.

`depmod`{.literal} requirements
:   Because the build environment lacks a running target kernel, ensure that `depmod`{.literal} runs explicitly against the specific target kernel version within the image during the build phase.

Early boot requirements

:   If you require a driver before the system mounts the real root file system, such as a storage controller driver required to access the root device, ensure that you also include the driver in the image `initramfs`{.literal}. Installing the module under `/usr/lib/modules`{.literal} alone is insufficient.

    -   Guidelines for driver providers

Decoupled hardware validation
:   RPM `.spec`{.literal} files do not contain hardware-probing logic during the installation phase. Move hardware validation to a `systemd`{.literal} service that runs at first boot.

Stateless installation
:   The driver does not rely on persistent state in `/var`{.literal} or `/etc`{.literal} directories created during the build, because the system handles these directories as writable runtime overlays in image mode.

**Additional resources**

-   [Introduction of image mode for RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/introducing-image-mode-for-rhel)
-   [Adding or changing content in the bootc image initramfs](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/managing-rhel-bootc-images#adding-modules-to-the-bootc-image-initramfs)

### [17.2. Deployment workflow for image mode drivers](#deployment-workflow-for-image-mode-drivers) {#deployment-workflow-for-image-mode-drivers .title}

Third-party drivers in image mode follow a build-time integration workflow that spans RPM refactoring, container image build, deployment, and first-boot initialization on target hardware.

Refactoring
:   You adjust the driver's RPM `%post`{.literal} scripts to avoid hardware detection (`dmidecode`{.literal}) and ensure any required startup configurations are packaged inside the image.

Containerizing
:   You use a multi-stage `Containerfile`{.literal} to compile the module or install the driver directly against the `rhel-bootc`{.literal} base image.

Finalizing
:   The container build process triggers `depmod`{.literal} to map dependencies within the image.

Provisioning

:   You push the image to a registry and deploy it using one of the following methods based on system state:

    -   For initial provisioning of a new system, install the image by using a supported image mode deployment method, such as `bootc install`{.literal} or images generated by using `bootc-image-builder`{.literal}.
    -   To update an existing `bootc`{.literal} system to a newer version of the same image reference, use `bootc upgrade`{.literal}.
    -   To change an existing system to a different image reference, use `bootc switch`{.literal}.

Initializing
:   On the first boot of the physical hardware, the driver is loaded from the immutable image, and any hardware-specific initialization from the refactoring phase occurs.

### [17.3. Integrating a driver by using a Containerfile](#integrating-a-driver-by-using-a-containerfile) {#integrating-a-driver-by-using-a-containerfile .title}

Integrate custom drivers by using a multi-stage `Containerfile`{.literal}. This decouples build tools and dependencies from the final production image, and ensures that only the runtime driver remains in the final bootable container image.

**Prerequisites**

-   You have initialized an image mode development environment with a container engine, such as `Podman`{.literal}, and you have access to a container registry.
-   You have the driver source code and a valid `.spec`{.literal} file on your build host.
-   The RPM package includes a `%post`{.literal} script that automatically runs `depmod`{.literal} to handle dependency mapping inside the container image during the build process.
-   If explicit module parameters or explicit startup loading are required, the corresponding configuration file, such as `/usr/lib/modules-load.d/hello.conf`{.literal}, is included in your RPM or container build context so that the driver loads automatically on system startup.

**Procedure**

1.  Create a multi-stage `Containerfile`{.literal} on your build host to compile and install the driver into the operating system image:

    ``` {.language-plaintext tabindex="-1"}
    # --- STAGE 1: Build Environment ---
    FROM registry.redhat.io/rhel10/rhel-bootc:latest AS builder

    # Install build tools and kernel development headers for the image kernel
    RUN dnf install -y make gcc rpm-build kernel-devel && \
        dnf clean all

    # Copy driver source and spec file into the builder stage
    COPY src/ /build/src/
    COPY SPECS/hello.spec /build/SPECS/

    # Build the driver RPM package inside the container context
    WORKDIR /build
    RUN rpmbuild --define "_topdir /build" -ba SPECS/hello.spec

    # --- STAGE 2: Final Production Image ---
    FROM registry.redhat.io/rhel10/rhel-bootc:latest

    # Copy only the generated RPM from the builder stage
    COPY --from=builder /build/RPMS/x86_64/hello-1.0-1.el10.x86_64.rpm /tmp/

    # Install the RPM. The internal %post script automatically triggers 'depmod'.
    RUN dnf install -y /tmp/hello-1.0-1.el10.x86_64.rpm && \
        dnf clean all && \
        rm /tmp/hello-1.0-1.el10.x86_64.rpm
    ```

2.  Build the `bootc`{.literal} container image:

    ``` {.language-plaintext tabindex="-1"}
    $ podman build -t registry.example.com/bootc-images/rhel-hello:latest .
    ```

3.  Push the completed image to your target container registry:

    ``` {.language-plaintext tabindex="-1"}
    $ podman push registry.example.com/bootc-images/rhel-hello:latest
    ```

4.  Deploy the image to the target system by using the appropriate method for your system state:

    -   For a new installation: Use `bootc-image-builder`{.literal} to generate a bootable ISO or disk image preconfigured with this container reference.

    -   For an existing system: Run an in-place reference turn on the target host:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo bootc switch registry.example.com/bootc-images/rhel-hello:latest
        ```

**Verification**

1.  Reboot the target system to boot into the newly deployed container image containing your driver:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo reboot
    ```

2.  Confirm that the driver loaded automatically during system startup by checking the kernel ring buffer and live modules:

    ``` {.language-plaintext tabindex="-1"}
    $ journalctl -b -k | grep -i hello
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ lsmod | grep '^hello'
    hello        12288  0
    ```

    If the module does not load automatically, verify that an appropriate hardware alias exists or that a configuration file resides in the `/usr/lib/modules-load.d/`{.literal} directory.

3.  Confirm that the module file exists in the correct immutable directory structure matching your running kernel:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo uname -r
    ```

    ``` {.language-plaintext tabindex="-1"}
    10.0.0-example.el10.x86_64
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ sudo ls -l /usr/lib/modules/$(uname -r)/extra/
    ```

    ``` {.language-plaintext tabindex="-1"}
    total 12
    -rwxr-xr-x. 1 root root 8512 Jan  1  1970 hello.ko
    ```

4.  Test manual lifecycle operations by unloading and re-loading the module:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo rmmod hello
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ sudo modprobe hello
    ```

5.  Inspect the kernel ring buffer logs to verify correct initialization and cleanup behavior:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dmesg | tail -n 5
    ```

    ``` {.language-plaintext tabindex="-1"}
    [   84.738633] hello: loading out-of-tree module taints kernel.
    [   84.738684] hello: module verification failed: signature and/or required key missing -tainting kernel.
    [   84.740548] Hello, world!
    [  138.206978] Goodbye!
    ```

    Note

    -   The `module verification failed`{.literal} message and kernel taint warnings are expected when you load custom, out-of-tree modules that you have not signed with a trusted Secure Boot key. These warnings do not prevent the module from executing successfully.
    -   When Unified Extensible Firmware Interface (UEFI) Secure Boot is disabled and kernel module signature enforcement is not active, an unsigned out-of-tree module loads successfully. The kernel reports a signature-verification warning and registers a tainted state, but does not block execution.
    -   When UEFI Secure Boot is enabled, the kernel rejects unsigned out-of-tree modules or modules signed with an untrusted key. For Secure Boot environments, sign the module with a public key trusted by the target system's firmware or the Machine Owner Key (MOK) database.

6.  Check the Secure Boot status on your target system:

    ``` {.language-shell-session tabindex="-1"}
    $ mokutil --sb-state
    ```

## [Chapter 18. Managing file systems in image mode for RHEL](#managing-file-systems-in-image-mode-for-rhel) {#chapter-18.-managing-file-systems-in-image-mode-for-rhel .title}

Configure file system layouts and mount points for your Red Hat Enterprise Linux Image Mode deployments. By managing these storage settings, you can define how the operating system handles persistent data, ensuring that critical information remains available across system updates and reboots.

Image mode uses OSTree as the back end, and enables composefs for storage by default. As a result, you can install third-party content in derived container images that write into `/opt`{.literal} for example, because the `/opt`{.literal} and `/usr`{.literal} local paths are plain directories, and not symbolic links into `/var`{.literal}.

Warning

When you install third-party content to `/opt`{.literal}, the third-party components might also attempt to write to subdirectories within `/opt`{.literal} during runtime, which can create potential conflicts.

### [18.1. Overview of physical and logical root with /sysroot](#physical-and-logical-root-with-sysroot) {#overview-of-physical-and-logical-root-with-sysroot .title}

When a `bootc`{.literal} system is fully booted, the operating system mounts the physical host root file system at `/sysroot`{.literal} and presents a deployment root, similar to a `chroot`{.literal} environment.

The remaining filesystem paths are part of a deployment root which is used as a final target for the system boot. The system uses the `ostree=kernel`{.literal} argument to find the deployment root.

`/usr`{.literal}

:   It is preferred to keep all operating system content in the `/usr`{.literal}. Directories such as `/bin`{.literal} works as symbolic links to `/usr/bin`{.literal}. This layout creates a separation of operating system and host specific resources.

    Note

    When `composefs`{.literal} is enabled, `/usr`{.literal} is not different from `/`{.literal}. Both directories are part of the same immutable image, so you do not need to perform a full `UsrMove`{.literal} with a bootc system.

`/usr/local`{.literal}

:   With bootc systems, you can create custom container images as the default entrypoint. Because of that, the base images configure `/usr/local`{.literal} to be a regular directory, that is, the default directory.

    The default filesystem layout has both `/opt`{.literal} and `/usr/local`{.literal} as regular directories, they writable at build time and immutable at runtime. This differs from RHEL CoreOS, for example, which makes these symlinks into `/var`{.literal}.

`/etc`{.literal}

:   The `/etc`{.literal} directory contains mutable persistent state by default, but it supports enabling the `etc.transient config`{.literal} option. When the directory is in mutable persistent state, it performs a 3-way merge across upgrades:

    -   Uses the new default `/etc`{.literal} as a base

    -   Applies the diff between current and previous `/etc`{.literal} to the new `/etc`{.literal} directory

    -   Retains locally modified files that are different from the default `/usr/etc`{.literal} of the same deployment in `/etc`{.literal}.

        The `ostree-finalize-staged.service`{.literal} performs these tasks during shutdown time, before creating the new boot loader entry. This happens because many components of a Linux system ship default configuration files in the `/etc`{.literal} directory. Even if the default package does not ship it, the software only checks for configuration files in `/etc`{.literal}.

        In the package-based update systems with no distinct versions of `/etc`{.literal} are populated only during the installation time, and cannot be changed at any point after installation. This causes the `/etc`{.literal} system state to be influenced by the initial image version and can lead to problems to apply a change, for example, to `/etc/sudoers.conf`{.literal}, and requires external intervention.

`/var`{.literal}

:   For example, there is only one `/var`{.literal} directory. By default, the files and data placed in the `/var`{.literal} directory are persistent until explicitly deleted, and available across different sessions and system restarts. You can turn the `/var`{.literal} partition or its subdirectories into a mount point, such as a temporary file system (TMPFS) or a network mount point. If you do not make a distinct partition for `/var`{.literal}, the system performs a bind mount, and creates a single, shared and persistent `/ostree/deploy/$stateroot/var`{.literal} in the `/var`{.literal} directory, so that both directories share the same data across deployments.

    By default, the content in `/var`{.literal} acts as a volume. The content from the container image is copied during the initial installation time, and is not updated thereafter.

    The `/var`{.literal} and the `/etc`{.literal} directories are different. You can use `/etc`{.literal} for small configuration files, and the expected configuration files are often bound to the operating system binaries in `/usr`{.literal}. The `/var`{.literal} directory has arbitrarily large data, for example, system logs, databases, and by default, do not roll back if the operating system state is rolled back.

    For example, making an update such as `dnf downgrade postgresql`{.literal} should not affect the physical database in `/var/lib/postgres`{.literal}. Similarly, making a `bootc update`{.literal} or `bootc rollback`{.literal} do not affect this application data.

    If the `/var`{.literal} is separate, it also work cleanly to stage new operating system updates before applying them. The updates are downloaded and ready, but only take effect on reboot. The same applies for Docker volume, as it decouples the application code from its data.

    You can use this case if you want applications to have a pre-created directory structure, for example, `/var/lib/postgresql`{.literal}. Use `systemd tmpfiles.d`{.literal} for this. You can also use `StateDirectory=`{.literal}*`<directory>`{.literal}* in units.

Other directories
:   There is no support to ship content in `/run`{.literal}, `/proc`{.literal} or other API Filesystems in container images. Apart from that, other top level directories such as `/usr`{.literal}, and `/opt`{.literal}, are lifecycled with the container image.

`/opt`{.literal}

:   Because `bootc`{.literal} uses `composefs`{.literal}, the `/opt`{.literal} directory is read-only, alongside other top level directories such as `/usr`{.literal}.

    When a software needs to write to its own directory in `/opt/exampleapp`{.literal}, a common pattern is to use a symbolic link to redirect to, for example, `/var`{.literal} for operations such as log files:

``` {.language-plaintext tabindex="-1"}
RUN rmdir /opt/exampleapp/logs && ln -sr /var/log/exampleapp /opt/exampleapp/logs
```

Optionally, you can configure the systemd unit to launch the service to do these mounts dynamically. For example:

``` {.language-plaintext tabindex="-1"}
BindPaths=/var/log/exampleapp:/opt/exampleapp/logs
```

Enabling transient root
:   Enable transient root to allow software to write transiently (until the next reboot) to all top-level directories, including `/usr`{.literal} and `/opt`{.literal}. It uses symlinks to `/var`{.literal} for persistent content. To enable a fully transient writable `rootfs`{.literal} by default, set the following option in `/usr/lib/ostree/prepare-root.conf`{.literal}.

``` {.language-plaintext tabindex="-1"}
[root]
transient = true
```

This enables a software to transiently write to `/opt`{.literal}, with symlinks to `/var`{.literal} for content that must persist.

**Additional resources**

-   [Details about file configuration, building and testing RHEL bootc images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/building-and-testing-rhel-bootc-images)

### [18.2. Version selection and bootup](#version-selection-and-bootup) {#version-selection-and-bootup .title}

Image mode for RHEL uses GRUB by default, with exception to IBM Z® architectures. Each version of image mode for RHEL currently available on a system has a menu entry.

The menu entry references an OSTree deployment, which consists of a Linux kernel, an `initramfs`{.literal} and a hash linking to an OSTree commit, which you can pass by using the `ostree=kernel`{.literal} argument.

During bootup, OSTree reads the kernel argument to determine which deployment to use as the root filesystem. Each update or change to the system, such as package installation, addition of kernel arguments, creates a new deployment.

This enables rolling back to a previous deployment if the update causes problems.

## [Chapter 19. Configure bootc images on first boot by using Ignition](#using-ignition-with-bootc-images) {#chapter-19.-configure-bootc-images-on-first-boot-by-using-ignition .title}

You can configure `bootc`{.literal} systems dynamically at first boot by using the Ignition tool. With Ignition, you can standardize a small number of base images and customize them at runtime. This eliminates the need to create separate image variants for each hardware or environment combination.

On first boot, Ignition executes user-provided configuration files to configure environment-specific details, such as networking, users, and storage, before the system starts.

### [19.1. About dynamic provisioning in bootc by using Ignition](#ignition-overview-for-bootc) {#about-dynamic-provisioning-in-bootc-by-using-ignition .title}

Ignition is a first-boot provisioning system that configures Linux systems during the `initramfs`{.literal} phase. You can use Ignition to dynamically configure `bootc`{.literal} systems without maintaining multiple image variants.

Ignition runs only once, during the first boot of a system. It reads a declarative configuration file and applies the specified changes before the system transitions to the real root file system.

Ignition can perform the following configuration tasks:

-   Create users and groups

-   Add SSH authorized keys

-   Write files and directories

-   Configure systemd units

-   Set up disk partitions and file systems

-   Configure network settings

    How Ignition works with `bootc`{.literal}

    :   `bootc`{.literal} images use `OSTree`{.literal} for atomic updates and rollbacks. Ignition integrates with `OSTree`{.literal} by mounting the `/var`{.literal} directory writable during the `initramfs`{.literal} phase, enabling configuration changes to persist.

        The following sequence describes the Ignition boot process:

        1.  The boot loader passes the `ignition.firstboot`{.literal} kernel parameter.
        2.  The `initramfs`{.literal} loads and starts Ignition services.
        3.  Ignition fetches the configuration from the platform-specific data source.
        4.  Ignition mounts `/var`{.literal} writable and applies the configuration.
        5.  The `initramfs`{.literal} transitions to the real root file system.
        6.  After the first boot completes, the system removes the firstboot marker.

    Benefits of using `Ignition`{.literal}
    :   To keep your core operating system image generic and reusable across your entire infrastructure, you can use `Ignition`{.literal} to inject environment-specific configuration during boot, which enables a \"build once, configure at runtime\" approach. This approach has the following benefits:

-   Reduced image sprawl: Maintain a small set of base images instead of dozens of variants.

-   Dynamic configuration: Apply environment-specific settings such as DNS resolvers, NTP servers, and network parameters at boot time.

-   Declarative provisioning: Define the required system state in a `JSON`{.literal} configuration file.

-   Runs on first boot only: Ignition executes a single time during initial provisioning. This prevents accidental re-configurations on subsequent restarts.

### [19.2. About Ignition integration layers for bootc](#ignition-integration-layers-for-bootc) {#about-ignition-integration-layers-for-bootc .title}

`bootc`{.literal} images rely on specific integration layers to process Ignition configurations on first boot. Understanding these layers helps you ensure your custom base images are properly equipped for dynamic provisioning.

The `ignition-edge`{.literal} package provides four integration layers that bridge Ignition with `OSTree`{.literal}:

`sshd`{.literal} `authorized_keys.d`{.literal} support
:   Ignition writes SSH keys to the `~/.ssh/authorized_keys.d/ignition`{.literal} directory. Upstream `OpenSSH`{.literal} does not support glob patterns in `AuthorizedKeysFile`{.literal}, so the `sshd`{.literal} configuration must explicitly list the paths.

`OSTree`{.literal} `/var`{.literal} mount and populate

:   A built-in `dracut`{.literal} module automatically bind-mounts the `/var`{.literal} directory as writable and populates standard subdirectories before the Ignition file stage runs.

    Because OSTree systems enforce a read-only `/usr`{.literal} file system, no action is required on your part. However, ensure that any custom files or persistent data created by Ignition are targeted to the `/var`{.literal} or `/etc`{.literal} directories rather than `/usr`{.literal}.

First-boot completion
:   A `systemd`{.literal} service that removes the `/boot/ignition.firstboot`{.literal} stamp after Ignition runs. This marker prevents Ignition from re-running on subsequent boots.

Network enablement
:   A service that enables network access in the `initramfs`{.literal} when Ignition needs to fetch remote configurations.

Supported dracut modules

:   The following `dracut`{.literal} modules support Ignition on `bootc`{.literal}:

    -   `35ignition-edge`{.literal}: The primary integration module that installs Ignition support scripts, generators, and `systemd`{.literal} units.
    -   `10coreos-sysctl`{.literal}: Configures kernel parameters required during boot.
    -   `99journal-conf`{.literal}: Configures journal logging for the `initramfs`{.literal} phase.
    -   `99emergency-shell-setup`{.literal}: Provides debugging capabilities when Ignition fails.

Supported systemd services

:   The integration includes the following `systemd`{.literal} services:

    -   `ignition-firstboot-complete.service`{.literal}: Runs after Ignition completes and removes the firstboot marker from the `/boot`{.literal} directory.
    -   `coreos-check-ssh-keys.service`{.literal}: Displays SSH key status on the system console after boot.
    -   `coreos-ignition-write-issues.service`{.literal}: Writes Ignition status information to the `/etc/issue.d/`{.literal} directory for display at login.

**Additional resources**

-   [Enable Ignition in bootc container images](#enabling-ignition-in-bootc-container-images "19.5. Enable Ignition in bootc container images")

### [19.3. Required packages for Ignition support](#required-packages-for-ignition-support) {#required-packages-for-ignition-support .title}

To configure Ignition support in `bootc`{.literal} images, you must install the required packages and their dependencies.

+---------------------------+---------------------------------------------------------------------------------------------------------------------------------+-----------------+
| Package                   | Description                                                                                                                     | Required        |
+:==========================+:================================================================================================================================+:================+
| `ignition`{.literal}      | The Ignition provisioning utility that reads and applies configuration.                                                         | Yes             |
+---------------------------+---------------------------------------------------------------------------------------------------------------------------------+-----------------+
| `ignition-edge`{.literal} | Integration layers for `OSTree`{.literal}-based systems, including `dracut`{.literal} modules and `systemd`{.literal} services. | Yes             |
+---------------------------+---------------------------------------------------------------------------------------------------------------------------------+-----------------+
| `dracut`{.literal}        | The `initramfs`{.literal} generator that includes Ignition modules.                                                             | Yes             |
+---------------------------+---------------------------------------------------------------------------------------------------------------------------------+-----------------+

: Table 19.1. Core packages for Ignition support

Show more

Note

You do not need to explicitly list `dracut`{.literal} in your `Containerfile`{.literal}. Standard `bootc`{.literal} base images already include it, and it updates automatically when you install `ignition-edge`{.literal}.

Platform-specific packages
:   Depending on your deployment platform, you might need additional packages:

+------------------------------+-----------------------------------------------------------------------------------+----------------------------------------------+
| Package                      | Description                                                                       | Platform                                     |
+:=============================+:==================================================================================+:=============================================+
| `afterburn`{.literal}        | Fetches instance metadata from cloud platforms and configures SSH keys.           | Cloud deployments (AWS, Azure, Google Cloud) |
+------------------------------+-----------------------------------------------------------------------------------+----------------------------------------------+
| `afterburn-dracut`{.literal} | `dracut`{.literal} module for Afterburn integration in the `initramfs`{.literal}. | Cloud deployments                            |
+------------------------------+-----------------------------------------------------------------------------------+----------------------------------------------+
| `qemu-guest-agent`{.literal} | QEMU guest agent for virtual machine integration.                                 | QEMU/KVM                                     |
+------------------------------+-----------------------------------------------------------------------------------+----------------------------------------------+

: Table 19.2. Platform-specific packages

Show more

**Additional resources**

-   [Enable Ignition in bootc container images](#enabling-ignition-in-bootc-container-images "19.5. Enable Ignition in bootc container images")

### [19.4. Ignition platform parameters](#ignition-platform-parameters) {#ignition-platform-parameters .title}

Ignition uses platform identifiers to locate and retrieve configuration payloads during early boot. Identifying the correct platform parameter ensures that Ignition targets the appropriate metadata service or boot media.

The `ignition.platform.id`{.literal} kernel argument specifies the configuration source, such as `qemu`{.literal}, `aws`{.literal}, or `metal`{.literal}.

When you build or provision a `bootc`{.literal} image, you can pass this parameter directly by using the boot loader or embed it into the image configuration.

+------------------------+--------------------------------------------+-------------------------------------------------------------------------------------------+
| Platform ID            | Description                                | Configuration source                                                                      |
+:=======================+:===========================================+:==========================================================================================+
| `metal`{.literal}      | Bare-metal servers without cloud metadata. | Boot partition: `/boot/ignition/config.ign`{.literal}                                     |
+------------------------+--------------------------------------------+-------------------------------------------------------------------------------------------+
| `qemu`{.literal}       | QEMU/KVM virtual machines.                 | `fw_cfg`{.literal}: `/etc/ignition/config.ign`{.literal} or `virtio-blk`{.literal} device |
+------------------------+--------------------------------------------+-------------------------------------------------------------------------------------------+
| `aws`{.literal}        | Amazon Web Services EC2 instances.         | EC2 instance user data                                                                    |
+------------------------+--------------------------------------------+-------------------------------------------------------------------------------------------+
| `azure`{.literal}      | Microsoft Azure virtual machines.          | Azure instance metadata service                                                           |
+------------------------+--------------------------------------------+-------------------------------------------------------------------------------------------+
| `gcp`{.literal}        | Google Cloud Platform Compute Engine.      | GCP metadata server                                                                       |
+------------------------+--------------------------------------------+-------------------------------------------------------------------------------------------+
| `virtualbox`{.literal} | Oracle VirtualBox virtual machines.        | Guest properties                                                                          |
+------------------------+--------------------------------------------+-------------------------------------------------------------------------------------------+
| `vmware`{.literal}     | VMware vSphere/ESXi virtual machines.      | vSphere `guestinfo`{.literal}                                                             |
+------------------------+--------------------------------------------+-------------------------------------------------------------------------------------------+

: Table 19.3. Ignition platform parameters

Show more

Architecture-specific parameters
:   Different CPU architectures require specific configuration delivery methods:

+----------------------+-------------------------------------------------------------------------------------+
| Architecture         | Preferred delivery method                                                           |
+:=====================+:====================================================================================+
| `x86_64`{.literal}   | `fw_cfg`{.literal} (`-fw_cfg name=opt/com.coreos/config,file=config.ign`{.literal}) |
+----------------------+-------------------------------------------------------------------------------------+
| `AArch64`{.literal}  | `fw_cfg`{.literal} (`-fw_cfg name=opt/com.coreos/config,file=config.ign`{.literal}) |
+----------------------+-------------------------------------------------------------------------------------+
| `s390x`{.literal}    | `virtio-blk`{.literal} device with Ignition configuration                           |
+----------------------+-------------------------------------------------------------------------------------+
| `ppc64le`{.literal}  | `virtio-blk`{.literal} device with Ignition configuration                           |
+----------------------+-------------------------------------------------------------------------------------+

: Table 19.4. Architecture-specific parameters

Show more

Kernel command line examples
:   The following examples show how to set Ignition parameters in the kernel command line:

Bare metal
:   `ignition.platform.id=metal ignition.firstboot`{.literal}

QEMU with `fw_cfg`{.literal}
:   `ignition.platform.id=qemu ignition.firstboot`{.literal}

AWS EC2
:   `ignition.platform.id=aws ignition.firstboot`{.literal}

### [19.5. Enable Ignition in bootc container images](#enabling-ignition-in-bootc-container-images) {#enable-ignition-in-bootc-container-images .title}

To configure Ignition support in `bootc`{.literal} images, you must install the required packages and configure the `initramfs`{.literal}. You must complete this procedure to provision `bootc`{.literal} systems dynamically at first boot.

**Prerequisites**

-   You have a container build environment with Podman. See [Building a container image](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/building-and-testing-rhel-bootc-images#building-a-container-image).
-   You have access to a `bootc`{.literal} base image, such as CentOS Stream, Fedora, or RHEL.

**Procedure**

1.  Create a new directory for your `bootc`{.literal} image build:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir ignition-bootc && cd ignition-bootc
    ```

2.  Create a `Containerfile`{.literal} with the required packages and configuration:

    ``` {.language-plaintext tabindex="-1"}
    FROM registry.redhat.io/rhel10/rhel-bootc:latest

    # Install Ignition and integration packages
    RUN dnf install -y \
        ignition \
        ignition-edge \
        && dnf clean all

    # Configure sshd to read Ignition-provided SSH keys
    RUN mkdir -p /etc/ssh/sshd_config.d && \
        echo 'AuthorizedKeysFile .ssh/authorized_keys .ssh/authorized_keys.d/ignition' \
        > /etc/ssh/sshd_config.d/40-ignition-authorized-keys.conf
    ```

    Important

    Do not attempt to run `dracut`{.literal} to build an `initramfs`{.literal} inside the container layer. Image compilation tools, such as `bootc-image-builder`{.literal}, automatically import the installed Ignition binaries and inject them into the physical boot `initramfs`{.literal} when compiling the final disk image, such as an ISO, AMI, or raw image.

3.  Build the container image:

    ``` {.language-plaintext tabindex="-1"}
    $ podman build -t localhost/ignition-bootc:latest .
    ```

4.  Push the image to your container registry:

    ``` {.language-plaintext tabindex="-1"}
    $ podman push localhost/ignition-bootc:latest quay.io/myorg/ignition-bootc:latest
    ```

**Verification**

1.  Confirm that the `ignition`{.literal} and `ignition-edge`{.literal} packages are installed in the container:

    ``` {.language-plaintext tabindex="-1"}
    $ rpm -qa | grep ignition
    ```

2.  Verify that the `/etc/ssh/sshd_config.d/40-ignition-authorized-keys.conf`{.literal} file exists and has the correct `sshd`{.literal} keys configured.

3.  Verify that the `/usr/lib/ostree/prepare-root.conf`{.literal} file contains the transient root configuration:

    ``` {.language-plaintext tabindex="-1"}
    [composefs]
    enabled = maybe

    [root]
    transient = true
    ```

### [19.6. Create an Ignition configuration for bare-metal deployments](#creating-an-ignition-configuration-for-bare-metal-deployments) {#create-an-ignition-configuration-for-bare-metal-deployments .title}

To provision bare-metal servers without cloud metadata services, you can create an Ignition configuration file and place it on the boot partition.

**Prerequisites**

-   You have an Ignition-enabled `bootc`{.literal} image. See [Enable Ignition in bootc container images](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/using-ignition-with-bootc-images#enabling-ignition-in-bootc-container-images).

-   You have access to the target system's boot media.

-   The `butane`{.literal} utility is installed on your local machine to convert Butane YAML configurations to Ignition JSON.

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dnf install -y butane
    ```

**Procedure**

1.  Create a Butane configuration file named `config.bu`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    variant: r4e
    version: 1.5.0
    passwd:
      users:
        - name: core
          ssh_authorized_keys:
            - ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAB... user@example.com
    storage:
      files:
        - path: /etc/hostname
          mode: 0644
          contents:
            inline: bootc-server-01
        - path: /etc/resolv.conf
          mode: 0644
          contents:
            inline: |
              nameserver 192.168.1.1
              nameserver 8.8.8.8
              search example.com
        - path: /etc/chrony.conf
          mode: 0644
          contents:
            inline: |
              server ntp1.example.com iburst
              server ntp2.example.com iburst
              driftfile /var/lib/chrony/drift
              makestep 1.0 3
              rtcsync
    systemd:
      units:
        - name: custom-firstboot.service
          enabled: true
          contents: |
            [Unit]
            Description=Custom first boot configuration
            After=network-online.target
            Wants=network-online.target
            ConditionFirstBoot=yes

            [Service]
            Type=oneshot
            ExecStart=/usr/bin/echo "First boot configuration complete"

            [Install]
            WantedBy=multi-user.target
    ```

2.  Convert the Butane configuration to the Ignition JSON format:

    ``` {.language-plaintext tabindex="-1"}
    $ butane --strict config.bu > config.ign
    ```

3.  Create the `/boot/ignition/`{.literal} directory on the target system's boot partition:

    ``` {.language-plaintext tabindex="-1"}
    $ mkdir -p /mnt/boot/ignition
    ```

4.  Copy the Ignition configuration file to the `/boot/ignition/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    $ cp config.ign /mnt/boot/ignition/config.ign
    ```

5.  Configure the boot loader to pass the required kernel parameters. Add the following parameters to the kernel command line:

    `ignition.platform.id=metal ignition.firstboot`{.literal}

6.  Boot the system from the configured media. Ignition reads the configuration and applies it during the `initramfs`{.literal} phase.

**Verification**

1.  After the system boots, log in using the SSH key specified in the configuration:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh core@<server_ip>
    ```

2.  Verify the host name:

    ``` {.language-plaintext tabindex="-1"}
    $ hostnamectl
    ```

3.  Check that the DNS configuration is applied:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /etc/resolv.conf
    ```

4.  View the Ignition logs to check for any errors:

    ``` {.language-plaintext tabindex="-1"}
    $ journalctl -u ignition-files.service
    ```

### [19.7. Create an Ignition configuration for cloud deployments](#creating-an-ignition-configuration-for-cloud-deployments) {#create-an-ignition-configuration-for-cloud-deployments .title}

To provision `bootc`{.literal} instances on AWS, Azure, Google Cloud, and other cloud platforms, you can pass the Ignition configuration through the cloud provider's user data mechanism.

**Prerequisites**

-   You have an Ignition-enabled `bootc`{.literal} image uploaded to your cloud provider. See [Creating AMI images by using bootc-image-builder and uploading them to AWS](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/creating-bootc-compatible-base-disk-images-by-using-bootc-image-builder#creating-ami-images-by-using-bootc-image-builder-and-uploading-them-to-aws).

-   You have access to the cloud provider's console or CLI.

-   The `butane`{.literal} utility is installed on your local machine to convert Butane YAML configurations to Ignition JSON.

    ``` {.language-plaintext tabindex="-1"}
    $ sudo dnf install -y butane
    ```

**Procedure**

1.  Create a Butane configuration file named `cloud-config.bu`{.literal}:

    ``` {.language-plaintext tabindex="-1"}
    variant: r4e
    version: 1.5.0
    passwd:
      users:
        - name: core
          groups:
            - wheel
            - sudo
    storage:
      files:
        - path: /etc/hostname
          mode: 0644
          contents:
            inline: <hostname>
        - path: /etc/sysconfig/network-scripts/ifcfg-eth0
          mode: 0644
          contents:
            inline: |
              DEVICE=eth0
              BOOTPROTO=dhcp
              ONBOOT=yes
        - path: /etc/profile.d/cloud-env.sh
          mode: 0644
          contents:
            inline: |
              export CLOUD_PROVIDER="aws"
              export ENVIRONMENT="production"
      directories:
        - path: /var/log/applications
          mode: 0755
    systemd:
      units:
        - name: cloud-init-replacement.service
          enabled: true
          contents: |
            [Unit]
            Description=Cloud initialization tasks
            After=network-online.target
            Wants=network-online.target
            ConditionFirstBoot=yes

            [Service]
            Type=oneshot
           ExecStart=/bin/sh -c '/usr/bin/curl -s http://169.254.169.254/latest/meta-data/instance-id > /var/lib/instance-id'
            ExecStart=/usr/bin/echo "Cloud initialization complete"

            [Install]
            WantedBy=multi-user.target
    ```

2.  Convert the Butane configuration to an Ignition JSON file:

    ``` {.language-plaintext tabindex="-1"}
    $ butane --strict cloud-config.bu > cloud-config.ign
    ```

3.  Deploy the instance with the Ignition configuration as user data.

    -   For AWS EC2, run:

        ``` {.language-plaintext tabindex="-1"}
        $ aws ec2 run-instances --image-id <ami_id> --instance-type <instance_type> --user-data file://cloud-config.ign --key-name <key_pair_name>
        ```

    -   For Azure, run:

        ``` {.language-plaintext tabindex="-1"}
        $ az vm create --resource-group <resource_group> --name <vm_name> --image <ignition_image> --custom-data cloud-config.ign --admin-username core
        ```

    -   For Google Cloud, run:

        ``` {.language-plaintext tabindex="-1"}
        $ gcloud compute instances create <instance_name> --image <ignition_image> --metadata-from-file user-data=cloud-config.ign --machine-type <machine_type>
        ```

    -   For QEMU/KVM testing, run:

        ``` {.language-plaintext tabindex="-1"}
        $ qemu-system-x86_64 \ -machine q35 \ -cpu host \ -enable-kvm \ -m 4096 \ -fw_cfg name=opt/com.coreos/config,file=<path_to_config_file> \ -drive file=bootc-image.qcow2,format=qcow2 \ -netdev user,id=net0,hostfwd=tcp::2222-:22 \ -device virtio-net-pci,netdev=net0 \
          -append "ignition.platform.id=qemu ignition.firstboot"
        ```

**Verification**

1.  Connect to the instance:

    ``` {.language-plaintext tabindex="-1"}
    $ ssh core@<instance_ip>
    ```

2.  Verify that the cloud environment variables are set:

    ``` {.language-plaintext tabindex="-1"}
    $ source /etc/profile.d/cloud-env.sh
    ```

    ``` {.language-plaintext tabindex="-1"}
    $ echo ${CLOUD_PROVIDER}
    ```

3.  Check the Ignition execution status:

    ``` {.language-plaintext tabindex="-1"}
    $ journalctl -t ignition --no-pager
    ```

4.  Verify that the instance ID was captured (AWS example):

    ``` {.language-plaintext tabindex="-1"}
    $ cat /var/lib/instance-id
    ```

### [19.8. Ignition configuration options](#ignition-configuration-options) {#ignition-configuration-options .title}

You can configure various system aspects by using Ignition configuration sections. Follow these guidelines to ensure correct configuration syntax and structure.

Configuration format
:   Ignition uses the JSON format for configurations. The standard workflow uses Butane (YAML) for human-readable authoring, then converts to Ignition JSON.

**Converting Butane to Ignition**

``` {.language-plaintext tabindex="-1"}
$ butane --strict config.bu > config.ign
```

+------------------------------+--------------------------------------------------------------------------------------+
| Section                      | Purpose                                                                              |
+:=============================+:=====================================================================================+
| `ignition`{.literal}         | Specifies the configuration version and optional remote configuration sources.       |
+------------------------------+--------------------------------------------------------------------------------------+
| `storage`{.literal}          | Defines files, directories, links, disks, file systems, and RAID arrays.             |
+------------------------------+--------------------------------------------------------------------------------------+
| `passwd`{.literal}           | Configures users and groups.                                                         |
+------------------------------+--------------------------------------------------------------------------------------+
| `systemd`{.literal}          | Manages `systemd`{.literal} units (enable, disable, mask, or provide unit contents). |
+------------------------------+--------------------------------------------------------------------------------------+
| `kernel_arguments`{.literal} | Modifies kernel command line parameters for subsequent boots.                        |
+------------------------------+--------------------------------------------------------------------------------------+

: Table 19.5. Ignition configuration sections

Show more

Storage configuration
:   The `storage`{.literal} section supports the following resources:

+-------------------------+-------------------------------------------------------------------------+-----------------------------------+
| Resource                | Description                                                             | Example use case                  |
+:========================+:========================================================================+:==================================+
| `files`{.literal}       | Create or overwrite files with specified contents, mode, and ownership. | Configuration files, scripts      |
+-------------------------+-------------------------------------------------------------------------+-----------------------------------+
| `directories`{.literal} | Create directories with specified mode and ownership.                   | Log directories, application data |
+-------------------------+-------------------------------------------------------------------------+-----------------------------------+
| `links`{.literal}       | Create symbolic or hard links.                                          | Alternative paths, compatibility  |
+-------------------------+-------------------------------------------------------------------------+-----------------------------------+
| `disks`{.literal}       | Partition disks by using GPT.                                           | Data partitions                   |
+-------------------------+-------------------------------------------------------------------------+-----------------------------------+
| `filesystems`{.literal} | Create and format file systems.                                         | Additional storage volumes        |
+-------------------------+-------------------------------------------------------------------------+-----------------------------------+
| `raid`{.literal}        | Configure software RAID arrays.                                         | Redundant storage                 |
+-------------------------+-------------------------------------------------------------------------+-----------------------------------+

: Table 19.6. Storage section resources

Show more

File configuration example

:   

``` {.language-plaintext tabindex="-1"}
  storage:
    files:
      - path: /etc/resolv.conf
        mode: 0644
        contents:
          inline: |
            ...
      - path: /etc/chrony.conf      # <-- same level as first entry
        mode: 0644
```

User configuration

:   

``` {.language-plaintext tabindex="-1"}
passwd:
  users:
    - name: admin
      uid: 1001
      groups:
        - wheel
        - sudo
      ssh_authorized_keys:
        - ssh-rsa AAAAB3... admin@example.com
      password_hash: $6$rounds=4096$salt$hash...
    - name: appuser
      uid: 1002
      system: true
      no_create_home: true
```

Systemd unit configuration

:   

``` {.language-plaintext tabindex="-1"}
systemd:
  units:
    - name: myapp.service
      enabled: true
      contents: |
        [Unit]
        Description=My Application
        After=network-online.target

        [Service]
        Type=simple
        ExecStart=/usr/bin/myapp
        Restart=always

        [Install]
        WantedBy=multi-user.target
    - name: debug-shell.service
      mask: true
```

Kernel arguments

:   

``` {.language-plaintext tabindex="-1"}
kernel_arguments:
  should_exist:
    - systemd.unified_cgroup_hierarchy=1
    - mitigations=auto
  should_not_exist:
    - quiet
```

Multi-data-center configuration example
:   When managing systems across multiple data centers, create environment-specific configurations:

``` {.language-plaintext tabindex="-1"}
variant: r4e
version: 1.5.0
storage:
  files:
    - path: /etc/resolv.conf
      mode: 0644
      contents:
        inline: |
          nameserver 10.1.0.1
          nameserver 10.1.0.2
          search dc1.example.com example.com
      - path: /etc/chrony.conf
        mode: 0644
        contents:
          inline: |
            server ntp.dc1.example.com iburst prefer
            server ntp.example.com iburst
            driftfile /var/lib/chrony/drift
      - path: /etc/datacenter
        mode: 0644
        contents:
          inline: dc1
```

Configuration validation
:   You can validate Ignition configurations before deployment:

``` {.language-plaintext tabindex="-1"}
$ ignition-validate config.ign
```

Alternatively, you can use Butane's strict mode during conversion:

``` {.language-plaintext tabindex="-1"}
$ butane --strict config.bu > config.ign
```

### [19.9. Troubleshoot Ignition](#troubleshooting-ignition) {#troubleshoot-ignition .title}

You can diagnose Ignition issues by examining logs, checking service status, and verifying configuration delivery.

+-----------------------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Issue                       | Cause                                                                                               | Solution                                                                                                                                                      |
+:============================+:====================================================================================================+:==============================================================================================================================================================+
| Ignition does not run       | Missing `ignition.firstboot`{.literal} kernel parameter.                                            | Add `ignition.firstboot`{.literal} to the kernel command line in the `boot loader`{.literal} configuration.                                                   |
+-----------------------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Configuration not found     | Incorrect platform ID or missing configuration file.                                                | Verify that `ignition.platform.id`{.literal} matches your deployment method. Check the configuration location for your platform.                              |
+-----------------------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| SSH keys not accepted       | The `sshd`{.literal} service is not configured to read the `authorized_keys.d`{.literal} directory. | Add `sshd`{.literal} configuration: `AuthorizedKeysFile .ssh/authorized_keys .ssh/authorized_keys.d/ignition`{.literal}                                       |
+-----------------------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Files not persisted         | Writing to read-only file system locations.                                                         | Write files to the `/var`{.literal} or `/etc`{.literal} directory, which maps to `/var`{.literal} on `OSTree`{.literal} systems. Do not use `/usr`{.literal}. |
+-----------------------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ignition runs on every boot | First-boot marker not removed.                                                                      | Verify `ignition-firstboot-complete.service`{.literal} is enabled and runs successfully.                                                                      |
+-----------------------------+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 19.7. Ignition troubleshooting

Show more

View Ignition logs

:   You can check the Ignition execution logs by using the `journalctl`{.literal} utility.

    -   To view all Ignition messages, run:

        ``` {.language-plaintext tabindex="-1"}
        # journalctl -t ignition --no-pager
        ```

    -   To view logs for a specific Ignition service, such as `ignition-disks.service`{.literal}, `ignition-files.service`{.literal}, or `ignition-fetch.service`{.literal}, run:

        ``` {.language-plaintext tabindex="-1"}
        # journalctl -u ignition-disks.service
        ```

    -   To view the `initramfs`{.literal} Ignition logs from the current boot, run:

        ``` {.language-plaintext tabindex="-1"}
        # journalctl -b 0 | grep -i ignition
        ```

Checking service status

:   You can verify the status of Ignition-related services by using the `systemctl`{.literal} utility.

    -   To check the status of the first-boot completion service, run:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl status ignition-firstboot-complete.service
        ```

    -   To check the status of the SSH key notification service, run:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl status coreos-check-ssh-keys.service
        ```

    -   To list all Ignition-related services, run:

        ``` {.language-plaintext tabindex="-1"}
        # systemctl list-units 'ignition' 'coreos'
        ```

Verify configuration delivery

:   You can check if Ignition successfully received its configuration depending on your deployment environment.

    -   Inspect the Ignition configuration on bare metal

On bare-metal deployments, the Ignition configuration file is stored directly on the boot partition. To inspect the cached or copied configuration:

1.  Mount the boot partition:

    ``` {.language-plaintext tabindex="-1"}
    # mount /dev/disk/by-label/boot /mnt
    ```

2.  List the contents of the `/mnt/ignition/`{.literal} directory:

    ``` {.language-plaintext tabindex="-1"}
    # ls -la /mnt/ignition/
    ```

3.  View and format the contents of the Ignition configuration file:

    ``` {.language-plaintext tabindex="-1"}
    # cat /mnt/ignition/config.ign | jq .
    ```

4.  Unmount the boot partition:

    ``` {.language-plaintext tabindex="-1"}
    # umount /mnt
    ```

    -   Verify Ignition configuration fetching under QEMU

When you pass an Ignition configuration to a QEMU instance by using `initramfs`{.literal}, Ignition caches the downloaded payload in the `/run`{.literal} directory.

1.  Check if Ignition cached the configuration file:

    ``` {.language-plaintext tabindex="-1"}
    # ls -la /run/ignition.json
    ```

2.  View the contents of the cached configuration file:

    ``` {.language-plaintext tabindex="-1"}
    # cat /run/ignition.json | jq .
    ```

    Debug in the initramfs

    :   If Ignition fails during boot, the system might drop to an emergency shell. You can use the following commands to diagnose the issue:

        -   To check the status of the Ignition fetch service, run:

            ``` {.language-plaintext tabindex="-1"}
            # systemctl status ignition-fetch.service
            ```

        -   To view the error output for the Ignition fetch service, run:

            ``` {.language-plaintext tabindex="-1"}
            # journalctl -u ignition-fetch.service
            ```

        -   To check if the configuration source is accessible (QEMU `fw_cfg`{.literal} example), run:

            ``` {.language-plaintext tabindex="-1"}
            # cat /sys/firmware/qemu_fw_cfg/by_name/opt/com.coreos/config/raw
            ```

        -   To manually run Ignition in debug mode, run:

            ``` {.language-plaintext tabindex="-1"}
            # /usr/bin/ignition --platform=qemu --stage=fetch --log-to-stdout
            ```

    Resolve SSH key issues
    :   If SSH keys are not working on your deployed system, complete the following checks:

3.  Check where Ignition wrote the SSH keys:

    ``` {.language-plaintext tabindex="-1"}
    # ls -la /home/core/.ssh/
    ```

    ``` {.language-plaintext tabindex="-1"}
    # ls -la /home/core/.ssh/authorized_keys.d/
    ```

4.  Verify that the `sshd`{.literal} service configuration is set up correctly:

    ``` {.language-plaintext tabindex="-1"}
    # grep -r AuthorizedKeysFile /etc/ssh/
    ```

5.  Check the `sshd`{.literal} service logs for authorization events:

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -u sshd.service | grep -i authorized
    ```

    Resolve first-boot marker issues
    :   If Ignition runs on subsequent boots, complete the following checks:

6.  Check if the first-boot marker exists:

    ``` {.language-plaintext tabindex="-1"}
    # ls -la /boot/ignition.firstboot
    ```

7.  Check the status of the first-boot completion service:

    ``` {.language-plaintext tabindex="-1"}
    # systemctl status ignition-firstboot-complete.service
    ```

    ``` {.language-plaintext tabindex="-1"}
    # journalctl -u ignition-firstboot-complete.service
    ```

8.  If necessary, manually remove the first-boot marker:

    ``` {.language-plaintext tabindex="-1"}
    # mount -o remount,rw /boot
    ```

    ``` {.language-plaintext tabindex="-1"}
    # rm -f /boot/ignition.firstboot
    ```

    ``` {.language-plaintext tabindex="-1"}
    # rm -rf /boot/ignition
    ```

    Resolve configuration validation errors

    :   You can validate your configuration files before deployment to catch syntax errors:

        -   To validate an Ignition JSON file, run:

            ``` {.language-plaintext tabindex="-1"}
            # ignition-validate config.ign
            ```

        -   To validate a Butane YAML file, run:

            ``` {.language-plaintext tabindex="-1"}
            $ butane --strict config.bu > /dev/null
            ```

        -   To pretty-print and inspect the Ignition configuration, run:

            ``` {.language-plaintext tabindex="-1"}
            # cat config.ign | jq .
            ```

    Emergency console access
    :   If you cannot connect to the system by using SSH, use the following rescue steps:

9.  Connect to the system console (serial or VGA).

10. Examine the console output for Ignition error messages during boot.

11. If the system boots successfully, view the `/etc/issue.d/`{.literal} directory for status messages:

    ``` {.language-plaintext tabindex="-1"}
    $ cat /etc/issue.d/30_ssh_authorized_keys.issue
    ```

    Collect diagnostic information

    :   To gather system details for further troubleshooting, run the following diagnostic commands:

        -   To view system information:

            ``` {.language-plaintext tabindex="-1"}
            # hostnamectl
            ```

            ``` {.language-plaintext tabindex="-1"}
            # rpm -qa | grep ignition
            ```

        -   To view boot parameters:

            ``` {.language-plaintext tabindex="-1"}
            # cat /proc/cmdline
            ```

        -   To save the current boot's Ignition logs to a file:

            ``` {.language-plaintext tabindex="-1"}
            # journalctl -b 0 -t ignition > ignition.log
            ```

        -   To save a list of failed services to a file:

            ``` {.language-plaintext tabindex="-1"}
            # systemctl list-units --failed > failed-units.log
            ```

## [Chapter 20. Performing soft reboots to RHEL bootc images](#performing-soft-reboots-to-RHEL-bootc-images) {#chapter-20.-performing-soft-reboots-to-rhel-bootc-images .title}

Apply updates to Red Hat Enterprise Linux bootc systems by performing a `systemd`{.literal} soft reboot. This process reloads the operating system components without requiring a full hardware restart, ensuring faster deployment of changes and minimizing maintenance downtime.

### [20.1. Overview of performing soft reboots to RHEL bootc images](#overview-of-performing-soft-reboots-to-rhel-bootc-images) {#overview-of-performing-soft-reboots-to-rhel-bootc-images .title}

A soft reboot enables you to apply updates to Red Hat Enterprise Linux `bootc`{.literal} images without performing a full hardware restart. This process minimizes downtime by reloading the operating system components while skipping the firmware initialization stage, ensuring faster application of changes.

A soft reboot primarily resolves common software-related problems with minimal risk. It is a standard troubleshooting step for issues such as:

-   Minor software glitches: A soft reboot resolves temporary errors that cause applications to freeze, crash, or misbehave.
-   Performance issues: Over time, open applications and background processes consume resources and slow down a system. A soft reboot clears these processes and refreshes the RAM, which can improve performance.
-   Network problems: For issues such as connectivity drops, a restart refreshes the network settings of the system.
-   Completing updates: Some system updates require a reboot to be finalized properly.

In a RHEL environment with `systemd`{.literal}, a soft reboot restarts the user space while leaving the kernel and hardware running, which offers a significant benefits over a traditional, full reboot:

-   Reduced downtime: A soft reboot significantly reduces downtime because it skips the time-consuming boot process involving the BIOS/UEFI, boot loader, kernel, and initial RAM disk (`initrd`{.literal}) . The system can quickly become responsive again, which is important for critical servers where minimizing downtime is essential.
-   Improved operational efficiency: For software and configuration changes that do not involve the kernel, you can use soft reboot to apply updates without a full system restart. This is particularly useful for containerized or image-based systems where a new root filesystem snapshot can activate instantly.

When invoked, the `systemd-soft-reboot.service`{.literal} system service performs the following actions:

-   Sends a `SIGTERM`{.literal} signal to any processes left running, without waiting for the processes to exit.
-   Continues with a `SIGKILL`{.literal} signal to stop any process immediately.
-   If the `/run/nextroot/`{.literal} directory exists, which can be a regular directory, a directory mount point, or a symlink to either, it switches the file system root to it.
-   Re-runs the service manager from the root file system, which s updated, and enqueues a new boot transaction as a normal reboot.
-   `Soft-reboot.target`{.literal} pulls in this service and performs a user space-only reboot operation.

### [20.2. Soft reboot behavior in package and image mode](#soft-reboot-behavior-in-package-and-image-mode) {#soft-reboot-behavior-in-package-and-image-mode .title}

A system running in image mode performs a soft reboot similar to as a package mode system that reboots only userspace. The difference is that you must build the updates to these packages and services first on the container image.

Soft reboot behavior in the package mode

:   In a package-based system, for example, a RHEL system that uses `dnf`{.literal}, the soft reboot process involves shutting down and restarting `systemd`{.literal} units to load new libraries and binaries. You can apply updates with minimal downtime. When you apply updates by using `dnf`{.literal} in RHEL, `systemd`{.literal} manages the behavior of the system during a soft reboot. The key units and expected behaviors are:

    -   Service restarts: A soft reboot triggers `systemd`{.literal} to stop and restart all running services. Updated packages for services, such as, the web servers or databases, apply the patch when the service restarts and reloads the new binaries.
    -   Unit dependencies: `systemd`{.literal} shuts down and starts units based on their defined dependencies and ordering. A soft reboot ensures these relationships are maintained, minimizing the chance of an improper shutdown sequence.
    -   Processes and libraries: For updated shared libraries such as `glibc`{.literal} or `openssl`{.literal}, a running process continues to use the older, mapped library until it restarts. A soft reboot ensures that all processes stop and subsequently restart, causing them to link against the new version of the library.
    -   Minimal downtime: A soft reboot is significantly faster than a hard reboot, because it does not reinitialize the kernel and hardware. It is effective for applying most userspace updates with minimal service interruption.
    -   Command-line tools: The `dnf-plugins-core`{.literal} package includes the `needs-restarting`{.literal} tool. After running a `dnf update`{.literal}, you can run `dnf needs-restarting`{.literal} command to check if a soft reboot or specific service restart is required to apply the changes.

Userspace patching addresses security vulnerabilities and bugs in user-facing applications and shared libraries. When you apply patches, a soft reboot or process restart is required to load the new code. For example:

-   `OpenSSL`{.literal}: Use case: Critical OpenSSL vulnerability discovered.

Problem: Applications that use OpenSSL, such as web servers, databases, and SSH daemons, remain exposed without a restart, continuing to use the vulnerable shared library.

Soft reboot solution: After performing a `dnf update openssl`{.literal}, a soft reboot stops dependent processes. `Systemd`{.literal} then restarts these services, automatically loading the new, patched `libssl.so`{.literal} and `libcrypto.so`{.literal} libraries, securing the system without a full machine reboot.

-   `Glibc`{.literal}: Use case: A bug or security flaw is found in the `GNU C`{.literal} Library (glibc).

Problem: Glibc is a foundational userspace component that nearly every program on the system depends on. A vulnerability in glibc impacts the entire system. Restarting one or two services is not enough, as many other processes will still be vulnerable.

Soft reboot solution: A dnf update `glibc`{.literal} followed by a soft reboot is the most reliable way to ensure that all processes restart and re-link to the new glibc. This avoids the longer downtime of a full system reboot while guaranteeing the update is applied everywhere.

-   `dbus-broker`{.literal}:

Use case: Updating the `dbus-broker`{.literal} daemon for security or performance.

Problem: Dbus-broker is a critical system service. While updates are usually resilient, the sensitivity of the protocol requires restarting the broker and related services.

Soft reboot solution: A soft reboot restarts `dbus-broker`{.literal} and all dependent services and applications, with `systemd`{.literal} ensuring a clean shutdown and re-initialization.

Soft reboot behaviour in image mode for RHEL
:   In RHEL image mode (bootc), `systemd`{.literal} performs a fast, userspace-only restart (soft reboot). `Systemd-soft-reboot.service`{.literal} orchestrates this process, resetting the userspace while keeping the kernel and hardware running.

In an image-based system, you can manage updates in two ways:

-   Staged updates: The system fetches these updates from a container registry and installs them to an alternate, inactive partition or filesystem. It continues to run on the old version until it initiates a reboot.

A soft reboot switches the system to the newly staged, updated root filesystem and replaces the entire userspace at once. The system boots into the new, updated operating system image, and if issues appear, it retains the ability to roll back to the previous image on a subsequent boot.

-   Unstaged updates: Dynamic, in-place updates to the running userspace, such as configuration changes or restarting a single service. They do not involve creating and booting from a new, complete operating system image. A soft reboot reloads the current userspace from the same root file system. It does not pull or switch to a new, updated operating system image.

You can use it to reset the current software state without touching the kernel, which is useful for applying non-image-level changes or resolving userspace issues.

The `systemd`{.literal} soft reboot mechanism is different from a `kexec`{.literal} reboot. The `kexec`{.literal} and `kernel switching`{.literal} features are not available in the `systemd`{.literal} soft reboot, as it only restarts the userspace, leaving the kernel untouched. This ensures continuity and avoids the potential complexities and inconsistencies that can arise from changing kernels without a hardware reset. An updated operating system image that includes a new kernel version requires a traditional, full reboot.

### [20.3. Initiating a soft reboot](#initiating-a-soft-reboot) {#initiating-a-soft-reboot .title}

Initiate a soft reboot on Red Hat Enterprise Linux to apply system updates without performing a full hardware restart. This method minimizes downtime by reloading the operating system components while skipping the firmware initialization process.

You can detect and prepare the system for a soft reboot when the system administrator runs `bootc upgrade`{.literal}, `bootc switch`{.literal}, or `bootc rollback`{.literal} by using one of the two options:

-   `--soft-reboot=auto`{.literal}: It automatically prepares the system if soft-reboot is possible and will not error out if the system is not capable of soft-reboot.
-   `--soft-reboot=required`{.literal}: Automatically prepares the system if soft reboot is possible, but it errors out if the system is not capable of a soft reboot.

These options help you to manage when the limited downtime is required by stopping an `--apply`{.literal} operation or informing you not to call reboot as bootc has not exited cleanly.

**Prerequisites**

-   You have information about the current status of the system.

**Procedure**

1.  Perform an update, switch, or rollback operation by using the `bootc`{.literal} tool to stage the new container image. Otherwise, the soft runs again in the current userspace.

    ``` {.language-plaintext tabindex="-1"}
    $ sudo bootc update --soft-reboot=required --apply
    ```

2.  Initiate a soft reboot, for example, while running bootc switch:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo bootc switch --soft-reboot=required --apply quay.io/test_rh/soft-reboot:1
    ```

**Verification**

-   Verify the soft reboot is completed:

    ``` {.language-plaintext tabindex="-1"}
    $ systemctl show --value --property SoftRebootsCount
    1
    ```

-   Check the new `soft reboot:yes`{.literal} flag:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo bootc status --verbose
    ```

### [20.4. Known limitations of soft reboots](#known-limitations-of-soft-reboots) {#known-limitations-of-soft-reboots .title}

A soft reboot running in image mode has specific limitations because it is designed to update the userspace while leaving the kernel untouched.

The known limitations are:

-   Kernel and hardware remain unchanged: Any changes to the kernel, hardware drivers, or low-level kernel parameters are not applied during a soft reboot. For these updates to take effect, a full system reboot is necessary. Also, the kernel settings, for example, those configured by using `sysctl`{.literal}, are not reset during a soft reboot. The system continues to use the same settings from before the reboot.
-   Firmware initialization: During a soft reboot, the operating system skips the firmware initialization. This is because the operating system retains control and directly restarts the kernel using a system call, instead of fully relinquishing control to the hardware. The `kexec system call`{.literal} manages this process.
-   User responsibility for kernel module alignment with userspace changes: Even in image mode for RHEL, the user remains responsible for rebuilding and aligning custom kernel modules with userspace changes and a soft reboot does not bypass this. In fact, a soft reboot specifically keeps the running kernel, which can introduce compatibility issues if the userspace has been updated to expect a different kernel version or set of modules.

## [Chapter 21. Managing users, groups, SSH keys, and secrets in image mode for RHEL](#managing-users-groups-ssh-keys-and-secrets-in-image-mode-for-rhel) {#chapter-21.-managing-users-groups-ssh-keys-and-secrets-in-image-mode-for-rhel .title}

You can control system access by managing users, groups, SSH keys, and secrets in Image Mode for Red Hat Enterprise Linux. By configuring these credentials, you can establish secure authentication and authorization policies for your container-native operating system deployments.

### [21.1. Users and groups configuration](#users-and-groups-configuration) {#users-and-groups-configuration .title}

Configure users and groups in your Red Hat Enterprise Linux `bootc`{.literal} image to establish system access controls and administrative permissions. Defining these settings during the image build ensures consistent authentication policies across all deployments derived from that image.

Users and groups configuration for generic base images
:   Usually, the distribution base images do not have any configuration. Do not encrypt passwords and SSH keys with publicly-available private keys in generic images because of security risks.

Injecting SSH keys through `systemd`{.literal} credentials
:   You can use `systemd`{.literal} to inject a root password or SSH `authorized_keys`{.literal} file in some environments. For example, use System Management firmware (SMBIOS) to inject SSH keys system firmware. You can configure this in local virtualization environments, such as `qemu`{.literal}.

Injecting users and SSH keys by using `cloud-init`{.literal}
:   Many Infrastructure as a service (IaaS) and virtualization systems use metadata servers that are commonly processed by software such as `cloud-init`{.literal} or `ignition`{.literal}. See [AWS instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html). The base image you are using might include `cloud-init`{.literal} or Ignition, or you can install it in your own derived images. In this model, the SSH configuration is managed outside of the bootc image.

Adding users and credentials by using container or unit custom logic
:   Systems such as `cloud-init`{.literal} are not privileged. You can inject any logic you want to manage credentials in the way you want to launch a container image, for example, by using a `systemd`{.literal} unit. To manage the credentials, you can use a custom network-hosted source, for example, [FreeIPA](https://www.freeipa.org/page/Main_Page).

Adding users and credentials statically in the container build

:   In package-oriented systems, you can use the derived build to inject users and credentials by using the following command:

    ``` {.language-plaintext tabindex="-1"}
    RUN useradd someuser
    ```

    You can find issues in the default `shadow-utils`{.literal} implementation of `useradd`{.literal}: Users and groups IDs are allocated dynamically, and this can cause drift.

User and group home directories and `/var`{.literal} directory

:   For systems configured with persistent `/home → /var/home`{.literal}, any changes to `/var`{.literal} made in the container image after initial installation will not be applied on subsequent updates.

    For example, if you inject `/var/home/someuser/.ssh/authorized_keys`{.literal} into a container build, existing systems do not get the updated `authorized_keys`{.literal} file.

Using DynamicUser=yes for `systemd`{.literal} units

:   Use the `systemd`{.literal} `DynamicUser=yes`{.literal} option where possible for system users.

    This is significantly better than the pattern of allocating users or groups at package install time, because it avoids potential UID or GID drift.

Using `nss-altfiles`{.literal}

:   The `nss-altfiles`{.literal} splits system users into `/usr/lib/passwd`{.literal} and `/usr/lib/group`{.literal}, aligning with the way the OSTree project handles the 3 way merge for `/etc`{.literal} as it relates to `/etc/passwd`{.literal}. Currently, if the `/etc/passwd`{.literal} file is modified in any way on the local system, then subsequent changes to `/etc/passwd`{.literal} in the container image are not applied.

    Base images built by `rpm-ostree`{.literal} have `nss-altfiles`{.literal} enabled by default.

    Also, base images have a system users pre-allocated and managed by the NSS file to avoid UID or GID drift.

    In a derived container build, you can also append users to `/usr/lib/passwd`{.literal}, for example. Use `sysusers.d`{.literal} or `DynamicUser=yes`{.literal}.

Using `systemd`{.literal}-sysusers

:   Use `systemd`{.literal}-sysusers, for example, in your derived build. For more information, see the `systemd`{.literal} [-sysusers](https://www.freedesktop.org/software/systemd/man/latest/systemd-sysusers.html) documentation.

    ``` {.language-plaintext tabindex="-1"}
    COPY mycustom-user.conf /usr/lib/sysusers.d
    ```

    The `sysusers`{.literal} tool makes changes to the traditional `/etc/passwd`{.literal} file as necessary during boot time. If `/etc`{.literal} is persistent, this can avoid `UID`{.literal} or `GID`{.literal} drift. It means that the `UID`{.literal} or `GID`{.literal} allocation depends on how a specific machine was upgraded over time.

Machine-local state for users

:   The filesystem layout depends on the base image.

    By default, the user data is stored in both `/etc`{.literal}, `/etc/passwd`{.literal}, `/etc/shadow`{.literal} and `groups`{.literal}, and `/home`{.literal}, depending on the base image. However, the generic base images have to both be machine-local persistent state. In this model `/home`{.literal} is a symlink to `/var/home/`{.literal}*`user`{.literal}*.

Injecting users and SSH keys at system provisioning time

:   For base images where `/etc`{.literal} and `/var`{.literal} are configured to persist by default, you can inject users by using installers such as Anaconda or Kickstart.

    Typically, generic installers are designed for one time bootstrap. Then, the configuration becomes a mutable machine-local state that you can change in Day 2 operations, by using some other mechanism.

    You can use the Anaconda installer to set the initial password. However, changing this initial password requires a different in-system tool, such as `passwd`{.literal}.

    These flows work equivalently in a `bootc-compatible`{.literal} system, to support users directly installing generic base images, without requiring changes to the different in-system tool.

Transient home directories

:   Many operating system deployments minimize persistent, mutable, and executable state. This can damage user home directories.

    The `/home`{.literal} directory can be set as `tmpfs`{.literal}, to ensure that user data is cleared across reboots. This approach works especially well when combined with a transient `/etc`{.literal} directory.

    To configure the user's home directory to, for example, inject SSH `authorized_keys`{.literal} or other files, use the `systemd`{.literal} `tmpfiles.d`{.literal} snippets:

    ``` {.language-plaintext tabindex="-1"}
    f~ /home/user/.ssh/authorized_keys 600 user user - <base64 encoded data>
    ```

    SSH is embedded in the image as: `/usr/lib/tmpfiles.d/<username-keys.conf`{.literal}. Another example is a service embedded in the image that can fetch keys from the network and write them. This is the pattern used by `cloud-init`{.literal}.

UID and GID drift
:   The `/etc/passwd`{.literal} and similar files are a mapping between names and numeric identifiers. When the mapping is dynamic and mixed with \"stateless\" container image builds, it can cause issues. Each container image build might result in the UID changing due to RPM installation ordering or other reasons. This can be a problem if that user maintains a persistent state. To handle such cases, convert it to use `sysusers.d`{.literal} or use `DynamicUser=yes`{.literal}.

### [21.2. Methods for injecting secrets into bootc systems](#methods-for-injecting-secrets-into-bootc-systems) {#methods-for-injecting-secrets-into-bootc-systems .title}

You can inject secrets into `bootc`{.literal} container images by using several methods, including embedding secrets at build time, fetching them from cloud metadata servers, embedding them into disk images, passing them through installer tools, or using systemd credentials to deliver them securely to services at runtime.

Injecting secrets by embedding them in a container build
:   You can include secrets in the container image if the registry server is suitably protected. In some cases, embedding only bootstrap secrets into the container image is a viable pattern, especially alongside a mechanism for having a machine authenticate to a cluster. In this pattern, a provisioning tool, whether run as part of the host system or a container image, uses the bootstrap secret to inject or update other secrets, such as SSH keys and certificates.

Injecting secrets by using cloud metadata
:   Most production Infrastructure as a Service (IaaS) systems support a metadata server or equivalent which can securely host secrets, particularly bootstrap secrets. Your container image can include tools such as `cloud-init`{.literal} or `ignition`{.literal} to fetch these secrets.

Injecting secrets by embedding them in disk images
:   You can embed bootstrap secrets only in disk images. For example, when you generate a cloud disk image from an input container image, such as AMI or OpenStack, the disk image can contain secrets that are effectively machine-local state. Rotating them requires an additional management tool or refreshing the disk images.

Injecting secrets by using bare-metal installers
:   Installer tools like Anaconda support injecting configuration through secrets.

Injecting secrets through `systemd`{.literal} credentials

:   The `systemd`{.literal} project has a credential concept for securely acquiring and passing credential data to systems and services, which applies in some deployment methodologies. When you start a service with one or more credentials set, systemd sets the `$CREDENTIALS_DIRECTORY`{.literal} environment variable. This variable contains an absolute path to the directory where the credentials are present, and the system places one file for each configured credential in this directory.

    Additionally, the `%d`{.literal} specifier in unit files resolves to the service's credential directory, which the system passes to the service processes alongside the `$CREDENTIALS_DIRECTORY`{.literal} environment variable.

### [21.3. Injecting secrets in image mode for RHEL](#injecting-secrets-in-image-mode-for-rhel) {#injecting-secrets-in-image-mode-for-rhel .title}

You can embed a registry pull secret in a `bootc`{.literal} container image at build time so that `bootc`{.literal} and Podman can pull protected images and updates. Use a secret mount during the image build, then link the secret to the persistent credential path in the image.

**Prerequisites**

-   You have access to a RHEL bootc base container image.
-   You have created the necessary secret files or credentials on the host machine or in a secure secret storage service.

**Procedure**

1.  Create `containers-auth.conf`{.literal} file:

    ``` {.language-plaintext tabindex="-1"}
    # Make /run/containers/0/auth.json (a transient runtime file)
    # a symlink to our /usr/lib/container-auth.json (a persistent file)
    # which is also symlinked from /etc/ostree/auth.json.
    d /run/containers/0 0755 root root -
    L /run/user/0/containers/auth.json - - - - ../../../../usr/lib/container-auth.json
    ```

2.  For `bootc`{.literal} to fetch updates from a registry that requires authentication, you must include a pull secret in a file. In the following example, the `creds`{.literal} secret contains the registry pull secret.

    ``` {.language-plaintext tabindex="-1"}
    FROM quay.io/<namespace>/<image>:<tag>
    COPY containers-auth.conf /usr/lib/tmpfiles.d/link-podman-credentials.conf
    RUN --mount=type=secret,id=creds,required=true cp /run/secrets/creds /usr/lib/container-auth.json && \
      chmod 0600 /usr/lib/container-auth.json && \
      ln -sr /usr/lib/container-auth.json /etc/ostree/auth.json
    ```

3.  Build an image by using `podman build`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    $ podman build --secret id=creds,src=$HOME/.docker/config.json
    ```

    Use a single pull secret for `bootc`{.literal} and Podman by using a symlink to both locations to a common persistent file embedded in the container image, for example `/usr/lib/container-auth.json`{.literal}.

### [21.4. Injecting pull secrets for registries and disabling TLS](#injecting-pull-secrets-for-registries-and-disabling-tls) {#injecting-pull-secrets-for-registries-and-disabling-tls .title}

To make it possible for containerized environments to pull images from private or insecure registries, you can configure container images, pull secrets, and disable TLS for a registry within a system.

You can include container pull secrets and other configuration to access a registry inside the base image. However, when installing by using Anaconda, the installation environment might need a duplicate copy of \"bootstrap\" configuration to access the targeted registry when fetching over the network.

To perform arbitrary changes to the installation environment before the target bootc container image is fetched, you can use the Anaconda `%pre`{.literal} command.

**Prerequisites**

-   You are performing an installation by using Anaconda with a Kickstart file.
-   You have a valid registry authentication credential (pull secret) for the target private container registry, for example, `quay.io`{.literal}.
-   You have the address of the target container registry that hosts the `bootc`{.literal} image.

**Procedure**

1.  Configure a pull secret:

    ``` {.language-plaintext tabindex="-1"}
    %pre
    mkdir -p /etc/ostree
    cat > /etc/ostree/auth.json << 'EOF'
    {
            "auths": {
                    "quay.io": {
                            "auth": "<your secret here>"
                    }
            }
    }
    EOF
    %end
    ```

    With this configuration, the system pulls images from `quay.io`{.literal} by using the provided authentication credentials, which are stored in `/etc/ostree/auth.json`{.literal}.

2.  Disable TLS for an insecure registry:

    ``` {.language-plaintext tabindex="-1"}
    %pre
    mkdir -p /etc/containers/registries.conf.d/
    cat > /etc/containers/registries.conf.d/local-registry.conf << 'EOF'

    [[registry]]
    location="[IP_Address]:5000"
    insecure=true
    EOF
    %end
    ```

    With this configuration, the system pulls container images from a registry that is not secured with TLS. You can use it in development or internal networks.

    You can also use `%pre`{.literal} to:

    -   Fetch data from the network by using binaries included in the installation environment, such as `curl`{.literal}.

    -   Inject trusted certificate authorities into the installation environment `/etc/pki/ca-trust/source/anchors`{.literal} by using the `update-ca-trust`{.literal} command.

        You can configure insecure registries similarly by modifying the `/etc/containers`{.literal} directory. See the `containers-auth.json(5)`{.literal} for more detailed information about the format and configurations of the `auth.json`{.literal} file.

**Additional resources**

-   [Working with container registries](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/building_running_and_managing_containers/working-with-container-images)

### [21.5. Configuring container pull secrets](#configuring-container-pull-secrets) {#configuring-container-pull-secrets .title}

You can configure container pull secrets for an image that is already built. If you use an external installer such as Anaconda for bare metal or `bootc-image-builder`{.literal}, you must configure the systems by using any applicable pull secrets.

**Prerequisites**

-   The `container-tools`{.literal} meta-package is installed.
-   You have a valid registry pull secret file with authentication credentials for the target container registry.

**Procedure**

1.  Create a symbolic link between `bootc`{.literal} and Podman to use a single pull secret. By creating the symbolic link, you ensure that both locations are present to a common persistent file embedded in the container image.

    ``` {.language-plaintext tabindex="-1"}
    FROM quay.io/<namespace>/<image>:<tag>
    COPY containers-auth.conf /usr/lib/tmpfiles.d/link-podman-credentials.conf
    RUN --mount=type=secret,id=creds,required=true cp /run/secrets/creds /usr/lib/container-auth.json && \
      chmod 0600 /usr/lib/container-auth.json && \
      ln -sr /usr/lib/container-auth.json /etc/ostree/auth.json
    ```

    You can configure the container pull secrets to an image that is already built. If you use an external installer such as Anaconda for bare metal, or `bootc-image-builder`{.literal}, you must configure the systems with any applicable pull secrets.

2.  Create the `containers-auth.conf`{.literal} file.

    ``` {.language-plaintext tabindex="-1"}
    # Make /run/containers/0/auth.json (a transient runtime file)
    # a symlink to our /usr/lib/container-auth.json (a persistent file)
    # which is also symlinked from /etc/ostree/auth.json.
    d /run/containers/0 0755 root root -
    L /run/user/0/containers/auth.json - - - - ../../../../usr/lib/container-auth.json
    ```

3.  Build an image by using the `podman build`{.literal} command:

    ``` {.language-plaintext tabindex="-1"}
    $ podman build --secret id=creds,src=$HOME/.docker/config.json
    ```

    When you run the `Containerfile`{.literal}, the following actions happen:

    -   The `Containerfile`{.literal} makes `containers-auth.conf`{.literal} a transient runtime file.

    -   It creates a symbolic link to the `containers-auth.conf`{.literal} file.

    -   It also creates a persistent file, which is also symbolic linked from `/etc/ostree/auth.json`{.literal}.

        Podman does not have system-wide credentials. Podman accepts the `containers-auth`{.literal} locations that are underneath the following directories:

    -   `/run`{.literal}: The content of this directory vanishes on reboot, which is not required.

    -   `/root`{.literal}: Part of root home directory, which is local mutable state by default.

        To unify `bootc`{.literal} and Podman credentials, use a single default global pull secret for both `bootc`{.literal} and Podman. The following container build is an example to unify the `bootc`{.literal} and the Podman credentials. The example expects a secret named `creds`{.literal} to contain the registry pull secret to build.

**Additional resources**

-   [Injecting secrets in image mode for RHEL](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/index#injecting-secrets-to-a-image-mode-for-rhel_managing-users-groups-ssh-key-and-secrets-in-image-mode-for-rhel)

### [21.6. Authentication file locations for bootc updates](#authentication-file-locations-for-bootc-updates) {#authentication-file-locations-for-bootc-updates .title}

When `bootc`{.literal} fetches updates from a container registry that requires authentication, it reads credentials from specific file paths on the host system. These paths differ from the default locations that Podman uses, because some of the default Podman paths are not appropriate for system services.

The following table lists the supported authentication file locations for `bootc`{.literal} updates:

+---------------------------------------+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Path                                  | Persistence                   | Description                                                                                                                                                                                      |
+:======================================+:==============================+:=================================================================================================================================================================================================+
| `/etc/ostree/auth.json`{.literal}     | Persistent, machine-local     | Stored on the local filesystem and preserved across reboots. Use this location for long-lived credentials on a specific machine.                                                                 |
+---------------------------------------+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/run/ostree/auth.json`{.literal}     | Ephemeral, runtime            | Stored in the runtime filesystem and cleared on reboot. Use this location for short-lived or dynamically derived credentials, such as tokens fetched from a cloud metadata service at boot time. |
+---------------------------------------+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `/usr/lib/ostree/auth.json`{.literal} | Persistent, embedded in image | Included as part of the container image. Use this location for credentials that are common across all systems deployed from the same image. Changes require a new image build.                   |
+---------------------------------------+-------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: Table 21.1. Supported authentication file locations

Show more

Note

These paths differ from the default Podman authentication paths. Podman reads credentials from `$XDG_RUNTIME_DIR/containers/auth.json`{.literal} for rootless users and from `/run/containers/0/auth.json`{.literal} for the root user. The `bootc`{.literal} does not read from these locations by default.

For more information about the authentication file format, see the `containers-auth.json(5)`{.literal} man page on your system.

### [21.7. Bootstrap secret strategies for deployed bootc systems](#bootstrap-secret-strategies-for-deployed-bootc-systems) {#bootstrap-secret-strategies-for-deployed-bootc-systems .title}

You can supply initial registry credentials, or bootstrap secrets, to deployed bootc systems by using several strategies depending on your infrastructure. A bootstrap secret provides the minimum authentication needed for a system to fetch its first update and establish ongoing connectivity with a container registry or management service.

The following strategies are available for providing bootstrap secrets to deployed bootc systems:

Fetch secrets from cloud metadata services

:   Most production Infrastructure as a Service (IaaS) platforms expose a metadata server that can securely host bootstrap secrets. Include a tool such as `cloud-init`{.literal} or `ignition`{.literal} in your container image to fetch the secrets from the metadata endpoint on first boot. For example, on AWS, you can use `cloud-init`{.literal} to retrieve an ECR authentication token from the instance metadata and write it to `/run/ostree/auth.json`{.literal}.

    This approach keeps secrets out of the container image and supports per-instance credential isolation.

Embed secrets in disk images

:   When you generate a cloud disk image, such as an AMI or OpenStack Glance image, from an input container image by using `bootc-image-builder`{.literal}, you can inject bootstrap secrets into the disk image. These secrets are machine-local state and persist only in that specific disk image. Rotating the secrets requires either refreshing the disk image or deploying a management tool to update them in place.

    This approach is suitable for environments where secrets must be present before the first network connection.

Use a bootstrap-then-rotate pattern

:   Embed only minimal bootstrap secrets in the container image or disk image. After the system boots and connects to the registry, use a provisioning tool, whether it runs as a host service or a container, to authenticate to a management cluster and inject or rotate additional secrets, such as SSH keys, TLS certificates, and long-lived registry credentials.

    This pattern limits the exposure of long-lived credentials in shared artifacts and allows centralized secret management.

newdoc-version: 2.18.7 :\_template-generated: 2026-10-07 :\_mod-docs-content-type: PROCEDURE

### [21.8. Configuring credential helpers for bootc registry authentication](#configuring-credential-helpers-for-bootc-registry-authentication) {#configuring-credential-helpers-for-bootc-registry-authentication .title}

You can configure credential helpers to dynamically provide registry authentication tokens for `bootc`{.literal} updates instead of storing static credentials. This approach is useful when you use cloud-native registries, such as AWS Elastic Container Registry (ECR), that issue short-lived tokens.

**Prerequisites**

-   A deployed and booted bootc system.
-   The credential helper binary is installed and accessible in the system `PATH`{.literal}. For example, the `ecr-login`{.literal} binary for AWS ECR.
-   The `/etc/containers/registries.conf`{.literal} file or a drop-in file in `/etc/containers/registries.conf.d/`{.literal} is configured for the target registry.

**Procedure**

1.  Configure the credential helper in the container registry configuration. Create or edit a drop-in configuration file:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo cat > /etc/containers/registries.conf.d/<registry_name>.conf << 'EOF'
    [registry]
    location = "<registry_url>"
    credential-helpers = ["<helper_name>"]
    EOF
    ```

    where:

    \<registry_name\>
    :   Specifies a descriptive name for the configuration file, for example, `ecr`{.literal}.

    \<registry_url\>
    :   Specifies the URL of the container registry, for example, `123456789012.dkr.ecr.us-east-1.amazonaws.com`{.literal}.

    \<helper_name\>
    :   Specifies the name of the credential helper, for example, `ecr-login`{.literal}.

2.  Write a no-op authentication file to the `bootc`{.literal} pull secret location. When you use credential helpers, `bootc`{.literal} still requires an authentication file to be present, but the file must contain only an empty JSON object:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo echo '{}' > /etc/ostree/auth.json
    $ sudo chmod 0600 /etc/ostree/auth.json
    ```

    Important

    Do not omit this step. Without a valid authentication file in the pull secret location, `bootc`{.literal} does not invoke the credential helper and fails to authenticate. The file must contain `{}`{.literal} (an empty JSON object), not be an empty file.

**Verification**

-   Verify that `bootc`{.literal} can access the registry by checking for available updates:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo bootc upgrade --check
    ```

### [21.9. Perform an explicit registry login on a deployed bootc system](#perform-an-explicit-registry-login-on-a-deployed-bootc-system) {#perform-an-explicit-registry-login-on-a-deployed-bootc-system .title}

After deploying a bootc system, you can configure registry authentication so that `bootc`{.literal} can pull container image updates from authenticated registries. Use the `podman login`{.literal} command with the `--authfile`{.literal} option to write credentials to a `bootc`{.literal}-compatible location.

**Prerequisites**

-   A deployed and booted bootc system.
-   Network connectivity to the target container registry.
-   The `container-tools`{.literal} meta-package is installed.
-   You have valid credentials (user name and password or token) for the target registry.

**Procedure**

1.  Log in to the target registry and write the credentials to the persistent `bootc`{.literal} authentication file:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman login --authfile /etc/ostree/auth.json <registry_url>
    ```

    where:

    \<registry_url\>

    :   Specifies the URL of the container registry, for example, `quay.io`{.literal}.

        Enter your user name and password when prompted.

        Alternatively, to pass the password non-interactively, use the `--password-stdin`{.literal} option:

        ``` {.language-plaintext tabindex="-1"}
        $ echo <password> | sudo podman login --authfile /etc/ostree/auth.json -u <user_name> --password-stdin <registry_url>
        ```

        where:

    \<password\>
    :   Specifies your registry password or access token.

    \<user_name\>
    :   Specifies your registry user name.

    \<registry_url\>
    :   Specifies the URL of the container registry.

2.  Optional: If you require ephemeral credentials that do not persist across reboots, write the credentials to the runtime authentication file instead:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo podman login --authfile /run/ostree/auth.json <registry_url>
    ```

    This is useful when the credentials are short-lived or derived dynamically from an external source at boot time, such as an AWS ECR token.

**Verification**

-   Verify that `bootc`{.literal} can access the registry by checking for available updates:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo bootc upgrade --check
    ```

### [21.10. Synchronize bootc and Podman registry credentials](#synchronize-bootc-and-podman-registry-credentials) {#synchronize-bootc-and-podman-registry-credentials .title}

By default, `bootc`{.literal} and Podman read registry credentials from different file paths. To keep both tools in sync, create symbolic links or `systemd`{.literal} `tmpfiles.d`{.literal} fragments so that a single `podman login`{.literal} command provides credentials for both container operations and host operating system updates.

**Prerequisites**

-   A deployed and booted bootc system.
-   The `container-tools`{.literal} meta-package is installed.

**Procedure**

1.  Create a `systemd`{.literal} `tmpfiles.d`{.literal} configuration file to establish the symbolic links at boot time:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo cat > /etc/tmpfiles.d/bootc-podman-auth.conf << 'EOF'
    d /run/containers/0 0755 root root -
    L /run/containers/0/auth.json - - - - /etc/ostree/auth.json
    EOF
    ```

    This configuration creates the `/run/containers/0/`{.literal} directory and a symbolic link from the Podman root-user credential path to the persistent `bootc`{.literal} authentication file at `/etc/ostree/auth.json`{.literal}.

2.  Apply the `tmpfiles.d`{.literal} configuration without rebooting:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo systemd-tmpfiles --create /etc/tmpfiles.d/bootc-podman-auth.conf
    ```

3.  Optional: If an automation process runs `podman login`{.literal} and writes to the ephemeral Podman path at `/run/user/0/containers/auth.json`{.literal}, link that location to the `bootc`{.literal} runtime path instead:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo ln -sf /run/user/0/containers/auth.json /run/ostree/auth.json
    ```

    This is useful when credentials are refreshed dynamically, such as by a `systemd`{.literal} timer that runs `podman login`{.literal} with rotating tokens.

**Verification**

1.  Verify that the symbolic link exists:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo ls -l /run/containers/0/auth.json
    ```

    The output shows a symbolic link pointing to `/etc/ostree/auth.json`{.literal}.

2.  Verify that both `bootc`{.literal} and Podman can authenticate to the registry:

    ``` {.language-plaintext tabindex="-1"}
    $ sudo bootc upgrade --check
    $ podman pull <registry_url>/<namespace>/<image>:<tag>
    ```

Note

To embed this credential synchronization directly into your container image so that it applies to all systems deployed from the image, add the `tmpfiles.d`{.literal} configuration file to the image during the container build. Place the file at `/usr/lib/tmpfiles.d/bootc-podman-auth.conf`{.literal}.

For more information, see `containers-auth.json(5)`{.literal} and `tmpfiles.d(5)`{.literal} man pages on your system.

## [Chapter 22. System configuration](#system-configuration) {#chapter-22.-system-configuration .title}

Image mode for RHEL uses a container-native approach to build, deploy, and manage the operating system as immutable container layers, based on the `registry.redhat.io/rhel10/rhel-bootc`{.literal} image.

### [22.1. Transient runtime reconfiguration](#transient-runtime-reconfiguration) {#transient-runtime-reconfiguration .title}

Transient runtime reconfiguration in Red Hat Enterprise Linux Image Mode involves making temporary adjustments to a live system. You can safely test configurations and troubleshoot issues before permanently embedding those changes into your immutable container image.

You can perform a dynamic reconfiguration in the base image configuration. For example, you can run the `firewall-cmd --permanent`{.literal} command to achieve persistent changes across a reboot.

Warning

The `/etc`{.literal} directory is persistent by default. If you make changes by using the tools, for example `firewall-cmd --permanent`{.literal}, the contents of the `/etc`{.literal} on the system can differ from the one described in the container image.

In the default configuration, first make the changes in the base image. Then, queue the changes without restarting running systems. Finally, simultaneously write to apply the changes to existing systems only in memory.

You can configure the `/etc`{.literal} directory to be transient by using bind mounts. In this case, the `etc`{.literal} directory is a part of the machine's local root filesystem. For example, if you inject static IP addresses by using Anaconda Kickstart, they persist across upgrades.

The system applies a three-way merge across upgrades, and each deployment keeps its own copy of /etc.

The `/run`{.literal} directory
:   The `/run`{.literal} directory is an API filesystem that is defined to be deleted when the system is restarted. Use the `/run`{.literal} directory for transient files.

Dynamic reconfiguration models
:   In the Pull model, you can include code directly embedded in your base image or a privileged container. This code contacts the remote network server for configuration, and subsequently launch additional container images, by using the Podman API.

In the Push model, some workloads are implemented by tools such as Ansible.

systemd
:   You can use systemd units for dynamic transient reconfiguration by writing to `/run/systemd`{.literal} directory. For example, the `systemctl edit --runtime myservice.service`{.literal} dynamically changes the configuration of the `myservice.service`{.literal} unit, without persisting the changes.

NetworkManager
:   Use a `/run/NetworkManager/conf.d`{.literal} directory for applying temporary network configuration. Use the `nmcli connection modify --temporary`{.literal} command to write changes only in memory. Without the `--temporary`{.literal} option, the command writes persistent changes.

Podman
:   Use the `podman run --rm`{.literal} command to automatically remove the container when it exits. Without the `--rm`{.literal} option, the `podman run`{.literal} command creates a container that persists across system reboots.

### [22.2. Using DNF with image mode for RHEL](#using-dnf-with-image-mode-for-RHEL) {#using-dnf-with-image-mode-for-rhel .title}

Use the DNF tool within your Containerfile to manage software packages for Red Hat Enterprise Linux bootc images. This ensures that all dependencies are resolved at build time, resulting in a predictable and immutable deployment.

The `rhel10/rhel-bootc`{.literal} container image includes the `dnf`{.literal} package manager. You can use dnf for several use cases:

Using `dnf`{.literal} as a part of a container build
:   You can use the `RUN dnf install`{.literal} directive in the Containerfile.

Using `dnf`{.literal} at runtime

:   

Warning

The functionality depends on the `dnf`{.literal} version. You might get an error: `error: can’t create transaction lock on /usr/share/rpm/.rpm.lock (Read-only file system)`{.literal}.

You can use the `bootc-usr-overlay`{.literal} command to create a writable overlay filesystem for `/usr`{.literal} directory. The `dnf install`{.literal} writes to this overlay and you can use it for installing debugging tools. Note that changes are lost on reboot.

Configuring storage

:   The supported storage technologies are the following:

    -   `xfs`{.literal}/`ext4`{.literal}
    -   Logical volume management (LVM)
    -   Linux Unified Key Setup (LUKS)

You can add other storage packages to the host system.

-   **Storage with `bootc-image-builder`{.literal}** You can use the bootc-image-builder tool to create a disk image. The available configuration for partitioning and layout is relatively fixed. The default filesystem type is derived from the container image's bootc install configuration.
-   **Storage with bootc install** You can use the `bootc install to-disk`{.literal} command for flat storage configurations and `bootc install to-filesystem`{.literal} command for more advanced installations. For more information see [Advanced installation with to-filesystem and to-disk](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/using_image_mode_for_rhel_to_build_deploy_and_manage_operating_systems/deploying-the-rhel-bootc-images#advanced-installation-with-to-filesystem).

### [22.3. Network configuration](#network-configuration) {#network-configuration .title}

The default images include the `NetworkManager`{.literal} dynamic network control and configuration system; bootc attempts to connect using DHCP on every plugged-in interface. You can apply a temporary network configuration, by configuring the `/run/NetworkManager/conf.d`{.literal} directory.

However, if you need to use static addressing or more complex networking such as VLANs, bonds, bridges, teams, among others, you can use different ways. Regardless of the way you choose to configure networking, it results as a configuration for NetworkManager, which takes the form of `NetworkManager`{.literal} keyfiles.

Host Network Configuration options
:   Complex networking configuration often also requires per-machine state. You can generate machine-specific container images that have, for example, static IP addressing included. You can also include code to generate network configuration from inside the image by inspecting the MAC address of the host.

Network configuration options available

:   The following are the available options for configuring static IP, and how the configuration can be done:

    -   By using a Containerfile: Create a container image with static IP or include code to generate network configuration from inside the image based on MAC address.

        -   Use the configuration specified in [Device List Format](https://networkmanager.dev/docs/api/1.32.10/NetworkManager.conf.html#device-spec) to match the MAC address or other addresses.

        -   To configure a network, you can use the `nmcli connection add`{.literal} similarly to what you do to a booted system. However, during build time, you must use the command combined with an explicit `--offline`{.literal} argument. See [Configuring an Ethernet connection by using nmcli](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/configuring_and_managing_networking/configuring-an-ethernet-connection#configuring-an-ethernet-connection-by-using-nmcli) for more details.

        -   Add the following command before the `nmcli`{.literal} command in the ContainerFile:

            ``` {.language-plaintext tabindex="-1"}
            RUN nmcli --offline connection add
            ```

    -   By using Anaconda: You can use an Anaconda Kickstart to configure networking, including Wi-Fi, for bare-metal installations. The configuration is stored by default in the `/etc/NetworkManager/system-connections/`{.literal} file, and is inherently per-machine state.

    -   By using kernel arguments: Add kernel parameters on first boot to define networking configuration. The kernel arguments are mostly defined in the `dracut.cmdline`{.literal} man page. You can apply these kernel arguments on first boot by using different methods. When using `bootc install`{.literal}, you can also set per-machine kernel arguments by using `--karg`{.literal}.

    -   By using NetworkManager key files: `nmcli`{.literal} or `nm-initrd-generator`{.literal}

Generating NetworkManager keyfiles by using `nmcli`{.literal}

:   The `nmcli`{.literal} NetworkManager command line tool provides an offline mode that does not communicate with the NetworkManager daemon and just writes the keyfile content to standard output.

    -   Run the `nmcli`{.literal} tool for each connection profile you want to create:

        ``` {.language-plaintext tabindex="-1"}
        $ nmcli --offline connection add \
                type ethernet ifname enp1s0 \
                ipv4.method manual ipv4.addresses 192.0.0.1/24 \
                ipv6.method disabled

        [connection]
        id=ethernet-enp1s0
        uuid=ff242096-f803-425f-9a77-4c3ec92686bd
        type=ethernet
        interface-name=enp1s0

        [ethernet]

        [ipv4]
        address1=192.0.0.1/24
        method=manual

        [ipv6]
        addr-gen-mode=default
        method=disabled
        [proxy]
        ```

See the settings man page for a list of the properties that can be specified by using `nmcli`{.literal}. Bash autocompletion is available.

Generating NetworkManager Keyfiles by `using nm-initrd-generator`{.literal}

:   NetworkManager contains the `nm-initrd-generator`{.literal} tool, that can generate keyfiles from `dracut`{.literal} kernel argument syntax. You can use the tool to either convert from kernel arguments to keyfiles or to just quickly generate some keyfiles giving a small amount of input and then modify some more detailed settings.

    -   Generate keyfiles for a bond by using `nm-initrd-generator`{.literal}:

        ``` {.language-plaintext tabindex="-1"}
        $ sudo podman run --rm -ti quay.io/<namespace>/<image>:<tag> /usr/libexec/nm-initrd-generator -s -- "ip=bond0:dhcp" "bond=bond0:ens2,ens3:mode=active-backup,miimon=100" "nameserver=8.8.8.8"

        * Connection 'bond0' *

        [connection]
        id=bond0
        uuid=643c17b5-b364-4137-b273-33f450a45476
        type=bond
        interface-name=bond0
        multi-connect=1
        permissions=

        [ethernet]
        mac-address-blacklist=

        [bond]
        miimon=100
        mode=active-backup

        [ipv4]
        dns=8.8.8.8;
        dns-search=
        may-fail=false
        method=auto

        [ipv6]
        addr-gen-mode=eui64
        dns-search=
        method=auto

        [proxy]

        * Connection 'ens3' *

        [connection]
        id=ens3
        uuid=b42cc917-fd87-47df-9ac2-34622ecddd8c
        type=ethernet
        interface-name=ens3
        master=643c17b5-b364-4137-b273-33f450a45476
        multi-connect=1
        permissions=
        slave-type=bond

        [ethernet]
        mac-address-blacklist=

        * Connection 'ens2' *

        [connection]
        id=ens2
        uuid=e111bb4e-3ee3-4612-afc2-1d2dfff97671
        type=ethernet
        interface-name=ens2
        master=643c17b5-b364-4137-b273-33f450a45476
        multi-connect=1
        permissions=
        slave-type=bond

        [ethernet]
        mac-address-blacklist=
        ```

The command generates three keyfiles for each interface: `bond0`{.literal}, `ens3`{.literal}, and `ens2`{.literal}. You can use the generated output, add more settings or modify existing settings, and then commit the files into a container image.

Configuring a static IP

:   -   You can use the following `dracut`{.literal} kernel arguments:

    Template:

``` {.language-plaintext tabindex="-1"}
ip=${ip}::${gateway}:${netmask}:${hostname}:${interface}:none:${nameserver}
```

Example:

``` {.language-plaintext tabindex="-1"}
ip=10.10.10.10::10.10.10.1:255.255.255.0:myhostname:ens2:none:8.8.8.8
```

Writing configuration embedded in container images
:   Store the NetworkManager configuration embedded in container images in `/usr/lib/NetworkManager/system-connections/`{.literal} because this form is part of the immutable image state. You can also write configuration to `/etc/NetworkManager/system-connections/`{.literal} as part of the container image. The default OSTree 3-way merge, that is, using the old default configuration, the active `/etc`{.literal} system, and the new default configuration, applies with any machine-specific configuration.

The keyfiles must have the `600`{.literal} root-only access permissions, otherwise `NetworkManager`{.literal} ignores them.

Disabling automatic configuration of Ethernet devices

:   By default, `NetworkManager`{.literal} attempts to autoconfigure by using the DHCP or SLAAC addresses on every interface with a cable plugged in. In some network environments this might not be desirable. For that, it is possible to change the NetworkManager behavior by adding a configuration file, such as `/usr/lib/NetworkManager/conf.d/noauto.conf`{.literal}.

    -   Disable the `NetworkManager`{.literal} autoconfiguration of Ethernet devices

        ``` {.language-plaintext tabindex="-1"}
        [main]
        # Do not do automatic (DHCP or SLAAC) configuration on ethernet devices
        # with no other matching connections.
        no-auto-default=*
        ```

### [22.4. Setting a hostname in image mode for RHEL](#setting-a-hostname) {#setting-a-hostname-in-image-mode-for-rhel .title}

You can set a custom hostname for your image mode for RHEL system by modifying the `/etc/hostname`{.literal} file. Setting a hostname identifies the system on the network and simplifies management in multi-host environments.

**Prerequisites**

-   You have a base `bootc`{.literal} container image to extend, for example, `registry.redhat.io/rhel10/rhel-bootc:latest`{.literal}.
-   The `container-tools`{.literal} meta-package is installed if you are building or running containers locally.

**Procedure**

-   Set the hostname by choosing one of the following methods:

    At build time in a `Containerfile`{.literal}

    :   1.  Add the following instruction to your `Containerfile`{.literal} to embed the hostname in the image:

        ``` {.language-shell-session tabindex="-1"}
        FROM registry.redhat.io/rhel10/rhel-bootc:latest

        RUN echo "<hostname>" > /etc/hostname
        ```

        Replace `myhostname`{.literal} with the required hostname for the system.

    By using Anaconda with a Kickstart file

    :   1.  Add the following directive to your Kickstart file to set the hostname during installation:

        ``` {.language-shell-session tabindex="-1"}
        network --hostname=<hostname>
        ```

        Replace `myhostname`{.literal} with the required hostname for the system.

    At runtime with a privileged container or on the booted system

    :   1.  On the running system, write the required hostname to the `/etc/hostname`{.literal} file:

        ``` {.language-shell-session tabindex="-1"}
        # echo "<hostname>" > /etc/hostname
        ```

        Replace `myhostname`{.literal} with the required hostname for the system.

        Note

        Because `/etc`{.literal} is persistent and mutable by default in image mode for RHEL, changes to `/etc/hostname`{.literal} on a running system persist across reboots. However, if `/etc`{.literal} is configured as transient, the hostname reverts on reboot.

**Verification**

1.  Change the hostname:

    ``` {.language-shell-session tabindex="-1"}
    # hostnamectl set-hostname <hostname>
    ```

2.  Reboot the system:

    ``` {.language-plaintext tabindex="-1"}
    # reboot
    ```

3.  Verify the hostname by running the following command:

    ``` {.language-shell-session tabindex="-1"}
    $ hostnamectl
    ```

    The output displays the configured hostname under `Static hostname`{.literal}.

### [22.5. Configuring proxied internet access in image Mode for RHEL](#configuring-proxied-internet-access-in-image-mode-for-RHEL) {#configuring-proxied-internet-access-in-image-mode-for-rhel .title}

If you are deploying to an environment that requires internet access by using a proxy, you need to configure services to access resources as intended.

**Procedure**

-   Defining common proxy environment variables. This common file has to be subsequently referenced explicitly by each service that requires internet access.

    ``` {.language-plaintext tabindex="-1"}
    # /etc/example-proxy.env
    https_proxy="http://example.com:8080"
    all_proxy="http://example.com:8080"
    http_proxy="http://example.com:8080"
    HTTP_PROXY="http://example.com:8080"
    HTTPS_PROXY="http://example.com:8080"
    no_proxy="*.example.com,127.0.0.1,0.0.0.0,localhost"
    ```

-   Defining drop-in units for core services. The `bootc`{.literal} and `podman`{.literal} tools commonly need proxy configuration and the `bootc`{.literal} does not always run as a `systemd`{.literal} unit.

    ``` {.language-plaintext tabindex="-1"}
    # /usr/lib/systemd/system/bootc-fetch-apply-updates.service.d/99-proxy.conf
    [Service]
    EnvironmentFile=/etc/example-proxy.env
    ```

-   Defining proxy use for Podman `systemd`{.literal} units

    You can set the configuration for proxy and environment settings of `podman`{.literal} and containers in the `/etc/containers/containers.conf`{.literal} configuration file as a root user or in the `$HOME/.config/containers/containers.conf`{.literal} configuration file as a non-root user.

## [Chapter 23. Getting the source code of bootc container images](#getting-the-source-code-of-container-images) {#chapter-23.-getting-the-source-code-of-bootc-container-images .title}

Retrieve the source code for your Red Hat Enterprise Linux container images to fulfill open source license obligations. With the source packages, you can audit the software, verify its provenance, or rebuild components for debugging purposes.

You can find the source code for bootc images in the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/search).

To access the source code of bootc container images:

1.  Access the [Red Hat Ecosystem Catalog](https://catalog.redhat.com/search) and search for `rhel-bootc`{.literal}.

2.  In the **Get this image** tab, click **Get the source** and follow the instructions.

3.  After you extract the content, the input RPM package list and other content resources are available in the `extra_src_dir`{.literal} directory.

    The `.tar`{.literal} files are snapshots of the input git repository, and contain YAML files with the package lists.

## [Chapter 24. Contributing to the bootc upstream projects](#contributing-to-the-upstream-projects) {#chapter-24.-contributing-to-the-bootc-upstream-projects .title}

Contribute to the upstream open source projects associated with Image Mode for Red Hat Enterprise Linux to collaborate on tool development. Participating in these communities helps you to report issues, submit code fixes, and propose enhancements directly to the project maintainers.

You can contribute to the following upstream bootc projects:

-   The upstream git repository is in [CentOS Stream](https://gitlab.com/redhat/centos-stream/containers/bootc)
-   The CentOS Stream sources in the [Fedora upstream project](https://docs.fedoraproject.org/en-US/bootc)

## [Legal Notice](#idm140335710530848) {#legal-notice .legalnotice}

Copyright © Red Hat.

Except as otherwise noted below, the text of and illustrations in this documentation are licensed by Red Hat under the Creative Commons Attribution--Share Alike 3.0 Unported license . If you distribute this document or an adaptation of it, you must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce, and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent permitted by applicable law.

Red Hat, the Red Hat logo, JBoss, Hibernate, and RHCE are trademarks or registered trademarks of Red Hat, LLC. or its subsidiaries in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

XFS is a trademark or registered trademark of Hewlett Packard Enterprise Development LP or its subsidiaries in the United States and other countries.

The OpenStack® Word Mark and OpenStack logo are trademarks or registered trademarks of the Linux Foundation, used under license.

All other trademarks are the property of their respective owners.
