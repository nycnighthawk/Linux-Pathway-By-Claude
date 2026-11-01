# CM — Configuration Management

## CM-01 Policy and Procedures {#cm-1}

**Statement.** - a. Develop, document, and disseminate to [organization-defined personnel or roles]:
  - 1. [organization-defined value] configuration management policy that:
    - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
    - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
  - 2. Procedures to facilitate the implementation of the configuration management policy and the associated configuration management controls;
- b. Designate an [official] to manage the development, documentation, and dissemination of the configuration management policy and procedures; and
- c. Review and update the current configuration management:
  - 1. Policy [frequency] and following [events] ; and
  - 2. Procedures [frequency] and following [events].

**Guidance.** Configuration management policy and procedures address the controls in the CM family that are implemented within systems and organizations. The risk management strategy is an important factor in establishing such policies and procedures. Policies and procedures contribute to security and privacy assurance. Therefore, it is important that security and privacy programs collaborate on the development of configuration management policy and procedures. Security and privacy program policies and procedures at the organization level are preferable, in general, and may obviate the need for mission- or system-specific policies and procedures. The policy can be included as part of the general security and privacy policy or be represented by multiple policies that reflect the complex nature of organizations. Procedures can be established for security and privacy programs, for mission/business processes, and for systems, if needed. Procedures describe how the policies or controls are implemented and can be directed at the individual or role that is the object of the procedure. Procedures can be documented in system security and privacy plans or in one or more separate documents. Events that may precipitate an update to configuration management policy and procedures include, but are not limited to, assessment or audit findings, security incidents or breaches, or changes in applicable laws, executive orders, directives, regulations, policies, standards, and guidelines. Simply restating controls does not constitute an organizational policy or procedure.

## CM-02 Baseline Configuration {#cm-2}

**Statement.** - a. Develop, document, and maintain under configuration control, a current baseline configuration of the system; and
- b. Review and update the baseline configuration of the system:
  - 1. [frequency];
  - 2. When required due to [circumstances] ; and
  - 3. When system components are installed or upgraded.

**Guidance.** Baseline configurations for systems and system components include connectivity, operational, and communications aspects of systems. Baseline configurations are documented, formally reviewed, and agreed-upon specifications for systems or configuration items within those systems. Baseline configurations serve as a basis for future builds, releases, or changes to systems and include security and privacy control implementations, operational procedures, information about system components, network topology, and logical placement of components in the system architecture. Maintaining baseline configurations requires creating new baselines as organizational systems change over time. Baseline configurations of systems reflect the current enterprise architecture.

### CM-02(01) Reviews and Updates (withdrawn) {#cm-2.1}

### CM-02(02) Automation Support for Accuracy and Currency {#cm-2.2}

**Statement.** Maintain the currency, completeness, accuracy, and availability of the baseline configuration of the system using [automated mechanisms].

