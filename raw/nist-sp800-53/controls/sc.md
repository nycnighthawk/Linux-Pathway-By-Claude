# SC — System and Communications Protection

## SC-01 Policy and Procedures {#sc-1}

**Statement.** - a. Develop, document, and disseminate to [organization-defined personnel or roles]:
  - 1. [organization-defined value] system and communications protection policy that:
    - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
    - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
  - 2. Procedures to facilitate the implementation of the system and communications protection policy and the associated system and communications protection controls;
- b. Designate an [official] to manage the development, documentation, and dissemination of the system and communications protection policy and procedures; and
- c. Review and update the current system and communications protection:
  - 1. Policy [frequency] and following [events] ; and
  - 2. Procedures [frequency] and following [events].

**Guidance.** System and communications protection policy and procedures address the controls in the SC family that are implemented within systems and organizations. The risk management strategy is an important factor in establishing such policies and procedures. Policies and procedures contribute to security and privacy assurance. Therefore, it is important that security and privacy programs collaborate on the development of system and communications protection policy and procedures. Security and privacy program policies and procedures at the organization level are preferable, in general, and may obviate the need for mission- or system-specific policies and procedures. The policy can be included as part of the general security and privacy policy or be represented by multiple policies that reflect the complex nature of organizations. Procedures can be established for security and privacy programs, for mission or business processes, and for systems, if needed. Procedures describe how the policies or controls are implemented and can be directed at the individual or role that is the object of the procedure. Procedures can be documented in system security and privacy plans or in one or more separate documents. Events that may precipitate an update to system and communications protection policy and procedures include assessment or audit findings, security incidents or breaches, or changes in applicable laws, executive orders, directives, regulations, policies, standards, and guidelines. Simply restating controls does not constitute an organizational policy or procedure.

## SC-02 Separation of System and User Functionality {#sc-2}

**Statement.** Separate user functionality, including user interface services, from system management functionality.

