# python-template

## GitHub Actions publishing

Before running `.github/workflows/publish.yml`, register a
[PyPI trusted publisher](https://docs.pypi.org/trusted-publishers/adding-a-publisher/)
for the package. Use this GitHub repository's owner and name, workflow filename
`publish.yml`, and no environment name. The workflow uses GitHub OIDC and no longer
reads the `PYPI_TOKEN` secret.

The version bump workflow still needs `PAT_TOKEN` with repository contents write
access to push commits and tags and trigger the publishing workflows.
