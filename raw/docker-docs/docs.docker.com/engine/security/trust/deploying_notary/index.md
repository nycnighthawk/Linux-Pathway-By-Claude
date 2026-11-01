---
{"title": "Deploy Notary Server with Compose", "url": "https://docs.docker.com/engine/security/trust/deploying_notary/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Deploy Notary Server with Compose {#deploy-notary-server-with-compose pagefind-weight="10"}

------------------------------------------------------------------------

Table of contents

------------------------------------------------------------------------

The easiest way to deploy Notary Server is by using Docker Compose. To follow the procedure on this page, you must have already [installed Docker Compose](https://docs.docker.com/compose/install/).

1.  Clone the Notary repository.

    ``` {.chroma tabindex="0"}
    $ git clone https://github.com/theupdateframework/notary.git
    ```

2.  Build and start Notary Server with the sample certificates.

    ``` {.chroma tabindex="0"}
    $ docker compose up -d 
    ```

    For more detailed documentation about how to deploy Notary Server, see the [instructions to run a Notary service](https://github.com/theupdateframework/notary/blob/master/docs/running_a_service.md) as well as [the Notary repository](https://github.com/theupdateframework/notary) for more information.

3.  Make sure that your Docker or Notary client trusts Notary Server\'s certificate before you try to interact with the Notary server.

See the instructions for [Docker](/reference/cli/docker/#notary) or for [Notary](https://github.com/docker/notary#using-notary) depending on which one you are using.

## [If you want to use Notary in production](#if-you-want-to-use-notary-in-production) {#if-you-want-to-use-notary-in-production .scroll-mt-20 .flex .items-center .gap-2}

The Compose sample on this page is for local testing and uses sample certificates. For a production deployment, follow the upstream [instructions to run a Notary service](https://github.com/theupdateframework/notary/blob/master/docs/running_a_service.md) and the rest of [the Notary repository](https://github.com/theupdateframework/notary).
