# Install Dependencies Using Poetry
The project depends on libraries that are not published in the official Python Package
Index (PyPI). These packages are hosted in the private TINAA GitLab instance, which use
self-signed certificates. In order to successfully connect to the TINAA package
registry, Poetry has to be configured to accept the TINAA root certificate.
This can be done with the following command:

```text
poetry config certificates.tinaa.cert <path_to_root_certificate.pem>
```

The root certificate can be found in the repository, for example under backend/cacerts
folder.

Once the certificate is configured to be accepted by Poetry, the dependencies of the
service can be installed by simply issuing:

```text
poetry install
```

# Configure Robot Framework Language Server

PyCharm Plugin: https://plugins.jetbrains.com/plugin/16086-robot-framework-language-server
VS Code Extension: https://marketplace.visualstudio.com/items?itemName=robocorp.robotframework-lsp
