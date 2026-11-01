# IA — Identification and Authentication

## IA-01 Policy and Procedures {#ia-1}

**Statement.** - a. Develop, document, and disseminate to [organization-defined personnel or roles]:
  - 1. [organization-defined value] identification and authentication policy that:
    - (a) Addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and
    - (b) Is consistent with applicable laws, executive orders, directives, regulations, policies, standards, and guidelines; and
  - 2. Procedures to facilitate the implementation of the identification and authentication policy and the associated identification and authentication controls;
- b. Designate an [official] to manage the development, documentation, and dissemination of the identification and authentication policy and procedures; and
- c. Review and update the current identification and authentication:
  - 1. Policy [frequency] and following [events] ; and
  - 2. Procedures [frequency] and following [events].

**Guidance.** Identification and authentication policy and procedures address the controls in the IA family that are implemented within systems and organizations. The risk management strategy is an important factor in establishing such policies and procedures. Policies and procedures contribute to security and privacy assurance. Therefore, it is important that security and privacy programs collaborate on the development of identification and authentication policy and procedures. Security and privacy program policies and procedures at the organization level are preferable, in general, and may obviate the need for mission- or system-specific policies and procedures. The policy can be included as part of the general security and privacy policy or be represented by multiple policies that reflect the complex nature of organizations. Procedures can be established for security and privacy programs, for mission or business processes, and for systems, if needed. Procedures describe how the policies or controls are implemented and can be directed at the individual or role that is the object of the procedure. Procedures can be documented in system security and privacy plans or in one or more separate documents. Events that may precipitate an update to identification and authentication policy and procedures include assessment or audit findings, security incidents or breaches, or changes in applicable laws, executive orders, directives, regulations, policies, standards, and guidelines. Simply restating controls does not constitute an organizational policy or procedure.

## IA-02 Identification and Authentication (Organizational Users) {#ia-2}

**Statement.** Uniquely identify and authenticate organizational users and associate that unique identification with processes acting on behalf of those users.

