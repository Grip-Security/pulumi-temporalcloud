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

__all__ = ['NamespaceSearchAttributeArgs', 'NamespaceSearchAttribute']

@pulumi.input_type
class NamespaceSearchAttributeArgs:
    def __init__(__self__, *,
                 namespace_id: pulumi.Input[str],
                 type: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a NamespaceSearchAttribute resource.
        :param pulumi.Input[str] namespace_id: The ID of the namespace to which this search attribute belongs.
        :param pulumi.Input[str] type: The type of the search attribute. Must be one of `bool`, `datetime`, `double`, `int`, `keyword`, `keyword_list` or `text`. (case-insensitive)
        :param pulumi.Input[str] name: The name of the search attribute.
        """
        pulumi.set(__self__, "namespace_id", namespace_id)
        pulumi.set(__self__, "type", type)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> pulumi.Input[str]:
        """
        The ID of the namespace to which this search attribute belongs.
        """
        return pulumi.get(self, "namespace_id")

    @namespace_id.setter
    def namespace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of the search attribute. Must be one of `bool`, `datetime`, `double`, `int`, `keyword`, `keyword_list` or `text`. (case-insensitive)
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the search attribute.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _NamespaceSearchAttributeState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering NamespaceSearchAttribute resources.
        :param pulumi.Input[str] name: The name of the search attribute.
        :param pulumi.Input[str] namespace_id: The ID of the namespace to which this search attribute belongs.
        :param pulumi.Input[str] type: The type of the search attribute. Must be one of `bool`, `datetime`, `double`, `int`, `keyword`, `keyword_list` or `text`. (case-insensitive)
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if namespace_id is not None:
            pulumi.set(__self__, "namespace_id", namespace_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the search attribute.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the namespace to which this search attribute belongs.
        """
        return pulumi.get(self, "namespace_id")

    @namespace_id.setter
    def namespace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "namespace_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the search attribute. Must be one of `bool`, `datetime`, `double`, `int`, `keyword`, `keyword_list` or `text`. (case-insensitive)
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class NamespaceSearchAttribute(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a [search attribute](https://docs.temporal.io/visibility#search-attribute) in a Temporal Cloud namespace. Note the limits on [quantity](https://docs.temporal.io/cloud/limits#number-of-custom-search-attributes) and [naming](https://docs.temporal.io/cloud/limits#custom-search-attribute-names).

        ## Import

        Search Attributes can be imported to incorporate existing Namespace Search Attributes into your Terraform pipeline.

        To import a Search Attribute, you need

        - a resource configuration in your Terraform configuration file/module to accept the imported Search Attribute. In the example below, the placeholder is "temporalcloud_namespace_search_attribute" "saimport"

        - the Namespace ID, which includes the Namespace Name and Account ID available at the top of the Namespace's page in the Temporal Cloud UI. In the example below, this is namespaceid.acctid

        - the name of the Search Attribute, which is available in the Search Attribute configuration of Namespace's page in the Temporal Cloud UI. In the example below, this is searchAttr

        ```sh
        $ pulumi import temporalcloud:index/namespaceSearchAttribute:NamespaceSearchAttribute saimport namespaceid.acctid/searchAttr
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the search attribute.
        :param pulumi.Input[str] namespace_id: The ID of the namespace to which this search attribute belongs.
        :param pulumi.Input[str] type: The type of the search attribute. Must be one of `bool`, `datetime`, `double`, `int`, `keyword`, `keyword_list` or `text`. (case-insensitive)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamespaceSearchAttributeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a [search attribute](https://docs.temporal.io/visibility#search-attribute) in a Temporal Cloud namespace. Note the limits on [quantity](https://docs.temporal.io/cloud/limits#number-of-custom-search-attributes) and [naming](https://docs.temporal.io/cloud/limits#custom-search-attribute-names).

        ## Import

        Search Attributes can be imported to incorporate existing Namespace Search Attributes into your Terraform pipeline.

        To import a Search Attribute, you need

        - a resource configuration in your Terraform configuration file/module to accept the imported Search Attribute. In the example below, the placeholder is "temporalcloud_namespace_search_attribute" "saimport"

        - the Namespace ID, which includes the Namespace Name and Account ID available at the top of the Namespace's page in the Temporal Cloud UI. In the example below, this is namespaceid.acctid

        - the name of the Search Attribute, which is available in the Search Attribute configuration of Namespace's page in the Temporal Cloud UI. In the example below, this is searchAttr

        ```sh
        $ pulumi import temporalcloud:index/namespaceSearchAttribute:NamespaceSearchAttribute saimport namespaceid.acctid/searchAttr
        ```

        :param str resource_name: The name of the resource.
        :param NamespaceSearchAttributeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamespaceSearchAttributeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 namespace_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NamespaceSearchAttributeArgs.__new__(NamespaceSearchAttributeArgs)

            __props__.__dict__["name"] = name
            if namespace_id is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_id'")
            __props__.__dict__["namespace_id"] = namespace_id
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(NamespaceSearchAttribute, __self__).__init__(
            'temporalcloud:index/namespaceSearchAttribute:NamespaceSearchAttribute',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            namespace_id: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'NamespaceSearchAttribute':
        """
        Get an existing NamespaceSearchAttribute resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the search attribute.
        :param pulumi.Input[str] namespace_id: The ID of the namespace to which this search attribute belongs.
        :param pulumi.Input[str] type: The type of the search attribute. Must be one of `bool`, `datetime`, `double`, `int`, `keyword`, `keyword_list` or `text`. (case-insensitive)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _NamespaceSearchAttributeState.__new__(_NamespaceSearchAttributeState)

        __props__.__dict__["name"] = name
        __props__.__dict__["namespace_id"] = namespace_id
        __props__.__dict__["type"] = type
        return NamespaceSearchAttribute(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the search attribute.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namespaceId")
    def namespace_id(self) -> pulumi.Output[str]:
        """
        The ID of the namespace to which this search attribute belongs.
        """
        return pulumi.get(self, "namespace_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the search attribute. Must be one of `bool`, `datetime`, `double`, `int`, `keyword`, `keyword_list` or `text`. (case-insensitive)
        """
        return pulumi.get(self, "type")
