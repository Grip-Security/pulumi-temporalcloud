// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace GripSecurity.Temporalcloud.Inputs
{

    public sealed class NexusEndpointWorkerTargetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The target cloud namespace to route requests to. Namespace must be in same account as the endpoint.
        /// </summary>
        [Input("namespaceId", required: true)]
        public Input<string> NamespaceId { get; set; } = null!;

        /// <summary>
        /// The task queue on the cloud namespace to route requests to.
        /// </summary>
        [Input("taskQueue", required: true)]
        public Input<string> TaskQueue { get; set; } = null!;

        public NexusEndpointWorkerTargetArgs()
        {
        }
        public static new NexusEndpointWorkerTargetArgs Empty => new NexusEndpointWorkerTargetArgs();
    }
}
