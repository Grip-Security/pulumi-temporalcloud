---
title: Temporal Cloud Installation & Configuration
meta_desc: Information on how to install the Temporal Cloud provider.
layout: package
---

## Installation

The Pulumi Temporal Cloud provider is available as a package in all Pulumi languages:

* JavaScript/TypeScript: [`@grip-security/pulumi-temporalcloud`](https://www.npmjs.com/package/@grip-security/pulumi-temporalcloud)
* Python: [`pulumi-temporalcloud`](https://pypi.org/project/pulumi-temporalcloud/)
* Go: [`github.com/Grip-Security/pulumi-temporalcloud/sdk/go/temporalcloud`](https://pkg.go.dev/github.com/Grip-Security/pulumi-temporalcloud/sdk)
* .NET: [`GripSecurity.PulumiTemporalCloud`](https://www.nuget.org/packages/GripSecurity.PulumiTemporalCloud)

### Provider Binary

The Temporal Cloud provider binary is a third party binary. It can be installed using the `pulumi plugin` command.

```bash
pulumi plugin install resource temporalcloud <version>
```

Replace the version string with your desired version.

## Setup

To provision resources with the Pulumi Temporal Cloud provider, you need to have Temporal Cloud API key.
See [this documentation](https://docs.temporal.io/cloud/api-keys) for information on how to obtain an API key.

### Set environment variables

Coming soon
