ARG BUILD_FROM
FROM $BUILD_FROM

# Install requirements for add-on
RUN \
  apk add --no-cache \
    python3 py3-pip \
  && pip3 install \
    --no-cache-dir \
    --prefer-binary \
    Flask requests

# Copy data for add-on
COPY rootfs /