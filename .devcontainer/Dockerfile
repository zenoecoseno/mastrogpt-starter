FROM node:22

# Install basic development tools
RUN \
     apt update && \
     apt install -y less man-db sudo vim jq python-is-python3 python3-virtualenv

# Ensure default `node` user has access to `sudo`
ARG USERNAME=node
RUN \
    echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# install ops and plugins
USER node
RUN \
    LATEST=https://api.github.com/repos/apache/openserverless-cli/releases/latest ;\
    VERSION=$(curl -s  "$LATEST" | jq -r '.name | .[1:]') ;\
    echo downloading ops $VERSION ;\
    curl -sL https://bit.ly/get-ops | VERSION=$VERSION bash
ENV PATH="/home/node/.local/bin:${PATH}"
RUN \
    ops -update
RUN \
    ops -plugin https://github.com/mastrogpt/olaris-ai ;\
    ops ai
