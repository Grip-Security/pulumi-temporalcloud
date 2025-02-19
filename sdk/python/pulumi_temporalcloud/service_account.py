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

__all__ = ['ServiceAccountArgs', 'ServiceAccount']

@pulumi.input_type
class ServiceAccountArgs:
    def __init__(__self__, *,
                 account_access: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_accesses: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceAccountNamespaceAccessArgs']]]] = None,
                 timeouts: Optional[pulumi.Input['ServiceAccountTimeoutsArgs']] = None):
        """
        The set of arguments for constructing a ServiceAccount resource.
        :param pulumi.Input[str] account_access: The role on the account. Must be one of admin, developer, or read (case-insensitive).
        :param pulumi.Input[str] name: The name associated with the service account.
        :param pulumi.Input[Sequence[pulumi.Input['ServiceAccountNamespaceAccessArgs']]] namespace_accesses: The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Service Accounts with an account*access role of admin cannot be assigned explicit permissions to namespaces. Admins implicitly receive access to all Namespaces.
        """
        pulumi.set(__self__, "account_access", account_access)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace_accesses is not None:
            pulumi.set(__self__, "namespace_accesses", namespace_accesses)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter(name="accountAccess")
    def account_access(self) -> pulumi.Input[str]:
        """
        The role on the account. Must be one of admin, developer, or read (case-insensitive).
        """
        return pulumi.get(self, "account_access")

    @account_access.setter
    def account_access(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_access", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name associated with the service account.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namespaceAccesses")
    def namespace_accesses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceAccountNamespaceAccessArgs']]]]:
        """
        The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Service Accounts with an account*access role of admin cannot be assigned explicit permissions to namespaces. Admins implicitly receive access to all Namespaces.
        """
        return pulumi.get(self, "namespace_accesses")

    @namespace_accesses.setter
    def namespace_accesses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceAccountNamespaceAccessArgs']]]]):
        pulumi.set(self, "namespace_accesses", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['ServiceAccountTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['ServiceAccountTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


@pulumi.input_type
class _ServiceAccountState:
    def __init__(__self__, *,
                 account_access: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_accesses: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceAccountNamespaceAccessArgs']]]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 timeouts: Optional[pulumi.Input['ServiceAccountTimeoutsArgs']] = None):
        """
        Input properties used for looking up and filtering ServiceAccount resources.
        :param pulumi.Input[str] account_access: The role on the account. Must be one of admin, developer, or read (case-insensitive).
        :param pulumi.Input[str] name: The name associated with the service account.
        :param pulumi.Input[Sequence[pulumi.Input['ServiceAccountNamespaceAccessArgs']]] namespace_accesses: The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Service Accounts with an account*access role of admin cannot be assigned explicit permissions to namespaces. Admins implicitly receive access to all Namespaces.
        :param pulumi.Input[str] state: The current state of the Service Account.
        """
        if account_access is not None:
            pulumi.set(__self__, "account_access", account_access)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace_accesses is not None:
            pulumi.set(__self__, "namespace_accesses", namespace_accesses)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if timeouts is not None:
            pulumi.set(__self__, "timeouts", timeouts)

    @property
    @pulumi.getter(name="accountAccess")
    def account_access(self) -> Optional[pulumi.Input[str]]:
        """
        The role on the account. Must be one of admin, developer, or read (case-insensitive).
        """
        return pulumi.get(self, "account_access")

    @account_access.setter
    def account_access(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_access", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name associated with the service account.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namespaceAccesses")
    def namespace_accesses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServiceAccountNamespaceAccessArgs']]]]:
        """
        The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Service Accounts with an account*access role of admin cannot be assigned explicit permissions to namespaces. Admins implicitly receive access to all Namespaces.
        """
        return pulumi.get(self, "namespace_accesses")

    @namespace_accesses.setter
    def namespace_accesses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServiceAccountNamespaceAccessArgs']]]]):
        pulumi.set(self, "namespace_accesses", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of the Service Account.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input['ServiceAccountTimeoutsArgs']]:
        return pulumi.get(self, "timeouts")

    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input['ServiceAccountTimeoutsArgs']]):
        pulumi.set(self, "timeouts", value)


class ServiceAccount(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_access: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_accesses: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ServiceAccountNamespaceAccessArgs', 'ServiceAccountNamespaceAccessArgsDict']]]]] = None,
                 timeouts: Optional[pulumi.Input[Union['ServiceAccountTimeoutsArgs', 'ServiceAccountTimeoutsArgsDict']]] = None,
                 __props__=None):
        """
        Provisions a Temporal Cloud Service Account.

        ## Import

        Service Accounts can be imported to incorporate existing Service Accounts into your Terraform pipeline.

        To import a Service Account, you need

        - a resource configuration in your Terraform configuration file/module to accept the imported Service Account. In the example below, the placeholder is "temporalcloud_service_account" "saimport"

        - the Service Accounts's ID, which is found using the Temporal Cloud CLI tcld sa l. In the example below, this is e3cb94fbdbb845f480044d053d00665b

        ```sh
        $ pulumi import temporalcloud:index/serviceAccount:ServiceAccount saimport e3cb94fbdbb845f480044d053d00665b
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_access: The role on the account. Must be one of admin, developer, or read (case-insensitive).
        :param pulumi.Input[str] name: The name associated with the service account.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ServiceAccountNamespaceAccessArgs', 'ServiceAccountNamespaceAccessArgsDict']]]] namespace_accesses: The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Service Accounts with an account*access role of admin cannot be assigned explicit permissions to namespaces. Admins implicitly receive access to all Namespaces.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceAccountArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provisions a Temporal Cloud Service Account.

        ## Import

        Service Accounts can be imported to incorporate existing Service Accounts into your Terraform pipeline.

        To import a Service Account, you need

        - a resource configuration in your Terraform configuration file/module to accept the imported Service Account. In the example below, the placeholder is "temporalcloud_service_account" "saimport"

        - the Service Accounts's ID, which is found using the Temporal Cloud CLI tcld sa l. In the example below, this is e3cb94fbdbb845f480044d053d00665b

        ```sh
        $ pulumi import temporalcloud:index/serviceAccount:ServiceAccount saimport e3cb94fbdbb845f480044d053d00665b
        ```

        :param str resource_name: The name of the resource.
        :param ServiceAccountArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceAccountArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_access: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_accesses: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ServiceAccountNamespaceAccessArgs', 'ServiceAccountNamespaceAccessArgsDict']]]]] = None,
                 timeouts: Optional[pulumi.Input[Union['ServiceAccountTimeoutsArgs', 'ServiceAccountTimeoutsArgsDict']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceAccountArgs.__new__(ServiceAccountArgs)

            if account_access is None and not opts.urn:
                raise TypeError("Missing required property 'account_access'")
            __props__.__dict__["account_access"] = account_access
            __props__.__dict__["name"] = name
            __props__.__dict__["namespace_accesses"] = namespace_accesses
            __props__.__dict__["timeouts"] = timeouts
            __props__.__dict__["state"] = None
        super(ServiceAccount, __self__).__init__(
            'temporalcloud:index/serviceAccount:ServiceAccount',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_access: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace_accesses: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ServiceAccountNamespaceAccessArgs', 'ServiceAccountNamespaceAccessArgsDict']]]]] = None,
            state: Optional[pulumi.Input[str]] = None,
            timeouts: Optional[pulumi.Input[Union['ServiceAccountTimeoutsArgs', 'ServiceAccountTimeoutsArgsDict']]] = None) -> 'ServiceAccount':
        """
        Get an existing ServiceAccount resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_access: The role on the account. Must be one of admin, developer, or read (case-insensitive).
        :param pulumi.Input[str] name: The name associated with the service account.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ServiceAccountNamespaceAccessArgs', 'ServiceAccountNamespaceAccessArgsDict']]]] namespace_accesses: The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Service Accounts with an account*access role of admin cannot be assigned explicit permissions to namespaces. Admins implicitly receive access to all Namespaces.
        :param pulumi.Input[str] state: The current state of the Service Account.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServiceAccountState.__new__(_ServiceAccountState)

        __props__.__dict__["account_access"] = account_access
        __props__.__dict__["name"] = name
        __props__.__dict__["namespace_accesses"] = namespace_accesses
        __props__.__dict__["state"] = state
        __props__.__dict__["timeouts"] = timeouts
        return ServiceAccount(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountAccess")
    def account_access(self) -> pulumi.Output[str]:
        """
        The role on the account. Must be one of admin, developer, or read (case-insensitive).
        """
        return pulumi.get(self, "account_access")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name associated with the service account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namespaceAccesses")
    def namespace_accesses(self) -> pulumi.Output[Optional[Sequence['outputs.ServiceAccountNamespaceAccess']]]:
        """
        The set of namespace accesses. Empty sets are not allowed, omit the attribute instead. Service Accounts with an account*access role of admin cannot be assigned explicit permissions to namespaces. Admins implicitly receive access to all Namespaces.
        """
        return pulumi.get(self, "namespace_accesses")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the Service Account.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional['outputs.ServiceAccountTimeouts']]:
        return pulumi.get(self, "timeouts")

