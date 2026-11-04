---
{"title": "Export to Docker with GitHub Actions", "url": "https://docs.docker.com/build/ci/github-actions/export-docker/", "retrieved": "2026-11-01", "license": "Apache-2.0"}
---

# Export to Docker with GitHub Actions {#export-to-docker-with-github-actions pagefind-weight="10"}

------------------------------------------------------------------------

------------------------------------------------------------------------

You may want your build result to be available in the Docker client through `docker images` to be able to use it in another step of your workflow:

``` {.chroma tabindex="0"}
name: ci

on:
  push:

jobs:
  docker:
    runs-on: ubuntu-latest
    steps:
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v4
      
      - name: Build
        uses: docker/build-push-action@v7
        with:
          load: true
          tags: myimage:latest
      
      - name: Inspect
        run: |
          docker image inspect myimage:latest
```
