// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace GripSecurity.PulumiTemporalCloud
{
    /// <summary>
    /// Create a [search attribute](https://docs.temporal.io/visibility#search-attribute) in a Temporal Cloud namespace. Note the limits on [quantity](https://docs.temporal.io/cloud/limits#number-of-custom-search-attributes) and [naming](https://docs.temporal.io/cloud/limits#custom-search-attribute-names).
    /// 
    /// ## Import
    /// 
    /// Search Attributes can be imported to incorporate existing Namespace Search Attributes into your Terraform pipeline.
    /// 
    /// To import a Search Attribute, you need
    /// 
    /// - a resource configuration in your Terraform configuration file/module to accept the imported Search Attribute. In the example below, the placeholder is "temporalcloud_namespace_search_attribute" "saimport"
    /// 
    /// - the Namespace ID, which includes the Namespace Name and Account ID available at the top of the Namespace's page in the Temporal Cloud UI. In the example below, this is namespaceid.acctid
    /// 
    /// - the name of the Search Attribute, which is available in the Search Attribute configuration of Namespace's page in the Temporal Cloud UI. In the example below, this is searchAttr
    /// 
    /// ```sh
    /// $ pulumi import temporalcloud:index/namespaceSearchAttribute:NamespaceSearchAttribute saimport namespaceid.acctid/searchAttr
    /// ```
    /// </summary>
    [PulumiTemporalCloudResourceType("temporalcloud:index/namespaceSearchAttribute:NamespaceSearchAttribute")]
    public partial class NamespaceSearchAttribute : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The name of the search attribute.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of the namespace to which this search attribute belongs.
        /// </summary>
        [Output("namespaceId")]
        public Output<string> NamespaceId { get; private set; } = null!;

        /// <summary>
        /// The type of the search attribute. Must be one of `bool`, `datetime`, `double`, `int`, `keyword`, `keyword_list` or `text`. (case-insensitive)
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;


        /// <summary>
        /// Create a NamespaceSearchAttribute resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NamespaceSearchAttribute(string name, NamespaceSearchAttributeArgs args, CustomResourceOptions? options = null)
            : base("temporalcloud:index/namespaceSearchAttribute:NamespaceSearchAttribute", name, args ?? new NamespaceSearchAttributeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private NamespaceSearchAttribute(string name, Input<string> id, NamespaceSearchAttributeState? state = null, CustomResourceOptions? options = null)
            : base("temporalcloud:index/namespaceSearchAttribute:NamespaceSearchAttribute", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing NamespaceSearchAttribute resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NamespaceSearchAttribute Get(string name, Input<string> id, NamespaceSearchAttributeState? state = null, CustomResourceOptions? options = null)
        {
            return new NamespaceSearchAttribute(name, id, state, options);
        }
    }

    public sealed class NamespaceSearchAttributeArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the search attribute.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the namespace to which this search attribute belongs.
        /// </summary>
        [Input("namespaceId", required: true)]
        public Input<string> NamespaceId { get; set; } = null!;

        /// <summary>
        /// The type of the search attribute. Must be one of `bool`, `datetime`, `double`, `int`, `keyword`, `keyword_list` or `text`. (case-insensitive)
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public NamespaceSearchAttributeArgs()
        {
        }
        public static new NamespaceSearchAttributeArgs Empty => new NamespaceSearchAttributeArgs();
    }

    public sealed class NamespaceSearchAttributeState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the search attribute.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the namespace to which this search attribute belongs.
        /// </summary>
        [Input("namespaceId")]
        public Input<string>? NamespaceId { get; set; }

        /// <summary>
        /// The type of the search attribute. Must be one of `bool`, `datetime`, `double`, `int`, `keyword`, `keyword_list` or `text`. (case-insensitive)
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public NamespaceSearchAttributeState()
        {
        }
        public static new NamespaceSearchAttributeState Empty => new NamespaceSearchAttributeState();
    }
}
