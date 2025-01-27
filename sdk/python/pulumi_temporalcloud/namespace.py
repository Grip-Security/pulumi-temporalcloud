# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['NamespaceArgs', 'Namespace']

@pulumi.input_type
class NamespaceArgs:
    def __init__(__self__, *,
                 regions: pulumi.Input[Sequence[pulumi.Input[str]]],
                 retention_days: pulumi.Input[int],
                 accepted_client_ca: Optional[pulumi.Input[str]] = None,
                 api_key_auth: Optional[pulumi.Input[bool]] = None,
                 certificate_filters: Optional[pulumi.Input[Sequence[pulumi.Input['NamespaceCertificateFilterArgs']]]] = None,
                 codec_server: Optional[pulumi.Input['NamespaceCodecServerArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input['NamespaceTimeoutsArgs']] = None):
        """
        The set of arguments for constructing a Namespace resource.
        :param pulumi.Input[int] retention_days: The number of days to retain workflow history. Any changes to the retention period will be applied to all new running workflows.
        :param pulumi.Input[str] accepted_client_ca: The Base64-encoded CA cert in PEM format that clients use when authenticating with Temporal Cloud. This is a required field when a Namespace uses mTLS authentication.
        :param pulumi.Input[bool] api_key_auth: If true, Temporal Cloud will use API key authentication for this namespace. If false, mutual TLS (mTLS) authentication will be used.
        :param pulumi.Input[Sequence[pulumi.Input['NamespaceCertificateFilterArgs']]] certificate_filters: A list of filters to apply to client certificates when initiating a connection Temporal Cloud. If present, connections will only be allowed from client certificates whose distinguished name properties match at least one of the filters. Empty lists are not allowed, omit the attribute instead.
        :param pulumi.Input['NamespaceCodecServerArgs'] codec_server: A codec server is used by the Temporal Cloud UI to decode payloads for all users interacting with this namespace, even if the workflow history itself is encrypted.
        :param pulumi.Input[str] name: The name of the namespace.
        """
        pulumi.set(__self__, "regions", regions)
        pulumi.set(__self__, "retention_days", retention_days)
        if accepted_client_ca is not None:
            pulumi.set(__self__, "accepted_client_ca", accepted_client_ca)
        if api_key_auth is not None:
            pulumi.set(__self__, "api_key_auth", api_key_auth)
        if certificate_filters is not None:
            pulumi.set(__self__, "certificate_filters", certificate_filters)
        if codec_server is not None:
            pulumi.set(__self__, "codec_server", codec_server)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter
    def regions(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "regions")

    @regions.setter
    def regions(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "regions", value)

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> pulumi.Input[int]:
        """
        The number of days to retain workflow history. Any changes to the retention period will be applied to all new running workflows.
        """
        return pulumi.get(self, "retention_days")

    @retention_days.setter
    def retention_days(self, value: pulumi.Input[int]):
        pulumi.set(self, "retention_days", value)

    @property
    @pulumi.getter(name="acceptedClientCa")
    def accepted_client_ca(self) -> Optional[pulumi.Input[str]]:
        """
        The Base64-encoded CA cert in PEM format that clients use when authenticating with Temporal Cloud. This is a required field when a Namespace uses mTLS authentication.
        """
        return pulumi.get(self, "accepted_client_ca")

    @accepted_client_ca.setter
    def accepted_client_ca(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accepted_client_ca", value)

    @property
    @pulumi.getter(name="apiKeyAuth")
    def api_key_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, Temporal Cloud will use API key authentication for this namespace. If false, mutual TLS (mTLS) authentication will be used.
        """
        return pulumi.get(self, "api_key_auth")

    @api_key_auth.setter
    def api_key_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "api_key_auth", value)

    @property
    @pulumi.getter(name="certificateFilters")
    def certificate_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NamespaceCertificateFilterArgs']]]]:
        """
        A list of filters to apply to client certificates when initiating a connection Temporal Cloud. If present, connections will only be allowed from client certificates whose distinguished name properties match at least one of the filters. Empty lists are not allowed, omit the attribute instead.
        """
        return pulumi.get(self, "certificate_filters")

    @certificate_filters.setter
    def certificate_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NamespaceCertificateFilterArgs']]]]):
        pulumi.set(self, "certificate_filters", value)

    @property
    @pulumi.getter(name="codecServer")
    def codec_server(self) -> Optional[pulumi.Input['NamespaceCodecServerArgs']]:
        """
        A codec server is used by the Temporal Cloud UI to decode payloads for all users interacting with this namespace, even if the workflow history itself is encrypted.
        """
        return pulumi.get(self, "codec_server")

    @codec_server.setter
    def codec_server(self, value: Optional[pulumi.Input['NamespaceCodecServerArgs']]):
        pulumi.set(self, "codec_server", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the namespace.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['NamespaceTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['NamespaceTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


@pulumi.input_type
class _NamespaceState:
    def __init__(__self__, *,
                 accepted_client_ca: Optional[pulumi.Input[str]] = None,
                 api_key_auth: Optional[pulumi.Input[bool]] = None,
                 certificate_filters: Optional[pulumi.Input[Sequence[pulumi.Input['NamespaceCertificateFilterArgs']]]] = None,
                 codec_server: Optional[pulumi.Input['NamespaceCodecServerArgs']] = None,
                 endpoints: Optional[pulumi.Input['NamespaceEndpointsArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 retention_days: Optional[pulumi.Input[int]] = None,
                 timeouts: Optional[pulumi.Input['NamespaceTimeoutsArgs']] = None):
        """
        Input properties used for looking up and filtering Namespace resources.
        :param pulumi.Input[str] accepted_client_ca: The Base64-encoded CA cert in PEM format that clients use when authenticating with Temporal Cloud. This is a required field when a Namespace uses mTLS authentication.
        :param pulumi.Input[bool] api_key_auth: If true, Temporal Cloud will use API key authentication for this namespace. If false, mutual TLS (mTLS) authentication will be used.
        :param pulumi.Input[Sequence[pulumi.Input['NamespaceCertificateFilterArgs']]] certificate_filters: A list of filters to apply to client certificates when initiating a connection Temporal Cloud. If present, connections will only be allowed from client certificates whose distinguished name properties match at least one of the filters. Empty lists are not allowed, omit the attribute instead.
        :param pulumi.Input['NamespaceCodecServerArgs'] codec_server: A codec server is used by the Temporal Cloud UI to decode payloads for all users interacting with this namespace, even if the workflow history itself is encrypted.
        :param pulumi.Input['NamespaceEndpointsArgs'] endpoints: The endpoints for the namespace.
        :param pulumi.Input[str] name: The name of the namespace.
        :param pulumi.Input[int] retention_days: The number of days to retain workflow history. Any changes to the retention period will be applied to all new running workflows.
        """
        if accepted_client_ca is not None:
            pulumi.set(__self__, "accepted_client_ca", accepted_client_ca)
        if api_key_auth is not None:
            pulumi.set(__self__, "api_key_auth", api_key_auth)
        if certificate_filters is not None:
            pulumi.set(__self__, "certificate_filters", certificate_filters)
        if codec_server is not None:
            pulumi.set(__self__, "codec_server", codec_server)
        if endpoints is not None:
            pulumi.set(__self__, "endpoints", endpoints)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if regions is not None:
            pulumi.set(__self__, "regions", regions)
        if retention_days is not None:
            pulumi.set(__self__, "retention_days", retention_days)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter(name="acceptedClientCa")
    def accepted_client_ca(self) -> Optional[pulumi.Input[str]]:
        """
        The Base64-encoded CA cert in PEM format that clients use when authenticating with Temporal Cloud. This is a required field when a Namespace uses mTLS authentication.
        """
        return pulumi.get(self, "accepted_client_ca")

    @accepted_client_ca.setter
    def accepted_client_ca(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accepted_client_ca", value)

    @property
    @pulumi.getter(name="apiKeyAuth")
    def api_key_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, Temporal Cloud will use API key authentication for this namespace. If false, mutual TLS (mTLS) authentication will be used.
        """
        return pulumi.get(self, "api_key_auth")

    @api_key_auth.setter
    def api_key_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "api_key_auth", value)

    @property
    @pulumi.getter(name="certificateFilters")
    def certificate_filters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NamespaceCertificateFilterArgs']]]]:
        """
        A list of filters to apply to client certificates when initiating a connection Temporal Cloud. If present, connections will only be allowed from client certificates whose distinguished name properties match at least one of the filters. Empty lists are not allowed, omit the attribute instead.
        """
        return pulumi.get(self, "certificate_filters")

    @certificate_filters.setter
    def certificate_filters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NamespaceCertificateFilterArgs']]]]):
        pulumi.set(self, "certificate_filters", value)

    @property
    @pulumi.getter(name="codecServer")
    def codec_server(self) -> Optional[pulumi.Input['NamespaceCodecServerArgs']]:
        """
        A codec server is used by the Temporal Cloud UI to decode payloads for all users interacting with this namespace, even if the workflow history itself is encrypted.
        """
        return pulumi.get(self, "codec_server")

    @codec_server.setter
    def codec_server(self, value: Optional[pulumi.Input['NamespaceCodecServerArgs']]):
        pulumi.set(self, "codec_server", value)

    @property
    @pulumi.getter
    def endpoints(self) -> Optional[pulumi.Input['NamespaceEndpointsArgs']]:
        """
        The endpoints for the namespace.
        """
        return pulumi.get(self, "endpoints")

    @endpoints.setter
    def endpoints(self, value: Optional[pulumi.Input['NamespaceEndpointsArgs']]):
        pulumi.set(self, "endpoints", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the namespace.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "regions")

    @regions.setter
    def regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "regions", value)

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[pulumi.Input[int]]:
        """
        The number of days to retain workflow history. Any changes to the retention period will be applied to all new running workflows.
        """
        return pulumi.get(self, "retention_days")

    @retention_days.setter
    def retention_days(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "retention_days", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['NamespaceTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['NamespaceTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


class Namespace(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accepted_client_ca: Optional[pulumi.Input[str]] = None,
                 api_key_auth: Optional[pulumi.Input[bool]] = None,
                 certificate_filters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['NamespaceCertificateFilterArgs', 'NamespaceCertificateFilterArgsDict']]]]] = None,
                 codec_server: Optional[pulumi.Input[Union['NamespaceCodecServerArgs', 'NamespaceCodecServerArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 retention_days: Optional[pulumi.Input[int]] = None,
                 timeouts: Optional[pulumi.Input[Union['NamespaceTimeoutsArgs', 'NamespaceTimeoutsArgsDict']]] = None,
                 __props__=None):
        """
        Provisions a Temporal Cloud namespace.

        ## Import

        Namespace can be imported to incorporate existing Namespaces into your Terraform pipeline.

        To import a Namespace, you need

        - a resource configuration in your Terraform configuration file/module to accept the imported Namespace. In the example below, the placeholder is "temporalcloud_namespace" "terraform"

        - the Namespace ID, which includes the Namespace Name and Account ID available at the top of the Namespace's page in the Temporal Cloud UI. In the example below, this is namespaceid.acctid

        ```sh
        $ pulumi import temporalcloud:index/namespace:Namespace terraform namespaceid.acctid
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accepted_client_ca: The Base64-encoded CA cert in PEM format that clients use when authenticating with Temporal Cloud. This is a required field when a Namespace uses mTLS authentication.
        :param pulumi.Input[bool] api_key_auth: If true, Temporal Cloud will use API key authentication for this namespace. If false, mutual TLS (mTLS) authentication will be used.
        :param pulumi.Input[Sequence[pulumi.Input[Union['NamespaceCertificateFilterArgs', 'NamespaceCertificateFilterArgsDict']]]] certificate_filters: A list of filters to apply to client certificates when initiating a connection Temporal Cloud. If present, connections will only be allowed from client certificates whose distinguished name properties match at least one of the filters. Empty lists are not allowed, omit the attribute instead.
        :param pulumi.Input[Union['NamespaceCodecServerArgs', 'NamespaceCodecServerArgsDict']] codec_server: A codec server is used by the Temporal Cloud UI to decode payloads for all users interacting with this namespace, even if the workflow history itself is encrypted.
        :param pulumi.Input[str] name: The name of the namespace.
        :param pulumi.Input[int] retention_days: The number of days to retain workflow history. Any changes to the retention period will be applied to all new running workflows.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamespaceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provisions a Temporal Cloud namespace.

        ## Import

        Namespace can be imported to incorporate existing Namespaces into your Terraform pipeline.

        To import a Namespace, you need

        - a resource configuration in your Terraform configuration file/module to accept the imported Namespace. In the example below, the placeholder is "temporalcloud_namespace" "terraform"

        - the Namespace ID, which includes the Namespace Name and Account ID available at the top of the Namespace's page in the Temporal Cloud UI. In the example below, this is namespaceid.acctid

        ```sh
        $ pulumi import temporalcloud:index/namespace:Namespace terraform namespaceid.acctid
        ```

        :param str resource_name: The name of the resource.
        :param NamespaceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamespaceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accepted_client_ca: Optional[pulumi.Input[str]] = None,
                 api_key_auth: Optional[pulumi.Input[bool]] = None,
                 certificate_filters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['NamespaceCertificateFilterArgs', 'NamespaceCertificateFilterArgsDict']]]]] = None,
                 codec_server: Optional[pulumi.Input[Union['NamespaceCodecServerArgs', 'NamespaceCodecServerArgsDict']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 retention_days: Optional[pulumi.Input[int]] = None,
                 timeouts: Optional[pulumi.Input[Union['NamespaceTimeoutsArgs', 'NamespaceTimeoutsArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NamespaceArgs.__new__(NamespaceArgs)

            __props__.__dict__["accepted_client_ca"] = accepted_client_ca
            __props__.__dict__["api_key_auth"] = api_key_auth
            __props__.__dict__["certificate_filters"] = certificate_filters
            __props__.__dict__["codec_server"] = codec_server
            __props__.__dict__["name"] = name
            if regions is None and not opts.urn:
                raise TypeError("Missing required property 'regions'")
            __props__.__dict__["regions"] = regions
            if retention_days is None and not opts.urn:
                raise TypeError("Missing required property 'retention_days'")
            __props__.__dict__["retention_days"] = retention_days
            __props__.__dict__["timeouts"] = timeouts
            __props__.__dict__["endpoints"] = None
        super(Namespace, __self__).__init__(
            'temporalcloud:index/namespace:Namespace',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accepted_client_ca: Optional[pulumi.Input[str]] = None,
            api_key_auth: Optional[pulumi.Input[bool]] = None,
            certificate_filters: Optional[pulumi.Input[Sequence[pulumi.Input[Union['NamespaceCertificateFilterArgs', 'NamespaceCertificateFilterArgsDict']]]]] = None,
            codec_server: Optional[pulumi.Input[Union['NamespaceCodecServerArgs', 'NamespaceCodecServerArgsDict']]] = None,
            endpoints: Optional[pulumi.Input[Union['NamespaceEndpointsArgs', 'NamespaceEndpointsArgsDict']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            retention_days: Optional[pulumi.Input[int]] = None,
            timeouts: Optional[pulumi.Input[Union['NamespaceTimeoutsArgs', 'NamespaceTimeoutsArgsDict']]] = None) -> 'Namespace':
        """
        Get an existing Namespace resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accepted_client_ca: The Base64-encoded CA cert in PEM format that clients use when authenticating with Temporal Cloud. This is a required field when a Namespace uses mTLS authentication.
        :param pulumi.Input[bool] api_key_auth: If true, Temporal Cloud will use API key authentication for this namespace. If false, mutual TLS (mTLS) authentication will be used.
        :param pulumi.Input[Sequence[pulumi.Input[Union['NamespaceCertificateFilterArgs', 'NamespaceCertificateFilterArgsDict']]]] certificate_filters: A list of filters to apply to client certificates when initiating a connection Temporal Cloud. If present, connections will only be allowed from client certificates whose distinguished name properties match at least one of the filters. Empty lists are not allowed, omit the attribute instead.
        :param pulumi.Input[Union['NamespaceCodecServerArgs', 'NamespaceCodecServerArgsDict']] codec_server: A codec server is used by the Temporal Cloud UI to decode payloads for all users interacting with this namespace, even if the workflow history itself is encrypted.
        :param pulumi.Input[Union['NamespaceEndpointsArgs', 'NamespaceEndpointsArgsDict']] endpoints: The endpoints for the namespace.
        :param pulumi.Input[str] name: The name of the namespace.
        :param pulumi.Input[int] retention_days: The number of days to retain workflow history. Any changes to the retention period will be applied to all new running workflows.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NamespaceState.__new__(_NamespaceState)

        __props__.__dict__["accepted_client_ca"] = accepted_client_ca
        __props__.__dict__["api_key_auth"] = api_key_auth
        __props__.__dict__["certificate_filters"] = certificate_filters
        __props__.__dict__["codec_server"] = codec_server
        __props__.__dict__["endpoints"] = endpoints
        __props__.__dict__["name"] = name
        __props__.__dict__["regions"] = regions
        __props__.__dict__["retention_days"] = retention_days
        __props__.__dict__["timeouts"] = timeouts
        return Namespace(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acceptedClientCa")
    def accepted_client_ca(self) -> pulumi.Output[Optional[str]]:
        """
        The Base64-encoded CA cert in PEM format that clients use when authenticating with Temporal Cloud. This is a required field when a Namespace uses mTLS authentication.
        """
        return pulumi.get(self, "accepted_client_ca")

    @property
    @pulumi.getter(name="apiKeyAuth")
    def api_key_auth(self) -> pulumi.Output[bool]:
        """
        If true, Temporal Cloud will use API key authentication for this namespace. If false, mutual TLS (mTLS) authentication will be used.
        """
        return pulumi.get(self, "api_key_auth")

    @property
    @pulumi.getter(name="certificateFilters")
    def certificate_filters(self) -> pulumi.Output[Optional[Sequence['outputs.NamespaceCertificateFilter']]]:
        """
        A list of filters to apply to client certificates when initiating a connection Temporal Cloud. If present, connections will only be allowed from client certificates whose distinguished name properties match at least one of the filters. Empty lists are not allowed, omit the attribute instead.
        """
        return pulumi.get(self, "certificate_filters")

    @property
    @pulumi.getter(name="codecServer")
    def codec_server(self) -> pulumi.Output[Optional['outputs.NamespaceCodecServer']]:
        """
        A codec server is used by the Temporal Cloud UI to decode payloads for all users interacting with this namespace, even if the workflow history itself is encrypted.
        """
        return pulumi.get(self, "codec_server")

    @property
    @pulumi.getter
    def endpoints(self) -> pulumi.Output['outputs.NamespaceEndpoints']:
        """
        The endpoints for the namespace.
        """
        return pulumi.get(self, "endpoints")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the namespace.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def regions(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "regions")

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> pulumi.Output[int]:
        """
        The number of days to retain workflow history. Any changes to the retention period will be applied to all new running workflows.
        """
        return pulumi.get(self, "retention_days")

    @property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional['outputs.NamespaceTimeouts']]:
        return pulumi.get(self, "timeouts")

