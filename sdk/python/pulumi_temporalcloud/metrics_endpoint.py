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

__all__ = ['MetricsEndpointArgs', 'MetricsEndpoint']

@pulumi.input_type
class MetricsEndpointArgs:
    def __init__(__self__, *,
                 accepted_client_ca: pulumi.Input[str],
                 timeouts: Optional[pulumi.Input['MetricsEndpointTimeoutsArgs']] = None):
        """
        The set of arguments for constructing a MetricsEndpoint resource.
        :param pulumi.Input[str] accepted_client_ca: The Base64-encoded CA cert in PEM format used to authenticate clients connecting to the metrics endpoint.
        """
        pulumi.set(__self__, "accepted_client_ca", accepted_client_ca)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter(name="acceptedClientCa")
    def accepted_client_ca(self) -> pulumi.Input[str]:
        """
        The Base64-encoded CA cert in PEM format used to authenticate clients connecting to the metrics endpoint.
        """
        return pulumi.get(self, "accepted_client_ca")

    @accepted_client_ca.setter
    def accepted_client_ca(self, value: pulumi.Input[str]):
        pulumi.set(self, "accepted_client_ca", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['MetricsEndpointTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['MetricsEndpointTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


@pulumi.input_type
class _MetricsEndpointState:
    def __init__(__self__, *,
                 accepted_client_ca: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input['MetricsEndpointTimeoutsArgs']] = None,
                 uri: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MetricsEndpoint resources.
        :param pulumi.Input[str] accepted_client_ca: The Base64-encoded CA cert in PEM format used to authenticate clients connecting to the metrics endpoint.
        :param pulumi.Input[str] uri: The Prometheus metrics endpoint URI
        """
        if accepted_client_ca is not None:
            pulumi.set(__self__, "accepted_client_ca", accepted_client_ca)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter(name="acceptedClientCa")
    def accepted_client_ca(self) -> Optional[pulumi.Input[str]]:
        """
        The Base64-encoded CA cert in PEM format used to authenticate clients connecting to the metrics endpoint.
        """
        return pulumi.get(self, "accepted_client_ca")

    @accepted_client_ca.setter
    def accepted_client_ca(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accepted_client_ca", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['MetricsEndpointTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['MetricsEndpointTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        """
        The Prometheus metrics endpoint URI
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)


class MetricsEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accepted_client_ca: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input[Union['MetricsEndpointTimeoutsArgs', 'MetricsEndpointTimeoutsArgsDict']]] = None,
                 __props__=None):
        """
        Configures a Temporal Cloud account's metrics

        ## Import

        ```sh
        $ pulumi import temporalcloud:index/metricsEndpoint:MetricsEndpoint terraform terraform.account-11111-metrics
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accepted_client_ca: The Base64-encoded CA cert in PEM format used to authenticate clients connecting to the metrics endpoint.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MetricsEndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Configures a Temporal Cloud account's metrics

        ## Import

        ```sh
        $ pulumi import temporalcloud:index/metricsEndpoint:MetricsEndpoint terraform terraform.account-11111-metrics
        ```

        :param str resource_name: The name of the resource.
        :param MetricsEndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MetricsEndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accepted_client_ca: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input[Union['MetricsEndpointTimeoutsArgs', 'MetricsEndpointTimeoutsArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MetricsEndpointArgs.__new__(MetricsEndpointArgs)

            if accepted_client_ca is None and not opts.urn:
                raise TypeError("Missing required property 'accepted_client_ca'")
            __props__.__dict__["accepted_client_ca"] = accepted_client_ca
            __props__.__dict__["timeouts"] = timeouts
            __props__.__dict__["uri"] = None
        super(MetricsEndpoint, __self__).__init__(
            'temporalcloud:index/metricsEndpoint:MetricsEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accepted_client_ca: Optional[pulumi.Input[str]] = None,
            timeouts: Optional[pulumi.Input[Union['MetricsEndpointTimeoutsArgs', 'MetricsEndpointTimeoutsArgsDict']]] = None,
            uri: Optional[pulumi.Input[str]] = None) -> 'MetricsEndpoint':
        """
        Get an existing MetricsEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accepted_client_ca: The Base64-encoded CA cert in PEM format used to authenticate clients connecting to the metrics endpoint.
        :param pulumi.Input[str] uri: The Prometheus metrics endpoint URI
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MetricsEndpointState.__new__(_MetricsEndpointState)

        __props__.__dict__["accepted_client_ca"] = accepted_client_ca
        __props__.__dict__["timeouts"] = timeouts
        __props__.__dict__["uri"] = uri
        return MetricsEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acceptedClientCa")
    def accepted_client_ca(self) -> pulumi.Output[str]:
        """
        The Base64-encoded CA cert in PEM format used to authenticate clients connecting to the metrics endpoint.
        """
        return pulumi.get(self, "accepted_client_ca")

    @property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional['outputs.MetricsEndpointTimeouts']]:
        return pulumi.get(self, "timeouts")

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Output[str]:
        """
        The Prometheus metrics endpoint URI
        """
        return pulumi.get(self, "uri")