**Guidance.** Automated mechanisms that help organizations maintain consistent baseline configurations for systems include configuration management tools, hardware, software, firmware inventory tools, and network management tools. Automated tools can be used at the organization level, mission and business process level, or system level on workstations, servers, notebook computers, network components, or mobile devices. Tools can be used to track version numbers on operating systems, applications, types of software installed, and current patch levels. Automation support for accuracy and currency can be satisfied by the implementation of [CM-8(2)](#cm-8.2) for organizations that combine system component inventory and baseline configuration activities.

### CM-02(03) Retention of Previous Configurations {#cm-2.3}

**Statement.** Retain [number] of previous versions of baseline configurations of the system to support rollback.

**Guidance.** Retaining previous versions of baseline configurations to support rollback include hardware, software, firmware, configuration files, configuration records, and associated documentation.

### CM-02(04) Unauthorized Software (withdrawn) {#cm-2.4}

### CM-02(05) Authorized Software (withdrawn) {#cm-2.5}

### CM-02(06) Development and Test Environments {#cm-2.6}

**Statement.** Maintain a baseline configuration for system development and test environments that is managed separately from the operational baseline configuration.

**Guidance.** Establishing separate baseline configurations for development, testing, and operational environments protects systems from unplanned or unexpected events related to development and testing activities. Separate baseline configurations allow organizations to apply the configuration management that is most appropriate for each type of configuration. For example, the management of operational configurations typically emphasizes the need for stability, while the management of development or test configurations requires greater flexibility. Configurations in the test environment mirror configurations in the operational environment to the extent practicable so that the results of the testing are representative of the proposed changes to the operational systems. Separate baseline configurations do not necessarily require separate physical environments.

### CM-02(07) Configure Systems and Components for High-risk Areas {#cm-2.7}

**Statement.** - (a) Issue [systems or system components] with [configurations] to individuals traveling to locations that the organization deems to be of significant risk; and
- (b) Apply the following controls to the systems or components when the individuals return from travel: [controls].

**Guidance.** When it is known that systems or system components will be in high-risk areas external to the organization, additional controls may be implemented to counter the increased threat in such areas. For example, organizations can take actions for notebook computers used by individuals departing on and returning from travel. Actions include determining the locations that are of concern, defining the required configurations for the components, ensuring that components are configured as intended before travel is initiated, and applying controls to the components after travel is completed. Specially configured notebook computers include computers with sanitized hard drives, limited applications, and more stringent configuration settings. Controls applied to mobile devices upon return from travel include examining the mobile device for signs of physical tampering and purging and reimaging disk drives. Protecting information that resides on mobile devices is addressed in the [MP](#mp) (Media Protection) family.

## CM-03 Configuration Change Control {#cm-3}

**Statement.** - a. Determine and document the types of changes to the system that are configuration-controlled;
- b. Review proposed configuration-controlled changes to the system and approve or disapprove such changes with explicit consideration for security and privacy impact analyses;
- c. Document configuration change decisions associated with the system;
- d. Implement approved configuration-controlled changes to the system;
- e. Retain records of configuration-controlled changes to the system for [time period];
- f. Monitor and review activities associated with configuration-controlled changes to the system; and
- g. Coordinate and provide oversight for configuration change control activities through [configuration change control element] that convenes [organization-defined value].

**Guidance.** Configuration change control for organizational systems involves the systematic proposal, justification, implementation, testing, review, and disposition of system changes, including system upgrades and modifications. Configuration change control includes changes to baseline configurations, configuration items of systems, operational procedures, configuration settings for system components, remediate vulnerabilities, and unscheduled or unauthorized changes. Processes for managing configuration changes to systems include Configuration Control Boards or Change Advisory Boards that review and approve proposed changes. For changes that impact privacy risk, the senior agency official for privacy updates privacy impact assessments and system of records notices. For new systems or major upgrades, organizations consider including representatives from the development organizations on the Configuration Control Boards or Change Advisory Boards. Auditing of changes includes activities before and after changes are made to systems and the auditing activities required to implement such changes. See also [SA-10](#sa-10).

### CM-03(01) Automated Documentation, Notification, and Prohibition of Changes {#cm-3.1}

**Statement.** Use [automated mechanisms] to:
- (a) Document proposed changes to the system;
- (b) Notify [approval authorities] of proposed changes to the system and request change approval;
- (c) Highlight proposed changes to the system that have not been approved or disapproved within [time period];
- (d) Prohibit changes to the system until designated approvals are received;
- (e) Document all changes to the system; and
- (f) Notify [personnel] when approved changes to the system are completed.

**Guidance.** None.

### CM-03(02) Testing, Validation, and Documentation of Changes {#cm-3.2}

**Statement.** Test, validate, and document changes to the system before finalizing the implementation of the changes.

**Guidance.** Changes to systems include modifications to hardware, software, or firmware components and configuration settings defined in [CM-6](#cm-6) . Organizations ensure that testing does not interfere with system operations that support organizational mission and business functions. Individuals or groups conducting tests understand security and privacy policies and procedures, system security and privacy policies and procedures, and the health, safety, and environmental risks associated with specific facilities or processes. Operational systems may need to be taken offline, or replicated to the extent feasible, before testing can be conducted. If systems must be taken offline for testing, the tests are scheduled to occur during planned system outages whenever possible. If the testing cannot be conducted on operational systems, organizations employ compensating controls.

### CM-03(03) Automated Change Implementation {#cm-3.3}

**Statement.** Implement changes to the current system baseline and deploy the updated baseline across the installed base using [automated mechanisms].

**Guidance.** Automated tools can improve the accuracy, consistency, and availability of configuration baseline information. Automation can also provide data aggregation and data correlation capabilities, alerting mechanisms, and dashboards to support risk-based decision-making within the organization.

### CM-03(04) Security and Privacy Representatives {#cm-3.4}

**Statement.** Require [organization-defined security and privacy representatives] to be members of the [configuration change control element].

**Guidance.** Information security and privacy representatives include system security officers, senior agency information security officers, senior agency officials for privacy, or system privacy officers. Representation by personnel with information security and privacy expertise is important because changes to system configurations can have unintended side effects, some of which may be security- or privacy-relevant. Detecting such changes early in the process can help avoid unintended, negative consequences that could ultimately affect the security and privacy posture of systems. The configuration change control element referred to in the second organization-defined parameter reflects the change control elements defined by organizations in [CM-3g](#cm-3_smt.g).

### CM-03(05) Automated Security Response {#cm-3.5}

**Statement.** Implement the following security responses automatically if baseline configurations are changed in an unauthorized manner: [security responses].

**Guidance.** Automated security responses include halting selected system functions, halting system processing, and issuing alerts or notifications to organizational personnel when there is an unauthorized modification of a configuration item.

### CM-03(06) Cryptography Management {#cm-3.6}

**Statement.** Ensure that cryptographic mechanisms used to provide the following controls are under configuration management: [controls].

**Guidance.** The controls referenced in the control enhancement refer to security and privacy controls from the control catalog. Regardless of the cryptographic mechanisms employed, processes and procedures are in place to manage those mechanisms. For example, if system components use certificates for identification and authentication, a process is implemented to address the expiration of those certificates.

### CM-03(07) Review System Changes {#cm-3.7}

**Statement.** Review changes to the system [frequency] or when [circumstances] to determine whether unauthorized changes have occurred.

**Guidance.** Indications that warrant a review of changes to the system and the specific circumstances justifying such reviews may be obtained from activities carried out by organizations during the configuration change process or continuous monitoring process.

### CM-03(08) Prevent or Restrict Configuration Changes {#cm-3.8}

**Statement.** Prevent or restrict changes to the configuration of the system under the following circumstances: [circumstances].

**Guidance.** System configuration changes can adversely affect critical system security and privacy functionality. Change restrictions can be enforced through automated mechanisms.

## CM-04 Impact Analyses {#cm-4}

**Statement.** Analyze changes to the system to determine potential security and privacy impacts prior to change implementation.

**Guidance.** Organizational personnel with security or privacy responsibilities conduct impact analyses. Individuals conducting impact analyses possess the necessary skills and technical expertise to analyze the changes to systems as well as the security or privacy ramifications. Impact analyses include reviewing security and privacy plans, policies, and procedures to understand control requirements; reviewing system design documentation and operational procedures to understand control implementation and how specific system changes might affect the controls; reviewing the impact of changes on organizational supply chain partners with stakeholders; and determining how potential changes to a system create new risks to the privacy of individuals and the ability of implemented controls to mitigate those risks. Impact analyses also include risk assessments to understand the impact of the changes and determine if additional controls are required.

### CM-04(01) Separate Test Environments {#cm-4.1}

**Statement.** Analyze changes to the system in a separate test environment before implementation in an operational environment, looking for security and privacy impacts due to flaws, weaknesses, incompatibility, or intentional malice.

**Guidance.** A separate test environment requires an environment that is physically or logically separate and distinct from the operational environment. The separation is sufficient to ensure that activities in the test environment do not impact activities in the operational environment and that information in the operational environment is not inadvertently transmitted to the test environment. Separate environments can be achieved by physical or logical means. If physically separate test environments are not implemented, organizations determine the strength of mechanism required when implementing logical separation.

### CM-04(02) Verification of Controls {#cm-4.2}

**Statement.** After system changes, verify that the impacted controls are implemented correctly, operating as intended, and producing the desired outcome with regard to meeting the security and privacy requirements for the system.

**Guidance.** Implementation in this context refers to installing changed code in the operational system that may have an impact on security or privacy controls.

## CM-05 Access Restrictions for Change {#cm-5}

**Statement.** Define, document, approve, and enforce physical and logical access restrictions associated with changes to the system.

**Guidance.** Changes to the hardware, software, or firmware components of systems or the operational procedures related to the system can potentially have significant effects on the security of the systems or individuals’ privacy. Therefore, organizations permit only qualified and authorized individuals to access systems for purposes of initiating changes. Access restrictions include physical and logical access controls (see [AC-3](#ac-3) and [PE-3](#pe-3) ), software libraries, workflow automation, media libraries, abstract layers (i.e., changes implemented into external interfaces rather than directly into systems), and change windows (i.e., changes occur only during specified times).

### CM-05(01) Automated Access Enforcement and Audit Records {#cm-5.1}

**Statement.** - (a) Enforce access restrictions using [automated mechanisms] ; and
- (b) Automatically generate audit records of the enforcement actions.

**Guidance.** Organizations log system accesses associated with applying configuration changes to ensure that configuration change control is implemented and to support after-the-fact actions should organizations discover any unauthorized changes.

### CM-05(02) Review System Changes (withdrawn) {#cm-5.2}

### CM-05(03) Signed Components (withdrawn) {#cm-5.3}

### CM-05(04) Dual Authorization {#cm-5.4}

**Statement.** Enforce dual authorization for implementing changes to [organization-defined system components and system-level information].

**Guidance.** Organizations employ dual authorization to help ensure that any changes to selected system components and information cannot occur unless two qualified individuals approve and implement such changes. The two individuals possess the skills and expertise to determine if the proposed changes are correct implementations of approved changes. The individuals are also accountable for the changes. Dual authorization may also be known as two-person control. To reduce the risk of collusion, organizations consider rotating dual authorization duties to other individuals. System-level information includes operational procedures.

### CM-05(05) Privilege Limitation for Production and Operation {#cm-5.5}

**Statement.** - (a) Limit privileges to change system components and system-related information within a production or operational environment; and
- (b) Review and reevaluate privileges [organization-defined frequency].

**Guidance.** In many organizations, systems support multiple mission and business functions. Limiting privileges to change system components with respect to operational systems is necessary because changes to a system component may have far-reaching effects on mission and business processes supported by the system. The relationships between systems and mission/business processes are, in some cases, unknown to developers. System-related information includes operational procedures.

### CM-05(06) Limit Library Privileges {#cm-5.6}

**Statement.** Limit privileges to change software resident within software libraries.

**Guidance.** Software libraries include privileged programs.

### CM-05(07) Automatic Implementation of Security Safeguards (withdrawn) {#cm-5.7}

## CM-06 Configuration Settings {#cm-6}

**Statement.** - a. Establish and document configuration settings for components employed within the system that reflect the most restrictive mode consistent with operational requirements using [common secure configurations];
- b. Implement the configuration settings;
- c. Identify, document, and approve any deviations from established configuration settings for [system components] based on [operational requirements] ; and
- d. Monitor and control changes to the configuration settings in accordance with organizational policies and procedures.

**Guidance.** Configuration settings are the parameters that can be changed in the hardware, software, or firmware components of the system that affect the security and privacy posture or functionality of the system. Information technology products for which configuration settings can be defined include mainframe computers, servers, workstations, operating systems, mobile devices, input/output devices, protocols, and applications. Parameters that impact the security posture of systems include registry settings; account, file, or directory permission settings; and settings for functions, protocols, ports, services, and remote connections. Privacy parameters are parameters impacting the privacy posture of systems, including the parameters required to satisfy other privacy controls. Privacy parameters include settings for access controls, data processing preferences, and processing and retention permissions. Organizations establish organization-wide configuration settings and subsequently derive specific configuration settings for systems. The established settings become part of the configuration baseline for the system.

Common secure configurations (also known as security configuration checklists, lockdown and hardening guides, and security reference guides) provide recognized, standardized, and established benchmarks that stipulate secure configuration settings for information technology products and platforms as well as instructions for configuring those products or platforms to meet operational requirements. Common secure configurations can be developed by a variety of organizations, including information technology product developers, manufacturers, vendors, federal agencies, consortia, academia, industry, and other organizations in the public and private sectors.

Implementation of a common secure configuration may be mandated at the organization level, mission and business process level, system level, or at a higher level, including by a regulatory agency. Common secure configurations include the United States Government Configuration Baseline [USGCB](#98498928-3ca3-44b3-8b1e-f48685373087) and security technical implementation guides (STIGs), which affect the implementation of [CM-6](#cm-6) and other controls such as [AC-19](#ac-19) and [CM-7](#cm-7) . The Security Content Automation Protocol (SCAP) and the defined standards within the protocol provide an effective method to uniquely identify, track, and control configuration settings.

### CM-06(01) Automated Management, Application, and Verification {#cm-6.1}

**Statement.** Manage, apply, and verify configuration settings for [system components] using [organization-defined automated mechanisms].

**Guidance.** Automated tools (e.g., hardening tools, baseline configuration tools) can improve the accuracy, consistency, and availability of configuration settings information. Automation can also provide data aggregation and data correlation capabilities, alerting mechanisms, and dashboards to support risk-based decision-making within the organization.

### CM-06(02) Respond to Unauthorized Changes {#cm-6.2}

**Statement.** Take the following actions in response to unauthorized changes to [configuration settings]: [actions].

**Guidance.** Responses to unauthorized changes to configuration settings include alerting designated organizational personnel, restoring established configuration settings, or—in extreme cases—halting affected system processing.

### CM-06(03) Unauthorized Change Detection (withdrawn) {#cm-6.3}

### CM-06(04) Conformance Demonstration (withdrawn) {#cm-6.4}

## CM-07 Least Functionality {#cm-7}

**Statement.** - a. Configure the system to provide only [mission-essential capabilities] ; and
- b. Prohibit or restrict the use of the following functions, ports, protocols, software, and/or services: [organization-defined prohibited or restricted functions, system ports, protocols, software, and/or services].

**Guidance.** Systems provide a wide variety of functions and services. Some of the functions and services routinely provided by default may not be necessary to support essential organizational missions, functions, or operations. Additionally, it is sometimes convenient to provide multiple services from a single system component, but doing so increases risk over limiting the services provided by that single component. Where feasible, organizations limit component functionality to a single function per component. Organizations consider removing unused or unnecessary software and disabling unused or unnecessary physical and logical ports and protocols to prevent unauthorized connection of components, transfer of information, and tunneling. Organizations employ network scanning tools, intrusion detection and prevention systems, and end-point protection technologies, such as firewalls and host-based intrusion detection systems, to identify and prevent the use of prohibited functions, protocols, ports, and services. Least functionality can also be achieved as part of the fundamental design and development of the system (see [SA-8](#sa-8), [SC-2](#sc-2) , and [SC-3](#sc-3)).

### CM-07(01) Periodic Review {#cm-7.1}

**Statement.** - (a) Review the system [frequency] to identify unnecessary and/or nonsecure functions, ports, protocols, software, and services; and
- (b) Disable or remove [organization-defined functions, ports, protocols, software, and services within the system deemed to be unnecessary and/or nonsecure].

**Guidance.** Organizations review functions, ports, protocols, and services provided by systems or system components to determine the functions and services that are candidates for elimination. Such reviews are especially important during transition periods from older technologies to newer technologies (e.g., transition from IPv4 to IPv6). These technology transitions may require implementing the older and newer technologies simultaneously during the transition period and returning to minimum essential functions, ports, protocols, and services at the earliest opportunity. Organizations can either decide the relative security of the function, port, protocol, and/or service or base the security decision on the assessment of other entities. Unsecure protocols include Bluetooth, FTP, and peer-to-peer networking.

### CM-07(02) Prevent Program Execution {#cm-7.2}

**Statement.** Prevent program execution in accordance with [organization-defined value].

**Guidance.** Prevention of program execution addresses organizational policies, rules of behavior, and/or access agreements that restrict software usage and the terms and conditions imposed by the developer or manufacturer, including software licensing and copyrights. Restrictions include prohibiting auto-execute features, restricting roles allowed to approve program execution, permitting or prohibiting specific software programs, or restricting the number of program instances executed at the same time.

### CM-07(03) Registration Compliance {#cm-7.3}

**Statement.** Ensure compliance with [registration requirements].

**Guidance.** Organizations use the registration process to manage, track, and provide oversight for systems and implemented functions, ports, protocols, and services.

### CM-07(04) Unauthorized Software — Deny-by-exception {#cm-7.4}

**Statement.** - (a) Identify [software programs];
- (b) Employ an allow-all, deny-by-exception policy to prohibit the execution of unauthorized software programs on the system; and
- (c) Review and update the list of unauthorized software programs [frequency].

**Guidance.** Unauthorized software programs can be limited to specific versions or from a specific source. The concept of prohibiting the execution of unauthorized software may also be applied to user actions, system ports and protocols, IP addresses/ranges, websites, and MAC addresses.

### CM-07(05) Authorized Software — Allow-by-exception {#cm-7.5}

**Statement.** - (a) Identify [software programs];
- (b) Employ a deny-all, permit-by-exception policy to allow the execution of authorized software programs on the system; and
- (c) Review and update the list of authorized software programs [frequency].

**Guidance.** Authorized software programs can be limited to specific versions or from a specific source. To facilitate a comprehensive authorized software process and increase the strength of protection for attacks that bypass application level authorized software, software programs may be decomposed into and monitored at different levels of detail. These levels include applications, application programming interfaces, application modules, scripts, system processes, system services, kernel functions, registries, drivers, and dynamic link libraries. The concept of permitting the execution of authorized software may also be applied to user actions, system ports and protocols, IP addresses/ranges, websites, and MAC addresses. Organizations consider verifying the integrity of authorized software programs using digital signatures, cryptographic checksums, or hash functions. Verification of authorized software can occur either prior to execution or at system startup. The identification of authorized URLs for websites is addressed in [CA-3(5)](#ca-3.5) and [SC-7](#sc-7).

### CM-07(06) Confined Environments with Limited Privileges {#cm-7.6}

**Statement.** Require that the following user-installed software execute in a confined physical or virtual machine environment with limited privileges: [user-installed software].

**Guidance.** Organizations identify software that may be of concern regarding its origin or potential for containing malicious code. For this type of software, user installations occur in confined environments of operation to limit or contain damage from malicious code that may be executed.

### CM-07(07) Code Execution in Protected Environments {#cm-7.7}

**Statement.** Allow execution of binary or machine-executable code only in confined physical or virtual machine environments and with the explicit approval of [personnel or roles] when such code is:
- (a) Obtained from sources with limited or no warranty; and/or
- (b) Without the provision of source code.

**Guidance.** Code execution in protected environments applies to all sources of binary or machine-executable code, including commercial software and firmware and open-source software.

### CM-07(08) Binary or Machine Executable Code {#cm-7.8}

**Statement.** - (a) Prohibit the use of binary or machine-executable code from sources with limited or no warranty or without the provision of source code; and
- (b) Allow exceptions only for compelling mission or operational requirements and with the approval of the authorizing official.

**Guidance.** Binary or machine executable code applies to all sources of binary or machine-executable code, including commercial software and firmware and open-source software. Organizations assess software products without accompanying source code or from sources with limited or no warranty for potential security impacts. The assessments address the fact that software products without the provision of source code may be difficult to review, repair, or extend. In addition, there may be no owners to make such repairs on behalf of organizations. If open-source software is used, the assessments address the fact that there is no warranty, the open-source software could contain back doors or malware, and there may be no support available.

### CM-07(09) Prohibiting The Use of Unauthorized Hardware {#cm-7.9}

**Statement.** - (a) Identify [hardware components];
- (b) Prohibit the use or connection of unauthorized hardware components;
- (c) Review and update the list of authorized hardware components [frequency].

**Guidance.** Hardware components provide the foundation for organizational systems and the platform for the execution of authorized software programs. Managing the inventory of hardware components and controlling which hardware components are permitted to be installed or connected to organizational systems is essential in order to provide adequate security.

## CM-08 System Component Inventory {#cm-8}

**Statement.** - a. Develop and document an inventory of system components that:
  - 1. Accurately reflects the system;
  - 2. Includes all components within the system;
  - 3. Does not include duplicate accounting of components or components assigned to any other system;
  - 4. Is at the level of granularity deemed necessary for tracking and reporting; and
  - 5. Includes the following information to achieve system component accountability: [information] ; and
- b. Review and update the system component inventory [frequency].

**Guidance.** System components are discrete, identifiable information technology assets that include hardware, software, and firmware. Organizations may choose to implement centralized system component inventories that include components from all organizational systems. In such situations, organizations ensure that the inventories include system-specific information required for component accountability. The information necessary for effective accountability of system components includes the system name, software owners, software version numbers, hardware inventory specifications, software license information, and for networked components, the machine names and network addresses across all implemented protocols (e.g., IPv4, IPv6). Inventory specifications include date of receipt, cost, model, serial number, manufacturer, supplier information, component type, and physical location.

Preventing duplicate accounting of system components addresses the lack of accountability that occurs when component ownership and system association is not known, especially in large or complex connected systems. Effective prevention of duplicate accounting of system components necessitates use of a unique identifier for each component. For software inventory, centrally managed software that is accessed via other systems is addressed as a component of the system on which it is installed and managed. Software installed on multiple organizational systems and managed at the system level is addressed for each individual system and may appear more than once in a centralized component inventory, necessitating a system association for each software instance in the centralized inventory to avoid duplicate accounting of components. Scanning systems implementing multiple network protocols (e.g., IPv4 and IPv6) can result in duplicate components being identified in different address spaces. The implementation of [CM-8(7)](#cm-8.7) can help to eliminate duplicate accounting of components.

### CM-08(01) Updates During Installation and Removal {#cm-8.1}

**Statement.** Update the inventory of system components as part of component installations, removals, and system updates.

**Guidance.** Organizations can improve the accuracy, completeness, and consistency of system component inventories if the inventories are updated as part of component installations or removals or during general system updates. If inventories are not updated at these key times, there is a greater likelihood that the information will not be appropriately captured and documented. System updates include hardware, software, and firmware components.

### CM-08(02) Automated Maintenance {#cm-8.2}

**Statement.** Maintain the currency, completeness, accuracy, and availability of the inventory of system components using [organization-defined automated mechanisms].

**Guidance.** Organizations maintain system inventories to the extent feasible. For example, virtual machines can be difficult to monitor because such machines are not visible to the network when not in use. In such cases, organizations maintain as up-to-date, complete, and accurate an inventory as is deemed reasonable. Automated maintenance can be achieved by the implementation of [CM-2(2)](#cm-2.2) for organizations that combine system component inventory and baseline configuration activities.

### CM-08(03) Automated Unauthorized Component Detection {#cm-8.3}

**Statement.** - (a) Detect the presence of unauthorized hardware, software, and firmware components within the system using [organization-defined automated mechanisms] [frequency] ; and
- (b) Take the following actions when unauthorized components are detected: [organization-defined value].

**Guidance.** Automated unauthorized component detection is applied in addition to the monitoring for unauthorized remote connections and mobile devices. Monitoring for unauthorized system components may be accomplished on an ongoing basis or by the periodic scanning of systems for that purpose. Automated mechanisms may also be used to prevent the connection of unauthorized components (see [CM-7(9)](#cm-7.9) ). Automated mechanisms can be implemented in systems or in separate system components. When acquiring and implementing automated mechanisms, organizations consider whether such mechanisms depend on the ability of the system component to support an agent or supplicant in order to be detected since some types of components do not have or cannot support agents (e.g., IoT devices, sensors). Isolation can be achieved , for example, by placing unauthorized system components in separate domains or subnets or quarantining such components. This type of component isolation is commonly referred to as "sandboxing."

### CM-08(04) Accountability Information {#cm-8.4}

**Statement.** Include in the system component inventory information, a means for identifying by [organization-defined value] , individuals responsible and accountable for administering those components.

**Guidance.** Identifying individuals who are responsible and accountable for administering system components ensures that the assigned components are properly administered and that organizations can contact those individuals if some action is required (e.g., when the component is determined to be the source of a breach, needs to be recalled or replaced, or needs to be relocated).

### CM-08(05) No Duplicate Accounting of Components (withdrawn) {#cm-8.5}

### CM-08(06) Assessed Configurations and Approved Deviations {#cm-8.6}

**Statement.** Include assessed component configurations and any approved deviations to current deployed configurations in the system component inventory.

**Guidance.** Assessed configurations and approved deviations focus on configuration settings established by organizations for system components, the specific components that have been assessed to determine compliance with the required configuration settings, and any approved deviations from established configuration settings.

### CM-08(07) Centralized Repository {#cm-8.7}

**Statement.** Provide a centralized repository for the inventory of system components.

**Guidance.** Organizations may implement centralized system component inventories that include components from all organizational systems. Centralized repositories of component inventories provide opportunities for efficiencies in accounting for organizational hardware, software, and firmware assets. Such repositories may also help organizations rapidly identify the location and responsible individuals of components that have been compromised, breached, or are otherwise in need of mitigation actions. Organizations ensure that the resulting centralized inventories include system-specific information required for proper component accountability.

### CM-08(08) Automated Location Tracking {#cm-8.8}

**Statement.** Support the tracking of system components by geographic location using [automated mechanisms].

**Guidance.** The use of automated mechanisms to track the location of system components can increase the accuracy of component inventories. Such capability may help organizations rapidly identify the location and responsible individuals of system components that have been compromised, breached, or are otherwise in need of mitigation actions. The use of tracking mechanisms can be coordinated with senior agency officials for privacy if there are implications that affect individual privacy.

### CM-08(09) Assignment of Components to Systems {#cm-8.9}

**Statement.** - (a) Assign system components to a system; and
- (b) Receive an acknowledgement from [personnel or roles] of this assignment.

**Guidance.** System components that are not assigned to a system may be unmanaged, lack the required protection, and become an organizational vulnerability.

## CM-09 Configuration Management Plan {#cm-9}

**Statement.** Develop, document, and implement a configuration management plan for the system that:
- a. Addresses roles, responsibilities, and configuration management processes and procedures;
- b. Establishes a process for identifying configuration items throughout the system development life cycle and for managing the configuration of the configuration items;
- c. Defines the configuration items for the system and places the configuration items under configuration management;
- d. Is reviewed and approved by [personnel or roles] ; and
- e. Protects the configuration management plan from unauthorized disclosure and modification.

**Guidance.** Configuration management activities occur throughout the system development life cycle. As such, there are developmental configuration management activities (e.g., the control of code and software libraries) and operational configuration management activities (e.g., control of installed components and how the components are configured). Configuration management plans satisfy the requirements in configuration management policies while being tailored to individual systems. Configuration management plans define processes and procedures for how configuration management is used to support system development life cycle activities.

Configuration management plans are generated during the development and acquisition stage of the system development life cycle. The plans describe how to advance changes through change management processes; update configuration settings and baselines; maintain component inventories; control development, test, and operational environments; and develop, release, and update key documents.

Organizations can employ templates to help ensure the consistent and timely development and implementation of configuration management plans. Templates can represent a configuration management plan for the organization with subsets of the plan implemented on a system by system basis. Configuration management approval processes include the designation of key stakeholders responsible for reviewing and approving proposed changes to systems, and personnel who conduct security and privacy impact analyses prior to the implementation of changes to the systems. Configuration items are the system components, such as the hardware, software, firmware, and documentation to be configuration-managed. As systems continue through the system development life cycle, new configuration items may be identified, and some existing configuration items may no longer need to be under configuration control.

### CM-09(01) Assignment of Responsibility {#cm-9.1}

**Statement.** Assign responsibility for developing the configuration management process to organizational personnel that are not directly involved in system development.

**Guidance.** In the absence of dedicated configuration management teams assigned within organizations, system developers may be tasked with developing configuration management processes using personnel who are not directly involved in system development or system integration. This separation of duties ensures that organizations establish and maintain a sufficient degree of independence between the system development and integration processes and configuration management processes to facilitate quality control and more effective oversight.

## CM-10 Software Usage Restrictions {#cm-10}

**Statement.** - a. Use software and associated documentation in accordance with contract agreements and copyright laws;
- b. Track the use of software and associated documentation protected by quantity licenses to control copying and distribution; and
- c. Control and document the use of peer-to-peer file sharing technology to ensure that this capability is not used for the unauthorized distribution, display, performance, or reproduction of copyrighted work.

**Guidance.** Software license tracking can be accomplished by manual or automated methods, depending on organizational needs. Examples of contract agreements include software license agreements and non-disclosure agreements.

### CM-10(01) Open-source Software {#cm-10.1}

**Statement.** Establish the following restrictions on the use of open-source software: [restrictions].

**Guidance.** Open-source software refers to software that is available in source code form. Certain software rights normally reserved for copyright holders are routinely provided under software license agreements that permit individuals to study, change, and improve the software. From a security perspective, the major advantage of open-source software is that it provides organizations with the ability to examine the source code. In some cases, there is an online community associated with the software that inspects, tests, updates, and reports on issues found in software on an ongoing basis. However, remediating vulnerabilities in open-source software may be problematic. There may also be licensing issues associated with open-source software, including the constraints on derivative use of such software. Open-source software that is available only in binary form may increase the level of risk in using such software.

## CM-11 User-installed Software {#cm-11}

**Statement.** - a. Establish [policies] governing the installation of software by users;
- b. Enforce software installation policies through the following methods: [methods] ; and
- c. Monitor policy compliance [frequency].

**Guidance.** If provided the necessary privileges, users can install software in organizational systems. To maintain control over the software installed, organizations identify permitted and prohibited actions regarding software installation. Permitted software installations include updates and security patches to existing software and downloading new applications from organization-approved "app stores." Prohibited software installations include software with unknown or suspect pedigrees or software that organizations consider potentially malicious. Policies selected for governing user-installed software are organization-developed or provided by some external entity. Policy enforcement methods can include procedural methods and automated methods.

### CM-11(01) Alerts for Unauthorized Installations (withdrawn) {#cm-11.1}

### CM-11(02) Software Installation with Privileged Status {#cm-11.2}

**Statement.** Allow user installation of software only with explicit privileged status.

**Guidance.** Privileged status can be obtained, for example, by serving in the role of system administrator.

### CM-11(03) Automated Enforcement and Monitoring {#cm-11.3}

**Statement.** Enforce and monitor compliance with software installation policies using [organization-defined automated mechanisms].

**Guidance.** Organizations enforce and monitor compliance with software installation policies using automated mechanisms to more quickly detect and respond to unauthorized software installation which can be an indicator of an internal or external hostile attack.

## CM-12 Information Location {#cm-12}

**Statement.** - a. Identify and document the location of [information] and the specific system components on which the information is processed and stored;
- b. Identify and document the users who have access to the system and system components where the information is processed and stored; and
- c. Document changes to the location (i.e., system or system components) where the information is processed and stored.

**Guidance.** Information location addresses the need to understand where information is being processed and stored. Information location includes identifying where specific information types and information reside in system components and how information is being processed so that information flow can be understood and adequate protection and policy management provided for such information and system components. The security category of the information is also a factor in determining the controls necessary to protect the information and the system component where the information resides (see [FIPS 199](#628d22a1-6a11-4784-bc59-5cd9497b5445) ). The location of the information and system components is also a factor in the architecture and design of the system (see [SA-4](#sa-4), [SA-8](#sa-8), [SA-17](#sa-17)).

### CM-12(01) Automated Tools to Support Information Location {#cm-12.1}

**Statement.** Use automated tools to identify [information by information type] on [system components] to ensure controls are in place to protect organizational information and individual privacy.

**Guidance.** The use of automated tools helps to increase the effectiveness and efficiency of the information location capability implemented within the system. Automation also helps organizations manage the data produced during information location activities and share such information across the organization. The output of automated information location tools can be used to guide and inform system architecture and design decisions.

## CM-13 Data Action Mapping {#cm-13}

**Statement.** Develop and document a map of system data actions.

**Guidance.** Data actions are system operations that process personally identifiable information. The processing of such information encompasses the full information life cycle, which includes collection, generation, transformation, use, disclosure, retention, and disposal. A map of system data actions includes discrete data actions, elements of personally identifiable information being processed in the data actions, system components involved in the data actions, and the owners or operators of the system components. Understanding what personally identifiable information is being processed (e.g., the sensitivity of the personally identifiable information), how personally identifiable information is being processed (e.g., if the data action is visible to the individual or is processed in another part of the system), and by whom (e.g., individuals may have different privacy perceptions based on the entity that is processing the personally identifiable information) provides a number of contextual factors that are important to assessing the degree of privacy risk created by the system. Data maps can be illustrated in different ways, and the level of detail may vary based on the mission and business needs of the organization. The data map may be an overlay of any system design artifact that the organization is using. The development of this map may necessitate coordination between the privacy and security programs regarding the covered data actions and the components that are identified as part of the system.

## CM-14 Signed Components {#cm-14}

**Statement.** Prevent the installation of [organization-defined software and firmware components] without verification that the component has been digitally signed using a certificate that is recognized and approved by the organization.

**Guidance.** Software and firmware components prevented from installation unless signed with recognized and approved certificates include software and firmware version updates, patches, service packs, device drivers, and basic input/output system updates. Organizations can identify applicable software and firmware components by type, by specific items, or a combination of both. Digital signatures and organizational verification of such signatures is a method of code authentication.
