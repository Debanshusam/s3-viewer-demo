## S3 Viewer with RBAC Prototype

``` mermaid
flowchart LR
    subgraph k8s
        subgraph pod
            envoy-proxy-sidecar-->s3-viewer
        end
    end
    user-->envoy-proxy-sidecar
    user-->oidc-provider
    envoy-proxy-sidecar-->oidc-provider
    s3-viewer-->s3
```

### Running

#### Reqs
* Docker
    * envoyproxy/envoy-dev
    * ghcr.io/soluto/oidc-server-mock:latest
* docker-compose
* Python > 3.7


#### Steps


1. Clone this repo
1. python -m venv env
1. source ./env/bin/activate
1. run ./build-container.sh
1. docker-compose up
1. navigate to http://localhost:10000 , use User1/pwd for credentials
