---
{"title": "Migrating from Ingress to Gateway", "url": "https://docs.cilium.io/en/stable/network/servicemesh/ingress-to-gateway/ingress-to-gateway/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Migrating from Ingress to Gateway[](#migrating-from-ingress-to-gateway "Link to this heading")

The Gateway API is not only the long-term successor to the Ingress API, it also supports use cases beyond HTTP/HTTPS-based applications.

This section highlights some of the limitations with Ingress, explains some of the benefits of the Gateway API, and describes some of the options available with migrating from Ingress API to Gateway API.

## Ingress API Limitations[](#ingress-api-limitations "Link to this heading")

Development of the Gateway API stemmed from the realization that the Kubernetes Ingress API has some limitations.

-   Limited support for advanced routing

The Ingress API supports basic routing based on path and host rules, but it lacks native support for more advanced routing features such as traffic splitting, header modification, and URL rewriting.

-   Limited protocol support

The Ingress API only supports HTTP and HTTPS traffic, and does not natively support other protocols like TCP or UDP. The Ingress API specification was too limited and not extensible enough. To address these technical limitations, software vendors and developers created vendor-specific annotations. However, using annotations created inconsistencies from one Ingress Controller to another. For example, issues often arise when switching from one Ingress Controller to another because annotations are often vendor-specific.

-   Operational constraints

Finally, the Ingress API suffers from operational constraints: it is not well suited for multi-team clusters with shared load-balancing infrastructure.

## Benefits of the Gateway API[](#benefits-of-the-gateway-api "Link to this heading")

The Gateway API was designed to address the limitations of Ingress API. The [Kubernetes SIG-Network](https://github.com/kubernetes/community/tree/master/sig-network) team designs and maintains the Gateway API.

For more information about the Gateway API, see [the Gateway API project page](https://gateway-api.sigs.k8s.io/).

The Gateway API provides a centralized mechanism for managing and enforcing policies for external traffic, including HTTP routing, TLS termination, traffic splitting/weighting, and header modification.

Native support of policies for external traffic means that annotations are no longer required to support ingress traffic patterns. This means that Gateway API resources are more portable from one Gateway API implementation to another.

When customization is required, Gateway API provides several flexible models, including specific extension points to enable diverse traffic patterns. As the Gateway API team adds extensions, the team looks for common denominators and promotes features of API conformance to maximize the ease of extending Ingress API resources.

Finally, the Gateway API is designed with role-based personas in mind. The Ingress model is based on a persona where developers manage and create ingress and service resources themselves.

In more complex deployments, more personas are involved:

-   Infrastructure Providers administrate the managed services of a cloud provider, or the infrastructure/network team when running Kubernetes on-premises.

-   Cluster Operators are responsible for the administration of a cluster.

-   Application Developers are responsible for defining application configuration and service composition.

By deconstructing the Ingress API into several Gateway API objects, personas gain the specific access and privileges that their responsibilities require.

For example, application developers in a specific team could be assigned permissions to create Route objects in a specified namespace without also gaining permissions to modify the Gateway configuration or edit Route objects in namespaces other than theirs.

## Recommended Migration Workflow[](#recommended-migration-workflow "Link to this heading")

Use this workflow for a smoother migration:

1.  Build migration scope and rollout phases.

2.  Inventory and classify your current NGINX annotations with [NGINX Ingress Annotations to Gateway API Migration](../nginx-annotations-migration/#gs-ingress-to-gateway-nginx-annotations).

3.  Create equivalent Gateway API resources and validate in parallel.

4.  Roll traffic gradually and monitor SLOs.

5.  Remove legacy Ingress resources after stabilization.

## Migration Methods[](#migration-methods "Link to this heading")

There are two primary methods to migrate Ingress API resources to Gateway API:

-   *manual*: manually creating Gateway API resources based on existing Ingress API resources.

-   *automated*: creating rules using the [ingress2gateway tool](https://github.com/kubernetes-sigs/ingress2gateway). The ingress2gateway project reads Ingress resources from a Kubernetes cluster based on your current Kube Config. It outputs YAML for equivalent Gateway API resources to stdout.

Note

The `ingress2gateway`{.docutils .literal .notranslate} tool remains experimental and is not recommended for production.

## Ingress Annotations Migration[](#ingress-annotations-migration "Link to this heading")

Most Ingress controllers use annotations to provide support for specific features, such as HTTP request manipulation and routing. As noted in [Benefits of the Gateway API](#benefits-of-the-gateway-api), the Gateway API avoids implementation-specific annotations in order to provide a portable configuration.

As a consequence, it's rare to port implementation-specific Ingress annotations to a Gateway API resource. Instead, the Gateway API provides native support for some of these features, including:

-   Request/response manipulation

-   Traffic splitting

-   Header, query parameter, or method-based routing

For NGINX-based migrations, use [NGINX Ingress Annotations to Gateway API Migration](../nginx-annotations-migration/#gs-ingress-to-gateway-nginx-annotations), which provides mapping hints.

## Migration Guides and Examples[](#migration-guides-and-examples "Link to this heading")

For examples of migrating to Cilium's Gateway API features, see:

-   [HTTP Migration Example](../http-migration/)
-   [TLS Migration](../tls-migration/)
-   [NGINX Ingress Annotations to Gateway API Migration](../nginx-annotations-migration/)
