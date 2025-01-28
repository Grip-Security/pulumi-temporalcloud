// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace GripSecurity.Temporalcloud.Outputs
{

    [OutputType]
    public sealed class GetNamespacesNamespaceEndpointsResult
    {
        /// <summary>
        /// The gRPC hostport address that the temporal workers, clients and tctl connect to.
        /// </summary>
        public readonly string GrpcAddress;
        /// <summary>
        /// The web UI address.
        /// </summary>
        public readonly string WebAddress;

        [OutputConstructor]
        private GetNamespacesNamespaceEndpointsResult(
            string grpcAddress,

            string webAddress)
        {
            GrpcAddress = grpcAddress;
            WebAddress = webAddress;
        }
    }
}