**Guidance.** Organizations can satisfy the identification and authentication requirements by complying with the requirements in [HSPD 12](#f16e438e-7114-4144-bfe2-2dfcad8cb2d0) . Organizational users include employees or individuals who organizations consider to have an equivalent status to employees (e.g., contractors and guest researchers). Unique identification and authentication of users applies to all accesses other than those that are explicitly identified in [AC-14](#ac-14) and that occur through the authorized use of group authenticators without individual authentication. Since processes execute on behalf of groups and roles, organizations may require unique identification of individuals in group accounts or for detailed accountability of individual activity.

Organizations employ passwords, physical authenticators, or biometrics to authenticate user identities or, in the case of multi-factor authentication, some combination thereof. Access to organizational systems is defined as either local access or network access. Local access is any access to organizational systems by users or processes acting on behalf of users, where access is obtained through direct connections without the use of networks. Network access is access to organizational systems by users (or processes acting on behalf of users) where access is obtained through network connections (i.e., nonlocal accesses). Remote access is a type of network access that involves communication through external networks. Internal networks include local area networks and wide area networks.

The use of encrypted virtual private networks for network connections between organization-controlled endpoints and non-organization-controlled endpoints may be treated as internal networks with respect to protecting the confidentiality and integrity of information traversing the network. Identification and authentication requirements for non-organizational users are described in [IA-8](#ia-8).

### IA-02(01) Multi-factor Authentication to Privileged Accounts {#ia-2.1}

**Statement.** Implement multi-factor authentication for access to privileged accounts.

**Guidance.** Multi-factor authentication requires the use of two or more different factors to achieve authentication. The authentication factors are defined as follows: something you know (e.g., a personal identification number [PIN]), something you have (e.g., a physical authenticator such as a cryptographic private key), or something you are (e.g., a biometric). Multi-factor authentication solutions that feature physical authenticators include hardware authenticators that provide time-based or challenge-response outputs and smart cards such as the U.S. Government Personal Identity Verification (PIV) card or the Department of Defense (DoD) Common Access Card (CAC). In addition to authenticating users at the system level (i.e., at logon), organizations may employ authentication mechanisms at the application level, at their discretion, to provide increased security. Regardless of the type of access (i.e., local, network, remote), privileged accounts are authenticated using multi-factor options appropriate for the level of risk. Organizations can add additional security measures, such as additional or more rigorous authentication mechanisms, for specific types of access.

### IA-02(02) Multi-factor Authentication to Non-privileged Accounts {#ia-2.2}

**Statement.** Implement multi-factor authentication for access to non-privileged accounts.

**Guidance.** Multi-factor authentication requires the use of two or more different factors to achieve authentication. The authentication factors are defined as follows: something you know (e.g., a personal identification number [PIN]), something you have (e.g., a physical authenticator such as a cryptographic private key), or something you are (e.g., a biometric). Multi-factor authentication solutions that feature physical authenticators include hardware authenticators that provide time-based or challenge-response outputs and smart cards such as the U.S. Government Personal Identity Verification card or the DoD Common Access Card. In addition to authenticating users at the system level, organizations may also employ authentication mechanisms at the application level, at their discretion, to provide increased information security. Regardless of the type of access (i.e., local, network, remote), non-privileged accounts are authenticated using multi-factor options appropriate for the level of risk. Organizations can provide additional security measures, such as additional or more rigorous authentication mechanisms, for specific types of access.

### IA-02(03) Local Access to Privileged Accounts (withdrawn) {#ia-2.3}

### IA-02(04) Local Access to Non-privileged Accounts (withdrawn) {#ia-2.4}

### IA-02(05) Individual Authentication with Group Authentication {#ia-2.5}

**Statement.** When shared accounts or authenticators are employed, require users to be individually authenticated before granting access to the shared accounts or resources.

**Guidance.** Individual authentication prior to shared group authentication mitigates the risk of using group accounts or authenticators.

### IA-02(06) Access to Accounts —separate Device {#ia-2.6}

**Statement.** Implement multi-factor authentication for [organization-defined value] access to [organization-defined value] such that:
- (a) One of the factors is provided by a device separate from the system gaining access; and
- (b) The device meets [strength of mechanism requirements].

**Guidance.** The purpose of requiring a device that is separate from the system to which the user is attempting to gain access for one of the factors during multi-factor authentication is to reduce the likelihood of compromising authenticators or credentials stored on the system. Adversaries may be able to compromise such authenticators or credentials and subsequently impersonate authorized users. Implementing one of the factors on a separate device (e.g., a hardware token), provides a greater strength of mechanism and an increased level of assurance in the authentication process.

### IA-02(07) Network Access to Non-privileged Accounts — Separate Device (withdrawn) {#ia-2.7}

### IA-02(08) Access to Accounts — Replay Resistant {#ia-2.8}

**Statement.** Implement replay-resistant authentication mechanisms for access to [organization-defined value].

**Guidance.** Authentication processes resist replay attacks if it is impractical to achieve successful authentications by replaying previous authentication messages. Replay-resistant techniques include protocols that use nonces or challenges such as time synchronous or cryptographic authenticators.

### IA-02(09) Network Access to Non-privileged Accounts — Replay Resistant (withdrawn) {#ia-2.9}

### IA-02(10) Single Sign-on {#ia-2.10}

**Statement.** Provide a single sign-on capability for [system accounts and services].

**Guidance.** Single sign-on enables users to log in once and gain access to multiple system resources. Organizations consider the operational efficiencies provided by single sign-on capabilities with the risk introduced by allowing access to multiple systems via a single authentication event. Single sign-on can present opportunities to improve system security, for example by providing the ability to add multi-factor authentication for applications and systems (existing and new) that may not be able to natively support multi-factor authentication.

### IA-02(11) Remote Access — Separate Device (withdrawn) {#ia-2.11}

### IA-02(12) Acceptance of PIV Credentials {#ia-2.12}

**Statement.** Accept and electronically verify Personal Identity Verification-compliant credentials.

**Guidance.** Acceptance of Personal Identity Verification (PIV)-compliant credentials applies to organizations implementing logical access control and physical access control systems. PIV-compliant credentials are those credentials issued by federal agencies that conform to FIPS Publication 201 and supporting guidance documents. The adequacy and reliability of PIV card issuers are authorized using [SP 800-79-2](#10963761-58fc-4b20-b3d6-b44a54daba03) . Acceptance of PIV-compliant credentials includes derived PIV credentials, the use of which is addressed in [SP 800-166](#e8552d48-cf41-40aa-8b06-f45f7fb4706c) . The DOD Common Access Card (CAC) is an example of a PIV credential.

### IA-02(13) Out-of-band Authentication {#ia-2.13}

**Statement.** Implement the following out-of-band authentication mechanisms under [conditions]: [out-of-band authentication].

**Guidance.** Out-of-band authentication refers to the use of two separate communication paths to identify and authenticate users or devices to an information system. The first path (i.e., the in-band path) is used to identify and authenticate users or devices and is generally the path through which information flows. The second path (i.e., the out-of-band path) is used to independently verify the authentication and/or requested action. For example, a user authenticates via a notebook computer to a remote server to which the user desires access and requests some action of the server via that communication path. Subsequently, the server contacts the user via the user’s cell phone to verify that the requested action originated from the user. The user may confirm the intended action to an individual on the telephone or provide an authentication code via the telephone. Out-of-band authentication can be used to mitigate actual or suspected "man-in the-middle" attacks. The conditions or criteria for activation include suspicious activities, new threat indicators, elevated threat levels, or the impact or classification level of information in requested transactions.

## IA-03 Device Identification and Authentication {#ia-3}

**Statement.** Uniquely identify and authenticate [devices and/or types of devices] before establishing a [organization-defined value] connection.

**Guidance.** Devices that require unique device-to-device identification and authentication are defined by type, device, or a combination of type and device. Organization-defined device types include devices that are not owned by the organization. Systems use shared known information (e.g., Media Access Control [MAC], Transmission Control Protocol/Internet Protocol [TCP/IP] addresses) for device identification or organizational authentication solutions (e.g., Institute of Electrical and Electronics Engineers (IEEE) 802.1x and Extensible Authentication Protocol [EAP], RADIUS server with EAP-Transport Layer Security [TLS] authentication, Kerberos) to identify and authenticate devices on local and wide area networks. Organizations determine the required strength of authentication mechanisms based on the security categories of systems and mission or business requirements. Because of the challenges of implementing device authentication on a large scale, organizations can restrict the application of the control to a limited number/type of devices based on mission or business needs.

### IA-03(01) Cryptographic Bidirectional Authentication {#ia-3.1}

**Statement.** Authenticate [devices and/or types of devices] before establishing [organization-defined value] connection using bidirectional authentication that is cryptographically based.

**Guidance.** A local connection is a connection with a device that communicates without the use of a network. A network connection is a connection with a device that communicates through a network. A remote connection is a connection with a device that communicates through an external network. Bidirectional authentication provides stronger protection to validate the identity of other devices for connections that are of greater risk.

### IA-03(02) Cryptographic Bidirectional Network Authentication (withdrawn) {#ia-3.2}

### IA-03(03) Dynamic Address Allocation {#ia-3.3}

**Statement.** - (a) Where addresses are allocated dynamically, standardize dynamic address allocation lease information and the lease duration assigned to devices in accordance with [organization-defined lease information and lease duration] ; and
- (b) Audit lease information when assigned to a device.

**Guidance.** The Dynamic Host Configuration Protocol (DHCP) is an example of a means by which clients can dynamically receive network address assignments.

### IA-03(04) Device Attestation {#ia-3.4}

**Statement.** Handle device identification and authentication based on attestation by [configuration management process].

**Guidance.** Device attestation refers to the identification and authentication of a device based on its configuration and known operating state. Device attestation can be determined via a cryptographic hash of the device. If device attestation is the means of identification and authentication, then it is important that patches and updates to the device are handled via a configuration management process such that the patches and updates are done securely and do not disrupt identification and authentication to other devices.

## IA-04 Identifier Management {#ia-4}

**Statement.** Manage system identifiers by:
- a. Receiving authorization from [personnel or roles] to assign an individual, group, role, service, or device identifier;
- b. Selecting an identifier that identifies an individual, group, role, service, or device;
- c. Assigning the identifier to the intended individual, group, role, service, or device; and
- d. Preventing reuse of identifiers for [time period].

**Guidance.** Common device identifiers include Media Access Control (MAC) addresses, Internet Protocol (IP) addresses, or device-unique token identifiers. The management of individual identifiers is not applicable to shared system accounts. Typically, individual identifiers are the usernames of the system accounts assigned to those individuals. In such instances, the account management activities of [AC-2](#ac-2) use account names provided by [IA-4](#ia-4) . Identifier management also addresses individual identifiers not necessarily associated with system accounts. Preventing the reuse of identifiers implies preventing the assignment of previously used individual, group, role, service, or device identifiers to different individuals, groups, roles, services, or devices.

### IA-04(01) Prohibit Account Identifiers as Public Identifiers {#ia-4.1}

**Statement.** Prohibit the use of system account identifiers that are the same as public identifiers for individual accounts.

**Guidance.** Prohibiting account identifiers as public identifiers applies to any publicly disclosed account identifier used for communication such as, electronic mail and instant messaging. Prohibiting the use of systems account identifiers that are the same as some public identifier, such as the individual identifier section of an electronic mail address, makes it more difficult for adversaries to guess user identifiers. Prohibiting account identifiers as public identifiers without the implementation of other supporting controls only complicates guessing of identifiers. Additional protections are required for authenticators and credentials to protect the account.

### IA-04(02) Supervisor Authorization (withdrawn) {#ia-4.2}

### IA-04(03) Multiple Forms of Certification (withdrawn) {#ia-4.3}

### IA-04(04) Identify User Status {#ia-4.4}

**Statement.** Manage individual identifiers by uniquely identifying each individual as [characteristics].

**Guidance.** Characteristics that identify the status of individuals include contractors, foreign nationals, and non-organizational users. Identifying the status of individuals by these characteristics provides additional information about the people with whom organizational personnel are communicating. For example, it might be useful for a government employee to know that one of the individuals on an email message is a contractor.

### IA-04(05) Dynamic Management {#ia-4.5}

**Statement.** Manage individual identifiers dynamically in accordance with [dynamic identifier policy].

**Guidance.** In contrast to conventional approaches to identification that presume static accounts for preregistered users, many distributed systems establish identifiers at runtime for entities that were previously unknown. When identifiers are established at runtime for previously unknown entities, organizations can anticipate and provision for the dynamic establishment of identifiers. Pre-established trust relationships and mechanisms with appropriate authorities to validate credentials and related identifiers are essential.

### IA-04(06) Cross-organization Management {#ia-4.6}

**Statement.** Coordinate with the following external organizations for cross-organization management of identifiers: [external organizations].

**Guidance.** Cross-organization identifier management provides the capability to identify individuals, groups, roles, or devices when conducting cross-organization activities involving the processing, storage, or transmission of information.

### IA-04(07) In-person Registration (withdrawn) {#ia-4.7}

### IA-04(08) Pairwise Pseudonymous Identifiers {#ia-4.8}

**Statement.** Generate pairwise pseudonymous identifiers.

**Guidance.** A pairwise pseudonymous identifier is an opaque unguessable subscriber identifier generated by an identity provider for use at a specific individual relying party. Generating distinct pairwise pseudonymous identifiers with no identifying information about a subscriber discourages subscriber activity tracking and profiling beyond the operational requirements established by an organization. The pairwise pseudonymous identifiers are unique to each relying party except in situations where relying parties can show a demonstrable relationship justifying an operational need for correlation, or all parties consent to being correlated in such a manner.

### IA-04(09) Attribute Maintenance and Protection {#ia-4.9}

**Statement.** Maintain the attributes for each uniquely identified individual, device, or service in [protected central storage].

**Guidance.** For each of the entities covered in [IA-2](#ia-2), [IA-3](#ia-3), [IA-8](#ia-8) , and [IA-9](#ia-9) , it is important to maintain the attributes for each authenticated entity on an ongoing basis in a central (protected) store.

## IA-05 Authenticator Management {#ia-5}

**Statement.** Manage system authenticators by:
- a. Verifying, as part of the initial authenticator distribution, the identity of the individual, group, role, service, or device receiving the authenticator;
- b. Establishing initial authenticator content for any authenticators issued by the organization;
- c. Ensuring that authenticators have sufficient strength of mechanism for their intended use;
- d. Establishing and implementing administrative procedures for initial authenticator distribution, for lost or compromised or damaged authenticators, and for revoking authenticators;
- e. Changing default authenticators prior to first use;
- f. Changing or refreshing authenticators [time period by authenticator type] or when [events] occur;
- g. Protecting authenticator content from unauthorized disclosure and modification;
- h. Requiring individuals to take, and having devices implement, specific controls to protect authenticators; and
- i. Changing authenticators for group or role accounts when membership to those accounts changes.

**Guidance.** Authenticators include passwords, cryptographic devices, biometrics, certificates, one-time password devices, and ID badges. Device authenticators include certificates and passwords. Initial authenticator content is the actual content of the authenticator (e.g., the initial password). In contrast, the requirements for authenticator content contain specific criteria or characteristics (e.g., minimum password length). Developers may deliver system components with factory default authentication credentials (i.e., passwords) to allow for initial installation and configuration. Default authentication credentials are often well known, easily discoverable, and present a significant risk. The requirement to protect individual authenticators may be implemented via control [PL-4](#pl-4) or [PS-6](#ps-6) for authenticators in the possession of individuals and by controls [AC-3](#ac-3), [AC-6](#ac-6) , and [SC-28](#sc-28) for authenticators stored in organizational systems, including passwords stored in hashed or encrypted formats or files containing encrypted or hashed passwords accessible with administrator privileges.

Systems support authenticator management by organization-defined settings and restrictions for various authenticator characteristics (e.g., minimum password length, validation time window for time synchronous one-time tokens, and number of allowed rejections during the verification stage of biometric authentication). Actions can be taken to safeguard individual authenticators, including maintaining possession of authenticators, not sharing authenticators with others, and immediately reporting lost, stolen, or compromised authenticators. Authenticator management includes issuing and revoking authenticators for temporary access when no longer needed.

### IA-05(01) Password-based Authentication {#ia-5.1}

**Statement.** For password-based authentication:
- (a) Maintain a list of commonly-used, expected, or compromised passwords and update the list [frequency] and when organizational passwords are suspected to have been compromised directly or indirectly;
- (b) Verify, when users create or update passwords, that the passwords are not found on the list of commonly-used, expected, or compromised passwords in IA-5(1)(a);
- (c) Transmit passwords only over cryptographically-protected channels;
- (d) Store passwords using an approved salted key derivation function, preferably using a keyed hash;
- (e) Require immediate selection of a new password upon account recovery;
- (f) Allow user selection of long passwords and passphrases, including spaces and all printable characters;
- (g) Employ automated tools to assist the user in selecting strong password authenticators; and
- (h) Enforce the following composition and complexity rules: [composition and complexity rules].

**Guidance.** Password-based authentication applies to passwords regardless of whether they are used in single-factor or multi-factor authentication. Long passwords or passphrases are preferable over shorter passwords. Enforced composition rules provide marginal security benefits while decreasing usability. However, organizations may choose to establish certain rules for password generation (e.g., minimum character length for long passwords) under certain circumstances and can enforce this requirement in IA-5(1)(h). Account recovery can occur, for example, in situations when a password is forgotten. Cryptographically protected passwords include salted one-way cryptographic hashes of passwords. The list of commonly used, compromised, or expected passwords includes passwords obtained from previous breach corpuses, dictionary words, and repetitive or sequential characters. The list includes context-specific words, such as the name of the service, username, and derivatives thereof.

### IA-05(02) Public Key-based Authentication {#ia-5.2}

**Statement.** - (a) For public key-based authentication:
  - (1) Enforce authorized access to the corresponding private key; and
  - (2) Map the authenticated identity to the account of the individual or group; and
- (b) When public key infrastructure (PKI) is used:
  - (1) Validate certificates by constructing and verifying a certification path to an accepted trust anchor, including checking certificate status information; and
  - (2) Implement a local cache of revocation data to support path discovery and validation.

**Guidance.** Public key cryptography is a valid authentication mechanism for individuals, machines, and devices. For PKI solutions, status information for certification paths includes certificate revocation lists or certificate status protocol responses. For PIV cards, certificate validation involves the construction and verification of a certification path to the Common Policy Root trust anchor, which includes certificate policy processing. Implementing a local cache of revocation data to support path discovery and validation also supports system availability in situations where organizations are unable to access revocation information via the network.

### IA-05(03) In-person or Trusted External Party Registration (withdrawn) {#ia-5.3}

### IA-05(04) Automated Support for Password Strength Determination (withdrawn) {#ia-5.4}

### IA-05(05) Change Authenticators Prior to Delivery {#ia-5.5}

**Statement.** Require developers and installers of system components to provide unique authenticators or change default authenticators prior to delivery and installation.

**Guidance.** Changing authenticators prior to the delivery and installation of system components extends the requirement for organizations to change default authenticators upon system installation by requiring developers and/or installers to provide unique authenticators or change default authenticators for system components prior to delivery and/or installation. However, it typically does not apply to developers of commercial off-the-shelf information technology products. Requirements for unique authenticators can be included in acquisition documents prepared by organizations when procuring systems or system components.

### IA-05(06) Protection of Authenticators {#ia-5.6}

**Statement.** Protect authenticators commensurate with the security category of the information to which use of the authenticator permits access.

**Guidance.** For systems that contain multiple security categories of information without reliable physical or logical separation between categories, authenticators used to grant access to the systems are protected commensurate with the highest security category of information on the systems. Security categories of information are determined as part of the security categorization process.

### IA-05(07) No Embedded Unencrypted Static Authenticators {#ia-5.7}

**Statement.** Ensure that unencrypted static authenticators are not embedded in applications or other forms of static storage.

**Guidance.** In addition to applications, other forms of static storage include access scripts and function keys. Organizations exercise caution when determining whether embedded or stored authenticators are in encrypted or unencrypted form. If authenticators are used in the manner stored, then those representations are considered unencrypted authenticators.

### IA-05(08) Multiple System Accounts {#ia-5.8}

**Statement.** Implement [security controls] to manage the risk of compromise due to individuals having accounts on multiple systems.

**Guidance.** When individuals have accounts on multiple systems and use the same authenticators such as passwords, there is the risk that a compromise of one account may lead to the compromise of other accounts. Alternative approaches include having different authenticators (passwords) on all systems, employing a single sign-on or federation mechanism, or using some form of one-time passwords on all systems. Organizations can also use rules of behavior (see [PL-4](#pl-4) ) and access agreements (see [PS-6](#ps-6) ) to mitigate the risk of multiple system accounts.

### IA-05(09) Federated Credential Management {#ia-5.9}

**Statement.** Use the following external organizations to federate credentials: [external organizations].

**Guidance.** Federation provides organizations with the capability to authenticate individuals and devices when conducting cross-organization activities involving the processing, storage, or transmission of information. Using a specific list of approved external organizations for authentication helps to ensure that those organizations are vetted and trusted.

### IA-05(10) Dynamic Credential Binding {#ia-5.10}

**Statement.** Bind identities and authenticators dynamically using the following rules: [binding rules].

**Guidance.** Authentication requires some form of binding between an identity and the authenticator that is used to confirm the identity. In conventional approaches, binding is established by pre-provisioning both the identity and the authenticator to the system. For example, the binding between a username (i.e., identity) and a password (i.e., authenticator) is accomplished by provisioning the identity and authenticator as a pair in the system. New authentication techniques allow the binding between the identity and the authenticator to be implemented external to a system. For example, with smartcard credentials, the identity and authenticator are bound together on the smartcard. Using these credentials, systems can authenticate identities that have not been pre-provisioned, dynamically provisioning the identity after authentication. In these situations, organizations can anticipate the dynamic provisioning of identities. Pre-established trust relationships and mechanisms with appropriate authorities to validate identities and related credentials are essential.

### IA-05(11) Hardware Token-based Authentication (withdrawn) {#ia-5.11}

### IA-05(12) Biometric Authentication Performance {#ia-5.12}

**Statement.** For biometric-based authentication, employ mechanisms that satisfy the following biometric quality requirements [biometric quality requirements].

**Guidance.** Unlike password-based authentication, which provides exact matches of user-input passwords to stored passwords, biometric authentication does not provide exact matches. Depending on the type of biometric and the type of collection mechanism, there is likely to be some divergence from the presented biometric and the stored biometric that serves as the basis for comparison. Matching performance is the rate at which a biometric algorithm correctly results in a match for a genuine user and rejects other users. Biometric performance requirements include the match rate, which reflects the accuracy of the biometric matching algorithm used by a system.

### IA-05(13) Expiration of Cached Authenticators {#ia-5.13}

**Statement.** Prohibit the use of cached authenticators after [time period].

**Guidance.** Cached authenticators are used to authenticate to the local machine when the network is not available. If cached authentication information is out of date, the validity of the authentication information may be questionable.

### IA-05(14) Managing Content of PKI Trust Stores {#ia-5.14}

**Statement.** For PKI-based authentication, employ an organization-wide methodology for managing the content of PKI trust stores installed across all platforms, including networks, operating systems, browsers, and applications.

**Guidance.** An organization-wide methodology for managing the content of PKI trust stores helps improve the accuracy and currency of PKI-based authentication credentials across the organization.

### IA-05(15) GSA-approved Products and Services {#ia-5.15}

**Statement.** Use only General Services Administration-approved products and services for identity, credential, and access management.

**Guidance.** General Services Administration (GSA)-approved products and services are products and services that have been approved through the GSA conformance program, where applicable, and posted to the GSA Approved Products List. GSA provides guidance for teams to design and build functional and secure systems that comply with Federal Identity, Credential, and Access Management (FICAM) policies, technologies, and implementation patterns.

### IA-05(16) In-person or Trusted External Party Authenticator Issuance {#ia-5.16}

**Statement.** Require that the issuance of [types of and/or specific authenticators] be conducted [organization-defined value] before [registration authority] with authorization by [personnel or roles].

**Guidance.** Issuing authenticators in person or by a trusted external party enhances and reinforces the trustworthiness of the identity proofing process.

### IA-05(17) Presentation Attack Detection for Biometric Authenticators {#ia-5.17}

**Statement.** Employ presentation attack detection mechanisms for biometric-based authentication.

**Guidance.** Biometric characteristics do not constitute secrets. Such characteristics can be obtained by online web accesses, taking a picture of someone with a camera phone to obtain facial images with or without their knowledge, lifting from objects that someone has touched (e.g., a latent fingerprint), or capturing a high-resolution image (e.g., an iris pattern). Presentation attack detection technologies including liveness detection, can mitigate the risk of these types of attacks by making it difficult to produce artifacts intended to defeat the biometric sensor.

### IA-05(18) Password Managers {#ia-5.18}

**Statement.** - (a) Employ [password managers] to generate and manage passwords; and
- (b) Protect the passwords using [controls].

**Guidance.** For systems where static passwords are employed, it is often a challenge to ensure that the passwords are suitably complex and that the same passwords are not employed on multiple systems. A password manager is a solution to this problem as it automatically generates and stores strong and different passwords for various accounts. A potential risk of using password managers is that adversaries can target the collection of passwords generated by the password manager. Therefore, the collection of passwords requires protection including encrypting the passwords (see [IA-5(1)(d)](#ia-5.1_smt.d) ) and storing the collection offline in a token.

## IA-06 Authentication Feedback {#ia-6}

**Statement.** Obscure feedback of authentication information during the authentication process to protect the information from possible exploitation and use by unauthorized individuals.

**Guidance.** Authentication feedback from systems does not provide information that would allow unauthorized individuals to compromise authentication mechanisms. For some types of systems, such as desktops or notebooks with relatively large monitors, the threat (referred to as shoulder surfing) may be significant. For other types of systems, such as mobile devices with small displays, the threat may be less significant and is balanced against the increased likelihood of typographic input errors due to small keyboards. Thus, the means for obscuring authentication feedback is selected accordingly. Obscuring authentication feedback includes displaying asterisks when users type passwords into input devices or displaying feedback for a very limited time before obscuring it.

## IA-07 Cryptographic Module Authentication {#ia-7}

**Statement.** Implement mechanisms for authentication to a cryptographic module that meet the requirements of applicable laws, executive orders, directives, policies, regulations, standards, and guidelines for such authentication.

**Guidance.** Authentication mechanisms may be required within a cryptographic module to authenticate an operator accessing the module and to verify that the operator is authorized to assume the requested role and perform services within that role.

## IA-08 Identification and Authentication (Non-organizational Users) {#ia-8}

**Statement.** Uniquely identify and authenticate non-organizational users or processes acting on behalf of non-organizational users.

**Guidance.** Non-organizational users include system users other than organizational users explicitly covered by [IA-2](#ia-2) . Non-organizational users are uniquely identified and authenticated for accesses other than those explicitly identified and documented in [AC-14](#ac-14) . Identification and authentication of non-organizational users accessing federal systems may be required to protect federal, proprietary, or privacy-related information (with exceptions noted for national security systems). Organizations consider many factors—including security, privacy, scalability, and practicality—when balancing the need to ensure ease of use for access to federal information and systems with the need to protect and adequately mitigate risk.

### IA-08(01) Acceptance of PIV Credentials from Other Agencies {#ia-8.1}

**Statement.** Accept and electronically verify Personal Identity Verification-compliant credentials from other federal agencies.

**Guidance.** Acceptance of Personal Identity Verification (PIV) credentials from other federal agencies applies to both logical and physical access control systems. PIV credentials are those credentials issued by federal agencies that conform to FIPS Publication 201 and supporting guidelines. The adequacy and reliability of PIV card issuers are addressed and authorized using [SP 800-79-2](#10963761-58fc-4b20-b3d6-b44a54daba03).

### IA-08(02) Acceptance of External Authenticators {#ia-8.2}

**Statement.** - (a) Accept only external authenticators that are NIST-compliant; and
- (b) Document and maintain a list of accepted external authenticators.

**Guidance.** Acceptance of only NIST-compliant external authenticators applies to organizational systems that are accessible to the public (e.g., public-facing websites). External authenticators are issued by nonfederal government entities and are compliant with [SP 800-63B](#e59c5a7c-8b1f-49ca-8de0-6ee0882180ce) . Approved external authenticators meet or exceed the minimum Federal Government-wide technical, security, privacy, and organizational maturity requirements. Meeting or exceeding Federal requirements allows Federal Government relying parties to trust external authenticators in connection with an authentication transaction at a specified authenticator assurance level.

### IA-08(03) Use of FICAM-approved Products (withdrawn) {#ia-8.3}

### IA-08(04) Use of Defined Profiles {#ia-8.4}

**Statement.** Conform to the following profiles for identity management [identity management profiles].

**Guidance.** Organizations define profiles for identity management based on open identity management standards. To ensure that open identity management standards are viable, robust, reliable, sustainable, and interoperable as documented, the Federal Government assesses and scopes the standards and technology implementations against applicable laws, executive orders, directives, policies, regulations, standards, and guidelines.

### IA-08(05) Acceptance of PIV-I Credentials {#ia-8.5}

**Statement.** Accept and verify federated or PKI credentials that meet [policy].

**Guidance.** Acceptance of PIV-I credentials can be implemented by PIV, PIV-I, and other commercial or external identity providers. The acceptance and verification of PIV-I-compliant credentials apply to both logical and physical access control systems. The acceptance and verification of PIV-I credentials address nonfederal issuers of identity cards that desire to interoperate with United States Government PIV systems and that can be trusted by Federal Government-relying parties. The X.509 certificate policy for the Federal Bridge Certification Authority (FBCA) addresses PIV-I requirements. The PIV-I card is commensurate with the PIV credentials as defined in cited references. PIV-I credentials are the credentials issued by a PIV-I provider whose PIV-I certificate policy maps to the Federal Bridge PIV-I Certificate Policy. A PIV-I provider is cross-certified with the FBCA (directly or through another PKI bridge) with policies that have been mapped and approved as meeting the requirements of the PIV-I policies defined in the FBCA certificate policy.

### IA-08(06) Disassociability {#ia-8.6}

**Statement.** Implement the following measures to disassociate user attributes or identifier assertion relationships among individuals, credential service providers, and relying parties: [measures].

**Guidance.** Federated identity solutions can create increased privacy risks due to the tracking and profiling of individuals. Using identifier mapping tables or cryptographic techniques to blind credential service providers and relying parties from each other or to make identity attributes less visible to transmitting parties can reduce these privacy risks.

## IA-09 Service Identification and Authentication {#ia-9}

**Statement.** Uniquely identify and authenticate [system services and applications] before establishing communications with devices, users, or other services or applications.

**Guidance.** Services that may require identification and authentication include web applications using digital certificates or services or applications that query a database. Identification and authentication methods for system services and applications include information or code signing, provenance graphs, and electronic signatures that indicate the sources of services. Decisions regarding the validity of identification and authentication claims can be made by services separate from the services acting on those decisions. This can occur in distributed system architectures. In such situations, the identification and authentication decisions (instead of actual identifiers and authentication data) are provided to the services that need to act on those decisions.

### IA-09(01) Information Exchange (withdrawn) {#ia-9.1}

### IA-09(02) Transmission of Decisions (withdrawn) {#ia-9.2}

## IA-10 Adaptive Authentication {#ia-10}

**Statement.** Require individuals accessing the system to employ [supplemental authentication techniques or mechanisms] under specific [circumstances or situations].

**Guidance.** Adversaries may compromise individual authentication mechanisms employed by organizations and subsequently attempt to impersonate legitimate users. To address this threat, organizations may employ specific techniques or mechanisms and establish protocols to assess suspicious behavior. Suspicious behavior may include accessing information that individuals do not typically access as part of their duties, roles, or responsibilities; accessing greater quantities of information than individuals would routinely access; or attempting to access information from suspicious network addresses. When pre-established conditions or triggers occur, organizations can require individuals to provide additional authentication information. Another potential use for adaptive authentication is to increase the strength of mechanism based on the number or types of records being accessed. Adaptive authentication does not replace and is not used to avoid the use of multi-factor authentication mechanisms but can augment implementations of multi-factor authentication.

## IA-11 Re-authentication {#ia-11}

**Statement.** Require users to re-authenticate when [circumstances or situations].

**Guidance.** In addition to the re-authentication requirements associated with device locks, organizations may require re-authentication of individuals in certain situations, including when roles, authenticators or credentials change, when security categories of systems change, when the execution of privileged functions occurs, after a fixed time period, or periodically.

## IA-12 Identity Proofing {#ia-12}

**Statement.** - a. Identity proof users that require accounts for logical access to systems based on appropriate identity assurance level requirements as specified in applicable standards and guidelines;
- b. Resolve user identities to a unique individual; and
- c. Collect, validate, and verify identity evidence.

**Guidance.** Identity proofing is the process of collecting, validating, and verifying a user’s identity information for the purposes of establishing credentials for accessing a system. Identity proofing is intended to mitigate threats to the registration of users and the establishment of their accounts. Standards and guidelines specifying identity assurance levels for identity proofing include [SP 800-63-3](#737513fa-6758-403f-831d-5ddab5e23cb3) and [SP 800-63A](#9099ed2c-922a-493d-bcb4-d896192243ff) . Organizations may be subject to laws, executive orders, directives, regulations, or policies that address the collection of identity evidence. Organizational personnel consult with the senior agency official for privacy and legal counsel regarding such requirements.

### IA-12(01) Supervisor Authorization {#ia-12.1}

**Statement.** Require that the registration process to receive an account for logical access includes supervisor or sponsor authorization.

**Guidance.** Including supervisor or sponsor authorization as part of the registration process provides an additional level of scrutiny to ensure that the user’s management chain is aware of the account, the account is essential to carry out organizational missions and functions, and the user’s privileges are appropriate for the anticipated responsibilities and authorities within the organization.

### IA-12(02) Identity Evidence {#ia-12.2}

**Statement.** Require evidence of individual identification be presented to the registration authority.

**Guidance.** Identity evidence, such as documentary evidence or a combination of documents and biometrics, reduces the likelihood of individuals using fraudulent identification to establish an identity or at least increases the work factor of potential adversaries. The forms of acceptable evidence are consistent with the risks to the systems, roles, and privileges associated with the user’s account.

### IA-12(03) Identity Evidence Validation and Verification {#ia-12.3}

**Statement.** Require that the presented identity evidence be validated and verified through [methods of validation and verification].

**Guidance.** Validation and verification of identity evidence increases the assurance that accounts and identifiers are being established for the correct user and authenticators are being bound to that user. Validation refers to the process of confirming that the evidence is genuine and authentic, and the data contained in the evidence is correct, current, and related to an individual. Verification confirms and establishes a linkage between the claimed identity and the actual existence of the user presenting the evidence. Acceptable methods for validating and verifying identity evidence are consistent with the risks to the systems, roles, and privileges associated with the users account.

### IA-12(04) In-person Validation and Verification {#ia-12.4}

**Statement.** Require that the validation and verification of identity evidence be conducted in person before a designated registration authority.

**Guidance.** In-person proofing reduces the likelihood of fraudulent credentials being issued because it requires the physical presence of individuals, the presentation of physical identity documents, and actual face-to-face interactions with designated registration authorities.

### IA-12(05) Address Confirmation {#ia-12.5}

**Statement.** Require that a [organization-defined value] be delivered through an out-of-band channel to verify the users address (physical or digital) of record.

**Guidance.** To make it more difficult for adversaries to pose as legitimate users during the identity proofing process, organizations can use out-of-band methods to ensure that the individual associated with an address of record is the same individual that participated in the registration. Confirmation can take the form of a temporary enrollment code or a notice of proofing. The delivery address for these artifacts is obtained from records and not self-asserted by the user. The address can include a physical or digital address. A home address is an example of a physical address. Email addresses and telephone numbers are examples of digital addresses.

### IA-12(06) Accept Externally-proofed Identities {#ia-12.6}

**Statement.** Accept externally-proofed identities at [identity assurance level].

**Guidance.** To limit unnecessary re-proofing of identities, particularly of non-PIV users, organizations accept proofing conducted at a commensurate level of assurance by other agencies or organizations. Proofing is consistent with organizational security policy and the identity assurance level appropriate for the system, application, or information accessed. Accepting externally-proofed identities is a fundamental component of managing federated identities across agencies and organizations.

## IA-13 Identity Providers and Authorization Servers {#ia-13}

**Statement.** Employ identity providers and authorization servers to manage user, device, and non-person entity (NPE) identities, attributes, and access rights supporting authentication and authorization decisions in accordance with [policy] using [mechanisms].

**Guidance.** Identity providers, both internal and external to the organization, manage the user, device, and NPE authenticators and issue statements, often called identity assertions, attesting to identities of other systems or systems components. Authorization servers create and issue access tokens to identified and authenticated users and devices that can be used to gain access to system or information resources. For example, single sign-on (SSO) provides identity provider and authorization server functions. Authenticator management (to include credential management) is covered by IA-05.

### IA-13(01) Protection of Cryptographic Keys {#ia-13.1}

**Statement.** Cryptographic keys that protect access tokens are generated, managed, and protected from disclosure and misuse.

**Guidance.** Identity assertions and access tokens are typically digitally signed. The private keys used to sign these assertions and tokens are protected commensurate with the impact of the system and information resources that can be accessed.

### IA-13(02) Verification of Identity Assertions and Access Tokens {#ia-13.2}

**Statement.** The source and integrity of identity assertions and access tokens are verified before granting access to system and information resources.

**Guidance.** This includes verification of digital signatures protecting identity assertions and access tokens, as well as included metadata. Metadata includes information about the access request such as information unique to user, system or information resource being accessed, or the transaction itself such as time. Protected system and information resources could include connected networks, applications, and APIs.

### IA-13(03) Token Management {#ia-13.3}

**Statement.** In accordance with [ia-13_odp.01], assertions and access tokens are:
- (a) generated;
- (b) issued;
- (c) refreshed;
- (d) revoked;
- (e) time-restricted; and
- (f) audience-restricted.

**Guidance.** An access token is a piece of data that represents the authorization granted to a user or NPE to access specific systems or information resources. Access tokens enable controlled access to services and resources. Properly managing the lifecycle of access tokens, including their issuance, validation, and revocation, is crucial to maintaining confidentiality of data and systems. Restricting token validity to a specific audience, e.g., an application or security domain, and restricting token validity lifetimes are important practices. Access tokens are revoked or invalidated if they are compromised, lost, or are no longer needed to mitigate the risks associated with stolen or misused tokens.
