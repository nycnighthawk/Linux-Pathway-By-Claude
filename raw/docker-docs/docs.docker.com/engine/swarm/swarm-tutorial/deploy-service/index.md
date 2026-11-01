---
{"title": "Deploy a service to the swarm", "url": "https://docs.docker.com/engine/swarm/swarm-tutorial/deploy-service/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Deploy a service to the swarm {#deploy-a-service-to-the-swarm pagefind-weight="10"}

------------------------------------------------------------------------

------------------------------------------------------------------------

After you [create a swarm](https://docs.docker.com/engine/swarm/swarm-tutorial/create-swarm/), you can deploy a service to the swarm. For this tutorial, you also [added worker nodes](https://docs.docker.com/engine/swarm/swarm-tutorial/add-nodes/), but that is not a requirement to deploy a service.

1.  Open a terminal and ssh into the machine where you run your manager node. For example, the tutorial uses a machine named `manager1`.

2.  Run the following command:

    ``` {.chroma tabindex="0"}
    $ docker service create --replicas 1 --name helloworld alpine ping docker.com

    9uk4639qpg7npwf3fn2aasksr
    ```

    -   The `docker service create` command creates the service.
    -   The `--name` flag names the service `helloworld`.
    -   The `--replicas` flag specifies the desired state of 1 running instance.
    -   The arguments `alpine ping docker.com` define the service as an Alpine Linux container that executes the command `ping docker.com`.

3.  Run `docker service ls` to see the list of running services:

    ``` {.chroma tabindex="0"}
    $ docker service ls

    ID            NAME        SCALE  IMAGE   COMMAND
    9uk4639qpg7n  helloworld  1/1    alpine  ping docker.com
    ```

## [Next steps](#next-steps) {#next-steps .scroll-mt-20 .flex .items-center .gap-2}

Now you\'re ready to inspect the service.

[Inspect the service](https://docs.docker.com/engine/swarm/swarm-tutorial/inspect-service/)
