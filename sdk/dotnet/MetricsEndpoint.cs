// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Temporalcloud
{
    /// <summary>
    /// Configures a Temporal Cloud account's metrics
    /// 
    /// ## Import
    /// 
    /// ```sh
    /// $ pulumi import temporalcloud:index/metricsEndpoint:MetricsEndpoint terraform terraform.account-11111-metrics
    /// ```
    /// </summary>
    [TemporalcloudResourceType("temporalcloud:index/metricsEndpoint:MetricsEndpoint")]
    public partial class MetricsEndpoint : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Base64-encoded CA cert in PEM format used to authenticate clients connecting to the metrics endpoint.
        /// </summary>
        [Output("acceptedClientCa")]
        public Output<string> AcceptedClientCa { get; private set; } = null!;

        [Output("timeouts")]
        public Output<Outputs.MetricsEndpointTimeouts?> Timeouts { get; private set; } = null!;

        /// <summary>
        /// The Prometheus metrics endpoint URI
        /// </summary>
        [Output("uri")]
        public Output<string> Uri { get; private set; } = null!;


        /// <summary>
        /// Create a MetricsEndpoint resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public MetricsEndpoint(string name, MetricsEndpointArgs args, CustomResourceOptions? options = null)
            : base("temporalcloud:index/metricsEndpoint:MetricsEndpoint", name, args ?? new MetricsEndpointArgs(), MakeResourceOptions(options, ""))
        {
        }

        private MetricsEndpoint(string name, Input<string> id, MetricsEndpointState? state = null, CustomResourceOptions? options = null)
            : base("temporalcloud:index/metricsEndpoint:MetricsEndpoint", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing MetricsEndpoint resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static MetricsEndpoint Get(string name, Input<string> id, MetricsEndpointState? state = null, CustomResourceOptions? options = null)
        {
            return new MetricsEndpoint(name, id, state, options);
        }
    }

    public sealed class MetricsEndpointArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Base64-encoded CA cert in PEM format used to authenticate clients connecting to the metrics endpoint.
        /// </summary>
        [Input("acceptedClientCa", required: true)]
        public Input<string> AcceptedClientCa { get; set; } = null!;

        [Input("timeouts")]
        public Input<Inputs.MetricsEndpointTimeoutsArgs>? Timeouts { get; set; }

        public MetricsEndpointArgs()
        {
        }
        public static new MetricsEndpointArgs Empty => new MetricsEndpointArgs();
    }

    public sealed class MetricsEndpointState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Base64-encoded CA cert in PEM format used to authenticate clients connecting to the metrics endpoint.
        /// </summary>
        [Input("acceptedClientCa")]
        public Input<string>? AcceptedClientCa { get; set; }

        [Input("timeouts")]
        public Input<Inputs.MetricsEndpointTimeoutsGetArgs>? Timeouts { get; set; }

        /// <summary>
        /// The Prometheus metrics endpoint URI
        /// </summary>
        [Input("uri")]
        public Input<string>? Uri { get; set; }

        public MetricsEndpointState()
        {
        }
        public static new MetricsEndpointState Empty => new MetricsEndpointState();
    }
}