**Guidance.** System management functionality includes functions that are necessary to administer databases, network components, workstations, or servers. These functions typically require privileged user access. The separation of user functions from system management functions is physical or logical. Organizations may separate system management functions from user functions by using different computers, instances of operating systems, central processing units, or network addresses; by employing virtualization techniques; or some combination of these or other methods. Separation of system management functions from user functions includes web administrative interfaces that employ separate authentication methods for users of any other system resources. Separation of system and user functions may include isolating administrative interfaces on different domains and with additional access controls. The separation of system and user functionality can be achieved by applying the systems security engineering design principles in [SA-8](#sa-8) , including [SA-8(1)](#sa-8.1), [SA-8(3)](#sa-8.3), [SA-8(4)](#sa-8.4), [SA-8(10)](#sa-8.10), [SA-8(12)](#sa-8.12), [SA-8(13)](#sa-8.13), [SA-8(14)](#sa-8.14) , and [SA-8(18)](#sa-8.18).

### SC-02(01) Interfaces for Non-privileged Users {#sc-2.1}

**Statement.** Prevent the presentation of system management functionality at interfaces to non-privileged users.

**Guidance.** Preventing the presentation of system management functionality at interfaces to non-privileged users ensures that system administration options, including administrator privileges, are not available to the general user population. Restricting user access also prohibits the use of the grey-out option commonly used to eliminate accessibility to such information. One potential solution is to withhold system administration options until users establish sessions with administrator privileges.

### SC-02(02) Disassociability {#sc-2.2}

**Statement.** Store state information from applications and software separately.

**Guidance.** If a system is compromised, storing applications and software separately from state information about users’ interactions with an application may better protect individuals’ privacy.

## SC-03 Security Function Isolation {#sc-3}

**Statement.** Isolate security functions from nonsecurity functions.

**Guidance.** Security functions are isolated from nonsecurity functions by means of an isolation boundary implemented within a system via partitions and domains. The isolation boundary controls access to and protects the integrity of the hardware, software, and firmware that perform system security functions. Systems implement code separation in many ways, such as through the provision of security kernels via processor rings or processor modes. For non-kernel code, security function isolation is often achieved through file system protections that protect the code on disk and address space protections that protect executing code. Systems can restrict access to security functions using access control mechanisms and by implementing least privilege capabilities. While the ideal is for all code within the defined security function isolation boundary to only contain security-relevant code, it is sometimes necessary to include nonsecurity functions as an exception. The isolation of security functions from nonsecurity functions can be achieved by applying the systems security engineering design principles in [SA-8](#sa-8) , including [SA-8(1)](#sa-8.1), [SA-8(3)](#sa-8.3), [SA-8(4)](#sa-8.4), [SA-8(10)](#sa-8.10), [SA-8(12)](#sa-8.12), [SA-8(13)](#sa-8.13), [SA-8(14)](#sa-8.14) , and [SA-8(18)](#sa-8.18).

### SC-03(01) Hardware Separation {#sc-3.1}

**Statement.** Employ hardware separation mechanisms to implement security function isolation.

**Guidance.** Hardware separation mechanisms include hardware ring architectures that are implemented within microprocessors and hardware-enforced address segmentation used to support logically distinct storage objects with separate attributes (i.e., readable, writeable).

### SC-03(02) Access and Flow Control Functions {#sc-3.2}

**Statement.** Isolate security functions enforcing access and information flow control from nonsecurity functions and from other security functions.

**Guidance.** Security function isolation occurs because of implementation. The functions can still be scanned and monitored. Security functions that are potentially isolated from access and flow control enforcement functions include auditing, intrusion detection, and malicious code protection functions.

### SC-03(03) Minimize Nonsecurity Functionality {#sc-3.3}

**Statement.** Minimize the number of nonsecurity functions included within the isolation boundary containing security functions.

**Guidance.** Where it is not feasible to achieve strict isolation of nonsecurity functions from security functions, it is necessary to take actions to minimize nonsecurity-relevant functions within the security function boundary. Nonsecurity functions contained within the isolation boundary are considered security-relevant because errors or malicious code in the software can directly impact the security functions of systems. The fundamental design objective is that the specific portions of systems that provide information security are of minimal size and complexity. Minimizing the number of nonsecurity functions in the security-relevant system components allows designers and implementers to focus only on those functions which are necessary to provide the desired security capability (typically access enforcement). By minimizing the nonsecurity functions within the isolation boundaries, the amount of code that is trusted to enforce security policies is significantly reduced, thus contributing to understandability.

### SC-03(04) Module Coupling and Cohesiveness {#sc-3.4}

**Statement.** Implement security functions as largely independent modules that maximize internal cohesiveness within modules and minimize coupling between modules.

**Guidance.** The reduction of inter-module interactions helps to constrain security functions and manage complexity. The concepts of coupling and cohesion are important with respect to modularity in software design. Coupling refers to the dependencies that one module has on other modules. Cohesion refers to the relationship between functions within a module. Best practices in software engineering and systems security engineering rely on layering, minimization, and modular decomposition to reduce and manage complexity. This produces software modules that are highly cohesive and loosely coupled.

### SC-03(05) Layered Structures {#sc-3.5}

**Statement.** Implement security functions as a layered structure minimizing interactions between layers of the design and avoiding any dependence by lower layers on the functionality or correctness of higher layers.

**Guidance.** The implementation of layered structures with minimized interactions among security functions and non-looping layers (i.e., lower-layer functions do not depend on higher-layer functions) enables the isolation of security functions and the management of complexity.

## SC-04 Information in Shared System Resources {#sc-4}

**Statement.** Prevent unauthorized and unintended information transfer via shared system resources.

**Guidance.** Preventing unauthorized and unintended information transfer via shared system resources stops information produced by the actions of prior users or roles (or the actions of processes acting on behalf of prior users or roles) from being available to current users or roles (or current processes acting on behalf of current users or roles) that obtain access to shared system resources after those resources have been released back to the system. Information in shared system resources also applies to encrypted representations of information. In other contexts, control of information in shared system resources is referred to as object reuse and residual information protection. Information in shared system resources does not address information remanence, which refers to the residual representation of data that has been nominally deleted; covert channels (including storage and timing channels), where shared system resources are manipulated to violate information flow restrictions; or components within systems for which there are only single users or roles.

### SC-04(01) Security Levels (withdrawn) {#sc-4.1}

### SC-04(02) Multilevel or Periods Processing {#sc-4.2}

**Statement.** Prevent unauthorized information transfer via shared resources in accordance with [procedures] when system processing explicitly switches between different information classification levels or security categories.

**Guidance.** Changes in processing levels can occur during multilevel or periods processing with information at different classification levels or security categories. It can also occur during serial reuse of hardware components at different classification levels. Organization-defined procedures can include approved sanitization processes for electronically stored information.

## SC-05 Denial-of-service Protection {#sc-5}

**Statement.** - a. [organization-defined value] the effects of the following types of denial-of-service events: [types of denial-of-service events] ; and
- b. Employ the following controls to achieve the denial-of-service objective: [controls by type of denial-of-service event].

**Guidance.** Denial-of-service events may occur due to a variety of internal and external causes, such as an attack by an adversary or a lack of planning to support organizational needs with respect to capacity and bandwidth. Such attacks can occur across a wide range of network protocols (e.g., IPv4, IPv6). A variety of technologies are available to limit or eliminate the origination and effects of denial-of-service events. For example, boundary protection devices can filter certain types of packets to protect system components on internal networks from being directly affected by or the source of denial-of-service attacks. Employing increased network capacity and bandwidth combined with service redundancy also reduces the susceptibility to denial-of-service events.

### SC-05(01) Restrict Ability to Attack Other Systems {#sc-5.1}

**Statement.** Restrict the ability of individuals to launch the following denial-of-service attacks against other systems: [denial-of-service attacks].

**Guidance.** Restricting the ability of individuals to launch denial-of-service attacks requires the mechanisms commonly used for such attacks to be unavailable. Individuals of concern include hostile insiders or external adversaries who have breached or compromised the system and are using it to launch a denial-of-service attack. Organizations can restrict the ability of individuals to connect and transmit arbitrary information on the transport medium (i.e., wired networks, wireless networks, spoofed Internet protocol packets). Organizations can also limit the ability of individuals to use excessive system resources. Protection against individuals having the ability to launch denial-of-service attacks may be implemented on specific systems or boundary devices that prohibit egress to potential target systems.

### SC-05(02) Capacity, Bandwidth, and Redundancy {#sc-5.2}

**Statement.** Manage capacity, bandwidth, or other redundancy to limit the effects of information flooding denial-of-service attacks.

**Guidance.** Managing capacity ensures that sufficient capacity is available to counter flooding attacks. Managing capacity includes establishing selected usage priorities, quotas, partitioning, or load balancing.

### SC-05(03) Detection and Monitoring {#sc-5.3}

**Statement.** - (a) Employ the following monitoring tools to detect indicators of denial-of-service attacks against, or launched from, the system: [monitoring tools] ; and
- (b) Monitor the following system resources to determine if sufficient resources exist to prevent effective denial-of-service attacks: [system resources].

**Guidance.** Organizations consider the utilization and capacity of system resources when managing risk associated with a denial of service due to malicious attacks. Denial-of-service attacks can originate from external or internal sources. System resources that are sensitive to denial of service include physical disk storage, memory, and CPU cycles. Techniques used to prevent denial-of-service attacks related to storage utilization and capacity include instituting disk quotas, configuring systems to automatically alert administrators when specific storage capacity thresholds are reached, using file compression technologies to maximize available storage space, and imposing separate partitions for system and user data.

## SC-06 Resource Availability {#sc-6}

**Statement.** Protect the availability of resources by allocating [resources] by [organization-defined value].

**Guidance.** Priority protection prevents lower-priority processes from delaying or interfering with the system that services higher-priority processes. Quotas prevent users or processes from obtaining more than predetermined amounts of resources.

## SC-07 Boundary Protection {#sc-7}

**Statement.** - a. Monitor and control communications at the external managed interfaces to the system and at key internal managed interfaces within the system;
- b. Implement subnetworks for publicly accessible system components that are [organization-defined value] separated from internal organizational networks; and
- c. Connect to external networks or systems only through managed interfaces consisting of boundary protection devices arranged in accordance with an organizational security and privacy architecture.

**Guidance.** Managed interfaces include gateways, routers, firewalls, guards, network-based malicious code analysis, virtualization systems, or encrypted tunnels implemented within a security architecture. Subnetworks that are physically or logically separated from internal networks are referred to as demilitarized zones or DMZs. Restricting or prohibiting interfaces within organizational systems includes restricting external web traffic to designated web servers within managed interfaces, prohibiting external traffic that appears to be spoofing internal addresses, and prohibiting internal traffic that appears to be spoofing external addresses. [SP 800-189](#f5edfe51-d1f2-422e-9b27-5d0e90b49c72) provides additional information on source address validation techniques to prevent ingress and egress of traffic with spoofed addresses. Commercial telecommunications services are provided by network components and consolidated management systems shared by customers. These services may also include third party-provided access lines and other service elements. Such services may represent sources of increased risk despite contract security provisions. Boundary protection may be implemented as a common control for all or part of an organizational network such that the boundary to be protected is greater than a system-specific boundary (i.e., an authorization boundary).

### SC-07(01) Physically Separated Subnetworks (withdrawn) {#sc-7.1}

### SC-07(02) Public Access (withdrawn) {#sc-7.2}

### SC-07(03) Access Points {#sc-7.3}

**Statement.** Limit the number of external network connections to the system.

**Guidance.** Limiting the number of external network connections facilitates monitoring of inbound and outbound communications traffic. The Trusted Internet Connection [DHS TIC](#4f42ee6e-86cc-403b-a51f-76c2b4f81b54) initiative is an example of a federal guideline that requires limits on the number of external network connections. Limiting the number of external network connections to the system is important during transition periods from older to newer technologies (e.g., transitioning from IPv4 to IPv6 network protocols). Such transitions may require implementing the older and newer technologies simultaneously during the transition period and thus increase the number of access points to the system.

### SC-07(04) External Telecommunications Services {#sc-7.4}

**Statement.** - (a) Implement a managed interface for each external telecommunication service;
- (b) Establish a traffic flow policy for each managed interface;
- (c) Protect the confidentiality and integrity of the information being transmitted across each interface;
- (d) Document each exception to the traffic flow policy with a supporting mission or business need and duration of that need;
- (e) Review exceptions to the traffic flow policy [frequency] and remove exceptions that are no longer supported by an explicit mission or business need;
- (f) Prevent unauthorized exchange of control plane traffic with external networks;
- (g) Publish information to enable remote networks to detect unauthorized control plane traffic from internal networks; and
- (h) Filter unauthorized control plane traffic from external networks.

**Guidance.** External telecommunications services can provide data and/or voice communications services. Examples of control plane traffic include Border Gateway Protocol (BGP) routing, Domain Name System (DNS), and management protocols. See [SP 800-189](#f5edfe51-d1f2-422e-9b27-5d0e90b49c72) for additional information on the use of the resource public key infrastructure (RPKI) to protect BGP routes and detect unauthorized BGP announcements.

### SC-07(05) Deny by Default — Allow by Exception {#sc-7.5}

**Statement.** Deny network communications traffic by default and allow network communications traffic by exception [organization-defined value].

**Guidance.** Denying by default and allowing by exception applies to inbound and outbound network communications traffic. A deny-all, permit-by-exception network communications traffic policy ensures that only those system connections that are essential and approved are allowed. Deny by default, allow by exception also applies to a system that is connected to an external system.

### SC-07(06) Response to Recognized Failures (withdrawn) {#sc-7.6}

### SC-07(07) Split Tunneling for Remote Devices {#sc-7.7}

**Statement.** Prevent split tunneling for remote devices connecting to organizational systems unless the split tunnel is securely provisioned using [safeguards].

**Guidance.** Split tunneling is the process of allowing a remote user or device to establish a non-remote connection with a system and simultaneously communicate via some other connection to a resource in an external network. This method of network access enables a user to access remote devices and simultaneously, access uncontrolled networks. Split tunneling might be desirable by remote users to communicate with local system resources, such as printers or file servers. However, split tunneling can facilitate unauthorized external connections, making the system vulnerable to attack and to exfiltration of organizational information. Split tunneling can be prevented by disabling configuration settings that allow such capability in remote devices and by preventing those configuration settings from being configurable by users. Prevention can also be achieved by the detection of split tunneling (or of configuration settings that allow split tunneling) in the remote device, and by prohibiting the connection if the remote device is using split tunneling. A virtual private network (VPN) can be used to securely provision a split tunnel. A securely provisioned VPN includes locking connectivity to exclusive, managed, and named environments, or to a specific set of pre-approved addresses, without user control.

### SC-07(08) Route Traffic to Authenticated Proxy Servers {#sc-7.8}

**Statement.** Route [internal communications traffic] to [external networks] through authenticated proxy servers at managed interfaces.

**Guidance.** External networks are networks outside of organizational control. A proxy server is a server (i.e., system or application) that acts as an intermediary for clients requesting system resources from non-organizational or other organizational servers. System resources that may be requested include files, connections, web pages, or services. Client requests established through a connection to a proxy server are assessed to manage complexity and provide additional protection by limiting direct connectivity. Web content filtering devices are one of the most common proxy servers that provide access to the Internet. Proxy servers can support the logging of Transmission Control Protocol sessions and the blocking of specific Uniform Resource Locators, Internet Protocol addresses, and domain names. Web proxies can be configured with organization-defined lists of authorized and unauthorized websites. Note that proxy servers may inhibit the use of virtual private networks (VPNs) and create the potential for "man-in-the-middle" attacks (depending on the implementation).

### SC-07(09) Restrict Threatening Outgoing Communications Traffic {#sc-7.9}

**Statement.** - (a) Detect and deny outgoing communications traffic posing a threat to external systems; and
- (b) Audit the identity of internal users associated with denied communications.

**Guidance.** Detecting outgoing communications traffic from internal actions that may pose threats to external systems is known as extrusion detection. Extrusion detection is carried out within the system at managed interfaces. Extrusion detection includes the analysis of incoming and outgoing communications traffic while searching for indications of internal threats to the security of external systems. Internal threats to external systems include traffic indicative of denial-of-service attacks, traffic with spoofed source addresses, and traffic that contains malicious code. Organizations have criteria to determine, update, and manage identified threats related to extrusion detection.

### SC-07(10) Prevent Exfiltration {#sc-7.10}

**Statement.** - (a) Prevent the exfiltration of information; and
- (b) Conduct exfiltration tests [frequency].

**Guidance.** Prevention of exfiltration applies to both the intentional and unintentional exfiltration of information. Techniques used to prevent the exfiltration of information from systems may be implemented at internal endpoints, external boundaries, and across managed interfaces and include adherence to protocol formats, monitoring for beaconing activity from systems, disconnecting external network interfaces except when explicitly needed, employing traffic profile analysis to detect deviations from the volume and types of traffic expected, call backs to command and control centers, conducting penetration testing, monitoring for steganography, disassembling and reassembling packet headers, and using data loss and data leakage prevention tools. Devices that enforce strict adherence to protocol formats include deep packet inspection firewalls and Extensible Markup Language (XML) gateways. The devices verify adherence to protocol formats and specifications at the application layer and identify vulnerabilities that cannot be detected by devices that operate at the network or transport layers. The prevention of exfiltration is similar to data loss prevention or data leakage prevention and is closely associated with cross-domain solutions and system guards that enforce information flow requirements.

### SC-07(11) Restrict Incoming Communications Traffic {#sc-7.11}

**Statement.** Only allow incoming communications from [authorized sources] to be routed to [authorized destinations].

**Guidance.** General source address validation techniques are applied to restrict the use of illegal and unallocated source addresses as well as source addresses that should only be used within the system. The restriction of incoming communications traffic provides determinations that source and destination address pairs represent authorized or allowed communications. Determinations can be based on several factors, including the presence of such address pairs in the lists of authorized or allowed communications, the absence of such address pairs in lists of unauthorized or disallowed pairs, or meeting more general rules for authorized or allowed source and destination pairs. Strong authentication of network addresses is not possible without the use of explicit security protocols, and thus, addresses can often be spoofed. Further, identity-based incoming traffic restriction methods can be employed, including router access control lists and firewall rules.

### SC-07(12) Host-based Protection {#sc-7.12}

**Statement.** Implement [host-based boundary protection mechanisms] at [system components].

**Guidance.** Host-based boundary protection mechanisms include host-based firewalls. System components that employ host-based boundary protection mechanisms include servers, workstations, notebook computers, and mobile devices.

### SC-07(13) Isolation of Security Tools, Mechanisms, and Support Components {#sc-7.13}

**Statement.** Isolate [information security tools, mechanisms, and support components] from other internal system components by implementing physically separate subnetworks with managed interfaces to other components of the system.

**Guidance.** Physically separate subnetworks with managed interfaces are useful in isolating computer network defenses from critical operational processing networks to prevent adversaries from discovering the analysis and forensics techniques employed by organizations.

### SC-07(14) Protect Against Unauthorized Physical Connections {#sc-7.14}

**Statement.** Protect against unauthorized physical connections at [managed interfaces].

**Guidance.** Systems that operate at different security categories or classification levels may share common physical and environmental controls, since the systems may share space within the same facilities. In practice, it is possible that these separate systems may share common equipment rooms, wiring closets, and cable distribution paths. Protection against unauthorized physical connections can be achieved by using clearly identified and physically separated cable trays, connection frames, and patch panels for each side of managed interfaces with physical access controls that enforce limited authorized access to these items.

### SC-07(15) Networked Privileged Accesses {#sc-7.15}

**Statement.** Route networked, privileged accesses through a dedicated, managed interface for purposes of access control and auditing.

**Guidance.** Privileged access provides greater accessibility to system functions, including security functions. Adversaries attempt to gain privileged access to systems through remote access to cause adverse mission or business impacts, such as by exfiltrating information or bringing down a critical system capability. Routing networked, privileged access requests through a dedicated, managed interface further restricts privileged access for increased access control and auditing.

### SC-07(16) Prevent Discovery of System Components {#sc-7.16}

**Statement.** Prevent the discovery of specific system components that represent a managed interface.

**Guidance.** Preventing the discovery of system components representing a managed interface helps protect network addresses of those components from discovery through common tools and techniques used to identify devices on networks. Network addresses are not available for discovery and require prior knowledge for access. Preventing the discovery of components and devices can be accomplished by not publishing network addresses, using network address translation, or not entering the addresses in domain name systems. Another prevention technique is to periodically change network addresses.

### SC-07(17) Automated Enforcement of Protocol Formats {#sc-7.17}

**Statement.** Enforce adherence to protocol formats.

**Guidance.** System components that enforce protocol formats include deep packet inspection firewalls and XML gateways. The components verify adherence to protocol formats and specifications at the application layer and identify vulnerabilities that cannot be detected by devices operating at the network or transport layers.

### SC-07(18) Fail Secure {#sc-7.18}

**Statement.** Prevent systems from entering unsecure states in the event of an operational failure of a boundary protection device.

**Guidance.** Fail secure is a condition achieved by employing mechanisms to ensure that in the event of operational failures of boundary protection devices at managed interfaces, systems do not enter into unsecure states where intended security properties no longer hold. Managed interfaces include routers, firewalls, and application gateways that reside on protected subnetworks (commonly referred to as demilitarized zones). Failures of boundary protection devices cannot lead to or cause information external to the devices to enter the devices nor can failures permit unauthorized information releases.

### SC-07(19) Block Communication from Non-organizationally Configured Hosts {#sc-7.19}

**Statement.** Block inbound and outbound communications traffic between [communication clients] that are independently configured by end users and external service providers.

**Guidance.** Communication clients independently configured by end users and external service providers include instant messaging clients and video conferencing software and applications. Traffic blocking does not apply to communication clients that are configured by organizations to perform authorized functions.

### SC-07(20) Dynamic Isolation and Segregation {#sc-7.20}

**Statement.** Provide the capability to dynamically isolate [system components] from other system components.

**Guidance.** The capability to dynamically isolate certain internal system components is useful when it is necessary to partition or separate system components of questionable origin from components that possess greater trustworthiness. Component isolation reduces the attack surface of organizational systems. Isolating selected system components can also limit the damage from successful attacks when such attacks occur.

### SC-07(21) Isolation of System Components {#sc-7.21}

**Statement.** Employ boundary protection mechanisms to isolate [system components] supporting [missions and/or business functions].

**Guidance.** Organizations can isolate system components that perform different mission or business functions. Such isolation limits unauthorized information flows among system components and provides the opportunity to deploy greater levels of protection for selected system components. Isolating system components with boundary protection mechanisms provides the capability for increased protection of individual system components and to more effectively control information flows between those components. Isolating system components provides enhanced protection that limits the potential harm from hostile cyber-attacks and errors. The degree of isolation varies depending upon the mechanisms chosen. Boundary protection mechanisms include routers, gateways, and firewalls that separate system components into physically separate networks or subnetworks; cross-domain devices that separate subnetworks; virtualization techniques; and the encryption of information flows among system components using distinct encryption keys.

### SC-07(22) Separate Subnets for Connecting to Different Security Domains {#sc-7.22}

**Statement.** Implement separate network addresses to connect to systems in different security domains.

**Guidance.** The decomposition of systems into subnetworks (i.e., subnets) helps to provide the appropriate level of protection for network connections to different security domains that contain information with different security categories or classification levels.

### SC-07(23) Disable Sender Feedback on Protocol Validation Failure {#sc-7.23}

**Statement.** Disable feedback to senders on protocol format validation failure.

**Guidance.** Disabling feedback to senders when there is a failure in protocol validation format prevents adversaries from obtaining information that would otherwise be unavailable.

### SC-07(24) Personally Identifiable Information {#sc-7.24}

**Statement.** For systems that process personally identifiable information:
- (a) Apply the following processing rules to data elements of personally identifiable information: [processing rules];
- (b) Monitor for permitted processing at the external interfaces to the system and at key internal boundaries within the system;
- (c) Document each processing exception; and
- (d) Review and remove exceptions that are no longer supported.

**Guidance.** Managing the processing of personally identifiable information is an important aspect of protecting an individual’s privacy. Applying, monitoring for, and documenting exceptions to processing rules ensure that personally identifiable information is processed only in accordance with established privacy requirements.

### SC-07(25) Unclassified National Security System Connections {#sc-7.25}

**Statement.** Prohibit the direct connection of [unclassified national security system] to an external network without the use of [boundary protection device].

**Guidance.** A direct connection is a dedicated physical or virtual connection between two or more systems. Organizations typically do not have complete control over external networks, including the Internet. Boundary protection devices (e.g., firewalls, gateways, and routers) mediate communications and information flows between unclassified national security systems and external networks.

### SC-07(26) Classified National Security System Connections {#sc-7.26}

**Statement.** Prohibit the direct connection of a classified national security system to an external network without the use of [boundary protection device].

**Guidance.** A direct connection is a dedicated physical or virtual connection between two or more systems. Organizations typically do not have complete control over external networks, including the Internet. Boundary protection devices (e.g., firewalls, gateways, and routers) mediate communications and information flows between classified national security systems and external networks. In addition, approved boundary protection devices (typically managed interface or cross-domain systems) provide information flow enforcement from systems to external networks.

### SC-07(27) Unclassified Non-national Security System Connections {#sc-7.27}

**Statement.** Prohibit the direct connection of [unclassified, non-national security system] to an external network without the use of [boundary protection device].

**Guidance.** A direct connection is a dedicated physical or virtual connection between two or more systems. Organizations typically do not have complete control over external networks, including the Internet. Boundary protection devices (e.g., firewalls, gateways, and routers) mediate communications and information flows between unclassified non-national security systems and external networks.

### SC-07(28) Connections to Public Networks {#sc-7.28}

**Statement.** Prohibit the direct connection of [system] to a public network.

**Guidance.** A direct connection is a dedicated physical or virtual connection between two or more systems. A public network is a network accessible to the public, including the Internet and organizational extranets with public access.

### SC-07(29) Separate Subnets to Isolate Functions {#sc-7.29}

**Statement.** Implement [organization-defined value] separate subnetworks to isolate the following critical system components and functions: [critical system components and functions].

**Guidance.** Separating critical system components and functions from other noncritical system components and functions through separate subnetworks may be necessary to reduce susceptibility to a catastrophic or debilitating breach or compromise that results in system failure. For example, physically separating the command and control function from the in-flight entertainment function through separate subnetworks in a commercial aircraft provides an increased level of assurance in the trustworthiness of critical system functions.

## SC-08 Transmission Confidentiality and Integrity {#sc-8}

**Statement.** Protect the [organization-defined value] of transmitted information.

**Guidance.** Protecting the confidentiality and integrity of transmitted information applies to internal and external networks as well as any system components that can transmit information, including servers, notebook computers, desktop computers, mobile devices, printers, copiers, scanners, facsimile machines, and radios. Unprotected communication paths are exposed to the possibility of interception and modification. Protecting the confidentiality and integrity of information can be accomplished by physical or logical means. Physical protection can be achieved by using protected distribution systems. A protected distribution system is a wireline or fiber-optics telecommunications system that includes terminals and adequate electromagnetic, acoustical, electrical, and physical controls to permit its use for the unencrypted transmission of classified information. Logical protection can be achieved by employing encryption techniques.

Organizations that rely on commercial providers who offer transmission services as commodity services rather than as fully dedicated services may find it difficult to obtain the necessary assurances regarding the implementation of needed controls for transmission confidentiality and integrity. In such situations, organizations determine what types of confidentiality or integrity services are available in standard, commercial telecommunications service packages. If it is not feasible to obtain the necessary controls and assurances of control effectiveness through appropriate contracting vehicles, organizations can implement appropriate compensating controls.

### SC-08(01) Cryptographic Protection {#sc-8.1}

**Statement.** Implement cryptographic mechanisms to [organization-defined value] during transmission.

**Guidance.** Encryption protects information from unauthorized disclosure and modification during transmission. Cryptographic mechanisms that protect the confidentiality and integrity of information during transmission include TLS and IPSec. Cryptographic mechanisms used to protect information integrity include cryptographic hash functions that have applications in digital signatures, checksums, and message authentication codes.

### SC-08(02) Pre- and Post-transmission Handling {#sc-8.2}

**Statement.** Maintain the [organization-defined value] of information during preparation for transmission and during reception.

**Guidance.** Information can be unintentionally or maliciously disclosed or modified during preparation for transmission or during reception, including during aggregation, at protocol transformation points, and during packing and unpacking. Such unauthorized disclosures or modifications compromise the confidentiality or integrity of the information.

### SC-08(03) Cryptographic Protection for Message Externals {#sc-8.3}

**Statement.** Implement cryptographic mechanisms to protect message externals unless otherwise protected by [alternative physical controls].

**Guidance.** Cryptographic protection for message externals addresses protection from the unauthorized disclosure of information. Message externals include message headers and routing information. Cryptographic protection prevents the exploitation of message externals and applies to internal and external networks or links that may be visible to individuals who are not authorized users. Header and routing information is sometimes transmitted in clear text (i.e., unencrypted) because the information is not identified by organizations as having significant value or because encrypting the information can result in lower network performance or higher costs. Alternative physical controls include protected distribution systems.

### SC-08(04) Conceal or Randomize Communications {#sc-8.4}

**Statement.** Implement cryptographic mechanisms to conceal or randomize communication patterns unless otherwise protected by [alternative physical controls].

**Guidance.** Concealing or randomizing communication patterns addresses protection from unauthorized disclosure of information. Communication patterns include frequency, periods, predictability, and amount. Changes to communications patterns can reveal information with intelligence value, especially when combined with other available information related to the mission and business functions of the organization. Concealing or randomizing communications prevents the derivation of intelligence based on communications patterns and applies to both internal and external networks or links that may be visible to individuals who are not authorized users. Encrypting the links and transmitting in continuous, fixed, or random patterns prevents the derivation of intelligence from the system communications patterns. Alternative physical controls include protected distribution systems.

### SC-08(05) Protected Distribution System {#sc-8.5}

**Statement.** Implement [protected distribution system] to [organization-defined value] during transmission.

**Guidance.** The purpose of a protected distribution system is to deter, detect, and/or make difficult physical access to the communication lines that carry national security information.

## SC-09 Transmission Confidentiality (withdrawn) {#sc-9}

## SC-10 Network Disconnect {#sc-10}

**Statement.** Terminate the network connection associated with a communications session at the end of the session or after [time period] of inactivity.

**Guidance.** Network disconnect applies to internal and external networks. Terminating network connections associated with specific communications sessions includes de-allocating TCP/IP address or port pairs at the operating system level and de-allocating the networking assignments at the application level if multiple application sessions are using a single operating system-level network connection. Periods of inactivity may be established by organizations and include time periods by type of network access or for specific network accesses.

## SC-11 Trusted Path {#sc-11}

**Statement.** - a. Provide a [organization-defined value] isolated trusted communications path for communications between the user and the trusted components of the system; and
- b. Permit users to invoke the trusted communications path for communications between the user and the following security functions of the system, including at a minimum, authentication and re-authentication: [security functions].

**Guidance.** Trusted paths are mechanisms by which users can communicate (using input devices such as keyboards) directly with the security functions of systems with the requisite assurance to support security policies. Trusted path mechanisms can only be activated by users or the security functions of organizational systems. User responses that occur via trusted paths are protected from modification by and disclosure to untrusted applications. Organizations employ trusted paths for trustworthy, high-assurance connections between security functions of systems and users, including during system logons. The original implementations of trusted paths employed an out-of-band signal to initiate the path, such as using the <BREAK> key, which does not transmit characters that can be spoofed. In later implementations, a key combination that could not be hijacked was used (e.g., the <CTRL> + <ALT> + <DEL> keys). Such key combinations, however, are platform-specific and may not provide a trusted path implementation in every case. The enforcement of trusted communications paths is provided by a specific implementation that meets the reference monitor concept.

### SC-11(01) Irrefutable Communications Path {#sc-11.1}

**Statement.** - (a) Provide a trusted communications path that is irrefutably distinguishable from other communications paths; and
- (b) Initiate the trusted communications path for communications between the [security functions] of the system and the user.

**Guidance.** An irrefutable communications path permits the system to initiate a trusted path, which necessitates that the user can unmistakably recognize the source of the communication as a trusted system component. For example, the trusted path may appear in an area of the display that other applications cannot access or be based on the presence of an identifier that cannot be spoofed.

## SC-12 Cryptographic Key Establishment and Management {#sc-12}

**Statement.** Establish and manage cryptographic keys when cryptography is employed within the system in accordance with the following key management requirements: [requirements].

**Guidance.** Cryptographic key management and establishment can be performed using manual procedures or automated mechanisms with supporting manual procedures. Organizations define key management requirements in accordance with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines and specify appropriate options, parameters, and levels. Organizations manage trust stores to ensure that only approved trust anchors are part of such trust stores. This includes certificates with visibility external to organizational systems and certificates related to the internal operations of systems. [NIST CMVP](#1acdc775-aafb-4d11-9341-dc6a822e9d38) and [NIST CAVP](#84dc1b0c-acb7-4269-84c4-00dbabacd78c) provide additional information on validated cryptographic modules and algorithms that can be used in cryptographic key management and establishment.

### SC-12(01) Availability {#sc-12.1}

**Statement.** Maintain availability of information in the event of the loss of cryptographic keys by users.

**Guidance.** Escrowing of encryption keys is a common practice for ensuring availability in the event of key loss. A forgotten passphrase is an example of losing a cryptographic key.

### SC-12(02) Symmetric Keys {#sc-12.2}

**Statement.** Produce, control, and distribute symmetric cryptographic keys using [organization-defined value] key management technology and processes.

**Guidance.** [SP 800-56A](#20957dbb-6a1e-40a2-b38a-66f67d33ac2e), [SP 800-56B](#0d083d8a-5cc6-46f1-8d79-3081d42bcb75) , and [SP 800-56C](#eef62b16-c796-4554-955c-505824135b8a) provide guidance on cryptographic key establishment schemes and key derivation methods. [SP 800-57-1](#110e26af-4765-49e1-8740-6750f83fcda1), [SP 800-57-2](#e7942589-e267-4a5a-a3d9-f39a7aae81f0) , and [SP 800-57-3](#8306620b-1920-4d73-8b21-12008528595f) provide guidance on cryptographic key management.

### SC-12(03) Asymmetric Keys {#sc-12.3}

**Statement.** Produce, control, and distribute asymmetric cryptographic keys using [organization-defined value].

**Guidance.** [SP 800-56A](#20957dbb-6a1e-40a2-b38a-66f67d33ac2e), [SP 800-56B](#0d083d8a-5cc6-46f1-8d79-3081d42bcb75) , and [SP 800-56C](#eef62b16-c796-4554-955c-505824135b8a) provide guidance on cryptographic key establishment schemes and key derivation methods. [SP 800-57-1](#110e26af-4765-49e1-8740-6750f83fcda1), [SP 800-57-2](#e7942589-e267-4a5a-a3d9-f39a7aae81f0) , and [SP 800-57-3](#8306620b-1920-4d73-8b21-12008528595f) provide guidance on cryptographic key management.

### SC-12(04) PKI Certificates (withdrawn) {#sc-12.4}

### SC-12(05) PKI Certificates / Hardware Tokens (withdrawn) {#sc-12.5}

### SC-12(06) Physical Control of Keys {#sc-12.6}

**Statement.** Maintain physical control of cryptographic keys when stored information is encrypted by external service providers.

**Guidance.** For organizations that use external service providers (e.g., cloud service or data center providers), physical control of cryptographic keys provides additional assurance that information stored by such external providers is not subject to unauthorized disclosure or modification.

## SC-13 Cryptographic Protection {#sc-13}

**Statement.** - a. Determine the [cryptographic uses] ; and
- b. Implement the following types of cryptography required for each specified cryptographic use: [types of cryptography].

**Guidance.** Cryptography can be employed to support a variety of security solutions, including the protection of classified information and controlled unclassified information, the provision and implementation of digital signatures, and the enforcement of information separation when authorized individuals have the necessary clearances but lack the necessary formal access approvals. Cryptography can also be used to support random number and hash generation. Generally applicable cryptographic standards include FIPS-validated cryptography and NSA-approved cryptography. For example, organizations that need to protect classified information may specify the use of NSA-approved cryptography. Organizations that need to provision and implement digital signatures may specify the use of FIPS-validated cryptography. Cryptography is implemented in accordance with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines.

### SC-13(01) FIPS-validated Cryptography (withdrawn) {#sc-13.1}

### SC-13(02) NSA-approved Cryptography (withdrawn) {#sc-13.2}

### SC-13(03) Individuals Without Formal Access Approvals (withdrawn) {#sc-13.3}

### SC-13(04) Digital Signatures (withdrawn) {#sc-13.4}

## SC-14 Public Access Protections (withdrawn) {#sc-14}

## SC-15 Collaborative Computing Devices and Applications {#sc-15}

**Statement.** - a. Prohibit remote activation of collaborative computing devices and applications with the following exceptions: [exceptions where remote activation is to be allowed] ; and
- b. Provide an explicit indication of use to users physically present at the devices.

**Guidance.** Collaborative computing devices and applications include remote meeting devices and applications, networked white boards, cameras, and microphones. The explicit indication of use includes signals to users when collaborative computing devices and applications are activated.

### SC-15(01) Physical or Logical Disconnect {#sc-15.1}

**Statement.** Provide [organization-defined value] disconnect of collaborative computing devices in a manner that supports ease of use.

**Guidance.** Failing to disconnect from collaborative computing devices can result in subsequent compromises of organizational information. Providing easy methods to disconnect from such devices after a collaborative computing session ensures that participants carry out the disconnect activity without having to go through complex and tedious procedures. Disconnect from collaborative computing devices can be manual or automatic.

### SC-15(02) Blocking Inbound and Outbound Communications Traffic (withdrawn) {#sc-15.2}

### SC-15(03) Disabling and Removal in Secure Work Areas {#sc-15.3}

**Statement.** Disable or remove collaborative computing devices and applications from [systems or system components] in [secure work areas].

**Guidance.** Failing to disable or remove collaborative computing devices and applications from systems or system components can result in compromises of information, including eavesdropping on conversations. A Sensitive Compartmented Information Facility (SCIF) is an example of a secure work area.

### SC-15(04) Explicitly Indicate Current Participants {#sc-15.4}

**Statement.** Provide an explicit indication of current participants in [online meetings and teleconferences].

**Guidance.** Explicitly indicating current participants prevents unauthorized individuals from participating in collaborative computing sessions without the explicit knowledge of other participants.

## SC-16 Transmission of Security and Privacy Attributes {#sc-16}

**Statement.** Associate [organization-defined security and privacy attributes] with information exchanged between systems and between system components.

**Guidance.** Security and privacy attributes can be explicitly or implicitly associated with the information contained in organizational systems or system components. Attributes are abstractions that represent the basic properties or characteristics of an entity with respect to protecting information or the management of personally identifiable information. Attributes are typically associated with internal data structures, including records, buffers, and files within the system. Security and privacy attributes are used to implement access control and information flow control policies; reflect special dissemination, management, or distribution instructions, including permitted uses of personally identifiable information; or support other aspects of the information security and privacy policies. Privacy attributes may be used independently or in conjunction with security attributes.

### SC-16(01) Integrity Verification {#sc-16.1}

**Statement.** Verify the integrity of transmitted security and privacy attributes.

**Guidance.** Part of verifying the integrity of transmitted information is ensuring that security and privacy attributes that are associated with such information have not been modified in an unauthorized manner. Unauthorized modification of security or privacy attributes can result in a loss of integrity for transmitted information.

### SC-16(02) Anti-spoofing Mechanisms {#sc-16.2}

**Statement.** Implement anti-spoofing mechanisms to prevent adversaries from falsifying the security attributes indicating the successful application of the security process.

**Guidance.** Some attack vectors operate by altering the security attributes of an information system to intentionally and maliciously implement an insufficient level of security within the system. The alteration of attributes leads organizations to believe that a greater number of security functions are in place and operational than have actually been implemented.

### SC-16(03) Cryptographic Binding {#sc-16.3}

**Statement.** Implement [mechanisms or techniques] to bind security and privacy attributes to transmitted information.

**Guidance.** Cryptographic mechanisms and techniques can provide strong security and privacy attribute binding to transmitted information to help ensure the integrity of such information.

## SC-17 Public Key Infrastructure Certificates {#sc-17}

**Statement.** - a. Issue public key certificates under an [certificate policy] or obtain public key certificates from an approved service provider; and
- b. Include only approved trust anchors in trust stores or certificate stores managed by the organization.

**Guidance.** Public key infrastructure (PKI) certificates are certificates with visibility external to organizational systems and certificates related to the internal operations of systems, such as application-specific time services. In cryptographic systems with a hierarchical structure, a trust anchor is an authoritative source (i.e., a certificate authority) for which trust is assumed and not derived. A root certificate for a PKI system is an example of a trust anchor. A trust store or certificate store maintains a list of trusted root certificates.

## SC-18 Mobile Code {#sc-18}

**Statement.** - a. Define acceptable and unacceptable mobile code and mobile code technologies; and
- b. Authorize, monitor, and control the use of mobile code within the system.

**Guidance.** Mobile code includes any program, application, or content that can be transmitted across a network (e.g., embedded in an email, document, or website) and executed on a remote system. Decisions regarding the use of mobile code within organizational systems are based on the potential for the code to cause damage to the systems if used maliciously. Mobile code technologies include Java applets, JavaScript, HTML5, WebGL, and VBScript. Usage restrictions and implementation guidelines apply to both the selection and use of mobile code installed on servers and mobile code downloaded and executed on individual workstations and devices, including notebook computers and smart phones. Mobile code policy and procedures address specific actions taken to prevent the development, acquisition, and introduction of unacceptable mobile code within organizational systems, including requiring mobile code to be digitally signed by a trusted source.

### SC-18(01) Identify Unacceptable Code and Take Corrective Actions {#sc-18.1}

**Statement.** Identify [unacceptable mobile code] and take [corrective actions].

**Guidance.** Corrective actions when unacceptable mobile code is detected include blocking, quarantine, or alerting administrators. Blocking includes preventing the transmission of word processing files with embedded macros when such macros have been determined to be unacceptable mobile code.

### SC-18(02) Acquisition, Development, and Use {#sc-18.2}

**Statement.** Verify that the acquisition, development, and use of mobile code to be deployed in the system meets [mobile code requirements].

**Guidance.** None.

### SC-18(03) Prevent Downloading and Execution {#sc-18.3}

**Statement.** Prevent the download and execution of [unacceptable mobile code].

**Guidance.** None.

### SC-18(04) Prevent Automatic Execution {#sc-18.4}

**Statement.** Prevent the automatic execution of mobile code in [software applications] and enforce [actions] prior to executing the code.

**Guidance.** Actions enforced before executing mobile code include prompting users prior to opening email attachments or clicking on web links. Preventing the automatic execution of mobile code includes disabling auto-execute features on system components that employ portable storage devices, such as compact discs, digital versatile discs, and universal serial bus devices.

### SC-18(05) Allow Execution Only in Confined Environments {#sc-18.5}

**Statement.** Allow execution of permitted mobile code only in confined virtual machine environments.

**Guidance.** Permitting the execution of mobile code only in confined virtual machine environments helps prevent the introduction of malicious code into other systems and system components.

## SC-19 Voice Over Internet Protocol (withdrawn) {#sc-19}

**Statement.** Technology-specific; addressed as any other technology or protocol.

## SC-20 Secure Name/Address Resolution Service (Authoritative Source) {#sc-20}

**Statement.** - a. Provide additional data origin authentication and integrity verification artifacts along with the authoritative name resolution data the system returns in response to external name/address resolution queries; and
- b. Provide the means to indicate the security status of child zones and (if the child supports secure resolution services) to enable verification of a chain of trust among parent and child domains, when operating as part of a distributed, hierarchical namespace.

**Guidance.** Providing authoritative source information enables external clients, including remote Internet clients, to obtain origin authentication and integrity verification assurances for the host/service name to network address resolution information obtained through the service. Systems that provide name and address resolution services include domain name system (DNS) servers. Additional artifacts include DNS Security Extensions (DNSSEC) digital signatures and cryptographic keys. Authoritative data includes DNS resource records. The means for indicating the security status of child zones include the use of delegation signer resource records in the DNS. Systems that use technologies other than the DNS to map between host and service names and network addresses provide other means to assure the authenticity and integrity of response data.

### SC-20(01) Child Subspaces (withdrawn) {#sc-20.1}

### SC-20(02) Data Origin and Integrity {#sc-20.2}

**Statement.** Provide data origin and integrity protection artifacts for internal name/address resolution queries.

**Guidance.** None.

## SC-21 Secure Name/Address Resolution Service (Recursive or Caching Resolver) {#sc-21}

**Statement.** Request and perform data origin authentication and data integrity verification on the name/address resolution responses the system receives from authoritative sources.

**Guidance.** Each client of name resolution services either performs this validation on its own or has authenticated channels to trusted validation providers. Systems that provide name and address resolution services for local clients include recursive resolving or caching domain name system (DNS) servers. DNS client resolvers either perform validation of DNSSEC signatures, or clients use authenticated channels to recursive resolvers that perform such validations. Systems that use technologies other than the DNS to map between host and service names and network addresses provide some other means to enable clients to verify the authenticity and integrity of response data.

### SC-21(01) Data Origin and Integrity (withdrawn) {#sc-21.1}

## SC-22 Architecture and Provisioning for Name/Address Resolution Service {#sc-22}

**Statement.** Ensure the systems that collectively provide name/address resolution service for an organization are fault-tolerant and implement internal and external role separation.

**Guidance.** Systems that provide name and address resolution services include domain name system (DNS) servers. To eliminate single points of failure in systems and enhance redundancy, organizations employ at least two authoritative domain name system servers—one configured as the primary server and the other configured as the secondary server. Additionally, organizations typically deploy the servers in two geographically separated network subnetworks (i.e., not located in the same physical facility). For role separation, DNS servers with internal roles only process name and address resolution requests from within organizations (i.e., from internal clients). DNS servers with external roles only process name and address resolution information requests from clients external to organizations (i.e., on external networks, including the Internet). Organizations specify clients that can access authoritative DNS servers in certain roles (e.g., by address ranges and explicit lists).

## SC-23 Session Authenticity {#sc-23}

**Statement.** Protect the authenticity of communications sessions.

**Guidance.** Protecting session authenticity addresses communications protection at the session level, not at the packet level. Such protection establishes grounds for confidence at both ends of communications sessions in the ongoing identities of other parties and the validity of transmitted information. Authenticity protection includes protecting against "man-in-the-middle" attacks, session hijacking, and the insertion of false information into sessions.

### SC-23(01) Invalidate Session Identifiers at Logout {#sc-23.1}

**Statement.** Invalidate session identifiers upon user logout or other session termination.

**Guidance.** Invalidating session identifiers at logout curtails the ability of adversaries to capture and continue to employ previously valid session IDs.

### SC-23(02) User-initiated Logouts and Message Displays (withdrawn) {#sc-23.2}

### SC-23(03) Unique System-generated Session Identifiers {#sc-23.3}

**Statement.** Generate a unique session identifier for each session with [randomness requirements] and recognize only session identifiers that are system-generated.

**Guidance.** Generating unique session identifiers curtails the ability of adversaries to reuse previously valid session IDs. Employing the concept of randomness in the generation of unique session identifiers protects against brute-force attacks to determine future session identifiers.

### SC-23(04) Unique Session Identifiers with Randomization (withdrawn) {#sc-23.4}

### SC-23(05) Allowed Certificate Authorities {#sc-23.5}

**Statement.** Only allow the use of [certificated authorities] for verification of the establishment of protected sessions.

**Guidance.** Reliance on certificate authorities for the establishment of secure sessions includes the use of Transport Layer Security (TLS) certificates. These certificates, after verification by their respective certificate authorities, facilitate the establishment of protected sessions between web clients and web servers.

## SC-24 Fail in Known State {#sc-24}

**Statement.** Fail to a [known system state] for the following failures on the indicated components while preserving [system state information] in failure: [types of system failures on system components].

**Guidance.** Failure in a known state addresses security concerns in accordance with the mission and business needs of organizations. Failure in a known state prevents the loss of confidentiality, integrity, or availability of information in the event of failures of organizational systems or system components. Failure in a known safe state helps to prevent systems from failing to a state that may cause injury to individuals or destruction to property. Preserving system state information facilitates system restart and return to the operational mode with less disruption of mission and business processes.

## SC-25 Thin Nodes {#sc-25}

**Statement.** Employ minimal functionality and information storage on the following system components: [system components].

**Guidance.** The deployment of system components with minimal functionality reduces the need to secure every endpoint and may reduce the exposure of information, systems, and services to attacks. Reduced or minimal functionality includes diskless nodes and thin client technologies.

## SC-26 Decoys {#sc-26}

**Statement.** Include components within organizational systems specifically designed to be the target of malicious attacks for detecting, deflecting, and analyzing such attacks.

**Guidance.** Decoys (i.e., honeypots, honeynets, or deception nets) are established to attract adversaries and deflect attacks away from the operational systems that support organizational mission and business functions. Use of decoys requires some supporting isolation measures to ensure that any deflected malicious code does not infect organizational systems. Depending on the specific usage of the decoy, consultation with the Office of the General Counsel before deployment may be needed.

### SC-26(01) Detection of Malicious Code (withdrawn) {#sc-26.1}

## SC-27 Platform-independent Applications {#sc-27}

**Statement.** Include within organizational systems the following platform independent applications: [platform-independent applications].

**Guidance.** Platforms are combinations of hardware, firmware, and software components used to execute software applications. Platforms include operating systems, the underlying computer architectures, or both. Platform-independent applications are applications with the capability to execute on multiple platforms. Such applications promote portability and reconstitution on different platforms. Application portability and the ability to reconstitute on different platforms increase the availability of mission-essential functions within organizations in situations where systems with specific operating systems are under attack.

## SC-28 Protection of Information at Rest {#sc-28}

**Statement.** Protect the [organization-defined value] of the following information at rest: [information at rest].

**Guidance.** Information at rest refers to the state of information when it is not in process or in transit and is located on system components. Such components include internal or external hard disk drives, storage area network devices, or databases. However, the focus of protecting information at rest is not on the type of storage device or frequency of access but rather on the state of the information. Information at rest addresses the confidentiality and integrity of information and covers user information and system information. System-related information that requires protection includes configurations or rule sets for firewalls, intrusion detection and prevention systems, filtering routers, and authentication information. Organizations may employ different mechanisms to achieve confidentiality and integrity protections, including the use of cryptographic mechanisms and file share scanning. Integrity protection can be achieved, for example, by implementing write-once-read-many (WORM) technologies. When adequate protection of information at rest cannot otherwise be achieved, organizations may employ other controls, including frequent scanning to identify malicious code at rest and secure offline storage in lieu of online storage.

### SC-28(01) Cryptographic Protection {#sc-28.1}

**Statement.** Implement cryptographic mechanisms to prevent unauthorized disclosure and modification of the following information at rest on [system components or media]: [information].

**Guidance.** The selection of cryptographic mechanisms is based on the need to protect the confidentiality and integrity of organizational information. The strength of mechanism is commensurate with the security category or classification of the information. Organizations have the flexibility to encrypt information on system components or media or encrypt data structures, including files, records, or fields.

### SC-28(02) Offline Storage {#sc-28.2}

**Statement.** Remove the following information from online storage and store offline in a secure location: [information].

**Guidance.** Removing organizational information from online storage to offline storage eliminates the possibility of individuals gaining unauthorized access to the information through a network. Therefore, organizations may choose to move information to offline storage in lieu of protecting such information in online storage.

### SC-28(03) Cryptographic Keys {#sc-28.3}

**Statement.** Provide protected storage for cryptographic keys [organization-defined value].

**Guidance.** A Trusted Platform Module (TPM) is an example of a hardware-protected data store that can be used to protect cryptographic keys.

## SC-29 Heterogeneity {#sc-29}

**Statement.** Employ a diverse set of information technologies for the following system components in the implementation of the system: [system components].

**Guidance.** Increasing the diversity of information technologies within organizational systems reduces the impact of potential exploitations or compromises of specific technologies. Such diversity protects against common mode failures, including those failures induced by supply chain attacks. Diversity in information technologies also reduces the likelihood that the means adversaries use to compromise one system component will be effective against other system components, thus further increasing the adversary work factor to successfully complete planned attacks. An increase in diversity may add complexity and management overhead that could ultimately lead to mistakes and unauthorized configurations.

### SC-29(01) Virtualization Techniques {#sc-29.1}

**Statement.** Employ virtualization techniques to support the deployment of a diversity of operating systems and applications that are changed [frequency].

**Guidance.** While frequent changes to operating systems and applications can pose significant configuration management challenges, the changes can result in an increased work factor for adversaries to conduct successful attacks. Changing virtual operating systems or applications, as opposed to changing actual operating systems or applications, provides virtual changes that impede attacker success while reducing configuration management efforts. Virtualization techniques can assist in isolating untrustworthy software or software of dubious provenance into confined execution environments.

## SC-30 Concealment and Misdirection {#sc-30}

**Statement.** Employ the following concealment and misdirection techniques for [systems] at [time periods] to confuse and mislead adversaries: [concealment and misdirection techniques].

**Guidance.** Concealment and misdirection techniques can significantly reduce the targeting capabilities of adversaries (i.e., window of opportunity and available attack surface) to initiate and complete attacks. For example, virtualization techniques provide organizations with the ability to disguise systems, potentially reducing the likelihood of successful attacks without the cost of having multiple platforms. The increased use of concealment and misdirection techniques and methods—including randomness, uncertainty, and virtualization—may sufficiently confuse and mislead adversaries and subsequently increase the risk of discovery and/or exposing tradecraft. Concealment and misdirection techniques may provide additional time to perform core mission and business functions. The implementation of concealment and misdirection techniques may add to the complexity and management overhead required for the system.

### SC-30(01) Virtualization Techniques (withdrawn) {#sc-30.1}

### SC-30(02) Randomness {#sc-30.2}

**Statement.** Employ [techniques] to introduce randomness into organizational operations and assets.

**Guidance.** Randomness introduces increased levels of uncertainty for adversaries regarding the actions that organizations take to defend their systems against attacks. Such actions may impede the ability of adversaries to correctly target information resources of organizations that support critical missions or business functions. Uncertainty may also cause adversaries to hesitate before initiating or continuing attacks. Misdirection techniques that involve randomness include performing certain routine actions at different times of day, employing different information technologies, using different suppliers, and rotating roles and responsibilities of organizational personnel.

### SC-30(03) Change Processing and Storage Locations {#sc-30.3}

**Statement.** Change the location of [processing and/or storage] [organization-defined value]].

**Guidance.** Adversaries target critical mission and business functions and the systems that support those mission and business functions while also trying to minimize the exposure of their existence and tradecraft. The static, homogeneous, and deterministic nature of organizational systems targeted by adversaries make such systems more susceptible to attacks with less adversary cost and effort to be successful. Changing processing and storage locations (also referred to as moving target defense) addresses the advanced persistent threat using techniques such as virtualization, distributed processing, and replication. This enables organizations to relocate the system components (i.e., processing, storage) that support critical mission and business functions. Changing the locations of processing activities and/or storage sites introduces a degree of uncertainty into the targeting activities of adversaries. The targeting uncertainty increases the work factor of adversaries and makes compromises or breaches of the organizational systems more difficult and time-consuming. It also increases the chances that adversaries may inadvertently disclose certain aspects of their tradecraft while attempting to locate critical organizational resources.

### SC-30(04) Misleading Information {#sc-30.4}

**Statement.** Employ realistic, but misleading information in [system components] about its security state or posture.

**Guidance.** Employing misleading information is intended to confuse potential adversaries regarding the nature and extent of controls deployed by organizations. Thus, adversaries may employ incorrect and ineffective attack techniques. One technique for misleading adversaries is for organizations to place misleading information regarding the specific controls deployed in external systems that are known to be targeted by adversaries. Another technique is the use of deception nets that mimic actual aspects of organizational systems but use, for example, out-of-date software configurations.

### SC-30(05) Concealment of System Components {#sc-30.5}

**Statement.** Employ the following techniques to hide or conceal [system components]: [techniques].

**Guidance.** By hiding, disguising, or concealing critical system components, organizations may be able to decrease the probability that adversaries target and successfully compromise those assets. Potential means to hide, disguise, or conceal system components include the configuration of routers or the use of encryption or virtualization techniques.

## SC-31 Covert Channel Analysis {#sc-31}

**Statement.** - a. Perform a covert channel analysis to identify those aspects of communications within the system that are potential avenues for covert [organization-defined value] channels; and
- b. Estimate the maximum bandwidth of those channels.

**Guidance.** Developers are in the best position to identify potential areas within systems that might lead to covert channels. Covert channel analysis is a meaningful activity when there is the potential for unauthorized information flows across security domains, such as in the case of systems that contain export-controlled information and have connections to external networks (i.e., networks that are not controlled by organizations). Covert channel analysis is also useful for multilevel secure systems, multiple security level systems, and cross-domain systems.

### SC-31(01) Test Covert Channels for Exploitability {#sc-31.1}

**Statement.** Test a subset of the identified covert channels to determine the channels that are exploitable.

**Guidance.** None.

### SC-31(02) Maximum Bandwidth {#sc-31.2}

**Statement.** Reduce the maximum bandwidth for identified covert [organization-defined value] channels to [values].

**Guidance.** The complete elimination of covert channels, especially covert timing channels, is usually not possible without significant performance impacts.

### SC-31(03) Measure Bandwidth in Operational Environments {#sc-31.3}

**Statement.** Measure the bandwidth of [subset of identified covert channels] in the operational environment of the system.

**Guidance.** Measuring covert channel bandwidth in specified operational environments helps organizations determine how much information can be covertly leaked before such leakage adversely affects mission or business functions. Covert channel bandwidth may be significantly different when measured in settings that are independent of the specific environments of operation, including laboratories or system development environments.

## SC-32 System Partitioning {#sc-32}

**Statement.** Partition the system into [system components] residing in separate [organization-defined value] domains or environments based on [circumstances for the physical or logical separation of components].

**Guidance.** System partitioning is part of a defense-in-depth protection strategy. Organizations determine the degree of physical separation of system components. Physical separation options include physically distinct components in separate racks in the same room, critical components in separate rooms, and geographical separation of critical components. Security categorization can guide the selection of candidates for domain partitioning. Managed interfaces restrict or prohibit network access and information flow among partitioned system components.

### SC-32(01) Separate Physical Domains for Privileged Functions {#sc-32.1}

**Statement.** Partition privileged functions into separate physical domains.

**Guidance.** Privileged functions that operate in a single physical domain may represent a single point of failure if that domain becomes compromised or experiences a denial of service.

## SC-33 Transmission Preparation Integrity (withdrawn) {#sc-33}

## SC-34 Non-modifiable Executable Programs {#sc-34}

**Statement.** For [system components] , load and execute:
- a. The operating environment from hardware-enforced, read-only media; and
- b. The following applications from hardware-enforced, read-only media: [applications].

**Guidance.** The operating environment for a system contains the code that hosts applications, including operating systems, executives, or virtual machine monitors (i.e., hypervisors). It can also include certain applications that run directly on hardware platforms. Hardware-enforced, read-only media include Compact Disc-Recordable (CD-R) and Digital Versatile Disc-Recordable (DVD-R) disk drives as well as one-time, programmable, read-only memory. The use of non-modifiable storage ensures the integrity of software from the point of creation of the read-only image. The use of reprogrammable, read-only memory can be accepted as read-only media provided that integrity can be adequately protected from the point of initial writing to the insertion of the memory into the system, and there are reliable hardware protections against reprogramming the memory while installed in organizational systems.

### SC-34(01) No Writable Storage {#sc-34.1}

**Statement.** Employ [system components] with no writeable storage that is persistent across component restart or power on/off.

**Guidance.** Disallowing writeable storage eliminates the possibility of malicious code insertion via persistent, writeable storage within the designated system components. The restriction applies to fixed and removable storage, with the latter being addressed either directly or as specific restrictions imposed through access controls for mobile devices.

### SC-34(02) Integrity Protection on Read-only Media {#sc-34.2}

**Statement.** Protect the integrity of information prior to storage on read-only media and control the media after such information has been recorded onto the media.

**Guidance.** Controls prevent the substitution of media into systems or the reprogramming of programmable read-only media prior to installation into the systems. Integrity protection controls include a combination of prevention, detection, and response.

### SC-34(03) Hardware-based Protection (withdrawn) {#sc-34.3}

## SC-35 External Malicious Code Identification {#sc-35}

**Statement.** Include system components that proactively seek to identify network-based malicious code or malicious websites.

**Guidance.** External malicious code identification differs from decoys in [SC-26](#sc-26) in that the components actively probe networks, including the Internet, in search of malicious code contained on external websites. Like decoys, the use of external malicious code identification techniques requires some supporting isolation measures to ensure that any malicious code discovered during the search and subsequently executed does not infect organizational systems. Virtualization is a common technique for achieving such isolation.

## SC-36 Distributed Processing and Storage {#sc-36}

**Statement.** Distribute the following processing and storage components across multiple [organization-defined value]: [organization-defined processing and storage components].

**Guidance.** Distributing processing and storage across multiple physical locations or logical domains provides a degree of redundancy or overlap for organizations. The redundancy and overlap increase the work factor of adversaries to adversely impact organizational operations, assets, and individuals. The use of distributed processing and storage does not assume a single primary processing or storage location. Therefore, it allows for parallel processing and storage.

### SC-36(01) Polling Techniques {#sc-36.1}

**Statement.** - (a) Employ polling techniques to identify potential faults, errors, or compromises to the following processing and storage components: [distributed processing and storage components] ; and
- (b) Take the following actions in response to identified faults, errors, or compromises: [actions].

**Guidance.** Distributed processing and/or storage may be used to reduce opportunities for adversaries to compromise the confidentiality, integrity, or availability of organizational information and systems. However, the distribution of processing and storage components does not prevent adversaries from compromising one or more of the components. Polling compares the processing results and/or storage content from the distributed components and subsequently votes on the outcomes. Polling identifies potential faults, compromises, or errors in the distributed processing and storage components.

### SC-36(02) Synchronization {#sc-36.2}

**Statement.** Synchronize the following duplicate systems or system components: [duplicate systems or system components].

**Guidance.** [SC-36](#sc-36) and [CP-9(6)](#cp-9.6) require the duplication of systems or system components in distributed locations. The synchronization of duplicated and redundant services and data helps to ensure that information contained in the distributed locations can be used in the mission or business functions of organizations, as needed.

## SC-37 Out-of-band Channels {#sc-37}

**Statement.** Employ the following out-of-band channels for the physical delivery or electronic transmission of [information, system components, or devices] to [individuals or systems]: [out-of-band channels].

**Guidance.** Out-of-band channels include local, non-network accesses to systems; network paths physically separate from network paths used for operational traffic; or non-electronic paths, such as the U.S. Postal Service. The use of out-of-band channels is contrasted with the use of in-band channels (i.e., the same channels) that carry routine operational traffic. Out-of-band channels do not have the same vulnerability or exposure as in-band channels. Therefore, the confidentiality, integrity, or availability compromises of in-band channels will not compromise or adversely affect the out-of-band channels. Organizations may employ out-of-band channels in the delivery or transmission of organizational items, including authenticators and credentials; cryptographic key management information; system and data backups; configuration management changes for hardware, firmware, or software; security updates; maintenance information; and malicious code protection updates. For example, cryptographic keys for encrypted files are delivered using a different channel than the file.

### SC-37(01) Ensure Delivery and Transmission {#sc-37.1}

**Statement.** Employ [controls] to ensure that only [individuals or systems] receive the following information, system components, or devices: [information, system components, or devices].

**Guidance.** Techniques employed by organizations to ensure that only designated systems or individuals receive certain information, system components, or devices include sending authenticators via an approved courier service but requiring recipients to show some form of government-issued photographic identification as a condition of receipt.

## SC-38 Operations Security {#sc-38}

**Statement.** Employ the following operations security controls to protect key organizational information throughout the system development life cycle: [operations security controls].

**Guidance.** Operations security (OPSEC) is a systematic process by which potential adversaries can be denied information about the capabilities and intentions of organizations by identifying, controlling, and protecting generally unclassified information that specifically relates to the planning and execution of sensitive organizational activities. The OPSEC process involves five steps: identification of critical information, analysis of threats, analysis of vulnerabilities, assessment of risks, and the application of appropriate countermeasures. OPSEC controls are applied to organizational systems and the environments in which those systems operate. OPSEC controls protect the confidentiality of information, including limiting the sharing of information with suppliers, potential suppliers, and other non-organizational elements and individuals. Information critical to organizational mission and business functions includes user identities, element uses, suppliers, supply chain processes, functional requirements, security requirements, system design specifications, testing and evaluation protocols, and security control implementation details.

## SC-39 Process Isolation {#sc-39}

**Statement.** Maintain a separate execution domain for each executing system process.

**Guidance.** Systems can maintain separate execution domains for each executing process by assigning each process a separate address space. Each system process has a distinct address space so that communication between processes is performed in a manner controlled through the security functions, and one process cannot modify the executing code of another process. Maintaining separate execution domains for executing processes can be achieved, for example, by implementing separate address spaces. Process isolation technologies, including sandboxing or virtualization, logically separate software and firmware from other software, firmware, and data. Process isolation helps limit the access of potentially untrusted software to other system resources. The capability to maintain separate execution domains is available in commercial operating systems that employ multi-state processor technologies.

### SC-39(01) Hardware Separation {#sc-39.1}

**Statement.** Implement hardware separation mechanisms to facilitate process isolation.

**Guidance.** Hardware-based separation of system processes is generally less susceptible to compromise than software-based separation, thus providing greater assurance that the separation will be enforced. Hardware separation mechanisms include hardware memory management.

### SC-39(02) Separate Execution Domain Per Thread {#sc-39.2}

**Statement.** Maintain a separate execution domain for each thread in [multi-threaded processing].

**Guidance.** None.

## SC-40 Wireless Link Protection {#sc-40}

**Statement.** Protect external and internal [organization-defined wireless links] from the following signal parameter attacks: [organization-defined types of signal parameter attacks or references to sources for such attacks].

**Guidance.** Wireless link protection applies to internal and external wireless communication links that may be visible to individuals who are not authorized system users. Adversaries can exploit the signal parameters of wireless links if such links are not adequately protected. There are many ways to exploit the signal parameters of wireless links to gain intelligence, deny service, or spoof system users. Protection of wireless links reduces the impact of attacks that are unique to wireless systems. If organizations rely on commercial service providers for transmission services as commodity items rather than as fully dedicated services, it may not be possible to implement wireless link protections to the extent necessary to meet organizational security requirements.

### SC-40(01) Electromagnetic Interference {#sc-40.1}

**Statement.** Implement cryptographic mechanisms that achieve [level of protection] against the effects of intentional electromagnetic interference.

**Guidance.** The implementation of cryptographic mechanisms for electromagnetic interference protects systems against intentional jamming that might deny or impair communications by ensuring that wireless spread spectrum waveforms used to provide anti-jam protection are not predictable by unauthorized individuals. The implementation of cryptographic mechanisms may also coincidentally mitigate the effects of unintentional jamming due to interference from legitimate transmitters that share the same spectrum. Mission requirements, projected threats, concept of operations, and laws, executive orders, directives, regulations, policies, and standards determine levels of wireless link availability, cryptography needed, and performance.

### SC-40(02) Reduce Detection Potential {#sc-40.2}

**Statement.** Implement cryptographic mechanisms to reduce the detection potential of wireless links to [level of reduction].

**Guidance.** The implementation of cryptographic mechanisms to reduce detection potential is used for covert communications and to protect wireless transmitters from geo-location. It also ensures that the spread spectrum waveforms used to achieve a low probability of detection are not predictable by unauthorized individuals. Mission requirements, projected threats, concept of operations, and applicable laws, executive orders, directives, regulations, policies, and standards determine the levels to which wireless links are undetectable.

### SC-40(03) Imitative or Manipulative Communications Deception {#sc-40.3}

**Statement.** Implement cryptographic mechanisms to identify and reject wireless transmissions that are deliberate attempts to achieve imitative or manipulative communications deception based on signal parameters.

**Guidance.** The implementation of cryptographic mechanisms to identify and reject imitative or manipulative communications ensures that the signal parameters of wireless transmissions are not predictable by unauthorized individuals. Such unpredictability reduces the probability of imitative or manipulative communications deception based on signal parameters alone.

### SC-40(04) Signal Parameter Identification {#sc-40.4}

**Statement.** Implement cryptographic mechanisms to prevent the identification of [wireless transmitters] by using the transmitter signal parameters.

**Guidance.** The implementation of cryptographic mechanisms to prevent the identification of wireless transmitters protects against the unique identification of wireless transmitters for the purposes of intelligence exploitation by ensuring that anti-fingerprinting alterations to signal parameters are not predictable by unauthorized individuals. It also provides anonymity when required. Radio fingerprinting techniques identify the unique signal parameters of transmitters to fingerprint such transmitters for purposes of tracking and mission or user identification.

## SC-41 Port and I/O Device Access {#sc-41}

**Statement.** [organization-defined value] disable or remove [connection ports or input/output devices] on the following systems or system components: [systems or system components].

**Guidance.** Connection ports include Universal Serial Bus (USB), Thunderbolt, and Firewire (IEEE 1394). Input/output (I/O) devices include compact disc and digital versatile disc drives. Disabling or removing such connection ports and I/O devices helps prevent the exfiltration of information from systems and the introduction of malicious code from those ports or devices. Physically disabling or removing ports and/or devices is the stronger action.

## SC-42 Sensor Capability and Data {#sc-42}

**Statement.** - a. Prohibit [organization-defined value] ; and
- b. Provide an explicit indication of sensor use to [group of users].

**Guidance.** Sensor capability and data applies to types of systems or system components characterized as mobile devices, such as cellular telephones, smart phones, and tablets. Mobile devices often include sensors that can collect and record data regarding the environment where the system is in use. Sensors that are embedded within mobile devices include microphones, cameras, Global Positioning System (GPS) mechanisms, and accelerometers. While the sensors on mobiles devices provide an important function, if activated covertly, such devices can potentially provide a means for adversaries to learn valuable information about individuals and organizations. For example, remotely activating the GPS function on a mobile device could provide an adversary with the ability to track the movements of an individual. Organizations may prohibit individuals from bringing cellular telephones or digital cameras into certain designated facilities or controlled areas within facilities where classified information is stored or sensitive conversations are taking place.

### SC-42(01) Reporting to Authorized Individuals or Roles {#sc-42.1}

**Statement.** Verify that the system is configured so that data or information collected by the [sensors] is only reported to authorized individuals or roles.

**Guidance.** In situations where sensors are activated by authorized individuals, it is still possible that the data or information collected by the sensors will be sent to unauthorized entities.

### SC-42(02) Authorized Use {#sc-42.2}

**Statement.** Employ the following measures so that data or information collected by [sc-42.01_odp] is only used for authorized purposes: [measures].

**Guidance.** Information collected by sensors for a specific authorized purpose could be misused for some unauthorized purpose. For example, GPS sensors that are used to support traffic navigation could be misused to track the movements of individuals. Measures to mitigate such activities include additional training to help ensure that authorized individuals do not abuse their authority and, in the case where sensor data is maintained by external parties, contractual restrictions on the use of such data.

### SC-42(03) Prohibit Use of Devices (withdrawn) {#sc-42.3}

### SC-42(04) Notice of Collection {#sc-42.4}

**Statement.** Employ the following measures to facilitate an individual’s awareness that personally identifiable information is being collected by [sensors]: [measures].

**Guidance.** Awareness that organizational sensors are collecting data enables individuals to more effectively engage in managing their privacy. Measures can include conventional written notices and sensor configurations that make individuals directly or indirectly aware through other devices that the sensor is collecting information. The usability and efficacy of the notice are important considerations.

### SC-42(05) Collection Minimization {#sc-42.5}

**Statement.** Employ [sensors] that are configured to minimize the collection of information about individuals that is not needed.

**Guidance.** Although policies to control for authorized use can be applied to information once it is collected, minimizing the collection of information that is not needed mitigates privacy risk at the system entry point and mitigates the risk of policy control failures. Sensor configurations include the obscuring of human features, such as blurring or pixelating flesh tones.

## SC-43 Usage Restrictions {#sc-43}

**Statement.** - a. Establish usage restrictions and implementation guidelines for the following system components: [components] ; and
- b. Authorize, monitor, and control the use of such components within the system.

**Guidance.** Usage restrictions apply to all system components including but not limited to mobile code, mobile devices, wireless access, and wired and wireless peripheral components (e.g., copiers, printers, scanners, optical devices, and other similar technologies). The usage restrictions and implementation guidelines are based on the potential for system components to cause damage to the system and help to ensure that only authorized system use occurs.

## SC-44 Detonation Chambers {#sc-44}

**Statement.** Employ a detonation chamber capability within [system, system component, or location].

**Guidance.** Detonation chambers, also known as dynamic execution environments, allow organizations to open email attachments, execute untrusted or suspicious applications, and execute Universal Resource Locator requests in the safety of an isolated environment or a virtualized sandbox. Protected and isolated execution environments provide a means of determining whether the associated attachments or applications contain malicious code. While related to the concept of deception nets, the employment of detonation chambers is not intended to maintain a long-term environment in which adversaries can operate and their actions can be observed. Rather, detonation chambers are intended to quickly identify malicious code and either reduce the likelihood that the code is propagated to user environments of operation or prevent such propagation completely.

## SC-45 System Time Synchronization {#sc-45}

**Statement.** Synchronize system clocks within and between systems and system components.

**Guidance.** Time synchronization of system clocks is essential for the correct execution of many system services, including identification and authentication processes that involve certificates and time-of-day restrictions as part of access control. Denial of service or failure to deny expired credentials may result without properly synchronized clocks within and between systems and system components. Time is commonly expressed in Coordinated Universal Time (UTC), a modern continuation of Greenwich Mean Time (GMT), or local time with an offset from UTC. The granularity of time measurements refers to the degree of synchronization between system clocks and reference clocks, such as clocks synchronizing within hundreds of milliseconds or tens of milliseconds. Organizations may define different time granularities for system components. Time service can be critical to other security capabilities—such as access control and identification and authentication—depending on the nature of the mechanisms used to support the capabilities.

### SC-45(01) Synchronization with Authoritative Time Source {#sc-45.1}

**Statement.** - (a) Compare the internal system clocks [frequency] with [authoritative time source] ; and
- (b) Synchronize the internal system clocks to the authoritative time source when the time difference is greater than [time period].

**Guidance.** Synchronization of internal system clocks with an authoritative source provides uniformity of time stamps for systems with multiple system clocks and systems connected over a network.

### SC-45(02) Secondary Authoritative Time Source {#sc-45.2}

**Statement.** - (a) Identify a secondary authoritative time source that is in a different geographic region than the primary authoritative time source; and
- (b) Synchronize the internal system clocks to the secondary authoritative time source if the primary authoritative time source is unavailable.

**Guidance.** It may be necessary to employ geolocation information to determine that the secondary authoritative time source is in a different geographic region.

## SC-46 Cross Domain Policy Enforcement {#sc-46}

**Statement.** Implement a policy enforcement mechanism [organization-defined value] between the physical and/or network interfaces for the connecting security domains.

**Guidance.** For logical policy enforcement mechanisms, organizations avoid creating a logical path between interfaces to prevent the ability to bypass the policy enforcement mechanism. For physical policy enforcement mechanisms, the robustness of physical isolation afforded by the physical implementation of policy enforcement to preclude the presence of logical covert channels penetrating the security domain may be needed. Contact [ncdsmo@nsa.gov](mailto:ncdsmo@nsa.gov) for more information.

## SC-47 Alternate Communications Paths {#sc-47}

**Statement.** Establish [alternate communication paths] for system operations organizational command and control.

**Guidance.** An incident, whether adversarial- or nonadversarial-based, can disrupt established communications paths used for system operations and organizational command and control. Alternate communications paths reduce the risk of all communications paths being affected by the same incident. To compound the problem, the inability of organizational officials to obtain timely information about disruptions or to provide timely direction to operational elements after a communications path incident, can impact the ability of the organization to respond to such incidents in a timely manner. Establishing alternate communications paths for command and control purposes, including designating alternative decision makers if primary decision makers are unavailable and establishing the extent and limitations of their actions, can greatly facilitate the organization’s ability to continue to operate and take appropriate actions during an incident.

## SC-48 Sensor Relocation {#sc-48}

**Statement.** Relocate [sensors and monitoring capabilities] to [locations] under the following conditions or circumstances: [conditions or circumstances].

**Guidance.** Adversaries may take various paths and use different approaches as they move laterally through an organization (including its systems) to reach their target or as they attempt to exfiltrate information from the organization. The organization often only has a limited set of monitoring and detection capabilities, and they may be focused on the critical or likely infiltration or exfiltration paths. By using communications paths that the organization typically does not monitor, the adversary can increase its chances of achieving its desired goals. By relocating its sensors or monitoring capabilities to new locations, the organization can impede the adversary’s ability to achieve its goals. The relocation of the sensors or monitoring capabilities might be done based on threat information that the organization has acquired or randomly to confuse the adversary and make its lateral transition through the system or organization more challenging.

### SC-48(01) Dynamic Relocation of Sensors or Monitoring Capabilities {#sc-48.1}

**Statement.** Dynamically relocate [sensors and monitoring capabilities] to [locations] under the following conditions or circumstances: [conditions or circumstances].

**Guidance.** None.

## SC-49 Hardware-enforced Separation and Policy Enforcement {#sc-49}

**Statement.** Implement hardware-enforced separation and policy enforcement mechanisms between [security domains].

**Guidance.** System owners may require additional strength of mechanism and robustness to ensure domain separation and policy enforcement for specific types of threats and environments of operation. Hardware-enforced separation and policy enforcement provide greater strength of mechanism than software-enforced separation and policy enforcement.

## SC-50 Software-enforced Separation and Policy Enforcement {#sc-50}

**Statement.** Implement software-enforced separation and policy enforcement mechanisms between [security domains].

**Guidance.** System owners may require additional strength of mechanism to ensure domain separation and policy enforcement for specific types of threats and environments of operation.

## SC-51 Hardware-based Protection {#sc-51}

**Statement.** - a. Employ hardware-based, write-protect for [system firmware components] ; and
- b. Implement specific procedures for [authorized individuals] to manually disable hardware write-protect for firmware modifications and re-enable the write-protect prior to returning to operational mode.

**Guidance.** None.
