## S3 Viewer with RBAC Prototype

Based on https://www.jpmorgan.com/technology/technology-blog/protecting-web-applications-via-envoy-oauth2-filter

Uses https://hidekuma.github.io/flask-s3-viewer/html/index.html

``` mermaid
flowchart LR
    subgraph k8s
        ingress
        ingress-->envoy-proxy-sidecar
        subgraph pod
            
            envoy-proxy-sidecar-->s3-viewer
        end
    end
    user-->|bearer token|ingress
    user-.get token.->oidc-provider
    envoy-proxy-sidecar-.verify token.->oidc-provider
    s3[(S3)]
    s3-viewer-->s3
```

### Running

#### Reqs
* Docker
    * envoyproxy/envoy-dev
    * ghcr.io/soluto/oidc-server-mock:latest
* docker-compose
* Python >= 3.7


#### Steps


1. Clone this repo
1. python -m venv env
1. source ./env/bin/activate
1. pip install -r requirements.txt
1. run ./build-container.sh
1. docker-compose up
1. navigate to http://localhost:10000 , use User1/pwd for credentials
